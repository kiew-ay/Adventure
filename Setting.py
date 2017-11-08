'''
----------------------------------------------------------------------------------------------------------------------------

IMPORTS

----------------------------------------------------------------------------------------------------------------------------
'''

import pygame
from pygame.locals import *
import sys
import random

# Define a class to represent a point for coordinate simplification

class point:
		def __init__(self, x=0,y=0,z=0):
			self.x = x
			self.y = y
			self.z = z

# Define a Room class to contain characters for a location

class Room:
	def __init__(self, characters, position, style, visited=True):
		self.characters = characters
		self.position = position
		self.style = style
		self.visited = visited

	def present(self): 												# Create a message that presents the style of the player's current room and the characters contained within the room
		message = "You are in a " + self.style + " room with "
		if len(self.characters) > 2:
			for i in range(1,len(self.characters)-1):
				message += "a " + self.characters[i].name + ", "
			message += "and a " + self.characters[-1].name + "."
		elif len(self.characters) == 2:
			message += self.characters[1].name
		else:
			message = "You are in an empty " + self.style + " room."
		return message

	def draw(self, screen):											# Draw a representation of the room to a Map Screen with the characters visible for player-visited rooms
		width, height = pygame.display.get_surface().get_size()

		pygame.draw.rect(screen, (255,255,255), (100*self.position.x, 100*self.position.y, 100, 100), 1)

		for i, character in enumerate(self.characters):

			if character.name == "Traveler":
				pygame.draw.circle(screen, (0,255,0), (100*self.position.x + 50, 100*self.position.y + 50), 3)
				self.visited = True

			if self.visited == True:

				if character.name == "Door":
					if character.wall == "right":
						pygame.draw.rect(screen, (255,255,255), (100*self.position.x + 95, 100*self.position.y + 40, 10, 20))
					if character.wall == "down":
						pygame.draw.rect(screen, (255,255,255), (100*self.position.x + 40, 100*self.position.y + 95, 20, 10))
					if character.wall == "left":
						pygame.draw.rect(screen, (255,255,255), (100*self.position.x - 5, 100*self.position.y + 40, 10, 20))
					if character.wall == "up":
						pygame.draw.rect(screen, (255,255,255), (100*self.position.x + 40, 100*self.position.y - 5, 20, 10))

				elif character.name == "Spooky Skeleton":
					pygame.draw.circle(screen, (255,0,0), (100*self.position.x + 50 + int(random.uniform(-45, 45)), 100*self.position.y + 50 + int(random.uniform(-45, 45))), 3)

				elif character.name == "Ghost":
					pygame.draw.circle(screen, (175,175,175), (100*self.position.x + 50 + int(random.uniform(-45, 45)), 100*self.position.y + 50 + int(random.uniform(-45, 45))), 4, 1)

				elif character.name == "Diamond":
					point_list = [(100*self.position.x + 50, 100*self.position.y + 60),
								  (100*self.position.x + 45, 100*self.position.y + 50), 
								  (100*self.position.x + 50, 100*self.position.y + 40), 
								  (100*self.position.x + 55, 100*self.position.y + 50)]
					pygame.draw.polygon(screen, (255, 255, 255), point_list)

def wait():
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					return
				elif event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()

class Map:
	def __init__(self, roomlist):
		self.roomlist = roomlist

	def generate(self):

		#Initiate pygame window
		pygame.init()
		background_colour = (0,0,0)

		mapsize = point(0,0,0)
		for i, target_room in enumerate(roomlist):
			if target_room.position.x > mapsize.x:
				mapsize.x = target_room.position.x
			if target_room.position.y > mapsize.y:
				mapsize.y = target_room.position.y

		(width, height) = (100 * (mapsize.x+1), 100 * (mapsize.y+1))


		screen = pygame.display.set_mode((width,height),pygame.NOFRAME)#
		screen.fill(background_colour)

		for i, target_room in enumerate(roomlist):
			target_room.draw(screen)

		pygame.display.flip() # Show the screen

class Dummy_Character:
	def __init__(self, name):
		self.name = name

class Door(Dummy_Character):
	def __init__(self, name, wall):
		Dummy_Character.__init__(self, "Door")
		self.wall = wall

Player_Char = Dummy_Character("Traveler")
Ghost = Dummy_Character("Ghost")
Skeleton = Dummy_Character("Spooky Skeleton")
Diamond = Dummy_Character("Diamond")

Door_Right = Door("Door", "right")
Door_Down = Door("Door", "down")
Door_Left = Door("Door", "left")
Door_Up = Door("Door", "up")

styles = ["Haunted Dungeon", "Haunted Forest"]


Room1 = Room([Player_Char, Ghost, Skeleton, Door_Right], point(0,0,0), styles[0])
Room2 = Room([Skeleton, Door_Right], point(1,0,0), styles[0])
Room3 = Room([Ghost, Ghost, Ghost, Door_Down], point(2,0,0), styles[0])
Room4 = Room([Door_Down, Skeleton], point(2,1,0), styles[0])
Room5 = Room([Diamond], point(2,2,0), styles[0])

print(Room1.present())


roomlist = [Room1, Room2, Room3, Room4, Room5]

'''	Simplest possible case

Room1 = Room([Player_Char, Ghost, Skeleton, Door_Right], point(0,0,0), styles[0])
Room2 = Room([Ghost, Diamond], point(1,0,0), styles[0])
roomlist = [Room1, Room2]

'''

Map1 = Map(roomlist)

# Dummy Main Game Loop:

done = False
while not done:

	Map1.generate()

	for event in pygame.event.get():
		if event.type == QUIT:
				done = True
				pygame.quit()
		elif event.type == KEYDOWN:
			pressed_key = event.key
			if pressed_key == K_ESCAPE:
				done = True
				pygame.quit()

		else:
			wait()

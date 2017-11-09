"""
                                EXAMPLE DUNGEON

This is an example Mission file, to get a sense of how a mission will be defined
in a file, and the API it will use with the support modules.


DESCRIPTION:    5 Rooms
                3 Items:    scroll
                            key1
                            diamond
                1 Enemy (skeleton)
                2 Win Conditions:   Obtain the diamond
                                    Kill the skeleton
                1 Lose Condition:   Hero dies


MAP
                      +-----------------+-----------------+
                      |       (k1)      |                 |
                      |                 |                 |
                      |                 |                 |
                      |        3                 4        |
                      |                 |                 |
                      |                 |                 |
                      |                 |                 |
    +-----------------+--------/--------+--------%1-------+
    |                 |       (sc)      |       (sk)      |
    |                 |                 |                 |
    |                 |                 |                 |
    |      start      /        2        |    treasure     |
    |                 |                 |                 |
    |                 |                 |                 |
    |                 |                 |       (d)       |
    +-----------------+-----------------+-----------------+


LEGEND:
------------------------------------------------------------
    SYMBOL  |   MEANING
------------------------------------------------------------
    /       |   Door (closed, unlocked)
    %*      |   Door (locked, needs key_*)
    (sc)    |   Scroll
    (k1)    |   Key 1
    (d)     |   Diamond
    (sk)    |   Skeleton
------------------------------------------------------------

"""


#---------------------------------- IMPORTS ------------------------------------
# (NOTE: UserInterface and Conflict probably don't need to be imported here...?)
import Setting
import Character
import Plot
import GetUserInfo


#----------------------------- GET CHARACTER INFO ------------------------------
hero_name = input("What is your name?  > ")
body_type = GetUserInfo.get_body_type()
mind_type = GetUserInfo.get_mind_type()


#--------------------------- CREATE ITEMS / ENEMIES ----------------------------
#instantiate objects to be placed in rooms
scroll   = Character.Item()
key1     = Character.Item()
diamond  = Character.Item()
skeleton = Character.Enemy(name="Skeleton", hp=35)


#--------------------------------- CREATE MAP ----------------------------------
# instantiate rooms
start    = Setting.Room()
room2    = Setting.Room(contents=[scroll])
room3    = Setting.Room(contents=[key1])
room4    = Setting.Room()
treasure = Setting.Room(contents=[skeleton, diamond])

# --> define starting room (which WorldCreator will use to place the hero in)
STARTING_ROOM = start

# create map layout
dungeon = Setting.layout(   [None,  room3,  room4],
                            [start, room2,  treasure]
                        )

# instantiate doors, and create relationships
door_start_2    = Character.Door(start, room2,    locked=False, closed=True)
door_2_3        = Character.Door(room2, room3,    locked=False, closed=True)
door_3_4        = Character.Door(room3, room4,    locked=False, closed=False)
door_4_treasure = Character.Door(room4, treasure, locked=True,  closed=True, key=key1)


#------------------------------------ HERO -------------------------------------
# instantiate hero
hero  = Character.Protagonist( name=hero_name,
                               body_type=body_type,
                               mind_type=mind_type )

# add to skills
punch = Punch(damage=10)
hero.skills.append(punch)

# add to inventory
torch = Character.Item()
hero.inventory.append(torch)    # give the hero a torch to start with


#-------------------- DEFINE (WIN/LOSE/TRIGGER) CONDITIONS ---------------------
# define win/lose conditions with Plot's Condition class methods
hero_has_diamond    = Plot.Condition.is_in(diamond, hero.inventory)
skeleton_dies       = Plot.Condition.die(skeleton)
hero_dies           = Plot.Condition.die(hero)

# add to win conditions
Plot.Checker.add_win_condition( hero_has_diamond )
Plot.Checker.add_win_condition( skeleton_dies )

# add to lose conditions
Plot.Checker.add_lose_condition( hero_dies )

"""This is the file for characters. Protagonists and Antagonists should be in here. I think this is going to include the class chooser function as well. SKills will be elsewhere."""

"""Note that profession scores sum to 16 for easy mathing, or maybe hard mathing"""
profession='Hobo'
profession_list = {
    'Face'      :{'body_type':'B','mind_type':'C','Stats':['body_attack',2,'body_defense',2,'mental_attack',6,'mental_defense',6]},
    'Leader'    :{'body_type':'A','mind_type':'A','Stats':['body_attack',3,'body_defense',3,'mental_attack',4,'mental_defense',6]}
    'Pro'       :{'body_type':'A','mind_type':'B','Stats':['body_attack',6,'body_defense',4,'mental_attack',6,'mental_defense',4]}
    'Body'      :{'body_type':'A','mind_type':'C','Stats':['body_attack',6,'body_defense',2,'mental_attack',6,'mental_defense',2]}
    'Expert'    :{'body_type':'B','mind_type':'A','Stats':['body_attack',4,'body_defense',4,'mental_attack',4,'mental_defense',4]}
    'Savant'    :{'body_type':'B','mind_type':'B','Stats':['body_attack',1,'body_defense',3,'mental_attack',6,'mental_defense',6]}
    'Brains'    :{'body_type':'C','mind_type':'A','Stats':['body_attack',1,'body_defense',1,'mental_attack',8,'mental_defense',6]}
    'Survivor'  :{'body_type':'C','mind_type':'B','Stats':['body_attack',1,'body_defense',7,'mental_attack',1,'mental_defense',7]}
    'Ringleader':{'body_type':'C','mind_type':'C','Stats':['body_attack',2,'body_defense',2,'mental_attack',8,'mental_defense',4]}
    'Hobo'      :{                                'Stats':['body_attack',1,'body_defense',13,'mental_attack',1,'mental_defense',1]}



def player_selector():
    name = 'What is your name? > ')
    body_type = ''
    mind_type = ''
    body_type = input("Are you more A) Strong, B) Quick, or C) Tough ").upper()
    mind_type = input("And are you more A)Knowledgeable, B)Clever, or C) Charming? ").upper()
    for job in profession_list:
        BODY_TYPE = profession_list[job]['body_type']
        MIND_TYPE = profession_list[job]['mind_type']

        if body_type == BODY_TYPE and mind_type -= MIND_TYPE
            profession=job

    print('Hi {}, you seem like the {} of this operation'.format(name,profession))


class Character(object):
    def __init__(self, body_attack, body_defense, mind_attack, mind_defense):
        self.body_attack = 

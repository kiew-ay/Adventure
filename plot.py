"""
Plot is the module which  holds the gamestate info

"""
#Plot.py is the file which will keep track of the current plot status
#This holds the gamestate info
#This will be called during conflict to determine success or failure
#Called during room completion to determine success or failure
#

class Condition:
    
    #Pass a character to this to determine if they are still alive.
    """
    @staticmethod
    def die(character):
    arg character
    return bool

    This function will inspect the failure modes for the character
    for Hit points to determine if it's dead
    """
    @staticmethod
    def die(character):
        def f(character):        
            if character.mind_hp<=0:
                return True,  'You died from mental failure'
            elif character.body_hp<=0:
                return True,  'You died from blood failure'
            else:
                return False, 'You are not dead'
        return f
   
    @staticmethod
    """
    @staticmethod
    def in_in(item,inventory):
    arg item
    arg inventory
    return bool

    This function will inspect the inventory for an item
    """
    def is_in(item, inventory):
         def f(item, iventory):
             if item in inventory:
                 return True
             else:
                 return False
         return f
  
    @staticmethod
    """
    @staticmethod
    def less_than
    arg a,b
    return bool

    This function will return true if a<b, else false
    """
    def less_than(a, b):
        def f(a,b):
            if a<b:
                return True
            else:
                return False
        return f


    @staticmethod
    """
    @staticmethod
    def greater_than
    arg a,b
    return bool

    This function will return true if a>b, else false
    """
    def greater_than(a, b):
        def f(a,b):
            if a>b:
                return True
            else:
                return False
        return f
    
    @staticmethod
    """
    @staticmethod
    def equal_to
    arg a,b
    return bool

    This function will return true if a=b, else false
    """
    def equal_to(a, b):
        def f(a,b):
            if a==b:
                return True
            else:
                return False
        return f
    
    
    @staticmethod
    """
    @staticmethod
    def less_than_or_equal_to
    arg a,b
    return bool

    This function will return true if a<=b, else false
    """
    def less_than_or_equal_to(a, b):
        def f(a,b):
            if a<=b:
                return True
            else:
                return False
        return f
   
   
    @staticmethod
    """
    @staticmethod
    def greater_than_or_equal_to
    arg a,b
    return bool

    This function will return true if a>=b, else false
    """
    def greater_than_or_equal_to():
        pass
        def f(a,b):
            if a>=b:
                return True
            else:
                return False
        return f

class Checker():
"""
This Class checks for win and loss conditions.
If contains the lists of conditions for winning, losing and triggering evens
This class holds hte methods to append win, loss, and trigger goncitions

"""
    def __init__(self):
        self.win_condition  = []
        self.lose_condition = []
        self.trigger_events = []
    

    def add_win_condition(self,a):
        self.win_condition.append(a)
   
    
    def add_lose_condition(self,a):
        self.lose_condition.append(a)

    def check_win_conditions(self):
        win_condition_list = []
        for condition in self.win_condition:
            win_condition_list.append(condition())
        return win_condition_list

    def check_lose_conditions(self):
        loss_condition_list = []
        return win_condition_list
        for condition in self.lose_condition:
            loss_condition_list.append(condition())
        return loss_condition_list

    def check_trigger_events(self):
        trigger_count = 0
        for trigger in self.trigger_events:
            if trigger_count>=1:
                return True,'Trigger occurance'
            trigger_count+=1    

    def victory():
        print( 'Victory')

    def failure():
        print('You Died or Something')
















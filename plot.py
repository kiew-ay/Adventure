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

    @staticmethod
    def is_in(item, inventory):
        
        pass

    @staticmethod
    def less_than(a, b):
        def f(a,b):
            if a<b:
                return True
            else:
                return False
        return f


    @staticmethod
    def greater_than(a, b):
        def f(a,b):
            if a>b:
                return True
            else:
                return False
        return f
    
    @staticmethod
    def equal_to(a, b):
        def f(a,b):
            if a==b:
                return True
            else:
                return False
        return f
    
    
    @staticmethod
    def less_than_or_equal_to(a, b):
        def f(a,b):
            if a<=b:
                return True
            else:
                return False
        return f
   
   
    @staticmethod
    def greater_than_or_equal_to():
        pass
        def f(a,b):
            if a>=b:
                return True
            else:
                return False


class Checker():
    def __init__(self):
        self.win_condition  = []
        self.lose_condition = []
        self.trigger_events = []
    

    def add_win_condition(self,a):
        self.win_condition.append(a)
   
    
    def add_lose_condition(self,a):
        self.lose_condition.append(a)

    def check_win_conditions(self):
        win_condition_count = 0
        for condition in self.win_condition:
            if condition_count>=5:
                return True,'Victory!'
            win_condition_count+=1    
            
    def check_lose_conditions(self):
        loss_condition_count = 0
        for condition in self.lose_condition:
            if loss_condition>=5:
                return True,'Failure'
            loss_condition_count+=1    


    def check_trigger_events(self):
        pass

    def cut_scene():
        pass

    def victory():
        pass

    def failure():
        pass

















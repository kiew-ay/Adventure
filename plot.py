#Plot.py is the file which will keep track of the current plot status
#This holds the gamestate info
#This will be called during conflict to determine success or failure
#Called during room completion to determine success or failure
#

class Condition:
    
#Pass a character to this to determine if they are still alive.
    @staticmethod
    def die(character):
##TODO MAKE THIS A REtuRN F FUNCTION
        def f(a,b)        
            if self.less_than_or_equal_to(character.mind_hp,0):
                return True,  'You died from mental failure'
            elif self.less_than_or_equal_to(character.body_hp,0):
                return True,  'You died from blood failure'
            else:
                return False, 'You are not dead'

    @staticmethod
    def is_in(item, inventory):
        
        pass

    @staticmethod
    def less_than(cls, a, b):
        def f(a,b):
            if a<b:
                return True
            else:
                return False
        return f


    @staticmethod
    def greater_than(cls, a, b):
        def f(a,b):
            if a>b:
                return True
            else:
                return False
        return f
    
    @staticmethod
    def equal_to(cls, a, b):
        def f(a,b):
            if a==b:
                return True
            else:
                return False
        return f
    
    
    @staticmethod
    def less_than_or_equal_to(cls, a, b):
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
        return f


class Plot():
    #win condition is a list(?) or dictionary of things
    win_condition  = []
    lose_condition = []
    trigger_events = []
    

    def add_win_condition():
        pass
    
    def add_lose_condition():
        pass

    def check_win_condition():
        pass

    def check_lose_condition():
        pass

    def check_trigger_event():
        pass

    def cut_scene():
        pass



















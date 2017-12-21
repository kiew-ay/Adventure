"""
================================================================================
                                 World Creator
================================================================================

This module is responsible for the following tasks:

    (1) Generating the world by coordinating the generation of the:
            - map
            - characters
            - items
            - plot

    (2) Running the main loop for gameplay

"""

#-------------------------------------------------------------------------------
# IMPORTS
import os
import sys
import importlib

import UserInterface as UI
import Conflict

# Add path up one level
#sys_path = str(os.path.abspath(os.path.join(os.path.dirname(__file__),
#                                            os.pardir)))


#-------------------------------------------------------------------------------
# VARIABLES


#-------------------------------------------------------------------------------
# FUNCTIONS

def import_mission_file():
    # get mission file from command line arguments
    mission_filename = sys.argv[1]

    # parse for importing
    mission_dir      = 'Mission'
    mission_import   = '{}.{}'.format(mission_dir, mission_filename)

    # import mission_file as Mission
    #Mission = __import__(mission_import)
    Mission = importlib.import_module(mission_import)
    return Mission


def init():
    global Mission
    global hero
    global current_room
    global plot

    Mission      = import_mission_file()
    hero         = Mission.hero
    current_room = Mission.STARTING_LOCATION
    plot         = Mission.plot


def main():
    global Mission
    global hero
    global current_room
    global plot

    while True:
        Setting.draw_room()
        UI.describe_setting()

        #-------------------------------------------------
        # give options for current room
        # this will be a dict -- each item will be:
        #                           key   : name of object
        #                           value : object
        room_options  = {}
        for character in current_room.contents:
            # name of character / item
            name = character['name']
            room_options[name] = character

        target = UI.prompt_options(room_options)

        #-------------------------------------------------
        # CONFLICT
        # instantiate a conflict between hero and target
        conflict = Conflict.conflict(hero, target)
        conflict.main()

        #-------------------------------------------------
        # check all plot conditions
        if plot.check_win_conditions():
            plot.victory()
            exit()
        if plot.check_lose_conditions():
            plot.failure()
            exit()


#-------------------------------------------------------------------------------
# MAIN
if __name__ == "__main__":
    init()
    main()

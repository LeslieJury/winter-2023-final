import random
import subprocess
import math
import os
import subprocess as sub




'''
Final Project
Leslie Jury
CSE 111

Sources:
https://stackoverflow.com/questions/11325019/how-to-output-to-the-console-and-file
https://stackoverflow.com/questions/28891053/run-npm-commands-using-python-subprocess
https://github.com/makegirlsmoe/makegirlsmoe_web
'''

Player_Health = 100 #Keeps track of player's health

Player_Life = True #Keeps track of if the player is alive



#SUCCESS
Angel_List = ["Adam", "Lilith", "Sachiel", 
                "Shamshel", "Ramiel", "Gaghiel", 
                "Israfel", "Sandalphon", "Matarael", 
                "Sahaquiel", "Ireul", "Leliel", 
                "Bardiel", "Zeruel", "Arael", 
                "Armisael", "Tabris", "Lilin"]

#Here is my debugging print function. this way I can debug using print statements but don't have to go back and delete them after.
debug = False
debug = True
def debug_print(item):
     if debug == True:
        print(item)


#This is to show what text will be displayed to the user through the UI
ui_output = False
ui_output = True


def Ui_Output(statement):
    if ui_output == True:
        print(statement)

#This is the simple function that takes in zero values and returns one value. I'm using this function for all of my user input to keep it in once place.

def Ask_User():
    Leslie = "cool"
    #user_input = int(input("What level do you want to start on? lvl 1-10: "))
    user_input = 0
    debug_print(user_input)
    return user_input



#This is the enemy randomizer function. It uses the random.choice() function to look through the list. This simplifies the program by removing one for loop.
def rand_enemies(angel_num):

    def level():
        selected_lvl = Ask_User()
        if selected_lvl >= 7:
            Ui_Output("Advanced mode")
            angel_num = angel_num * 1.5
        elif selected_lvl >= 4:
            Ui_Output("Intermediate mode")
             #Angel num stays the same
        else:
            Ui_Output("Beginner mode")
            angel_num = angel_num - 2
    #This is a nested function within rand_enemies that checks for duplicates, and if it finds one, it uses recursion to run rand_enemies again
    def check_duplicates():
        replacement_of_duplicate = random.choice(Angel_List)
        if random_angel in small_angel_list: #This function checks for any duplicates in the list.
            angel_num = small_angel_list.index(random_angel)
            del small_angel_list[angel_num]
            if replacement_of_duplicate != random_angel:
                small_angel_list.append(replacement_of_duplicate)
                return True
            else:
                check_duplicates()



    small_angel_list = []
    debug_print(angel_num)
    for i in range(angel_num):
        random_angel = random.choice(Angel_List)
        check_duplicates()
        small_angel_list.append(random_angel)
        debug_print(small_angel_list)
        
        if check_duplicates == True:
            return (small_angel_list)


#This is the mother function of the two previous, it ties them together and returns a single list without risk of duplicates.
#This prints the enemies you will be facing
def Enemy_Spawn():
    angels = rand_enemies()
    return angels

def Commander_Call():
    #This is where the makegirlsmoe comes in, it will randomly generate a woman's face to act as your commander for that mission.
    #This way everytime you start the simulation you get a unique cast of characters.
    os.system('dir')
    os.system('cd c:\\Users\lesli\OneDrive\Desktop\College 2022-23\CSE\CSE 111\Final Project\makegirlsmoe_web')
    os.system('npm start')
    #sub.Popen(['cmd', '/K', 'dir'])
    #sub.Popen(['cd c:\\Users\lesli\OneDrive\Desktop\College 2022-23\CSE\CSE 111\Final Project\makegirlsmoe_web'])
    #sub.Popen("npm start")

    debug_print("Commander Call")

def last_crit_chance(your_crit):
    power_point = (math.pow(your_crit, 2))
    return power_point
    
#As the user makes an attack, this function randomizes if it will be a critical hit or not.
def Critical_Assign():
    crit_factor = random.randrange(100)
    if crit_factor > 75:
        print("Player or Enemy is ")
        if crit_factor >= 90: #These if statements customize the consequences of your critical attack to match the magnitude of the critical factor
            print("elimanated")
            last_crit_chance(crit_factor)
        elif crit_factor >= 80:
            print("severely injured")
        else:
            print("badly wounded")
        print(" due to a critical attack of: " + crit_factor)


def main():
    Commander_Call()
    test_input = Ask_User()
    #test_User_Input(test_input)
    enemies = rand_enemies(5)
    print(enemies)

#def test_User_Input(test_input):
    #if test_input == int:
        #print("Passed")
    #assert 0 


main()
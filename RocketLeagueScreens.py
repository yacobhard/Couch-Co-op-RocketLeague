import re
from time import sleep
import webbrowser

myrocketleaguefile = r'YOURFILEPATH'


# file input
def get_resolution():
    f = open(myrocketleaguefile, 'r')
    message = f.read()
    f.close()

    x = re.findall("ResX=3840", message)  # Variable to test the truthy-ness of re.findall()

    if x:  # If ResX=3840 is present
        current = '3840'
    else:
        current = '1920'

    return current,  message


def take_the_input(resolution):
    acceptable_inputs = ['y', 'n', 'q']
    u = 'a'  # Set u to a value to initiate the loop

    while u not in acceptable_inputs:  # Loop

        if resolution == '3840':
            print("***********************************")
            print("Resolution is set to 2 player!")
        else:
            print("***********************************")
            print("Resolution is set to singleplayer!")

        print("Would you like to alter resolution?\n")
        u = input('y, n or q \n').lower()  # Take the input as lowercase
        print("***********************************")

        if u not in acceptable_inputs:  # Gateway to the program, only valid inputs
            print("Does not compute")
            print('Enter "q" to quit')
            continue  # Loop again

        return u  # Take a valid input


def open_game():  # Launch Rocket League
    print("Launching game...")
    webbrowser.open_new('steam://rungameid/252950')
    sleep(3)


def resolution_change(option, curr_res, config):
    if option == 'n':
        open_game()
        quit()

    elif option == 'y':  # Adjust Screen size
        if curr_res == '1920':  # Change to 2 player
            config = re.sub("Fullscreen=True", "Fullscreen=False", config)
            config = re.sub("Borderless=False", "Borderless=True", config)
            config = re.sub(curr_res, '3840', config)

        else:  # Change to single player settings
            config = re.sub("Fullscreen=False", "Fullscreen=True", config)
            config = re.sub("Borderless=True", "Borderless=False", config)
            config = re.sub(curr_res, '1920', config)

        wr = open(myrocketleaguefile, 'w+')
        wr.write(config)
        wr.close()

        print("Settings has been changed!")
        open_game()

    else:  # User input is q
        print("Exiting...")
        sleep(3)
        quit()


if __name__ == '__main__':
    curr_x, conf = get_resolution()
    user_input = take_the_input(curr_x)
    resolution_change(user_input, curr_x, conf)

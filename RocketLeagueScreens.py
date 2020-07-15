import re
from time import sleep
import webbrowser

myrocketleaguefile = 'C:\\Users\\Jake\\Documents\\My Games\\Rocket League\\TAGame\\Config\\TASystemSettings.ini'


# file input
def get_resolution():
    f = open(myrocketleaguefile, 'r')
    message = f.read()
    f.close()

    # read the value of Screen size x

    x = re.findall("ResX=3840", message)  # X variable to test the truthy-ness of re.findall()

    if x:  # If ResX=3840 is present
        print("***********************************")
        print("Resolution is set to 2 player!")
        current = '3840'
        opposite = '1920'

    else:  # If ResX=3840 is not present
        print("***********************************")
        print("Resolution is set to singleplayer!")
        current = '1920'
        opposite = '3840'

    return current, opposite


def take_the_input():
    acceptable_inputs = ['y', 'n', 'q']
    u = 'a'  # Set u to a value to initiate the loop

    print("***********************************")
    while u not in acceptable_inputs:  # Loop

        print("Would you like to alter resolution?")
        print('')
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


def resolution_change(option, curr, opp):
    if option == 'n':
        open_game()
        quit()

    elif option == 'y':  # Adjust Screen size

        new_config = re.sub(curr, opp, message)

        if current == '1920':  # Change to 2 player
            new_config = re.sub("Fullscreen=True", "Fullscreen=False", new_config)
            new_config = re.sub("Borderless=False", "Borderless=True", new_config)
            print("I detected current is " + str(curr))

        else:  # Change to single player settings
            new_config = re.sub("Fullscreen=False", "Fullscreen=True", new_config)
            new_config = re.sub("Borderless=True", "Borderless=False", new_config)
            print("I detected current is " + str(curr))

        wr = open(myrocketleaguefile, 'w+')
        wr.write(new_config)
        wr.close()

        print("Resolution has been changed!")
        open_game()

    else:  # User input is q
        print("Exiting...")
        sleep(3)
        quit()


if __name__ == '__main__':
    current_res, opposite_res = get_resolution()
    user_input = take_the_input()
    resolution_change(user_input, current_res, opposite_res)

import os
import random
import sys
from time import sleep

# Global variables
ANSI_WHITE = "\033[37m"
ANSI_RED = "\033[31m"
ANSI_BLUE = "\033[0;34m"
NEW_LINE = os.linesep

grid_width = 0
grid_height = 0


def main_menu():
    """Print the starting menu for the game using inputs to run the main function or quit the game"""
    while True:
        print("-----------\nBATTLESHIPS\n-----------")
        print("1.Play Game\n2.Quit\n")

        selected = input("Select an option:\n")
        # Takes input and dependin on value of input chooses an option.
        if selected == "1":
            print("Running Game\n")
            main()
        elif selected == "2":
            sys.exit()
        else:
            print("That isnt an option. Select another option")


def setting_custom_grid_size():
    """Take input for grid size and makes sure it matches formatting"""
    print("\n-----------------------------------------------")
    print("To set player_grid size please use 'Y,X' format")
    print("-----------------------------------------------\n")
    while True:
        # Assigns inputed values to height and width variables and checks if it matches the required format and returns the values.
        try:
            grid_width, grid_height = input(
                "Please enter your desired player_grid size (You cannot have more rows than columns):\n"
            ).split(",")
            return grid_width, grid_height, False
        except ValueError:
            print("You need to enter two values seperated by a ',' \n")


def print_grid(player_grid, title_text):
    """Run through each row checking if one of the index's is equal to 1 and
    turns it red and then prints the player_grid if the index does not equal 1
    then it will be printed in black. It also prints the top row and the left
    column with the values of y so it dynamically changes the cordinates of the
    player_grid."""

    print(title_text)

    # Checks if the width is greater then 9 and icreases the size of each cell on the grid
    if grid_width > 9:
        row = "| "
    else:
        row = "|"
    # Check to see if width is smaller then 8 to decrease the size of each cell on the grid
    for x in range(0, grid_width):
        row += str(x)
        if x > 8:
            row += "|"
        else:
            row += "| "

    print(row)

    for y in range(1, len(player_grid)):

        # Sets the first index of each row to y so the row numbers are icremeneted.
        try:
            player_grid[0][y] = y
        except IndexError:
            print("\nYou cannot have more rows then columns")
            break
        # Creates a string that starts with the row number surrounded by pipes.
        if y < 10:
            row = "| " + str(y) + "|"
        else:
            row = "|" + str(y) + "|"

        # the for loop , loops through each row within the player_grid range executing the code as it loops
        for x in range(1, len(player_grid[y])):
            # checks if any of the x indexs within each y row is equal to 1
            if player_grid[y][x] == 1 or player_grid[y][x] == 2:
                # If [x][y] is equal to 1 it applies the colour red to the x index of the y row and then reapplies the black colour
                row += " " + ANSI_RED + str(player_grid[y][x]) + ANSI_WHITE
            else:
                # if x does not equal 1 it adds the contents of player_grid[y][x] to the row string
                row += " " + str(player_grid[y][x])

            if x < grid_width:
                if x <= (grid_width - 2):
                    row += " "
                else:
                    row += ""

        # prints a square bracket at the end of each completed row.
        print(row + "|")

    # Using os.linsep to ensure that the correct line seperator is used based on
    # the OS the program is being run on e.g. \n
    print(NEW_LINE)


def cls():
    # clears the command line
    sleep(1)
    os.system("cls" if os.name == "nt" else "clear")


def grid_setup(width, height):
    """Creates each row of the player and computer player_grid using list comprehension and definable perameters"""

    global grid_width
    grid_width = width + 1
    global grid_height
    grid_height = height + 1

    # Creates the player_grid using list comprehension
    global player_grid
    player_grid = [[0 for x in range(grid_width)] for y in range(grid_height)]

    # Creates the computer_grid using list comprehension
    global computer_grid
    computer_grid = [[0 for x in range(grid_width)] for y in range(grid_height)]

    # Creates the player_guess_grid using list comprehension
    global player_guess_grid
    player_guess_grid = [[0 for x in range(grid_width)] for y in range(grid_height)]

    # Creates the top line of the player_grid
    global grid_top
    grid_top = [0 for x in range(grid_width)]

    # Creates the top line of the computer_grid_top
    global computer_grid_top
    computer_grid_top = [0 for x in range(grid_width)]

    # Creates the top line of the guess_top_grid
    global guess_top_grid
    guess_top_grid = [0 for x in range(grid_width)]


def setting_ship_location():
    """Creates a list for the row and column values and then runs through a while loop in which the player defines which row and column they wan thereship to
    be placed.
    it also checks if the number is bigger then the player_grid and if it is a message is displayed letting the player know that there selection was out of the
    player_grid limits
    and they need to pick again."""

    ship_location = []
    print("------------------------------------------")
    print("To enter the location use the 'Y,X' format")
    print("------------------------------------------\n")

    while True:
        x = 1

        # loops through the amount of boats you can assign
        while x <= 5:
            try:
                # Assigns the inputed data to the variables
                player_row, player_column = input(
                    str(f"Please select the location for ship num {x}\n")
                ).split(",")
                x += 1

                # Checks if the inputed option are within the range of the grid and allows user to redifine them incase they arn't, also calls checking functions
                if (int(player_row) + 1) > grid_height or (
                    int(player_column) + 1
                ) > grid_width:
                    print("The poition should be within the player_grid\n")
                    x -= 1
                    # redefines inputs
                    player_row, player_column = input(
                        f"Please select the location for ship num {x}\n"
                    ).split(",")
                    x += 1
                    GLC = gird_location_checking(
                        player_row, player_column, ship_location, x
                    )
                    x = int(GLC)

                else:
                    # Assigns the variables to the location list
                    GLC = gird_location_checking(
                        player_row, player_column, ship_location, x
                    )
                    x = int(GLC)
            # return the ship location list
            except ValueError:
                print("You need to enter two values seperated by a ',' \n")

        return ship_location


def computer_ship_location():
    """Creates a list for the row and column values and then runs through a while loop which defines the computer_row and computer_column
    variables with a random integer between 1 and what the player has set as the player_grid width and height. it also checks if the number is
    bigger then the player_grid and if it is the varisable is then redefined until it isnt greater then the grids limits."""

    computer_location = []
    i = 1

    # Generates a two random integeres for the computer guess location
    while i <= 5:

        computer_row = random.randint(1, grid_height - 1)
        computer_column = random.randint(1, grid_width - 1)

        i += 1
        # Checks if random ints are in grid range and redifines them if not, also calls the checking function
        if computer_row > grid_height or computer_column > grid_width:
            computer_row = random.randint(1, 5)
            computer_column = random.randint(1, 5)
            i += 1
            computer_location_checking(
                computer_row, computer_column, computer_location, i
            )

        else:
            CGLC = computer_location_checking(
                computer_row, computer_column, computer_location, i
            )
            i = CGLC

    return computer_location


def gird_location_checking(row, column, location, x):
    """Gets the values of the column and row variables provided and checks
    against the player_grid to see of that index location
    is alreadt filled with a 1 or not, if it is full it subtracts 1 from x and
    returns it forcing the while loop to step back
    and allow you to choose another location after displaying an error message,
    if its empty it is added to the location string"""

    # checks if user has entered duplicate cordinates.
    if player_grid[int(row)][int(column)] == 1:
        print("Youve already put a boat there")
        print(NEW_LINE)
        x -= 1

    else:
        location.append([row, column])
        update_grid(location)

    return x


def computer_location_checking(row, column, location, i):
    """Gets the values of the column and row variables provided and checks
    against the player_grid to see of that index location
    is alreadt filled with a 2 or not, if it is full it subtracts 1 from i and
    returns it forcing the while loop to step back
    and allow you to choose another location, if its empty it is added to the
    location string"""

    if computer_grid[row][column] == 2:
        i -= 1

    else:
        location.append([row, column])
        computer_update_grid(location)

    return i


def update_grid(ship_location):
    """Updates the inputed location of the ship using the ship_location indexs
    and itterating through using a for loop"""

    # Assigns variables of the row and column and changes that index to 1
    for x in range(len(ship_location)):

        player_row = ship_location[x][0]

        player_column = ship_location[x][1]

        player_grid[int(player_row)][int(player_column)] = 1

    print(NEW_LINE)


def computer_update_grid(computer_location):
    """updates the location of the computers ships using the computer_location
    index and iterating through using a for loop"""

    # Assigns variables of the row and column and changes that index to 1
    for x in range(len(computer_location)):
        computer_row = computer_location[x][0]

        computer_column = computer_location[x][1]

        computer_grid[computer_row][computer_column] = 2


def guess_update_grid_hit(guess_location):

    # Assings a red 0 to a hit location using the guess input
    for each in range(len(guess_location)):
        guess_row = guess_location[each][0]

        guess_column = guess_location[each][1]

        player_guess_grid[int(guess_row)][int(guess_column)] = (
            ANSI_RED + str(0) + ANSI_WHITE
        )


def guess_update_grid_miss(guess_location):

    # Assigns a blue 0 to a miss location using the guess input
    for x in range(len(guess_location)):
        guess_row = guess_location[x][0]

        guess_column = guess_location[x][1]

        player_guess_grid[int(guess_row)][int(guess_column)] = (
            ANSI_BLUE + str(0) + ANSI_WHITE
        )


def game_loop(location, ship_location):

    # loops through calling player and computer turn functions and stops when locations are empty.

    while location != [] or ship_location != []:

        player_turn(location)
        # If computer location is empty it prints win message
        if location == []:
            print("You have sunk all the enemies battleships !!")
            print("You win !!")
            break

        computer_turn(ship_location)
        # If player location is empty it prints a loose message
        if ship_location == []:
            print("The enemy has sunk all your battleships !!")
            print("You loose !!")
            break


def player_turn(location):

    guess_location_hit = []
    guess_location_miss = []

    try:
        # takes input, and determines weather its a hit or a miss.
        shot_row, shot_column = input(
            "Enter the location you would like to engage e.g 1,2\n"
        ).split(",")

        if computer_grid[int(shot_row)][int(shot_column)] == 2:
            # checks if inputs are an index within the location and assigns to a index variable.
            index = location.index([int(shot_row), int(shot_column)])
            # adds input to the hit location.
            guess_location_hit.append([shot_row, shot_column])
            computer_grid[int(shot_row)][int(shot_column)] = 0

            # the index is removed from the computer location list.
            print("You've sunk my battleship!!\n")
            location.pop(index)
            # calls the update functions for the grid and prints them
            computer_update_grid(location)
            guess_update_grid_hit(guess_location_hit)
            cls()
            print_grid(player_guess_grid, "Enemy grid:")
            print_grid(player_grid, "Player grid:")

        elif computer_grid[int(shot_row)][int(shot_column)] == 0:
            # adds the inputs to the miss location list.
            print("Thats a miss try again\n")
            # calls the update functions for the grid and prints them
            guess_location_miss.append([shot_row, shot_column])
            guess_update_grid_miss(guess_location_miss)
            cls()
            print_grid(player_guess_grid, "Enemy grid:")
            print_grid(player_grid, "Player grid:")

    # catches input errors
    except IndexError:
        print("Thats not wihtin player_grid limits try again\n")
    except ValueError:
        print("You need to enter a valid postion using the 'y,x' format")


def computer_turn(ship_location):

    computer_shot_row = random.randint(1, grid_height - 1)
    computer_shot_column = random.randint(1, grid_width - 1)

    if player_grid[computer_shot_row][computer_shot_column] == 1:
        # checks if inputs are an index within the location and assigns to a index variable.
        index = ship_location.index([computer_shot_row, computer_shot_column])
        # adds random integers to hit location
        player_grid[computer_shot_row][computer_shot_column] = 0
        print("computer fires and destroys you battleship !!\n")
        # the index is removed from the pklayer location list
        ship_location.pop(index)
        # calls the update functions for the grid and prints them
        update_grid(ship_location)
        cls()
        print_grid(player_guess_grid)
        print_grid(player_grid)

    elif player_grid[int(computer_shot_row)][int(computer_shot_column)] == 0:
        print("The computer fires and misses\n")
        cls()
        print_grid(player_guess_grid)
        print_grid(player_grid)


def main():
    # Calls all functions in order
    custom_grid = setting_custom_grid_size()
    grid_setup(int(custom_grid[0]), int(custom_grid[1]))
    ship_location = setting_ship_location()
    computer_location = computer_ship_location()
    cls()
    print_grid(player_grid, "Player grid:")
    game_loop(computer_location, ship_location)
    main_menu()


main_menu()

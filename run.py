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
    """Print the starting menu for the game using inputs to either exit the program or activate the main function and play the game"""
    while True:
        print("-----------\nBATTLESHIPS\n-----------")
        print("1.Play Game\n2.Quit\n")

        selected = input("Select an option:\n")

        if selected == "1":
            print("Running Game\n")
            main()
        elif selected == "2":
            sys.exit()
        else:
            print("That isnt an option. Select another option")


def setting_custom_grid_size():
    """Take the input from user to define player_grid size."""
    print("\n-----------------------------------------")
    print("To set player_grid size please use 'Y,X' format")
    print("-----------------------------------------\n")
    while True:
        try:
            grid_width, grid_height = input(
                "Please enter your desired player_grid size (You cannot have more rows than columns):\n"
            ).split(",")
            return grid_width, grid_height, False
        except ValueError:
            print("You need to enter two values seperated by a ',' \n")


def print_grid(player_grid):
    """Run through each row checking if one of the index's is equal to 1 and
    turns it red and then prints the player_grid if the index does not equal 1
    then it will be printed in black. It also prints the top row and the left
    column with the values of y so it dynamically changes the cordinates of the
    player_grid."""
    if grid_width > 9:
        row = "| "
    else:
        row = "|"

    for x in range(0, grid_width):
        row += str(x)
        if x > 8:
            row += "|"
        else:
            row += "| "

    # Using os.linsep to ensure that the correct line seperator is used based on
    # the OS the program is being run on e.g. \n
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
    print(NEW_LINE)


def cls():
    sleep(1)
    os.system("cls" if os.name == "nt" else "clear")


def grid_setup(width, height):
    """Creates each row of the player and computer player_grid using list comprehension and definable perameters"""

    global grid_width
    grid_width = width + 1
    global grid_height
    grid_height = height + 1

    global player_grid
    # creates a player_grid using list comprehension
    player_grid = [[0 for x in range(grid_width)] for y in range(grid_height)]

    global computer_grid
    computer_grid = [[0 for x in range(grid_width)] for y in range(grid_height)]

    global player_guess_grid
    player_guess_grid = [[0 for x in range(grid_width)] for y in range(grid_height)]

    global grid_top
    # creates the top line of the cordinates on the player_grid
    grid_top = [0 for x in range(grid_width)]

    global computer_grid_top
    computer_grid_top = [0 for x in range(grid_width)]

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

                if (int(player_row) + 1) > grid_height or (
                    int(player_column) + 1
                ) > grid_width:
                    print("The poition should be within the player_grid\n")
                    x -= 1
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

    while i <= 5:

        computer_row = random.randint(1, grid_height - 1)
        computer_column = random.randint(1, grid_width - 1)

        i += 1
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
    for x in range(len(ship_location)):
        # assigns the variable the location of the x axis
        player_row = ship_location[x][0]
        # assigns the variable the location of the y axis
        player_column = ship_location[x][1]
        # changes the inputed index into a 1
        player_grid[int(player_row)][int(player_column)] = 1

    print(NEW_LINE)


def computer_update_grid(computer_location):
    """updates the location of the computers ships using the computer_location
    index and iterating through using a for loop"""
    for x in range(len(computer_location)):
        computer_row = computer_location[x][0]

        computer_column = computer_location[x][1]

        computer_grid[computer_row][computer_column] = 2


def guess_update_grid_hit(guess_location):
    for each in range(len(guess_location)):
        guess_row = guess_location[each][0]

        guess_column = guess_location[each][1]

        player_guess_grid[int(guess_row)][int(guess_column)] = (
            ANSI_RED + str(0) + ANSI_WHITE
        )


def guess_update_grid_miss(guess_location):
    for x in range(len(guess_location)):
        guess_row = guess_location[x][0]

        guess_column = guess_location[x][1]

        player_guess_grid[int(guess_row)][int(guess_column)] = (
            ANSI_BLUE + str(0) + ANSI_WHITE
        )


def game_loop(location, ship_location):

    while location != [] or ship_location != []:

        player_turn(location)

        computer_turn(ship_location)


def player_turn(location):

    guess_location_hit = []
    guess_location_miss = []

    try:
        shot_row, shot_column = input(
            "Enter the location you would like to engage e.g 1,2\n"
        ).split(",")

        if computer_grid[int(shot_row)][int(shot_column)] == 2:
            index = location.index([int(shot_row), int(shot_column)])
            guess_location_hit.append([shot_row, shot_column])
            computer_grid[int(shot_row)][int(shot_column)] = 0

            print("You've sunk my battleship!!\n")
            location.pop(index)
            computer_update_grid(location)
            guess_update_grid_hit(guess_location_hit)
            cls()
            print_grid(player_guess_grid)
            print_grid(player_grid)

        elif computer_grid[int(shot_row)][int(shot_column)] == 0:
            print("Thats a miss try again\n")
            guess_location_miss.append([shot_row, shot_column])
            guess_update_grid_miss(guess_location_miss)
            cls()
            print_grid(player_guess_grid)
            print_grid(player_grid)

    except IndexError:
        print("Thats not wihtin player_grid limits try again\n")
    except ValueError:
        print("You need to enter a valid postion using the 'y,x' format")


def computer_turn(ship_location):

    computer_shot_row = random.randint(1, grid_height - 1)
    computer_shot_column = random.randint(1, grid_width - 1)

    if player_grid[computer_shot_row][computer_shot_column] == 1:
        index = ship_location.index([computer_shot_row, computer_shot_column])
        player_grid[computer_shot_row][computer_shot_column] = 0
        print("computer fires and destroys you battleship !!\n")
        ship_location.pop(index)
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
    custom_grid = setting_custom_grid_size()
    grid_setup(int(custom_grid[0]), int(custom_grid[1]))
    ship_location = setting_ship_location()
    computer_location = computer_ship_location()
    print_grid(player_grid)
    print_grid(computer_grid)
    game_loop(computer_location, ship_location)
    main_menu()


main_menu()

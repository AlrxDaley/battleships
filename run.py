import os

# Global variables
ANSI_WHITE = "\033[37m"
ANSI_RED = "\033[31m"
NEW_LINE = os.linesep

grid_width = 0
grid_height = 0


def main_menu():

    """Prints the starting menu for the game using inputs"""

    while True:
        print("-----------\nBATTLESHIPS\n-----------")
        print("1.Play Game\n2.Quit\n")

        selected = input("Select an option:\n")

        if selected == "1":
            print("Running Game\n")
            break
        elif selected == "2":
            quit()
        else:
            print("That isnt an option. Select another option")


def setting_custom_grid_size():

    """takes the input from user to define grid size"""

    print("\n-----------------------------------------")
    print("To set grid size please use 'Y,X' format")
    print("-----------------------------------------\n")
    while True:
        try:
            grid_width, grid_height = input(
            "Please enter your desired grid size (You cannot have more rows than columns):\n"
        ).split(",")
            return grid_width, grid_height,False
        except ValueError:
            print("You need to enter two values seperated by a ',' \n")

    


def print_grid():
    """Runs through each row checking if one of the index's is equal to 1 and turns it red and then prints the grid
    if the index does not equal 1 then it will be printed in black. It also prints the top row and the left column
    with the values of y so it dynamically changes the cordinates of the grid."""

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

    # Using os.linsep to ensure that the correct line seperator is used based on the OS the program is being run on e.g. \n
    print(row)

    for y in range(1, len(grid)):

        # Sets the first index of each row to y so the row numbers are icremeneted.
        try:
            grid[0][y] = y
        except IndexError:
            print("\nYou cannot have more rows then columns")
            break
        # Creates a string that starts with the row number surrounded by pipes.
        if y < 10:
            row = "| " + str(y) + "|"
        else:
            row = "|" + str(y) + "|"

        # the for loop , loops through each row within the grid range executing the code as it loops
        for x in range(1, len(grid[y])):
            # checks if any of the x indexs within each y row is equal to 1
            if grid[y][x] == 1:
                # If [x][y] is equal to 1 it applies the colour red to the x index of the y row and then reapplies the black colour
                row += " " + ANSI_RED + str(grid[y][x]) + ANSI_WHITE
            else:
                # if x does not equal 1 it adds the contents of grid[y][x] to the row string
                row += " " + str(grid[y][x])

            if x < grid_width:
                if x <= (grid_width - 2):
                    row += " "
                else:
                    row += ""

        # prints a square bracket at the end of each completed row.
        print(row + "|")
    print(NEW_LINE)


def grid_setup(width, height):
    """Creates each row of the grid using list comprehension and varible width and height to change the size of the grid"""

    global grid_width
    grid_width = width + 1
    global grid_height
    grid_height = height + 1

    global grid
    # creates a grid using list comprehension
    grid = [[0 for x in range(grid_width)] for y in range(grid_height)]
    global grid_top
    # creates the top line of the cordinates on the grid
    grid_top = [0 for x in range(grid_width)]
    print_grid()


def setting_ship_location():
    """Takes the input of the cordinates given by the user and adds them to a string and then returns them to be used in another function"""

    ship_location = []
    print("------------------------------------------")
    print("To enter the location use the 'Y,X' format")
    print("------------------------------------------\n")

    while True:
        # loops through the amount of boats you can assign
        try:
            for x in range(5):
                # Assigns the inputed data to the variables
                yship, xship = input(str(f"Please select the location for ship num {x+1}\n")).split(
                    ","
                )

                if (int(yship) + 1) > grid_height or (int(xship) + 1) > grid_width:
                    print("The poition should be within the grid\n")
                    yship, xship = input(f"Please select the location for ship num {x+1}\n").split(
                    ","
                    )
                    ship_location.append([yship, xship])
                    
                else:
                    # Assigns the variables to the location list
                    ship_location.append([yship, xship])

            # return the ship location list
            return ship_location,False
        except ValueError:
            print("You need to enter two values seperated by a ',' \n")


def update_grid(ship_location):
    """Updates the inputed location of the ship using the ship_location variable/list"""
    for x in range(len(ship_location)):
        # assigns the variable the location of the x axis
        ship_y = ship_location[x][0]
        # assigns the variable the location of the y axis
        ship_x = ship_location[x][1]
        # changes the inputed index into a 1
        grid[ship_y][ship_x] = 1

    print(NEW_LINE)
    print_grid()


def main():
    main_menu()
    custom_grid = setting_custom_grid_size()
    grid_setup(int(custom_grid[0]), int(custom_grid[1]))
    ship_location = setting_ship_location()
    update_grid(ship_location)


main()


def main_menu():

    """Prints the starting menu for the game using inputs"""

    while True:
        print("-----------\nBATTLESHIPS\n-----------")
        print("1.Play Game\n2.Select grid size\n3.Quit\n")

        selected = input("Select an option:\n")

        if selected == '1':
            print("Running Game\n")
            break
        elif selected == '2':
            print("Setting Grid Size")
            break
        elif selected == '3':
            quit()
        else:
            print("That isnt an option. Select another option")

def print_grid():
    """Runs through each row checking if one of the index's is equal to 1 and turns it red and then prints the grid
    if the index does not equal 1 then it will be printed in black. It also prints the top row and the left column
    with the values of y so it dynamically changes the cordinates of the grid."""

    for x in range(len(grid_top)):
        grid_top[x] = x
    print(grid_top)
 
    for y in range(1,len(grid)):
        #Sets the first index of each row to y so the rows are dynamically numbered.
        grid[0][y] = x
        #Creates a string to format each row so that there is a square bracket at the beginning an a comma between the row number and the first index.
        row = "[" + str(y) + ", "
        #the for loop , loops through each row within the grid range exicuting the code as it loops
        for x in range(1,len(grid[y])):
            #checks if any of the x indexs within each y row is equal to 1
            if grid[y][x] == 1:
                # If x is equal to 1 it applies the colour red to the x index of the y row and then reapplies the black colour to the seperating comma
                row += "\033[31m" + str(grid[y][x]) + "\033[37m" + ", "
            else:
                # if x does not equal 1 it adds the x index of the y row and then a seperating comma.
                row += str(grid[y][x]) + ", "
            
        #prints a square bracket at the end of each completed row.
        print(row + "]")


def grid_setup(width,height):
    """Creates each row of the grid using list comprehension and varible width and height to change the size of the grid"""
    global grid 
    #creates a grid using list comprehension
    grid = [[0 for x in range(width + 1)] for y in range(height +1)]
    global grid_top
    #creates the top line of the cordinates on the grid
    grid_top = [0 for x in range(width +1)]
    print_grid()

def setting_ship_location():
    """Takes the input of the cordinates given by the user and adds them to a string and then returns them to be used in another function"""
    ship_location = []
    print("------------------------------------------")
    print("To enter the location use the 'Y,X' format")
    print("------------------------------------------\n")

    #loops through the amount of boats you can assign
    for x in range(5):
        #Assigns the inputed data to the variables
        yship,xship = input(f"Please select the location for ship num {x+1}\n").split(",")
        #Assigns the variables to the location list
        ship_location.append([yship,xship])

    #return the ship location list
    return ship_location

def update_grid(ship_location):
    """Updates the inputed location of the ship using the ship_location variable/list"""
    for x in range(len(ship_location)):
        #assigns the variable the location of the x axis
        ship_x = ship_location[x][0]
        #assigns the variable the location of the y axis
        ship_y = ship_location[x][1]
        #changes the inputed index into a 1
        grid[(int(ship_x))][int(ship_y)] = 1

    print("\n")
    print_grid()



def main():
    main_menu()
    grid_setup(9,9)
    ship_location = setting_ship_location()
    update_grid(ship_location)

main()
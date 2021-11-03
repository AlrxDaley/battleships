
def main_menu():

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


def grid_setup(width,height):
    grid = [[0 for x in range(width + 1)] for y in range(height +1)]
    grid_top = [0 for x in range(width +1)]

    for x in range(len(grid_top)):
        grid_top[x] = x
    print(grid_top)
 
    for x in range(1,len(grid)):
        grid[x][0] = x
        grid_container = grid
        print(grid_container[x])

    print("\n")

    return grid_container


def setting_ship_location():
    
    ship_location = []

    for x in range(5):
        xship = input("Please select the y location of your ship:\n")
        yship = input("Please select the x location of your ship:\n")
        ship_location.append([xship,yship])
        
    return ship_location

def update_grid(grid,ship_location):

    for x in range(len(ship_location)):
        ship_x = ship_location[x][0]
        ship_y = ship_location[x][1]
        grid[(int(ship_x))][int(ship_y)] = 4

    print(grid)



def main():
    main_menu()
    grid = grid_setup(9,9)
    ship_location = setting_ship_location()
    update_grid(grid,ship_location)

main()
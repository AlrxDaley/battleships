

def main_menu():

    while True:
        print("-----------\nBATTLESHIPS\n-----------")
        print("1.Play\n2.Select grid size\n3.Quit\n")

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
    grid = [[0 for x in range(width)] for y in range(height)]

    for x in range(len(grid)):
        print(grid[x])
            


def main():
    main_menu()
    grid_setup(6,6)

main()
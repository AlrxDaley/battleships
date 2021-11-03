

def main_menu():

    while True:
        print("-----------\nBATTLESHIPS\n-----------")
        print("1.Play\n2.Select grid size\n3.Quit\n")

        selected = input("Select an option:\n")

        if selected == '1':
            print("Running Game")
            break
        elif selected == '2':
            print("Setting Grid Size")
            break
        elif selected == '3':
            quit()
        else:
            print("That isnt an option. Select another option")
            





main_menu()
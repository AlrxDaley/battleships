# Command line Battleships

command line battleships is a battleship game written in python and played in the terminal, which uses the code institute mocmk terminal to run
in heroku.

The aim of the game is to destroy all of the computers battleships before it destroys all of yours.

["Link to live terminal"](https://cdbattleships.herokuapp.com/)

![how it looks on a web page](images\web_page_image.png)

## Rules/How to play
---
Command line battlehips is based on the classic battleships game.

This game works by having you that player define the size fo the grid 
then enter the cordinates of you ships using the "y,x" format.

This then displays a board with all of your ships marked on it and 
another input request that asks what cordinates you would like to engage.

It will then display your grid and the guesses you have made on the enemy grid 
but you wont see where the enmey ships are unless you have hit them.

You and the computer will each take turns untill either you or the computer
have destroyed all enemy ships.

## Features
---
- Definable grid size
    - you get to place your ships
    - you cannot see the enemy ships unless they are hit

- Personal guess grid to show you where you have guessed and if its a hit or a miss
- You play against the computer 
- Accepts user inputs for multiple functions

- Error checking
    - Cannot enter random characters that dont conform to the proper format
    - You cannot place multiple ships ontop of each other


## Future features
---
- Have ships longer then one cell.
- Have the amount of ships definable by the player.
- Have a custom AI for the computer that can make logical informed guesses.
- Fluid display of information.
- Apply more object orianted coding values such as classes to simplify some aspects
- Show the computers guesses so you can track where they are firing


## Data Model
---
I decided to use list comprehension and 2d arrays to hold the player , computer and guess information.

Lists are used to store the locations of the players ships, enemy ships and the guess locations  and global variables that are defined 
by the player to store the grid size.

## Testing
---
- I have tested this project by:
    - Passing thr code through the pycodestyle (PEP8) linter and found the error e(501) but this was due to 
    the linter thinking the lines where to long but there was no significant errors.
    - Entered invalid inputs when a certain format was expected , grid locations where not within the limits and when you try to place two boats in 
    the same location. all of these were met with the expected error handling features.
    - Tested on my local terminal and on the heroku terminal.

### Bugs
---
Sloved Bugs:
- when a function was called inside of a for loop i restarted the for loop:
    - i fixed this buy using a while loop and incrementation to control the iteration better

- When adding the ship locations to the list if you had entered an input that didnt conform to the format it was still added to the list:
    - i fixed this buy adding a check to see if the input matched the standard formatting and if it didnt they had to re input their 
    answer correctly. if it did match the format the program would carry on like usual.
---
unsloved bugs:
- when creating the grid you cannot make the grid height greater then the grid width:
    - i have stopped errors breaking the code by addinf if statment to catch the errors and create a pre defined grid size.

- if you enter an invalid location when the player moves it just moves onto the computers turn and doesn’t let the user try again   

-  If I reuse a location that was a hit on the computer ship, it says miss and turns the location blue. Should say you’ve already guessed that location

### Validator Testing
---
- PEP8
    - Only error was E501 (Line too long)

## Deployment
---
This Project was deployed using code institutes mock terminal for heroku.
- Steps for deployment:
    - Fork or clone repository
    - Create a new Herokuy app
    - Set the buildpacks to 'python' and 'nodeJS' in that order
    - link the Heroku app to the repository
    - Click deploy

## Credits
---
- Code insitute for deployment terminal
- Wikipedia for the details on the battleship game
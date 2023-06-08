# Index - Table Of Contents:

1. [General Information](#About-everything-DESI)
2. [How To Play](#How-To-Play)
3. [Features](#Features)
4. [Technologies Used](#Technologies-Used)
5. [Coding Approach](#Coding-Approach)
6. [Testing](#Testing)
7. [Bugs](#Bugs)
8. [Unfixed bugs](#Unfixed-Bugs)
9. [Validator Testing](#Validator-Testing)
10. [Deployment](#Deployment)
11. [Credits](#Credits)

# About Mastermind-Code-Breaker
Mastermind-Code Breaker game is a Python terminal game, which runs on the Code Institute mock terminal on Heroku

Users will get an unknown code of 3, 4 or 5 colors depending on the difficulty.
Users will have to crack the code in 8 attempts in order to win the game

[Mastermind-Code Breaker Live app](https://mastermind-code-breaker-game.herokuapp.com/)

![Responsive image](/images/amiresponsive.png)
# How To Play
Mastermind-Code Breaker is a classic [Mastermind(Board Game)](https://en.wikipedia.org/wiki/Mastermind_(board_game)) .

In this version, the user will be given the level choice of easy, medium or difficult.

Easy level will have three colors long code, medium and difficult will have four and five colors respectively.

There will be 8 attempts to crack the code. User will be told how close they are if they don't get the exact code.

The clue will be given in the form of 'Hits' and 'Misses':

Hits -> If the user gets a right color on exact position
Misses-> If the user gets the right color but on different position

If user cracks the code in 8 attempts, they have won the game.

# Features
* Username Input

  * This is the first page user will interact with

  * User will have to enter his/her name

  * Wrong name (with space/wrong character) Will give error and user will be asked to enter the name again

    ![Username-input](/images/username_input.png)

* Welcome

  * After the name is entered, the user will be welcome

  * There will be two options displayed to navigate the game (Instruction or Menu)

    ![Welcome](/images/welcome_page.png)

* Instruction Page

  * This page displays the complete instruction about the game to help user to understand

    ![Instruction](/images/instruction.png)

* Menu

  * This page displays all the options for Level difficulty, scoreboard and to exit the game

    ![Menu](/images/menu.png)

* Levels

  * These are the gameboards for easy, medium and difficult levels, with three, four and five colors long code respectively

    ![Level-Easy](/images/easy_gameboard.png)
    ![Level-Medium](/images/medium_gameboard.png)
    ![Level-Difficult](/images/difficult_gameboard.png)

* Attempts-made

  * When the user makes an attempt, the number of attempt, clue and the color codes entered by the user are displayed

    ![Attempts](/images/attempts.png)

* Result

  * When the user is able to crack the code in less than or equal to 8 attempts, the score is displayed with 'Congratulations' message

  * When the user is unable the crack the code, a 'Lose' message is displayed with score '0' 

  * Score calculation: (10-(no_of_attempts-1))*10

    ![Win](/images/win.png)
    ![Lose](/images/lose.png)

* ScoreBoard

  * The sccoraboard is displayed with 10 top scores, the list is sorted in descending order, so that the highest score is on top

  * The top 3 are ranked as 1st, 2nd and Third

  * The score is stored in a spreadsheet with username and level difficulty

    ![ScoreBoard](/images/scoreboard.png)
    ![SpreadSheet](/images/sheet.png)

* Exit

  * There are several options given to user to exit the game
  * user can exit the game when still in the play or when on menu page
  
# Future Features
  * Score calculation based on level difficulty
  
  * Number of attempts veried according to level difficulty
  
  * Options to play solo, with computer or another player
# Coding Approach
  * I used methods to create all the features of the app and a class to store score and update spreadsheet
  
  * The score class stores the name, score and level in spreadsheet by calling the update method 
  
  * Different methods are called to perform a certain task such as: Taking input, choose an option, calculate score or display result
  
  * All methods are atomic
  
  * The app is run by calling "welcome()" method

# Technologies Used

#### Languages Used

* Python

#### Modules Used

* gspread
* os
* sys
* time
* random
* colorama
* operator
* google.auth


# Testing

* I tested the live app on different browsers such as Microsoft Edge, Opera, Firefox, Chrome, and Safari and it works on all browser
* I have also done manual testing for every features, every feature works as expected
* Especially for input validation, by giving wrong inputs (wrong number of inputs, integer instead of string, duplicate inputs etc), 
  the app handles every input ver well
* Tested in my local terminal and Code Institute Heroku terminal


# Bugs
* There were many errors were coming as project was progressing, all errors were solved as the projects moved forward
* A logical error appeared with number of attempts, only 7 attempts were displayed on gameboard, I solved the error by updating "attempts+1"
* welcome() function was giving unexpected output due to wrong indentation
* The PEP8 validator gave errors with whitespace, trailing whitespaces and character count
* All errors were removed

# Unfixed Bugs
* No bugs remaining

# Validator Testing
* [PEP8 Python Validator](https://pep8ci.herokuapp.com/)
   * PEP8 shows no errors or warning

![Python Validator](/images/validator.png)

# Deployment
- This project is deployed using Code Institute's mock terminal on Heroku, steps for deployment:
  - Fork or clone this repository
  - Create a new Heroku app
  - Add Variables -> creds.json and PORT
  - Set the builpacks to **Python** and **NodeJS**
  - Link the Heroku app to repository
  - Click on **Deploy**

The live link can be found here -[Live App](https://mastermind-code-breaker-game.herokuapp.com/)

# Credits
* Content
  * [StudyTonight](https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python) helped me to add color in text in python
  * [w3schools](https://www.w3schools.com/python/ref_string_center.asp) helped me to print string in centre of screen
  * [StackOverflow](https://stackoverflow.com/questions/11178061/print-list-without-brackets-in-a-single-row) helped me to print list without bracktes or colons
  * [StackOverflow](https://stackoverflow.com/questions/67172409/is-there-a-way-to-color-individual-elements-in-a-list-in-python) helped me to reset colored string color
  * [SimpliLearn](https://shorturl.at/gklp5) helped me to convert list to string
  * [Finxter](https://blog.finxter.com/how-to-print-underlined-text-in-python/) helped me to write code for underline text
  * [W3schools](https://www.w3schools.com/python/ref_string_format.asp) hepled me to learn string formatting
  * [w3schools](https://www.w3schools.com/), [StackOverflow](www.stackoverflow.com),  and Code Institute's walkthrough project [Love Sandwiches](https://github.com/Sadaf-Tariq/LoveSandwiches) helped me so much throughout my project




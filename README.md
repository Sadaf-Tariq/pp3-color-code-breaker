# Index - Table Of Contents:

1. [General Information](#About-everything-DESI)
2. [How To Play](#How-To-Play)
3. [Features](#Features)
4. [Technologies Used](#Technologies-Used)
5. [Testing](#Testing)
6. [Bugs](#Bugs)
7. [Unfixed bugs](#Unfixed-Bugs)
8. [Validator Testing](#Validator-Testing)
9. [Deployment](#Deployment)
10. [Credits](#Credits)

# About Mastermind-Code-Breaker
Mastermind-Code Breaker game is a Python terminal game, which runs on the Code Institute mock terminal on Heroku

Users will get an unknown code of 3, 4 or 5 colors depending on the difficulty.
Users will have to crack the code in 8 attempts in order to win the game

[Mastermind-Code Breaker Live app](https://mastermind-code-breaker-game.herokuapp.com/)

![Responsive image](/images/amiresponsive.png)
# How To Play
Mastermind-Code Breaker is a classic [Mastermind(Board Game)](https://en.wikipedia.org/wiki/Mastermind_(board_game).

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

  * The gallery link on the navigation bar takes the user to the gallery page where there are images available for the users 

  * The gallery images of food served by everything DESI and their catering service give a clear picture to users to make an informed decision

    ![ScoreBoard](/images/scoreboard.png)

* The Contact-us Page

  * The contact-us link on the navigation bar takes the user to the Contact us page, which consists of two sections. The contact section encourages the user to keep in contact and provides a phone number, email address, and street address where they can be found

  * It also includes information about its opening to help the users to know when they should be contacted

  * The enquiry section has a form for the users to give all the relevant information about the enquiry they want to make. This form feature establishes a connection between the user and the site

    ![The contact us page](/images/contact.png)

  * When the user presses the submit with all the information, they are taken to a Thank you window, further, emphasizing interaction 

    ![Thank you window](/images/thankyou.png)
# Technologies Used

#### Languages Used

* Python

# Testing

* I tested the website on different browsers such as Microsoft Edge, Opera, Firefox, Chrome, and Safari and it works on all browser
* I confirm that this project is responsive, functions on all standard screen sizes, tested responsiveness using the developer tools, and looks good 

<img src="/images/responsive(1).png"  width="750" height="500"> <img src="/images/responsive(2).png"  width="300" height="500"> <img src="/images/responsive(3).png"  width="500" height="700">

* I confirm that the header, navigation bar, highlights, footer, menu, and form text are all readable and easy to understand
* I have confirmed that the form works: requires entries in every field, will only accept emails in an email field, and the submit button works

# Bugs
* When I tested my HTML code for the index.html page on html validator, I got the error that one of the div element was unclosed which was causing another section to give another error, I solved the problem by removing that div element
* Another error I found for the menu.html page, where I put an anchor element inside a button element, I solved that error by replacing the button to form 
* For the style.css for the header element in a media query, I got an error because there was a margin selector that had a negative value, I solved that error by removing that selector

# Unfixed Bugs
There is no unfixed bugs but there is a warning indicated by html validator for gallery.html page of the website, for my design I do not need any header for this section of the page that is why this warning was not entertained
![Warning Image](/images/warning.png)

# Validator Testing
* HTML
  * No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)
* CSS
  * No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
* Accessibility
  * I confirmed that the colors and fonts chosen are easy to read and accessible by running it through lighthouse in developer tools

    ![Lighthouse report](/images/lighthouse.png)

# Deployment
- The site was deployed to GitHub pages. The steps to deploy are as follows:
  - In the GitHub repository, navigate to the Settings tab
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The live link can be found here - https://sadaf-tariq.github.io/pp1-everythingdesi/

# Credits
* Content
  * [Font awesome](https://fontawesome.com/) provided the icon for my header and cover text on the hero-image element
  * [w3schools](https://www.w3schools.com/) helped me in creating my form
  * [w3schools](https://www.w3schools.com/) helped me in creating my button for the menu page
  * [StackOverflow](www.stackoverflow.com) helped me to create a custom bottom border on the speciality section heading
  * [StackOverflow](www.stackoverflow.com) helped me to remove the error I was getting for an anchor element inside the button element
  * The code for the social media link for the footer was taken from Code Institute [Love Running](https://github.com/Sadaf-Tariq/love-running/blob/main/index.html) project
  * The text for the home page was taken from [Wikipedia](www.wikipedia .com) and some open-source sites
  * The logo image for the website was taken from [Wix](www.wix.com)
  * I got the inspiration for the website from Zouq restaurant, Koyla restaurant, and David Smyth Catering
  * [w3schools](https://www.w3schools.com/), [StackOverflow](www.stackoverflow.com),  and Code Institute's walkthrough project [Love Running](https://github.com/Sadaf-Tariq/love-running) helped me so much throughout my project

* Media
  * The images used in the website were taken from [Pexels](https://www.pexels.com/)



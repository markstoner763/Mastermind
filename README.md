# Mastermind

## Game Overview and Rules

This program is based on the game "Mastermind," first released in 1970. In this game, there are two players - the Codemaker, and Codebreaker. In this app, the program serves as the Codemaker, and the user plays as the Codebreaker.

The Codemaker creates a code that involves 4 "Code pegs." Each code peg has a relevant color, and respective position. The Codebreaker then has 10 chances to guess this code, and they must guess BOTH the color of each peg, and their exact order.

For instance, if the Codemaker chose this code:

> Red Black Yellow Blue

It would not be enough for the Codemaker to guess the four correct colors; they would also have to guess the exact order of "Red Black Yellow Blue," in order to win the game. 

Please note that a color may be chosen more than once, as there is no rule against duplicates.

For example:

> Green Green Green Green

would be a valid code for the Codemaker to choose.

## User Feedback

The Codemaker/user is not expected to guess this code without any assistance at all, however. After each guess, the Codemaker/app provides the user with feedback as the accuracy of their guess.

In the original game, the Codemaker player has little "Key Pegs" for this purpose, but in the app, the feedback is simply written for the user to read.

There are two specific elements to this feedback:

1. The Codemaker is told how many of their guessed colors is BOTH the correct color AND position, in the secret code.

2. The Codemaker is then told how many their guessed colors are the correct color, but NOT in the correct position.

## _To illustrate:_

If the Codemaker's code was as such:

> Blue Blue Yellow White

And the Codebreaker's guess was as follows:

> Blue Red Black Yellow

The user would then receive this feedback:

> "1 of your guesses is the correct color, in the correct position."
> "1 of your guesses is the correct color, but not in the correct position."

The first feedback line refers to the first "Blue" entry in the secret code, which the Codemaker has guessed correctly in both its color and position.

The second feedback line refers to the "Yellow" entry in the secret code, as while the Codemaker correctly guessed that Yellow is in the secret code, they do not have the correct position for Yellow, currently.

## Running this Program

This program works in Python 3, and may be run as such in a terminal:

```sh
python3 main.py
```

Once running, the program will generate a secret code in the background, and prompt the user to begin guessing the code. Making an attempt is as easy as typing four colors (separated by spaces), and hitting Enter/Return to submit the answer.

From there on out, it will be a maximum of 10 attempts offeered by the program, to guess the code.

Best of luck, and happy codebreaking!
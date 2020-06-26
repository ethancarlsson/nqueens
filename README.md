# nqueens
My nqueens solution

These are two short programs that solve the nqueens problem in python. 

The first uses the random module to brute force the problem and because of this it technically could solve the problem much faster than other solutions, but it could also take an infinite amount of time to solve even the 4 queens problem. The program will ask you how big you want the board to be. If you input an integer it will randomly search for the first solution to the problem. It can only find one solution.

The second uses itertools to find all possible solutions. It usually takes longer than the first solution but it will find all possible solutions to the problem. The GUI will also tell you how many solutions were found and allow you to cycle through them.

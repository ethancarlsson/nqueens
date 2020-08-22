# nqueens
My nqueens solution

These are few programs that solve the nqueens problem in python. 

<h2> nqueensrandomsolution </h2>
The first uses the random module to solve the problem and because of this it technically could solve the problem for any sized board immediately. However, it could also technically run fro an infinite amount of time for even the smallest board sizes.

<h2> nqueensitertoolssolution </h2>
The second uses permutations from the itertools module to find all possible solutions.

It uses a list with every number in range n; the number will represent a column to place the queen in and the position of the number will represent a row to place the queen in. This prevents the need to check for collisions along columns or rows. 

It will then create all permutations of this list, place it on the board and check for collisions along the diagonals. Because it has to create and check every possible board it has a higher than linear time complexity

<h2> solution_producer </h2>
This program doesn't solve the problem itself. Instead it creates a program that can solve the problem, it has the same structure as the itertoolssolution, but it is a lot faster. It does the following: 
<ul>
  <li> it calls upon the <b>condition_producer</b>: 
    <li> the condition_producer creates a series of text files containing an if statement. The if statement contains all possible collisions within a n sized list.</li>
   <li> It then appends all of these if statements after each permutation of the queen list. 
The produced program does not need to check for collisions and queens will only be placed on the board when it is already certain that there will be no collisions. Because of this it is much faster than the other solutions. It still has a roughly linear time complexity because it still needs to generate every permutation. </li>
</li>
</ul>
To use this solution you need to first run the solution producer and then run the produced solution program. 

<h2> solution_producer_withlistcomp </h2> 
This is the same as the solution_producer but it uses list comprehensions to speed everything up. 

<h2> How to make it faster </h2> 
All of the time that the program takes is related to the speed of producing permutations. Finding ways to speed up the permutations will be the best way to improve the speed of the program. 

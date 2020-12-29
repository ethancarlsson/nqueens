# nqueens
My nqueens solution

These are few programs that solve the nqueens problem in python. I have been working on them since I started learning to program and they show my progress in a number of ways. I will explain each solution below as well as their strengths and weaknesses. 

<h2> nqueensrandomsolution </h2>
<p>
This was my very first attempt to solve the problem the program will find the solution by randomly placing the queens and then checking to see if they connect on the diagonals.
</p>
<p>
You can tell I was still new to programming (I didn't really know what "self" meant so i just stuck it in the function because thats what they do in the tutorials), but it set the stage for how I began solving the problems in later iterations. The most relevant success I had here was that I made the board a 2d list in which each column was represented by an integer: 
      </p>

<code>
  [         
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 1, 2, 3, 4, 5, 6, 7],
    [0, 1, 2, 3, 4, 5, 6, 7],
  ]
</code>

<p>
This isn't groundbreaking but it meant I could create a list and randomly shuffle it to decide where the queens should be placed based on their position on the list rather than placing them on each individual list within the 2d array: 
 </p>
 <p>
<code>
      row_index_storage = list(range(self))
      random.shuffle(row_index_storage)
</code>
  </p>
<p>
  This meant that I only needed to check for colisions along the diagonal and not the columns.
</p>
<h3> Strengths </h3>
<ul>
  <li>
    Can potentially solve any size board immediately through random luck.
  </li>
 </ul>
<h3> Weaknesses </h3>
<ul>
  <li>
    Can potentially never solve even the smallest boards, and in practice it is very unlikely to succesfully find solutions on larger boards. 
  </li>
  <li>
    Only finds one solution and there is no way to tell if you have found all possible solutions for an n sized board. 
  </li>
 </ul>
<h3> How to use </h3>
<h5> Microsoft </h5>
<code> ...\nqueens> python nqueensrandomsolution.py </code>

<h2> itertoolssolution </h2>
<p>
This is actually a brute force solution, but I named it this way because I was using the itertools package and learning about generators at the time. It will find all possible solutions but it will take a very long time to do so. 
</p>
<h3> Strengths </h3>
<ul>
  <li>
    Will find all solutions.
  </li>
 </ul>
<h3> Weaknesses </h3>
<ul>
  <li>
    Is quite slow . 
  </li>
  <li>
    Only finds one solution and there is no way to tell if you have found all possible solutions for an n sized board. 
  </li>
 </ul>
<h3> How to use </h3>
<h5> Microsoft </h5>
<code> ...\nqueens> python nqueensitertoolssolution.py.py </code>


<h2> conditionproducer </h2>
<p>
This was my first attempt to really speed up the program. The correct path would have been to write a recursive backtracking algorithm, however I wanted to achieve the same thing with the diagonals as the rows and columns and simply not evaluate the diagonals. This isn't possible, but to get close to this I created a program which found all possible collisions on an n sized board and then wrote the program that solved the problems by preventing the placement of the queen with a long if statement.

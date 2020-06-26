from tkinter import *
from tkinter import ttk
import numpy
import random
from itertools import permutations

def boardmaker(self):
    solutions = []
    how_many_times = 0

    all_possibilities = []
    row_index_generator = permutations(list(range(self)))

    for generation in row_index_generator:
        columns = list(generation)
        all_possibilities.append(columns)

    for possibility in all_possibilities:
        how_many_times +=1
        rows = []
        counter = 0

        for i in range(self):
            rows.append(list(range(self)))
        
        
        for row in rows:
            index = possibility[counter]
            row[index] = 'x'
            counter+=1
        counter = 0-self
        diagonals = []
        for row in rows:
            diagonal_right = numpy.diagonal(rows,offset=counter)
            diagonals.append(list(diagonal_right))
            
            counter+=1
        for row in rows:
            diagonal_right = numpy.diagonal(rows,offset=counter)
            diagonals.append(list(diagonal_right))
            counter+=1
        counter = 0-self
        reversed_chessboard = numpy.fliplr(rows)
        for row in reversed_chessboard:
            diagonal_left = numpy.diagonal(reversed_chessboard,offset=counter)
            diagonals.append(list(diagonal_left))
            counter+=1
        for row in reversed_chessboard:
            diagonal_left = numpy.diagonal(reversed_chessboard,offset=counter)
            diagonals.append(list(diagonal_left))
            counter+=1
        
        collisions = 0
        for diagonal in diagonals: 
            x_in_diagonal = diagonal.count('x')
            if x_in_diagonal <= 1:
                pass
            else: 
                collisions+=1
        if collisions == 0:
            solutions.append(rows)
    return solutions    




root = Tk()
title_frame = Frame(root)
frame1 = Frame(root)
frame2 = Frame(root)
title_frame.pack()
frame1.pack()
frame2.pack()

ttk.Label(title_frame, text='Choose your board size and then click "Find solutions" to find every possible solution to the nqueens problem for that board size.').pack()

board_size = ttk.Spinbox(frame2, from_=4, to_=100)
board_size.grid(column=0, row=0)

def SolutionFunction():
    boardsize = board_size.get()
    chessboard = boardmaker(int(boardsize))


    ttk.Label(frame2, text='We found {} solutions'.format(len(chessboard))).grid(column=0, row=3)

    solution_generator = (n for n in chessboard)
    

    def NextSolution():
        next_solution = next(solution_generator)
        odd_or_even = 1
        for row in next_solution:
            if odd_or_even % 2 == 0:
                for square in row:
                    if square == 'x':
                        Frame(frame1, height=20, width=20, bg='red').grid(column=row.index(square), row=odd_or_even)
                    elif square  % 2 == 0:
                        Frame(frame1, height=20, width=20, bg='black').grid(column=square, row=odd_or_even)
                    else:
                        Frame(frame1, height=20, width=20, bg='white').grid(column=square, row=odd_or_even)
            else:
                for square in row:
                    if square == 'x':
                        Frame(frame1, height=20, width=20, bg='red').grid(column=row.index(square), row=odd_or_even)
                    elif square  % 2 == 0:
                        Frame(frame1, height=20, width=20, bg='white').grid(column=square, row=odd_or_even)
                    else:
                        Frame(frame1, height=20, width=20, bg='black').grid(column=square, row=odd_or_even)
            odd_or_even+=1
    NextSolution()
    ttk.Button(frame2, text='Show next solution', command=NextSolution).grid(column=0, row=2)



solution_button = ttk.Button(frame2, text='Find solutions', command=SolutionFunction).grid(column=0, row=1)


root.mainloop()
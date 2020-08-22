from condition_producer import possible

for i in range(3, 20):
    possible(i)

conditions = []

for i in range(4,20):
    with open(f'if_statements{i}.txt', 'r') as if_statements:
        statements = if_statements.read()
        statements = statements[:-4]
        conditions.append(statements + '== True:')

first_if_conditions = conditions.pop(0)
with open('produced_solutions.py','w') as produced_solutions:

    produced_solutions.write(f'''
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
        possibility = list(generation)
        how_many_times +=1
        counter = 0
        if self == 4:
            {first_if_conditions}

                rows = [list(range(self)) for i in range(self)]    

                for row in rows:
                    index = possibility[counter]
                    row[index] = 'x'
                    counter+=1

                solutions.append(rows)
''')
    counter = 5
    for condition in conditions:
        produced_solutions.write(f'''
        if self == {counter}:
            {condition}

                rows = [list(range(self)) for i in range(self)]

                for row in rows:
                    index = possibility[counter]
                    row[index] = 'x'
                    counter+=1
                solutions.append(rows)
            ''')
        counter+=1
    produced_solutions.write('''
    return solutions


root = Tk()
title_frame = Frame(root)
frame1 = Frame(root)
frame2 = Frame(root)
title_frame.pack()
frame1.pack()
frame2.pack()

ttk.Label(title_frame, text='Choose your board size and then click "Find solutions" to find every possible solution to the nqueens problem for that board size.').pack()

board_size = ttk.Spinbox(frame2, from_=4, to_=20)
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
''')
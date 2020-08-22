from tkinter import *
from tkinter import ttk
import numpy
import random

def boardmaker(self):
    queen_can_kill = True
    while queen_can_kill == True:
        rows = []
        counter = 0

        for _ in range(self):
            rows.append(list(range(self)))
        
        
        row_index_storage = list(range(self))
        random.shuffle(row_index_storage)
        
        for row in rows:
            index = row_index_storage[counter]
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
            queen_can_kill = False
            return rows

while True:
    try:
        x = int(input('how big is the board? '))
        if x<=3: 
            print('It is not possible to solve nqueens if you choose a number lower than 3. Please choose a number higher than 3.')
            pass
        else:
            break
    except ValueError:
        print('You need to select a whole number. Please try again with a whole number.')
        pass
        


chessboard = boardmaker(x)
print(chessboard)

root = Tk()
odd_or_even = 1
for row in chessboard:
    if odd_or_even % 2 == 0:
        for square in row:
            if square == 'x':
                Frame(root, height=20, width=20, bg='red').grid(column=row.index(square), row=odd_or_even)
            elif square  % 2 == 0:
                Frame(root, height=20, width=20, bg='black').grid(column=square, row=odd_or_even)
            else:
                Frame(root, height=20, width=20, bg='white').grid(column=square, row=odd_or_even)
    else:
        for square in row:
            if square == 'x':
                Frame(root, height=20, width=20, bg='red').grid(column=row.index(square), row=odd_or_even)
            elif square  % 2 == 0:
                Frame(root, height=20, width=20, bg='white').grid(column=square, row=odd_or_even)
            else:
                Frame(root, height=20, width=20, bg='black').grid(column=square, row=odd_or_even)
    odd_or_even+=1


root.mainloop()
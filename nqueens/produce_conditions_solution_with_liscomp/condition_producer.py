from itertools import combinations
import numpy


def possible(self):
    rows = []

    for _ in range(self):
        rows.append(list(range(self)))

###diagonals 

    diagonals1 = []
    diagonals2 = []
    counter = 0-self
    ## diagonals1
    for row in rows:
        diagonal_right = numpy.diagonal(rows,offset=counter)
        diagonals1.append(list(diagonal_right))
        counter+=1
    for row in rows:
        diagonal_right = numpy.diagonal(rows,offset=counter)
        diagonals1.append(list(diagonal_right))
        counter+=1
    ### other diagonals/flipped/diagonals2
    counter = 0-self
    reversed_chessboard = numpy.fliplr(rows)
    for row in reversed_chessboard:
        diagonal_left = numpy.diagonal(reversed_chessboard,offset=counter)
        diagonals2.append(list(diagonal_left))
        counter+=1
    for row in reversed_chessboard:
        diagonal_left = numpy.diagonal(reversed_chessboard,offset=counter)
        diagonals2.append(list(diagonal_left))
        counter+=1
    #diagonals1
    dictionary = {}
    for number in range(self):
        dictionary.update({number:-1})
    diagonal_map_list = []
    for diagonal in diagonals1:
        for square in diagonal: 
            square_count = dictionary.get(square)
            square_count = square_count+1
            dictionary.update({square:square_count})
        diagonal_map = [(dictionary.get(i), i) for i in diagonal]
        diagonal_map_list.append(diagonal_map)
    
    #diagonals2
    dictionary = {}
    for number in range(self):
        dictionary.update({number:-1})
    for diagonal in diagonals2:
        for square in diagonal: 
            square_count = dictionary.get(square)
            square_count = square_count+1
            dictionary.update({square:square_count})
        diagonal_map = [(dictionary.get(i), i) for i in diagonal]
        diagonal_map_list.append(diagonal_map)
    count = 0
    
    diagonal_clashes = []
    for diagonal in diagonal_map_list:
        x = combinations(diagonal,2)
        for i in x:
            count+=1
            diagonal_clashes.append(i)
        
    with open(f'if_statements{self}.txt','w') as if_statement_file:
        if_statement_file.write('if ')
        for clash in diagonal_clashes:
            row1 = clash[0][0]
            column1 = clash[0][1]
            row2 = clash[1][0]
            column2 = clash[1][1]

            
            if_statement_file.write(f'((possibility[{row1}] == {column1} and possibility[{row2}] == {column2}) == False) and ')


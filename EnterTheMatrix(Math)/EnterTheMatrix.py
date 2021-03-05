""" Fundamental Linear Algebra Examples """

x = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]       
        ]

y = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]    
        ]
print('Matrices:\n','x = ', x,'\n', 'y = ', y, '\n')

addition = [[x[i][j] + y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
print('Matrix Addition: ', addition,'\n')

transpose = [[y[j][i] for j in range(len(y))] for i in range(len(y[0]))]
print('Transpose Matrix y: ', transpose,'\n')

multiply = [[sum(a * b for a, b in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]
print('Matrix Multiplication xy: ', multiply,'\n')

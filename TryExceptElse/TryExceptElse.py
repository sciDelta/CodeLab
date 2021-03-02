""" Try - Except - Else Statements """

x = ['deadpool',1,2,3,'the pizza',4,5,6,'ninja',7,8,8.2,9,'ate', 
    'eighty eight', 3, 44, 1001, 1.4142135, 'nine inch nails',
    ]

numbers = []
not_numbers = []
for i in x:
    try:
        float(i)
    except ValueError:
        not_numbers.append(i)
    else:
        numbers.append(round(float(i),1))

print('Numbers: \n', numbers, '\n')
print('Not numbers: \n', not_numbers)

""" Extract and Equalise Data Units in Pure Python"""

x = {'Glenfarclas':'15000 or $60000/set',
     'Glenfidich':'150/375ml','MonkeyShoulder':'50/375ml', 'Glenrothes':'15000-60000/set',
     'Glenmorangie':'50/375ml','Balvenie':'60000/set','BlackIsle':'100/375ml',
     'Bells':'44/liter','Talisker':'132/700ml','Glenfarclas':'60000/set',
     'Glenfarclas':'60000/set','White & McKay':'39/1.75 liter',
     'Johnny Walker Red':'35/liter','Johnny Walker Black':'180/1.75liter',
     'Glenfarclas100':'20000-100000/set'
    }

""" Split value from units """
y = [val for key, val in x.items()]
z = [i.split('/') for i in y]

values = []
corrections = {}

""" Filter off values, isolate error substring values & equalise scaling """
for i in z:
    try:
        float(i[0])
    except ValueError:
        occurance = {i[0]: i[0].split('-')[0]}
        corrections.update(occurance)
        j = float(i[0].split('-')[0])
    else:
        if float(i[0]) == 60000.0:
            j = 12000.0
        elif i[1] == '375ml':
            j = round(float(i[0]) * 700 / 375, 1)
        elif i[1] == 'liter':
            j = round(float(i[0]) * 0.7, 1)
        elif i[1] == '1.75liter':
            j = round(float(i[0]) * 700 / 1750, 1)
        else:
            j = float(i[0])
    values.append(j)

""" Print check input, errors with corrections used and output """
print('input\n\n', x, '\n\ncorrections\n\n', corrections, '\n\noutput\n\n',values)

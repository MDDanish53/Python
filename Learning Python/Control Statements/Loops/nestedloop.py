for i in range(1, 3):
    '''
    by default step = 1
    i = 1 
    j = 3
    1, 3
    i = 1
    j = 4
    1, 4
    i = 1
    j = 5
    1, 5
    then similarly for i = 2 
    stop values are excluded
    '''
    for j in range(3, 6):
        print(f'{i},{j}')
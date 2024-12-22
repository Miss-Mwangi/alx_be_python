pattern = int(input('Enter the size of the pattern: '))

loop = 0
while loop < pattern:
    for num in range(pattern):
        print('*', end='')
    loop += 1
    print('\n', end='')

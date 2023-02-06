N = input()
smile = N.count(':-)')
sad = N.count(':-(')
if smile == 0 and sad == 0:
    print('none')
elif smile > sad:
    print('happy')
elif sad > smile:
    print('sad')
else:
    print('unsure')
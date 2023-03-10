def winner(winstatment_1, winstatment_2, player):
    if winstatment_1 or winstatment_2:
        print(f'{player.title()} is the winner')
        exit
    # else:
    #     pass

def drawing(b0, b1, b2, b3, b4, b5, b6, b7, b8):
    print('%s|%s|%s' % (b0 , b1, b2))
    print('-+-+-')
    print('%s|%s|%s' % (b3 , b4, b5))
    print('-+-+-')
    print('%s|%s|%s' % ( b6 , b7, b8))
    print()
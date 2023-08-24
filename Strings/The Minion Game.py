def minion_game(string):
    stuart, kevin = 0, 0
    for i in range(len(string)):
        if s[i] not in 'UEOAI':
            stuart += len(string) - i
        else:
            kevin += len(string) - i
    if stuart > kevin:
        print('Stuart ' + str(stuart))
    elif kevin > stuart:
        print('Kevin ' + str(kevin))
    else:
        print('Draw')
        
        
if __name__ == '__main__':
    s = input()
    minion_game(s)

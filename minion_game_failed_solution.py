#
'''
This is a python practise problem I found on hackerrank.
Struggled almost two days for this. Though this doesn't give the correct
answer, studying this code will help you learn a lot if you are a
beginner(So am I. Haha..). Looks like the error is in string count function.
It returns 1 instead of 2 when I search for 'ANA' in 'BANANA'.
You will find a working solution for this in the problem discussion on hackerrank.

link to the question: https://www.hackerrank.com/challenges/the-minion-game/problem
'''

from itertools import permutations

def minion_game(string):
    letters = [x for x in string]
    perm_ss = list()

    for i in range(1,len(string)+1):
        perm_ss.extend([''.join(x) for x in permutations(letters,i)])

    u_perms = set()
    u_perms.update(perm_ss)

    vl = list()
    cl = list()

    for x in u_perms:
        if (x[0] == 'A' or x[0]=='E' or x[0] == 'I' or x[0] == 'O' or x[0] =='U'):
            vl.append(x)
        else:
            cl.append(x)

    score_kevin,score_stuart = 0 , 0

    for x in vl:
        score_kevin+=string.count(x)

    for x in cl:
        score_stuart+=string.count(x)

    if score_kevin > score_stuart:
        print('Kevin' , score_kevin)
    elif score_kevin == score_stuart:
        print('Draw')
    else:
        print('Stuart' , score_stuart)


s = input()
minion_game(s)

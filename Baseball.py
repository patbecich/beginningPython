import numpy.random

import random

def hit_chance(p):
    return 'H' if random.random()< p else 'O'
a = input("Batting Average 1 ")
b = input("Batting Average 2 ")
c = input("Batting Average 3 ")
d = input("Batting Average 4 ")
e = input("Batting Average 5 ")
f = input("Batting Average 6 ")
g = input("Batting Average 7 ")
h = input("Batting Average 8 ")
i = input("Batting Average 9 ")

lineup_a = [a,b,c,d,e,f,g,h,i]

batter = 0



game_hits = 0
at_bats = 0
innings = range(9)

for inning in innings:
    outs = 0
    hits = 0

    while outs<3:
        p = lineup_a[batter]
        at_bat = hit_chance(p)
        if at_bat == 'H':
            hits += 1
            batter += 1
        else:
            outs += 1
            batter += 1
            at_bats += 1
        if batter >8:
           batter -= 9
    print 'inning '+str(inning+1)+': hits: '+str(hits)
    game_hits = game_hits+hits

print 'game_hits: '+ str(game_hits)

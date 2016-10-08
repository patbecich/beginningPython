import numpy.random

import random

def hit_chance(p):
    return 'H' if random.random()< p else 'O'
pitcher_a = input("Pitcher A H/BF")
a_a = input("Batting Average 1a ")
b_a = input("Batting Average 2a ")
c_a = input("Batting Average 3a ")
d_a = input("Batting Average 4a ")
e_a = input("Batting Average 5a ")
f_a = input("Batting Average 6a ")
g_a = input("Batting Average 7a ")
h_a = input("Batting Average 8a ")
i_a = input("Batting Average 9a ")

lineup_a = [a_a,b_a,c_a,d_a,e_a,f_a,g_a,h_a,i_a]

pitcher_b = input("Pitcher B H/BF")
a_b = input("Batting Average 1b ")
b_b = input("Batting Average 2b ")
c_b = input("Batting Average 3b ")
d_b = input("Batting Average 4b ")
e_b = input("Batting Average 5b ")
f_b = input("Batting Average 6b ")
g_b = input("Batting Average 7b ")
h_b = input("Batting Average 8b ")
i_b = input("Batting Average 9b ")

lineup_b = [a_b,b_b,c_b,d_b,e_b,f_b,g_b,h_b,i_b]


iterations = range(10000)
total_hits_a = 0
total_hits_b = 0

game_wins_a = 0
game_wins_b = 0
tie = 0

for i in iterations:

    batter_a = 0
    game_hits_a = 0
    at_bats_a = 0
    innings_a = range(9)

    for inning_a in innings_a:
        outs_a = 0
        hits_a = 0

        while outs_a<3:
            p = ((lineup_a[batter_a]+pitcher_b)/2)
            at_bat_a = hit_chance(p)
            if at_bat_a == 'H':
                hits_a += 1
                batter_a += 1
            else:
                outs_a += 1
                batter_a += 1
                at_bats_a += 1
            if batter_a >8:
                batter_a -= 9
        game_hits_a = game_hits_a+hits_a
    total_hits_a += game_hits_a
    
    batter_b = 0
    game_hits_b = 0
    at_bats_b = 0
    innings_b = range(9)

    for inning_b in innings_b:
        outs_b = 0
        hits_b = 0

        while outs_b<3:
            p = ((lineup_b[batter_b]+pitcher_a)/2)
            at_bat_b = hit_chance(p)
            if at_bat_b == 'H':
                hits_b += 1
                batter_b += 1
            else:
                outs_b += 1
                batter_b += 1
                at_bats_b += 1
            if batter_b >8:
                batter_b -= 9
        game_hits_b = game_hits_b+hits_b
    total_hits_b += game_hits_b

    if game_hits_a > game_hits_b:
        game_wins_a += 1
    if game_hits_a < game_hits_b:
        game_wins_b += 1
    if game_hits_a == game_hits_b:
        tie += 1

print 'team a wins: '+ str(game_wins_a)
print 'team b wins: '+ str(game_wins_b)
print 'ties: '+ str(tie)

print 'Average hits team A: '+str(total_hits_a/(iterations[-1]+1))
print 'Average hits team B: '+str(total_hits_b/(iterations[-1]+1))

print 'Team A defeats Team B '+ str(100*(float(game_wins_a)/float((iterations[-1]+1))))+'% of the time'

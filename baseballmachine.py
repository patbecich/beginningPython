
import random

def hit_chance(p):
    return 'H' if random.random()< p else 'O'
aa = input("Batting Average 1 ")
ab = input("Batting Average 2 ")
ac = input("Batting Average 3 ")
ad = input("Batting Average 4 ")
ae = input("Batting Average 5 ")
af = input("Batting Average 6 ")
ag = input("Batting Average 7 ")
ah = input("Batting Average 8 ")
ai = input("Batting Average 9 ")

ba = input("Batting Average 1 ")
bb = input("Batting Average 2 ")
bc = input("Batting Average 3 ")
bd = input("Batting Average 4 ")
be = input("Batting Average 5 ")
bf = input("Batting Average 6 ")
bg = input("Batting Average 7 ")
bh = input("Batting Average 8 ")
bi = input("Batting Average 9 ")

lineup_a = [aa,ab,ac,ad,ae,af,ag,ah,ai]

lineup_b = [ba,bb,bc,bd,be,bf,bg,bh,bi]

batter = 0



game_hits = 0
at_bats = 0
inning = 1

team = lineup_a

while inning < 10:
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
    print 'inning '+str(inning)+': hits: '+str(hits)
    inning += 1
    game_hits = game_hits+hits

print 'game_hits: '+ str(game_hits)

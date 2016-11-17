



def grid_maker(h, w):
    grid = [["-" for i in range(w)] for i in range(h)]
    return grid

def print_grid(grid):
    for row in grid:
        for e in row:
            print e,
        print



#Ball game

h = input("Give height")
w = input("Give width")

grid_list = grid_maker(h,w)

print_grid(grid_list)



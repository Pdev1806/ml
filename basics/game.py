game = [[0,0,0],[0,0,0],[0,0,0]]

def layout(game_map, player=0, row=0, col=0):
    print("   0  1  2")
    if player!=0:
        game_map[row][col] = player
    for count, row in enumerate(game_map):
        print(count, row)
    return(game_map)

print(game)
game = layout(game, player=1,row=2,col=1)
print(game)
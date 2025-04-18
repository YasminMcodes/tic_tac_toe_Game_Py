import itertools


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    #horizontal
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    #diagnonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally!(/)")
        return True

    diags = []
    for x in range(len(game)):
        diags.append(game[x][x])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally!(\\)")
        return True

    # vertical
    for col in range(len(game)):
        nwl = []
        for row in game:
            nwl.append(row[col])
        if all_same(nwl):
            print(f"Player {nwl[0]} is the winner vertically!")
            return True

    return False




def game_board(game_map,player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied choose another !")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player

        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("insert 0,1 or 2", e)
    except Exception as e:
        print("Something is wrong!", e)
        return game_map,  False
play = True
players = [1,2]
while play:
    game_size = int(input("what size of tic tac toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("what column do you want to play? (0,1,2): "))
            row_choice = int(input("what row do you want to play? (0,1,2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("the game is over , would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("ciao")
                play = False
            else:
                print("not a valid answer")
                play = False



'''
game = game_board(game, just_display=True)
game = game_board(game,1,3,0)
game = game_board(game,1,2,0)
game_board()
'''







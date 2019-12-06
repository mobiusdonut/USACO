fin = open("tttt.in", "r")
board = []
for i in range(3):
    board.append(list(fin.readline()[:-1]))
#for line in board:
    #print(line)

sinwins = set()
duwins = set()
for i in range(3):
    if len(set(board[i])) <= 1:
        sinwins.add(tuple(board[i][0]))
    elif len(set(board[i])) <= 2:
        duwins.add(tuple(set(board[i])))
    if len(set([board[0][i], board[1][i], board[2][i]])) <= 1:
        sinwins.add(tuple(set([board[0][i], board[1][i], board[2][i]])))
    elif len(set([board[0][i], board[1][i], board[2][i]])) <= 2:
        duwins.add(tuple(set([board[0][i], board[1][i], board[2][i]])))
if len(set([board[0][0], board[1][1], board[2][2]])) <= 1:
    sinwins.add(tuple(set([board[0][0], board[1][1], board[2][2]])))
elif len(set([board[0][0], board[1][1], board[2][2]])) <= 2:
    duwins.add(tuple(set([board[0][0], board[1][1], board[2][2]])))
if len(set([board[2][0], board[1][1], board[0][2]])) <= 1:
    sinwins.add(tuple(set([board[2][0], board[1][1], board[0][2]])))
elif len(set([board[2][0], board[1][1], board[0][2]])) <= 2:
    duwins.add(tuple(set([board[2][0], board[1][1], board[0][2]])))

fout = open("tttt.out", "w")
fout.write(str(len(sinwins)) + "\n")
fout.write(str(len(duwins)) + "\n")
fout.close()

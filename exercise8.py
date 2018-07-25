rerun=1
def rerunF():
    global rerun
    _rerun = input("Play another round?(y/n): ")
    rerun = 1 if _rerun=="y" else 0

while rerun==1:
    _player1 = str(input("Player 1 Make your choice.. ")).lower()
    _player2 = str(input("Player 2 Make your choice.. ")).lower()

    stuffList = ["rock", "paper", "scissors"]
    if _player1 not in stuffList or _player2 not in stuffList:
        print("What do you choose????")
        rerunF()

    rule = {"rock": {"scissors": "win", "paper": "lose", "rock": "draw"}, "paper": {"rock": "win", "scissors": "lost", "paper": "draw"}, "scissors": {"paper": "win", "rock": "lose", "scissors": "draw"}}

    if rule[_player1][_player2] == "draw":
        print("DRAW!")
        rerunF()
    print("Player one " + rule[_player1][_player2] + "!")
    print("Player two " + rule[_player2][_player1] + "!")
    rerunF()



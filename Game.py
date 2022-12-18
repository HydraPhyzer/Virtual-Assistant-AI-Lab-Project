import speech_recognition as sr
from colorama import Fore

def ListenMove():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        Audio = r.listen(source)
    try:
        Move = r.recognize_google(Audio).lower()

        # parse the recognized speech and return the corresponding move
        if "top left" in Move:
            return (0, 0)
        elif "top center" in Move or "top centre" in Move:
            return (0, 1)
        elif "top right" in Move:
            return (0, 2)
        elif "middle left" in Move:
            return (1, 0)
        elif "middle center" in Move or "middle centre" in Move:
            return (1, 1)
        elif "middle right" in Move:
            return (1, 2)
        elif "bottom left" in Move:
            return (2, 0)
        elif "bottom center" in Move or "bottom centre" in Move:
            return (2, 1)
        elif "bottom right" in Move:
            return (2, 2)
        else:
            print("Sorry, I didn't Understand That. Please Try Again.")
            return ListenMove()
    except sr.UnknownValueError:
        print("Sorry, I didn't Catch That. Repeat Your Move.")
        return ListenMove()

def MakeMove(Board, Player, Row, Col):
    if Board[Row][Col] == "-":
        Board[Row][Col] = Player
        return True
    else:
        print("That Space Is Already Occupied.")
        return False

def PrintBoard(Board):
    for Row in Board:
        print(" ".join(Row))

def CheckWin(Board, Player):
    # check Rows
    for Row in Board:
        if Row == [Player, Player, Player]:
            return True
    # check Columns
    for Col in range(3):
        if Board[0][Col] == Player and Board[1][Col] == Player and Board[2][Col] == Player:
            return True
    # check diagonals
    if Board[0][0] == Player and Board[1][1] == Player and Board[2][2] == Player:
        return True
    if Board[0][2] == Player and Board[1][1] == Player and Board[2][0] == Player:
        return True
    return False

def CheckGameOver(Board):
    # check if the Board is full
    for Row in Board:
        if "-" in Row:
            return False
    return True

def Play():
    Board = [["-" for _ in range(3)] for _ in range(3)]
    Players = ["X", "O"]
    PlayerIndex = 0
    while not CheckGameOver(Board):
        Player = Players[PlayerIndex]
        PrintBoard(Board)
        from colorama import init

        init(convert=True)
        print(Fore.GREEN)
        from Speak import Speak
        Speak(f"It's {Player} Turn")
        print(f"{Player}, It's Your Turn, Listening ...")
        print(Fore.WHITE)
        
        Row, Col = ListenMove()
        MoveMade = MakeMove(Board, Player, Row, Col)
        if MoveMade:
            if CheckWin(Board, Player):
                PrintBoard(Board)
                from Speak import Speak
                Speak(f"Hurray !{Player} Has Won The Game!")
                print(f"\n{Player} Has Won The Game! 🎉🙌")
                break
            PlayerIndex = (PlayerIndex + 1) % 2
    if CheckGameOver(Board):
        PrintBoard(Board)
        print("The Game Is a Draw.")

# Play()
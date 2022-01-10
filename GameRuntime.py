import GameBoard
import GameEngine
import Player
import Stats

class GameRuntime:

    @staticmethod
    def startMenu():
        print("Welcome to Dominos!\nWould you like to?")
        while True:
            val = GameEngine.GameEngine.retriveInput("1) Play\n2) Get Player Stats\n3) Get Match Histories\n4) Exit Program \n", True, "Please Enter an from 1-4")
            if val == 1:
                GameRuntime.simulateGame()
            elif val == 2:
                temp =''
                while True:
                    temp = GameEngine.GameEngine.retriveInput("Enter player name: ", False, "")
                    if temp.isalpha():
                        break
                    else:
                        print("Alphabetic Characters Only!")
                Stats.Stats.displayPlayerStats(temp) 
            elif val == 3:
                temp = 0
                while True:
                    temp = GameEngine.GameEngine.retriveInput("Enter the depth of viewing for match history: ", True, "")
                    if temp <= Stats.Stats.getHistorySize():
                        break
                    else:
                        print("must be less than " + str(Stats.Stats.getHistorySize()))
                Stats.Stats.displayHistory(temp) 
            elif val == 4:
                Stats.Stats.con.close()
                return

    @staticmethod
    def playerSetup():
        for x in range(GameEngine.GameEngine.num_players):
            temp = Player.Player()
            while True:
                temp.name = GameEngine.GameEngine.retriveInput("Player " + str(x+1) + ", Enter your name: ", False, "")
                if temp.name.isalpha():
                    break
                else:
                    print("Alphabetic Characters Only!")
            GameEngine.GameEngine.player_list.append(temp)
        print(GameEngine.GameEngine.player_list)

        while True:
            GameEngine.GameEngine.num_games = GameEngine.GameEngine.retriveInput("How many rounds?: ", True, "Please enter an odd int")
            if GameEngine.GameEngine.verifyGamesCount(GameEngine.GameEngine.num_games):
                break
            else:
                print("Please enter an odd integer")

    @staticmethod
    def roundSetup():
        GameEngine.GameEngine.reset()
        print("Round " + str(GameEngine.GameEngine.round_count) + "!")
        for x in range(GameEngine.GameEngine.num_players):
            print("PLayer '" + GameEngine.GameEngine.player_list[x].name + "' is drawing their hand!")
            GameEngine.GameEngine.player_list[x].hand = GameBoard.GameBoard.grabStartHand()
        GameEngine.GameEngine.determineTurnOrder()
        GameEngine.GameEngine.round_count += 1

    @staticmethod
    def playTurn(player):
        '''
        User should be able to only see valid dominos to play and the option to draw a domino from the pile
        '''
        print("Player " + player.name + "'s Turn!")
        print("Here's your Hand: " + player.hand.__str__())
        ls = GameBoard.GameBoard.validDominos(player.hand)

        num = 1
        print("0) draw a domino from pile")
        if ls != False:
            for op in ls:
                print(str(num) + ") Play: "  + op)
                num += 1

        while True:
            val = GameEngine.GameEngine.retriveInput('', True, 'Please enter an integer only')
            if val == 0:
                #pull from pile
                if GameBoard.GameBoard.getRemainPile() == False:
                    #if deck empty, check for avalibale hand options
                    if ls == False: return
                    print("Pile is empty, trying play a domino from your hand")
                else:
                    dom = GameBoard.GameBoard.grabDom()
                    print("You drew: " + dom)
                    if GameBoard.GameBoard.validDominos([dom]) != False:
                        GameBoard.GameBoard.putDomino(dom)
                    else:
                        player.addDom(dom)
                    return
            elif ls == False:
                print("you can only draw!")
            elif val >= 1 and val <= len(ls):
                #play a domino
                GameBoard.GameBoard.putDomino(ls[val-1])
                player.removeDom(ls[val-1])
                return
            else:
                print("enter 0-" + str(len(ls)))

    @staticmethod
    def simulateRound():
        while True:
            GameEngine.GameEngine.turn_num += 1
            print("Turn: " + str(GameEngine.GameEngine.turn_num))
            GameBoard.GameBoard.displayBoard()
            '''
            check if player has a win condition
            1) if a player's hand is empty
            2) if the pile is empty, or no player can play a domino from their hand or (if) existing pile
                the player with the lowest domino sum wins
            '''
            if len(GameBoard.GameBoard.board.deq) >= 13:
                for player in GameEngine.GameEngine.turn_order:
                    if player.isEmpty():
                        return player
                if GameBoard.GameBoard.getRemainPile() == False:
                    flag = True
                    for player in GameEngine.GameEngine.turn_order:
                        if GameBoard.GameBoard.validDominos(player.hand) != False:
                            flag = False
                            break
                    if flag:
                        ls = []
                        for player in GameEngine.GameEngine.turn_order:
                            s = 0
                            for dom in player.hand:
                                a,b = GameBoard.GameBoard.getDomNum(dom)
                                s += (a+b)
                            pair = (s, player)
                            ls.append(pair)
                        ls.sort()
                        return ls[0][1]
            GameRuntime.playTurn(GameEngine.GameEngine.turn_order[GameEngine.GameEngine.turn_index])
            GameEngine.GameEngine.turn_index += 1
            if GameEngine.GameEngine.turn_index == len(GameEngine.GameEngine.turn_order):
                GameEngine.GameEngine.turn_index = 0

    @staticmethod
    def simulateGame():
        GameRuntime.playerSetup()
        win_cond = (GameEngine.GameEngine.num_games//2)+1
        win_plr = ''
        playing = True
        while playing:
            GameRuntime.roundSetup()
            winner = GameRuntime.simulateRound()
            winner.winRound()
            print(winner.name + " wins the Round!\n")
            #check who has won x rounds
            for plr in GameEngine.GameEngine.player_list:
                if plr.win_count == win_cond:
                    print(plr.name + " is the Winner!")
                    win_plr = plr.name
                    playing = False
                    break
        name_ls = []
        for plr in GameEngine.GameEngine.player_list:
            name_ls.append(plr.name)
            Stats.Stats.updateStats(plr.name, (plr.win_count == win_cond))
        Stats.Stats.addMatchHist(name_ls, win_plr, GameEngine.GameEngine.num_games)
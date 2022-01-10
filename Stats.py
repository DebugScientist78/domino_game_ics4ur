import sqlite3

class Stats:
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    stats_insert_com = "INSERT INTO Stats (Player, 'Win Count', 'Play Count', winPlayRatio) VALUES (?, ?, ?, ?);"
    matchhist_insert_com = "INSERT INTO MatchHistory (matchNum, playerList, 'Winner', numRounds) VALUES (?, ?, ?, ?);"
    stats_update_com = "UPDATE Stats SET 'Win Count'= ?, 'Play Count' = ?, winPlayRatio = ? WHERE Player = ?;"
    player_select_com = "SELECT * from Stats WHERE Player = ?"
    
    #test execute
    @staticmethod
    def test():
        ta = 3
        na = "lol"
        Stats.cur.execute(Stats.stats_update_com, (2, 2, '2/2', 'pp'))
        Stats.con.commit()
        Stats.con.close()
    
    @staticmethod
    def addMatchHist(plr_ls, winner, num_rounds):
        try:
            Stats.cur.execute("SELECT * from MatchHistory")
            #gets latest match number
            match_num = len(Stats.cur.fetchall()) + 1
            #adds match to db
            Stats.cur.execute(Stats.matchhist_insert_com, (match_num, plr_ls.__str__(), winner, num_rounds))
            Stats.con.commit()
        except sqlite3.Error as err:
            print("Cannot add to match history", err)
    
    @staticmethod
    def updateStats(player_name, wins):
        try:
            Stats.cur.execute("SELECT * from Stats")
            records = Stats.cur.fetchall()
            #get list of all previous player data
            existing_players = []
            for row in records:
                existing_players.append(row[0])
            
            if player_name in existing_players:
                player_data = []
                for row in records:
                    if row[0] == player_name:
                        player_data = row
                        break
                win_c = player_data[1] + int(wins)
                play_c = player_data[2] + 1
                ratio = str(win_c)+'/'+str(play_c)
                Stats.cur.execute(Stats.stats_update_com, (win_c, play_c , ratio, player_name))
            else:
                win_c = int(wins)
                ratio = str(win_c) +"/1"
                Stats.cur.execute(Stats.stats_insert_com, (player_name, win_c, 1, ratio))
            Stats.con.commit()
        except sqlite3.Error as err:
            print("Cannot update player stats", err)

    @staticmethod
    def displayHistory(depth):
        try:
            Stats.cur.execute("SELECT * from MatchHistory")
            records = Stats.cur.fetchall()
            for x in range(1,depth+1):
                print("Match ID: " + str(records[-x][0]))
                print("List of Participants: " + records[-x][1])
                print("Winner: " + records[-x][2])
                print("Number of Rounds of the Match: " + str(records[-x][3]))
                print("")
        except sqlite3.Error as err:
            print("Cannot display match history", err)

    @staticmethod
    def getHistorySize():
        try:
            Stats.cur.execute("SELECT * from MatchHistory")
            records = Stats.cur.fetchall()  
            return len(records)
        except sqlite3.Error as err:
            print("Could not access match history", err)
            return -1

    @staticmethod
    def displayPlayerStats(player_name):
        try:
            Stats.cur.execute(Stats.player_select_com, (player_name,))
            record = Stats.cur.fetchone()
            print("Here are " + player_name + "'s Stats:")
            print("Number of games won: " + str(record[1]))
            print("Number of times played: " + str(record[2]))
            print("Win-Plays ratio: " + record[3])
            print("")
        except sqlite3.Error as err:
            print("Player not found", err)
            
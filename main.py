class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

class NFLTeam:
    def __init__(self, teamName):
        self.teamName = teamName
        self.players = []  # Initialize an empty list to hold Player objects

    def add_player(self, player):
        self.players.append(player)

# Create Player objects
player1 = Player("Joe Montana", "Quarterback")
player2 = Player("Barry Sanders", "Running Back")
player3 = Player("Jerry Rice", "Wide Receiver")
player4 = Player("Graham Gano", "Kicker")

# Create a list of players
playerList = [player1, player2, player3, player4]

# Create an NFLTeam object
myTeam = NFLTeam("All-Star Legends")

# Add players from the list to the team
for player in playerList:
    myTeam.add_player(player)

# Output the team name and its players
print(f"Team Name: {myTeam.teamName}")
print("Players:")
for player in myTeam.players:
    print(f"  - {player.playerName} ({player.playerPosition})")

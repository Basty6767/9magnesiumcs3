class VNLTeams:
    def __init__(self, players, country, ranking, numofwins):
        self.country = country
        self.ranking = ranking
        self.__private_players = players
        self.__private_numofwins = numofwins

    def serve(self):
        return f"{self.country} serves the ball!"

    def block(self):
        return f"{self.country} successfully blocked the opposing team's attack!"

    def subPlayer(self, name):
        self.__private_players -= 1
        return f"{name} has been substituted into the game."

    def addwin(self):
        self.__private_numofwins += 1
        return f"{self.country} has won a match!"

    def getplayers(self):
        return self.__private_players

    def getwins(self):
        return self.__private_numofwins
    

team1 = VNLTeams(12, "Philippines", 45, 8)
team2 = VNLTeams(12, "Japan", 3, 20)

print("----- BEFORE -----")
print(team1.country, team1.ranking, team1.getplayers(), team1.getwins())
print(team2.country, team2.ranking, team2.getplayers(), team2.getwins())

print("\nTeam 1 Actions:")
print(team1.serve())
print(team1.block())
print(team1.subPlayer("Rene Baterbonia"))
print(team1.addwin())

print("\n----- AFTER -----")
print(team1.country, team1.ranking, team1.getplayers(), team1.getwins())
print(team2.country, team2.ranking, team2.getplayers(), team2.getwins())
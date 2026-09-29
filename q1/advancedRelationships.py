class Team:
    """Parent Class holding general sports metrics"""
    def __init__(self, country, ranking, wins):
        self.Country = country
        self.Ranking = ranking
        self.__Wins = wins
        
    def addwin(self):
        self.__Wins += 1
        return f"{self.country} won the match!"
    
    def getWins(self):
        return self.__Wins
    

class Coaches:
    """Independent Class for Aggregation."""
    def __init__(self, name, plays="Standard"):
        self.Name = name
        self.__Players = []
        self.__Plays = plays
        
    def trainPlayer(self, player):
        return f"Coach {self.name} is training a player."
    
    def calltimeout(self):
        return f"Coach {self.name} has called a timeout."
    
class VNLTeam(Team):
    """Child Class inheriting general metrics from Team"""
    def __init__(self, country, ranking, wins, players_count):
        super().__init__(country, ranking, wins)
        self.__Players = players_count
        self.coaches = []
        
    def serve(self):
        return f"{self.country} is serving the ball!"
    
    def block(self, opponentSpike):
        return f"{self.country} blocked the spike from {opponentSpike}!"
    
    def addCoach(self, coach_obj):
        self.coaches.append(coach_obj)
        
    def display_info(self):
        print(f"VNL Team: {self.country} | Rank: #{self.Ranking} | Wins: {selfgetWins()}")
        print(f"Active Players on Roster: {self.__Players}")
        print("Coaching Staff:")
        for c in self.coaches:
            print(f" - {c.name}")
            

if __name__ == "__main__":
    print("--- Test 1: Inheritance ---")
    ph_team = VNLTeam("Philippines", 48, 8, 12)
    print(ph_team.serve())
    print(ph_team.addwin())
    
    print("\n--- Test 2: Aggregation ---")
    head_coach = Coaches("Phillipe Blain")
    ph_team.addCoach(head_coach)
    ph_team.display_info()
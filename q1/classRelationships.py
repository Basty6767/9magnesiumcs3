class Coach:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        

class VNLTeams:
    def __init__(self, country):
        self.country = country
        self.coaches = []
        
    def add_coach(self, coach_object):
        if len(self.coaches) < 3:
            self.coaches.append(coach_object)
        else:
            print("Error: Cannot have more than 3 coaches on the bench.")

    def display_relationship_info(self):
        print(f"VNL Team: {self.country}")
        print("Related object(s):")
        for coach in self.coaches:
            print(f"Coach Name: {coach.name}, Role: {coach.role}")
            

print("----- BEFORE RELATIONSHIP -----")
print("Objects have been created.")
team = VNLTeams("Japan")
coach1 = Coach("Philippe Blain", "Head Coach")
coach2 = Coach("Kenji Shimaoka", "Assistant Coach")
coach3 = Coach("Yusuke Tanaka", "Trainer")

print("\n----- BUILDING RELATIONSHIP -----")
print("Adding related objects...")
team.add_coach(coach1)
team.add_coach(coach2)
team.add_coach(coach3)

print("\n----- AFTER RELATIONSHIP -----")
team.display_relationship_info()
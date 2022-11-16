class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.team = player_dict['team']
        self.goals = player_dict['goals']
        self.assists = player_dict['assists']

    def __str__(self):
        return f"{self.name:20}{self.team:3}{self.goals:3} + {self.assists:3} ={self.goals + self.assists:3}"
    

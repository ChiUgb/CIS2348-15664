# Chiamaka Ugbaja
# 1772427

class Team:  # Initializes the class that will execute the code
    def __init__(self):  # constructor/used as placeholder to store variable for use throughout the code
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def get_win_percentage(self):  # get win percentage through formula
        return self.team_wins / (self.team_wins + self.team_losses)

    def set_team_name(self, name):  # define team name
        self.team_name = name

    def set_team_wins(self, wins):  # defines wins
        self.team_wins = wins

    def set_team_losses(self, losses):  # defines losses
        self.team_losses = losses


if __name__ == "__main__":  # calls this function first in terms of execution to fill variables with values

    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.set_team_name(team_name)
    team.set_team_wins(team_wins)
    team.set_team_losses(team_losses)

    if team.get_win_percentage() >= 0.5:  # if percentage is over 0.5 then print, else losing average
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')

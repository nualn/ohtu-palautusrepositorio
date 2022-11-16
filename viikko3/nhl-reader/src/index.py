import requests
import datetime
import time
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        if player_dict['nationality'] == 'FIN':
            player = Player(player_dict)
            players.append(player)
    
    

    players.sort(key=lambda player: player.goals + player.assists, reverse=True)
    print("Players from FIN " + str(datetime.datetime.now()) + '\n')

    for player in players:
        print(player)


if __name__ == "__main__":
    main()

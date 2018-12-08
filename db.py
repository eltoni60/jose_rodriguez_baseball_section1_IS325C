import csv
from objects import Player
from objects import Lineup

FILENAME = "players.txt"

def read_players():
    try:
        lineup = Lineup()
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                player = Player(row[0], row[1], row[2], row[3])
                #player["name"] = row[0]
                #player["position"] = row[1]
                #player["at_bats"] = row[2]
                #player["hits"] = row[3]
                lineup.add_player(player)
        return lineup
    except FileNotFoundError:
        return None

def write_players(lineup):
    with open(FILENAME, "w") as file:
        for player in lineup:
            file.write(player.print_player() + "\n")



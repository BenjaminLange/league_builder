import csv
import os


if __name__ == "__main__":
    def add_player_to_team(player):
        team = None
        team_name = None
        if (player["Experience"] == "YES"):
            team, team_name = get_least_experienced_team()
        else:
            team, team_name = get_smallest_team()
        player["Team"] = team_name
        team.append(player)

    def get_smallest_team():
        smallest_team = None
        team_name = None
        for key, team in teams.items():
            if (smallest_team is None):
                smallest_team = team
                team_name = key.title()
            else:
                if (len(team) < len(smallest_team)):
                    smallest_team = team
                    team_name = key.title()
        return smallest_team, team_name

    def get_least_experienced_team():
        least_experienced_team = None
        least_experience_count = 0
        team_name = None
        for key, team in teams.items():
            if (least_experienced_team is None):
                least_experienced_team = team
                least_experience_count = get_experience_count(team)
                team_name = key.title()
            else:
                experience_count = get_experience_count(team)
                if (experience_count < least_experience_count or
                        experience_count == 0):
                    least_experience_count = experience_count
                    least_experienced_team = team
                    team_name = key.title()
        return least_experienced_team, team_name

    def get_experience_count(team):
        experience_count = 0
        for player in team:
            if (player["Experience"] == "YES"):
                experience_count += 1
        return experience_count

    def print_teams():
        sharks_experience = 0
        dragons_experience = 0
        raptors_experience = 0

        for player in teams["sharks"]:
            if (player["Experience"] == "YES"):
                sharks_experience += 1

        for player in teams["dragons"]:
            if (player["Experience"] == "YES"):
                dragons_experience += 1

        for player in teams["raptors"]:
            if (player["Experience"] == "YES"):
                raptors_experience += 1

        print("Sharks Count: ", len(teams["sharks"]), sharks_experience)
        print("Dragons Count: ", len(teams["dragons"]), dragons_experience)
        print("Raptors Count: ", len(teams["raptors"]), raptors_experience)

    def generate_letters():
        for team in teams.values():
            for player in team:
                practice_date = None
                practice_time = None

                if (player["Team"] == "Sharks"):
                    practice_date = "March 17th"
                    practice_time = "3:00 PM"
                if (player["Team"] == "Dragons"):
                    practice_date = "March 17th"
                    practice_time = "1:00 PM"
                if (player["Team"] == "Raptors"):
                    practice_date = "March 18th"
                    practice_time = "1:00 PM"

                directory = os.path.dirname(os.path.realpath(__file__))
                os.makedirs(os.path.join(directory, "Letters"), exist_ok=True)
                directory = os.path.join(directory, "Letters")

                filename = player["Name"].lower().split()
                filename = '_'.join(filename) + ".txt"
                filename = os.path.join(directory, filename)
                letter = open(filename, 'w')
                letter.write('Dear {},\n\n'.format(player["Guardians"]))
                letter.write("Thank you for signing up {} with the soccer "
                             "league!!\n\n".format(player["Name"]))
                letter.write("They will be playing on the {} and the first "
                             "scheduled practice is on {} at {}.\n\n"
                             .format(
                                 player["Team"],
                                 practice_date,
                                 practice_time
                             ))
                letter.write("Please make sure that your child brings a soccer"
                             " ball and a water bottle to every practice.\n\n")
                letter.write("We look forward to meeting you and your child!!"
                             "\n\n")
                letter.write("Thanks!!\n\n")
                letter.write("The Coach")
                letter.close()

    teams = {
        "sharks": [],
        "dragons": [],
        "raptors": []
    }

    with open('soccer_players.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(reader):
            if (index == 0):
                continue
            player = {
                "Name": row[0],
                "Height": row[1],
                "Experience": row[2],
                "Guardians": row[3],
                "Team": ""
            }
            add_player_to_team(player)

        generate_letters()

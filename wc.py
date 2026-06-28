import random 
from wc_groups import groups
from wc_ko import knockout_pairs

def play_group(teams, current_group):
    table = {}
    for team in teams: 
        table[team] = {'played': 0, 'points': 0, 'wins': 0, 'draws': 0, 'losses': 0, 'gf': 0, 'ga': 0}

    for i in range(len(teams)):
        for x in range(i+1, len(teams)):
            team1, team2, goal1, goal2 = play_match(teams[i], teams[x], current_group)

            if goal1 > goal2:
                table[team1]['points'] += 3
                table[team1]['played'] += 1
                table[team1]['wins'] += 1
                table[team1]['gf'] += goal1
                table[team1]['ga'] += goal2
                table[team2]['played'] += 1
                table[team2]['losses'] += 1
                table[team2]['gf'] += goal2
                table[team2]['ga'] += goal1
            elif goal1 == goal2: 
                table[team1]['points'] += 1
                table[team1]['played'] += 1
                table[team1]['draws'] += 1
                table[team1]['gf'] += goal1
                table[team1]['ga'] += goal2
                table[team2]['points'] += 1
                table[team2]['played'] += 1
                table[team2]['draws'] += 1
                table[team2]['gf'] += goal2
                table[team2]['ga'] += goal1
            elif goal1 < goal2: 
                table[team1]['played'] += 1
                table[team1]['losses'] += 1
                table[team1]['gf'] += goal1
                table[team1]['ga'] += goal2
                table[team2]['played'] += 1
                table[team2]['wins'] += 1
                table[team2]['points'] += 3
                table[team2]['gf'] += goal2
                table[team2]['ga'] += goal1
            print("------------------------------")
    sorted_table = print_table(table)
    return sorted_table
    

def print_table(table):
    sorted_table = sorted(
        table.items(),
        key=lambda x: (x[1]["points"], x[1]["gf"] - x[1]["ga"], x[1]["gf"]),
        reverse=True
    )

    print("Team        P  W  D  L  GF  GA  GD  Pts")
    print("-----------------------------------------")

    for team, stats in sorted_table:
        gd = stats["gf"] - stats["ga"]

        print(
            team.ljust(10),
            str(stats["played"]).rjust(1),
            str(stats["wins"]).rjust(2),
            str(stats["draws"]).rjust(2),
            str(stats["losses"]).rjust(2),
            str(stats["gf"]).rjust(3),
            str(stats["ga"]).rjust(3),
            str(gd).rjust(3),
            str(stats["points"]).rjust(4)
        )
    return sorted_table 

def generate_goals(attacker_rating, defender_rating):
    goals = 0
    advantage = attacker_rating - defender_rating
    scoring_probability = 20 + advantage
    
    for i in range(5):
        if random.randint(1, 100) <= scoring_probability:
            goals += 1
            
    return goals

def play_match(team1, team2, group):

    print(team1 + ' vs ' + team2)
        
    rating1 = group[team1]
    rating2 = group[team2]

    goal1 = generate_goals(rating1, rating2)
    goal2 = generate_goals(rating2, rating1)
    
    print(team1 + ' ' + str(goal1) + ' - ' + str(goal2) + ' ' + team2)

    if goal1 > goal2:
        print(team1 + ' wins!')
    elif goal1 < goal2:
        print(team2 + ' wins!')
    elif goal1 == goal2:
        print('Draw!')
    
    result = team1, team2, goal1, goal2
    return result

qualifiers = []
third_placed = []

for group_name, current_group in groups.items():
    print(f"--- Playing Group {group_name} ---")
    teams = list(current_group.keys())
    sorted_table = play_group(teams, current_group)
    qualifiers.append(sorted_table[0][0])
    qualifiers.append(sorted_table[1][0])
    third_placed.append(sorted_table[2])

third_placed.sort(
    key=lambda x: (x[1]["points"], x[1]["gf"] - x[1]["ga"], x[1]["gf"]),
    reverse=True
)

print('\n--- Best 8 Third Placed Teams Advancing ---')

for team_data in third_placed[:8]:
    team_name = team_data[0]
    qualifiers.append(team_name)
    print(f"{team_name} advances!")

print(f"\nRound of 32 Qualifiers ({len(qualifiers)} teams):")
print(qualifiers)

def play_ko_match(team1, team2, current_group):
    print(team1 + ' vs ' + team2)
    
    rating1 = 0
    rating2 = 0
    
    for group_name, group_data in current_group.items():
        if team1 in group_data:
            rating1 = group_data[team1]
        if team2 in group_data:
            rating2 = group_data[team2]

    goal1 = generate_goals(rating1, rating2)
    goal2 = generate_goals(rating2, rating1)
    
    print(team1 + ' ' + str(goal1) + ' - ' + str(goal2) + ' ' + team2)

    if goal1 > goal2:
        winning_team = team1
        print(team1 + ' wins!')
    elif goal1 < goal2:
        winning_team = team2
        print(team2 + ' wins!')
    elif goal1 == goal2:
        winning_team = random.choice([team1, team2])
        print(winning_team + ' wins via penalties!')
    return winning_team

def knockout_rounds(teams, groups):
    matchups = [(teams[team1_index], teams[team2_index]) for team1_index, team2_index in knockout_pairs]
    winners = []
    for team1, team2 in matchups: 
        match_winner = play_ko_match(team1, team2, groups)
        winners.append(match_winner)
        print("------------------------------")
    return winners

def remaining_rounds(teams, groups):
    winners = []
    for i in range(0, len(teams), 2): 
        team1 = teams[i]
        team2 = teams[i+1]
        match_winner = play_ko_match(team1, team2, groups)
        winners.append(match_winner)
    return winners

print("\n--- ROUND OF 32 ---")
round_of_16 = knockout_rounds(qualifiers, groups)

print("\n--- ROUND OF 16 ---")
quarter_finalists = remaining_rounds(round_of_16, groups)

print("\n--- QUARTERFINALS ---")
semi_finalists = remaining_rounds(quarter_finalists, groups)

print("\n--- SEMIFINALS ---")
finalists = remaining_rounds(semi_finalists, groups)

print("\n--- GRAND FINAL ---")
champion = remaining_rounds(finalists, groups)

print(f"\n🏆 THE WORLD CUP CHAMPION IS: {champion[0]} 🏆")

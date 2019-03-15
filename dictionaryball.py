

game_dictionary = [{'home': True, 'team_name': 'Brooklyn Nets', 'colors': ['black', 'white'],
                            'players': [{
                                'name': 'Alan Anderson','number': 0,'shoe': 16, 'points': 22, 'rebounds': 12,
                                 'assists': 12, 'steals': 3, 'blocks': 1, 'slam_dunks': 1},
                                {'name': 'Reggie Evans','number': 30,'shoe': 14, 'points': 12, 'rebounds': 12,
                                 'assists': 12, 'steals': 12, 'blocks': 12, 'slam_dunks': 7},
                                {'name': 'Brooke Lopez','number': 11,'shoe': 17, 'points': 17, 'rebounds': 19,
                                 'assists': 10, 'steals': 3, 'blocks': 1, 'slam_dunks': 15},
                                {'name': 'Mason Plumlee','number': 1,'shoe': 19, 'points': 26, 'rebounds': 12,
                                 'assists': 6, 'steals': 3, 'blocks': 8, 'slam_dunks': 5},
                                {'name': 'Jason Terry','number': 31,'shoe': 15, 'points': 19, 'rebounds': 2,
                                 'assists': 2, 'steals': 4, 'blocks': 11, 'slam_dunks': 1}]},

                   {'away': False, 'team_name': 'Charlotte Hornets', 'colors': ['turquoise', 'black'],
                            'players': [
                                {'name': 'Jeff Ardien','number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1,
                                 'assists': 1, 'steals': 2, 'blocks': 7, 'slam_dunks': 2},
                                {'name': 'Bismak Biyombo','number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4,
                                 'assists': 7, 'steals': 7, 'blocks': 15, 'slam_dunks': 10},
                                {'name': 'DeSagna Diop','number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12,
                                 'assists': 12, 'steals': 4, 'blocks': 5, 'slam_dunks': 5},
                                {'name': 'Ben Gordon','number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3,
                                 'assists': 2, 'steals': 1, 'blocks': 1, 'slam_dunks': 0},
                                {'name': 'Brendan Haywood','number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12,
                                 'assists': 12, 'steals': 22, 'blocks': 5, 'slam_dunks': 12}]}]

def game_dict():
    return game_dictionary


# Build a function, num_points_scored that takes in an argument of a player's name and returns the number of points scored for that player.
# Think about where in the dictionary you will find a player's points. How can you iterate down into that level? Think about the return value of your function.
def num_points_scored(a_list_of_entries, player_name):
    num_of_points = None
    for entry in a_list_of_entries:
        for element in entry['players']:
            if element['name'] == player_name:
                num_of_points = element['points']
    return num_of_points

#print(num_points_scored(game_dictionary, 'Alan Anderson'))

def shoe_size(a_list_of_entries, player_name):
    shoe_size = None
    for entry in a_list_of_entries:
        for element in entry['players']:
            if element['name'] == player_name:
                shoe_size = element['shoe']
    return shoe_size

#print(shoe_size(game_dictionary, 'Alan Anderson'))

def team_colors(a_list_of_entries, team_name):
    team_colors = []
    for entry in a_list_of_entries:
        if entry['team_name'] == team_name:
            team_colors = entry['colors']
    return team_colors

#print(team_colors(game_dictionary,'Brooklyn Nets'))

def team_names(a_list_of_entries):
    team_names = []
    for element in a_list_of_entries:
        team_names.append(element['team_name'])
    return team_names

#print(team_names(game_dictionary))

#, that takes in an argument of a team name and returns a list of the jersey number's for that team.
def player_numbers(a_list_of_entries, team_name):
    jersey_numbers = []
    for entry in a_list_of_entries:
        if entry['team_name'] == team_name:
            for player in entry['players']:
                jersey_numbers.append(player['number'])
    return jersey_numbers

# print(player_numbers(game_dictionary, 'Brooklyn Nets'))
# print(player_numbers(game_dictionary, 'Charlotte Hornets'))

#takes in an argument of a player's name and returns a dictionary of that player's stats.
#Check out the following example of the expected return value of the player_stats function:
def player_stats(a_list_of_entries, player_name):
    player_stats = {}
    for entry in a_list_of_entries:
        for player in entry['players']:
            if player['name'] == player_name:
                player_stats['Name'] = player['name']
                player_stats['Number'] = player['number']
                player_stats['Shoe'] = player['shoe']
                player_stats['Points'] = player['points']
                player_stats['Rebounds'] = player['number']
                player_stats['Assists'] = player['assists']
                player_stats['Steals'] = player['steals']
                player_stats['Blocks'] = player['blocks']
                player_stats['Slam_Dunks'] = player['slam_dunks']
    return player_stats

#print(player_stats(game_dictionary, 'Alan Anderson'))

def big_shoe_rebounds(a_list_of_entries):
    largest_shoe_size = 0
    number_of_rebounds = 0
    for entry in a_list_of_entries:
        for player in entry['players']:
            if player['shoe'] > largest_shoe_size:
                largest_shoe_size = player['shoe']
                number_of_rebounds = player['rebounds']
    return f"The largest shoe size is: {largest_shoe_size} and the number of rebounds is: {number_of_rebounds}"

#print(big_shoe_rebounds(game_dictionary))

#Which player has the most points? Call the function most_points_scored.
def most_points_scored(a_list_of_entries):
    most_points = 0
    for entry in a_list_of_entries:
        for player in entry['players']:
            if player['points'] > most_points:
                most_points = player['points']
    return player['name'], most_points

#print(most_points(game_dictionary))

#Which team has the most points? Call the function winning_team
def team_points(a_list_of_entries, team_name):
    all_player_points = 0
    for entry in a_list_of_entries:
        if entry['team_name'] == team_name:
            for player in entry["players"]:
                player_points = num_points_scored(a_list_of_entries, player['name'])
                all_player_points += player_points
    return all_player_points

def winning_team(a_list_of_entries):
    brooklyn_nets_points = team_points(game_dictionary, "Brooklyn Nets")
    charlotte_hornets_points = team_points(game_dictionary, "Charlotte Hornets")
    if brooklyn_nets_points > charlotte_hornets_points:
        return "Brooklyn Nets win"
    if brooklyn_nets_points < charlotte_hornets_points:
        return "Charlotte Hornets wins"
    else:
        return "It's a tie!"

#print(winning_team(game_dictionary))


def player_with_longest_name(a_list_of_entries):
    longest_name_count = 0
    longest_name = None
    for entry in a_list_of_entries:
        for player in entry['players']:
            letters_in_name = len(player['name']) - 1
            if letters_in_name > longest_name_count:
                longest_name = player['name']
    return player['name']

#print(player_with_longest_name(game_dictionary))

def long_name_steals_a_ton(a_list_of_entries):
    longest_name = player_with_longest_name(game_dictionary)
    most_steals_count = 0
    player_with_most_steals = None
    for entry in a_list_of_entries:
        for player in entry['players']:
            if player['steals'] > most_steals_count:
                player_with_most_steals = player['name']
                most_steals_count = player['steals']
    if player_with_most_steals == longest_name:
        return True, player['name']
    else:
        return False

print(long_name_steals_a_ton(game_dictionary))



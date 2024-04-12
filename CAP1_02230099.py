################################
# Nima Dorji
# 1ECE
# 0223009
################################
# REFERENCES
# https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
# https://www.w3schools.com/python/python_file_open.asp
#https://chat.openai.com/
################################
# SOLUTION
# Your Solution Score:
# Put your number here
################################

# This is a Function defined to read the input data from a file
def read_input(game_file):
    # g_rounds variable initializes where it is a list to store game rounds data
    g_rounds = []
    
    # This code opens the file for reading and is named as g_file
    with open(game_file, 'r') as g_file:
         # In order to read each line of the file, for loop is used to iterlate through. 
        for line in g_file:
             # It splits the line into individual elements
            round_data = line.strip().split()
            # Then it is appended as the tuple having player choice and outcome in the list g_rounds.
            g_rounds.append((round_data[0], round_data[1]))
    # Return the list of game rounds data
    return g_rounds

# And function 'calculate_score' is defined to calculate the total score based on game rounds data.
def calculate_score(g_rounds):
    # Nested function to calculate score for each round
    def calculate_round(player_choice, rival_choice, result):
        # Dictionary options is declared to map player choices to scores
        options = {'A': 1, 'B': 2, 'C': 3}
        # Dictionary results to map game outcomes to scores
        results = {'X': 0, 'Y': 3, 'Z': 6}
        
        # This block of codes below calculate scores for player, rival, and result
        player_score = options[player_choice]
        rival_score = options[rival_choice]
        result_score = results[result]
        
        #This block of codes determine the result of the round(Draw, Win or Lose) and return the score
        if player_score == rival_score: 
            return player_score + result_score  # Draw
        elif (player_score == 1 and rival_score == 3) or (player_score > rival_score):
            return player_score + result_score  # Win
        else:
            return player_score + result_score  # Lose
    
    # Initialize total score to 0
    total_score = 0
 
    # Iteration through each game round
    for round_data in rounds:
        # Extract player choice and outcome
        player_choice, outcome = round_data
        # Determines the rival's choice based on player's choice
        opponent_choice = 'C' if player_choice == 'A' else ('A' if player_choice == 'B' else 'B')
        # Calculate score for the round and add to total score
        total_score += calculate_round(player_choice, opponent_choice, outcome)
    
    # Return the total score
    return total_score

# File name containing game rounds data is provided 
file_name = "input_9_cap1.txt"
# read input function is called and stored its data in rounds variable.
rounds = read_input(file_name)
# calculate_score is called and its values is stored in total score variable.
total_score = calculate_score(rounds)
# Print the total score
print("Total Score:", total_score)

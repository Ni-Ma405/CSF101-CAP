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
# Solution Score:50267

# Function is defined to read the input data from file
def read_input(game_file):
    # Open the game file in read mode
    with open(game_file, 'r') as g_file:
        # Read each line from the file, stripping whitespace and splitting by space to get shape and result pairs.
        g_rounds = [line.strip().split() for line in g_file] 
    return g_rounds
 
# Function "calculate_score" is defined to calculate final score based on game rounds data
def calculate_score(g_rounds):
    f_score = 0  # Setting the initial final score to zero.
    # Calculating the score based on the combinations of shapes choice and players result
    for shape_choice, players_result in g_rounds:  # Looping through each shape choice and result pair
        if shape_choice == 'A' and players_result== 'X':
            f_score += 3 # Adding 3 to the final score if the shape choice  is A and the result is X
        elif shape_choice  == 'A' and players_result == 'Y':
            f_score += 4  # Adding 4 to the final score if the shape choice is A and the result is Y
        elif shape_choice == 'A' and players_result == 'Z':
            f_score += 8  # Adding 8 to the final score if the shape choice is A and the result is Z
        elif shape_choice == 'B' and players_result == 'X':
            f_score += 1 # Adding 1 to the final score if the shape choice is B and the result is X
        elif shape_choice == 'B' and players_result == 'Y':
            f_score+= 5 # Adding 5 to the final score if the shape choice is B and the result is Y
        elif shape_choice == 'B' and players_result == 'Z':
            f_score += 9  # Adding 9 to the final score if the shape choice is B and the result is Z
        elif shape_choice == 'C' and players_result == 'X':
            f_score += 2  #  Adding 2 to the finsl score if the shape choice is C and the result is X
        elif shape_choice== 'C' and players_result == 'Y':
            f_score += 6  # Adding 6 to the final score if the shape choice is C and the result is Y
        elif shape_choice == 'C' and players_result == 'Z':
            f_score += 7 # Adding 7 to the final score if the shape choice is C and the result is Z
    return f_score  # Returning the final total score


file_p = "input_9_cap1.txt" # Defining the path to the input file


# Read the game data from the file
All_rounds = read_input(file_p)

f_score = calculate_score(All_rounds)  # Compute the final score using the game data
print("Total Score:", f_score)  # Print the total score
# Extras Done:
# 1) Use multiple aspects of a single data source in your analysis

# -----------------------------------------------------------------
# Text analysis start:
# The average video games metacritic review score in the videogames.csv dataset  is "68.83/100", taking a 
# sample size of 1212 games in history. The general consensus of a good video game score is "50/100",
# however, there are too many games listed above 50, which makes the reviewers and the metacritic 
# platform unreliable and biased. Metacritic reviews may not be justified.

# According to the printed data, games with more than 10 averaged hours of playtime is highly rated. This
# demonstrates that games with more than 10 averaged hours of playtime is rated highly. 
 
# Typically, the general consensus is that a game with more than 10 hours of playtime enables the reviewers to 
# make a reasonable and sound argument in their reviews. So, the average of the average playtime of all the games 
# listed 13.3 hours indicates that the metacritic users are justified in giving scores because of the high number 
# of hours played. 

# In conclusion, games with long lifetime is considered good. In addition, the metacritic reviews are legitimate 
# enough because there is no other real method of determining whether a game is good or bad. For potential 
# customers looking into purchasing a video game by simply searching up a particular game review on the platform. 
# Since the reviews are opinions, it helps the customer judge whether to make the choice of purchasing the game or 
# not.

# Text analysis end
# -----------------------------------------------------------------

# Imports CSV module
import csv
 
# Opens the CSV File
with open("videogames.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # The below statement will skip the first row
    next(csv_reader)

    num_of_games = 0
    score = 0
    playstyles_avg = 0
    
    # For loop repeats until the end of line
    for line in csv_reader:

        # If the average playstyle time is greater/less than 10 hours, then print them
        x = int(float(line[9]))
        y = int(float(line[16]))
        if y > 10:
            print("Metacritic Review Score:", x, " Avg hours played more than 10:", y)

        else:
            print("Metacritic Review Score:", x, " Avg Hours played less than 10:", y)
        
        print("----------------------------------------------------------------")
        num_of_games = num_of_games + 1 # Counts the number of games
        score = score + x # Adds up all the review scores
        playstyles_avg = playstyles_avg + y # Adds up all the average playstyle times


    print("The average review score of all games:", score/num_of_games)
    print("The average of the average playtime hours of all games:", playstyles_avg/num_of_games)

# Spare file directory: reader = csv.reader(open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/data/videogames.csv"))

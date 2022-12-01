# Extras Done:
# 1) Use multiple aspects of a single data source in your analysis

# -----------------------------------------------------------------
# Text analysis start:
# The average video games metacritic review score in the videogames.csv dataset  is "68.83/100", taking a 
# sample size of 1212 games in history. The general consensus of a good video game score is "50/100",
# however, there are too many games listed above 50, which makes the reviewers and the metacritic 
# platform unreliable and biased. Thus, metacritic reviews may not be justified. However, my analysis is flawed 
# because it is possible that all the games here are great, the reviews are opinion-oriented and 
# should not reflect the games's score that is deserving of that number. It is also possible that the some 
# of the games here are genuinely horrible.

# On the contrary, the average of the average playtime of all the games listed 13.3 hours indicates that the
# metacritic users are justified in giving scores because of the high number of hours played. 
# Typically, a game with more than 10 hours of playtime enables the reviewers to make a reasonable and sound 
# argument in their reviews.

# In conclusion, the metacritic reviews are legitimate enough because there is no other real method of determining
# whether a game is good or bad. For potential customers looking into purchasing a video game by simply searching 
# up a particular game review on the platform. Again, since the reviews are opinions, it helps the customer 
# judge whether to make the choice of purchasing the game or not.
# -----------------------------------------------------------------
import csv

with open("videogames.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # The below statement will skip the first row
    next(csv_reader)

    num_of_games = 0
    score = 0
    playstyles_avg = 0

    for line in csv_reader:
        num_of_games = num_of_games + 1
        score = score + int(float(line[9]))
        playstyles_avg = playstyles_avg + int(float(line[16]))

    print("The average review score of all games:", score/num_of_games)
    print("The average of the average playtime hours of all games:",playstyles_avg/num_of_games)

# Spare file directory: reader = csv.reader(open("/home/kerth/fall-2022-127-work-kertharv/fall-2022-127-work-kertharv/data/videogames.csv"))

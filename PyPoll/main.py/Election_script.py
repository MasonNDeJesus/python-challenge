# Same as the pybank part of the homework, I wanted to do something outside of what the professor was doing. Unfortunately, this part of the assignment was a lot simpler, so things will overlap a bit.
import csv

# Path to the CSV file
csv_file = "Resources/election_data.csv"

# Variables, super easy, really small amount of them
total_votes = 0
candidate_votes = {}
candidates = []

# Got this part from ChatGPT as I was a little confused on what I was doing wrong and found that the line of code from comics, lesson plan wasn't working
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    
    # Goes through the rows
    for row in reader:
        total_votes += 1
        candidate = row[2]
        
        # Adds candidates to list and ensures no repeates
        if candidate not in candidates:
            candidates.append(candidate)
        
        # Votes fir eacg candidate is counted
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

    # Calculate the percentage of votes each candidate won. I got an error here originally so I asked ChatGPT what was wrong. 
    candidate_percentages = {}
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        candidate_percentages[candidate] = percentage

    # Popular vote winner. Max was the only functioon I could think of since the highest number is simply what was needed
    winner = max(candidate_votes, key=candidate_votes.get)

    # Displaying the Election results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate in candidates:
        print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Something fun here
    options = ["y", "n"]
    user_choice = input("Would you Like to save the results in a text file? y/n: ")

    # The bane of this homework for me, exporting the results to a text file. ChatGPT came up with this line of code. I came up with the idea of adding the yes and no to create it
    if (user_choice == "y"):      
    # Copied from my pybank analysis sheet
        print("A text file has been created. It should have popped up below or above this script file (in Visual Studio Code)")
        with open("pypoll_analysis_results.txt", 'w') as output_file:
            output_file.write("Election Results\n")
            output_file.write("------------------\n")
            output_file.write(f"Total Votes: {total_votes}\n")
            output_file.write("-------------------------\n")
            for candidate in candidates:
                output_file.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
            output_file.write("-------------------------\n")
            output_file.write(f"Winner: {winner}\n")
            output_file.write("-------------------------\n")

    elif (user_choice == "n"):
        print("Dont't dock me because you chose wrong please!")

    else:
        print("Hmm, looks like you put in something wrong. The options are y and n")
# I decided to try and push myself a bit more for this assignment and decided to rely less on the walkthrough done by the professor but dear lord out of everything I did, exporting the text file was the thing that kicked my a** the most
# "import csv" comes from the comics lesson plan
import csv

# Setting the path to the file (comics, lesson plan)
csvpath = "Resources/budget_data.csv"

# Setting my variables. Found that setting something to "None" can be used to calculate the change that occurs in the data.
# I wanted to try a different function for finding trhe greatest, and came across float. ChatGPT explained it, so I decided to use it.
# the use of inf means (I think) there is always greater increase than -inf, and always a greater decrease than inf, which allows for every row of the data to be included when considering what is thre greatest increase/decrease
# The options is for something special I wanted try out
month_count = 0
total_profit = 0
previous_profit_loss = None
total_change = 0
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}


# Opening CSV using UTF-8 (comics, lesson plan)
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (comics, lesson plan)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Reading each row od data after header
    for row in csvreader:
        print(row)

       # Extracting the date and profit/loss row by row
        date = row[0]
        profit_loss = int(row[1])

        # Calculating total number of months. I use += to do addition and assignment within one step. Instead of month_count = mount_count +1, I can keep the lines smaller with +=
        month_count += 1

        # Calculating total proft/losses.
        total_profit += profit_loss

        # This code will calculate and update the change. Setting 
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            total_change += change

            # Setting the greatest increase/decrease to always "= change" will cause it to loop until it cannot find a greater increase/decrease.
            # Combining the "amount" with "data" under the "if" kept track of the corresponding date to the amount that was consideed the greatest increase/decrease
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = date
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = date

        # Profit/Loss is saved for the next sequence
        previous_profit_loss = profit_loss

    # Calculating the average change
    average_change = total_change / (month_count - 1)

    # Displaying the Financial Analysis results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

    #Something fun here
    options = ["y", "n"]
    user_choice = input("Would you Like to save the results in a new text file? y/n: ")

    # The bane of this homework for me, exporting the results to a text file. ChatGPT came up with this line of code. I came up with the idea of adding the yes and no to create it
    if (user_choice == "y"):
        print("A text file has been created. It should have popped up below or above this script file (in Visual Studio Code)")      
        with open("pybank_analysis_results.txt", 'w') as output_file:
            output_file.write("Financial Analysis\n")
            output_file.write("------------------\n")
            output_file.write(f"Total Months: {month_count}\n")
            output_file.write(f"Total: ${total_profit}\n")
            output_file.write(f"Average Change: ${average_change:.2f}\n")
            output_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
            output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

    elif (user_choice == "n"):
        print("Dont't dock me because you chose wrong please!")

    else:
        print("Now why would you do that? You know what, your gonna have to run python again for doing that!")
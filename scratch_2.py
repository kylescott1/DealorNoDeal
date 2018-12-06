# Import the random number generator to pick a random number in a given range
import random

# Set the possible values for each case
cases = [.01,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]

# Set the amount of cases selected for each round
rounds = [6,5,4,3,2,1,1,1,1]

# Set the round numbers into an array
roundnumber = [1,2,3,4,5,6,7,8,9]

# Create an array to capture the cases (other than your original case) that you have selected
casesSelected = []

# Create an array that contains the value of your original case
yourCase = []

# Set a global variable to set the round number and ensure it starts with 0 on the array
global myround
myround = -1

# Create the main function that will contain the logic for the game
def main():
    # Ask the user to select their original case number
    myCase = input("Choose the case that you think contains One Million Dollars (1 through 26): ")

    # Check to see if the value that the user inputted is within the range of valid case numbers
    if int(myCase) > 26 or int(myCase) < 1:
        print("That case number is incorrect! Please choose a case number between 1 and 26")
        main()
    else:
        # Randomly place dollar amounts into each case
        Case = random.choice(cases)

        # Removes that dollar amount so it cannot be re-used in future cases
        cases.remove(Case)

        # Adds your case to the list to keep track of your case dollar amount
        yourCase.append(Case)

        # Adds the number of the case you selected to the list
        casesSelected.append(myCase)

        # Sets you to the new function of selecting cases to be removed
        Remove(myCase, casesSelected)
		
# Create the function that will remove cases as you select them
def Remove(myCase, casesSelected):

    # Increment the global variable myround by one
    global myround
    myround = myround + 1
	
    # Set the round number for each round
    thisround = roundnumber[myround]
	
# Setup the amounts of cases per round
    if thisround == 1:
        turns = rounds[0]
    if thisround == 2:
        turns = rounds[1]
    if thisround == 3:
        turns = rounds[2]
    if thisround == 4:
        turns = rounds[3]
    if thisround == 5:
        turns = rounds[4]
    if thisround > 5:
        turns = rounds[5]
		
    # Tell the user how many cases to select for this round
    print("Round Number:", thisround)

    # Create the while loop to remove the case from each turn
    while turns != 0:

        # Ask user for the case number to be removed
        caseRemove = input("Choose a case to be removed (1 through 26): ")

        # Check to see if the value that the user inputted is within the range of valid case numbers
        if int(caseRemove) > 26 or int(caseRemove) < 1:
            print("That case number is incorrect! Please choose a case number between 1 and 26")

        # Check to see if the user has already selected this case
        if caseRemove in casesSelected:
            print("Sorry, that case has already been taken. Please try again.")
        else:
            # Randomly place dollar amounts into each case
            Case = random.choice(cases)
            # Set the dollar amount into CaseValue to show the user how much was in that case
            CaseValue = int(Case)
            # Removes that dollar amount so it cannot be re-used in future cases
            cases.remove(Case)
            casesSelected.append(caseRemove)
            # Show the user how much was in their selected case
            print("That case contained", "$", CaseValue)
            # Used to escape the while loop and signal the completion of the removals for this round
            turns = turns - 1
	
    # Checks to see if there is one case left and then send to the Banker function
    if len(cases) == 1:
        Banker(myCase, casesSelected)
    Banker(myCase, casesSelected)
	
# The Banker function is to offer the user the average amount of what is still inside the cases.
def Banker(myCase, casesSelected):
    # Find the average dollar amount of cases remaining
    bankOffer = sum(cases) / float(len(cases))

    # Checks to see if you have 1 case left over
    if len(cases) == 1:

        # Asks the user if they want to take the offer or not
        finalChoice = input("Would you like to keep your case? (Y)es or (N)o: ")
        if finalChoice == "y" or finalChoice == "Y":

            # Display to the user the amount that in their case
            yourCase2 = sum(yourCase)
            print("Congratulations! You won", "$", yourCase2)
            main()

        elif finalChoice == "N" or finalChoice == "n":
            # Display to the user the amount that they won
            print("Congratulations! You won", "$", "%.2f" % bankOffer)
            main()

        # Makes sure the user enters either Y or N or else keep asking them
        else:
            print("You must answer either (Y)es or (N)o.")
            Banker(myCase, casesSelected)

    # This is the banker's offer if there are more than one case remaining
    if len(cases) > 1:

        # Ask the user if they would like to accept the Banker's Offer
        print("The Banker Has Offered You", "$", "%.2f" % bankOffer, "Do You Accept This Amount? (Y)es or (N)o")
        offerDecision = input(">")

        # If the user accepts the offer, display the amount they won and the amount that was in their case
        if offerDecision == "Y" or offerDecision == "y":
            print("Congratulations! You have won", "$", "%.2f" % bankOffer)
            # Set value of the user case
            yourCase2 = sum(yourCase)
            # Display the amount in the original case
            print("Congratulations! Your case contained", "$", yourCase2)
        # If the user declines the offer, remove the selected cases from the game
        elif offerDecision == "N" or offerDecision == "n":
            Remove(myCase, casesSelected)
			
        # Make sure the user enters either Y or N
        else:
            print("You must answer either (Y)es or (N)o.")
            Banker(myCase, casesSelected)    
main()

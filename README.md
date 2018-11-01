
#Used to set case values
cases = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750,1000, 5000, 10000, 25000, 50000, 75000,100000, 200000,300000, 400000, 500000, 750000, 1000000]

#Used to see which case you've already selected
checklist = []

#Used to see the value of your case
yourCase = []


def main():
   """
   myCase is literally just for the looks, the number you choose doesn't determine anything at all besides which case you've selected because the value of your case is randomly selected, and is the probability of it being the same twice is 1/26
   """
   myCase = input("Choose a case 1-26")

   #Checks to see if the value you've input is within the index range of the the length of cases
   if int(myCase) > 26 or int(myCase) < 1:
      print("Out of Range")
      main()

   else:

      #Used to randomly select a value from the list of Values that was listed above
      Case = random.choice(cases)

      #Removes that Value so it cannot be re-used in future casses
      cases.remove(Case)

      #Adds your case to the list to keep track of your case Value
      yourCase.append(Case)

      #Adds the number of the case you selected to the list
      checkList.append(myCase)

      #Directs you to the new function
      Remove(myCase,checkList)
 

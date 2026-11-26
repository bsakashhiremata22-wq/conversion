
import random
import time

print("I" *190)
print("\n\t\t\t\t\t PLAYING HAND CRICKET WITH COMPUTER USING PYTHON AND RANDOM FUCTION\n ")
print("I" * 190)

print()
print("." * 60)
print("\t\t\tTOSS TIME")
print("." * 60)


def start_game():
        print("-"*70)
        print("\t\t\tGAMEPLAY BEGINS")
        print("-"*70)

def result(Your_score,Computer_score,):
    lead_runs = abs(Your_score - Computer_score)
    print()
    print("=" * 150)
    if Your_score > Computer_score:
        print(f"\t\t\t\tCONGRATULATIONS YOU WON BY {lead_runs} RUNS")
    elif Your_score < Computer_score:
        print(f"\t\t\t\tBETTER LUCK NEXT TIME \t YOU LOST BY {lead_runs} RUNS")
    elif Your_score == Computer_score:
        print(f"\t\t\t\tDRAW MATCH YOUR SCORE AND THE COMPUTER SCORE BOTH ARE SAME")
    print("=" * 150)

def Computer_out(Computer_score):
    print("\n\t\t [ COMPUTER GOT OUT ]")
    print("-" * 65)
    print(f"\t\t THE COMPUTER SCORE IS {Computer_score}")
    print("-" * 65)

def You_out(Your_score):
    print("\n\t\t [ YOU GOT OUT ]")
    print("-" * 65)
    print(f"\t\tYOUR SCORE IS {Your_score}")
    print("-" * 65)

def your_batting():
     while True:
        try:
            Your_batting_runs=int(input("\nEnter your batting score:"))
            if Your_batting_runs in range(1,7):
                return Your_batting_runs
            print("Enter the numbers within [1,2,3,4,5,6]")
        except ValueError:
             print("\nEnter only numbers ")

def your_bowling():
    while True:
        try:
            Your_bowling_runs = int(input("\nEnter your bowling score: "))
            if Your_bowling_runs in range(1,7):
                return Your_bowling_runs
            print("Enter the numbers within [1,2,3,4,5,6]")
        except ValueError:
                print("\nEnter only numbers ")
            

User_Choice = input("\nEnter the Choice (Even or odd): ").lower()
while User_Choice not in ["even", "odd"]:
    User_Choice = input("\nEnter the Choice as per given in the Bracket \nEnter the Choice (Even or odd): ").lower()

if User_Choice == "even":
    print("\nYour Choice is Even \nThen the Computer Choice is Odd\n")
else:
    print("\nYour Choice is Odd \nThen The Computer Choice is Even\n")

while True:
    try:
        user_number = int(input("Enter the number within the range(1-6): ")) 
        if  user_number  in range(1,7):
            break
        else:
            print("\nEnter the number within [1,2,3,4,5,6]")
    except ValueError:
        print("\nEnter only Numbers")

Computer_number = random.randint(1, 6)
print(f"\nYour Number is {user_number}\nThe Computer number is {Computer_number}\n")

print("\t\tTossing....\n")
time.sleep(0.9)

Total = user_number + Computer_number
if Total%2==0:
    Total_as_per_choice='Even'
else:
    Total_as_per_choice='Odd'
print(f"The sum of both of numbers is {Total} and It is {Total_as_per_choice} \n") 

Computer_decision = ["batting", "bowling"]


if User_Choice==Total_as_per_choice.lower():
    print("YOU WON THE TOSS")
else:
    print("COMPUTER WON THE TOSS")

if (Total % 2 == 0 and User_Choice == "even") or (Total % 2 != 0 and User_Choice == "odd"):

    Your_decision = (input("Tell your decision (Batting or Bowling):")).lower()
    
    while Your_decision not in ["batting", "bowling"]:
        Your_decision = (input("Tell your decision (Batting or Bowling):")).lower()

    time.sleep(1)
    start_game()

    if Your_decision == "batting":
        Your_score = 0

        print("FIRST INNINGS\n")

        Your_batting_runs=your_batting()
    
        Computer_bowling_runs = random.randint(1, 6)
        print(f"Computer bowling runs is {Computer_bowling_runs}\n")

        while Your_batting_runs != Computer_bowling_runs:
            Your_score += Your_batting_runs

            print(f"\nYour_Current_score: {Your_score}")

            Your_batting_runs=your_batting()
               
            Computer_bowling_runs = random.randint(1, 6)
            print(f"computer bowling runs is {Computer_bowling_runs}\n")

        You_out(Your_score)

        time.sleep(1)
         
        print("\nSECOND INNINGS")
        print(f"\t\t\t\t TARGET:{Your_score}")
        Computer_score = 0
        Computer_batting_runs = random.randint(1, 6)
    
        Your_bowling_runs=your_bowling()
        

        print(f"The Computer batting runs is {Computer_batting_runs}")

        while Computer_batting_runs != Your_bowling_runs:
            Computer_score += Computer_batting_runs

            if  Computer_score > Your_score:
                break

            print(f"\nComputer_Current_Score: {Computer_score}")

            Your_bowling_runs=your_bowling()

            Computer_batting_runs = random.randint(1, 6)
            print(f"The Computer batting runs is {Computer_batting_runs}")

        if Computer_score < Your_score:
            Computer_out(Computer_score)

        lead_runs = abs(Your_score - Computer_score)

        result(Your_score,Computer_score)

    else:
        Computer_score = 0
        Computer_batting_runs = random.randint(1, 6)

        print("\nFIRST INNINGS")

    
        Your_bowling_runs=your_bowling()

        print(f"The Computer batting runs is {Computer_batting_runs}")

        while Computer_batting_runs != Your_bowling_runs:
            Computer_score += Computer_batting_runs

            print(f"\nComputer_Current_Score: {Computer_score}")
             
            Your_bowling_runs=your_bowling()


            Computer_batting_runs = random.randint(1, 6)
            print(f"The Computer batting runs is {Computer_batting_runs}")

        Computer_out(Computer_score)

        print("\nSECOND INNINGS\n")
        print(f"\t\t\t\t TARGET:{Computer_score}")
        Your_score = 0

        Your_batting_runs=your_batting()
    
        Computer_bowling_runs = random.randint(1, 6)
        print(f"computer bowling runs is {Computer_bowling_runs}")

        while Your_batting_runs != Computer_bowling_runs:
            Your_score += Your_batting_runs

            if  Computer_score < Your_score:
                break

            print(f"\nYour_Current_score: {Your_score}")
    
            Your_batting_runs=your_batting()
        
            Computer_bowling_runs = random.randint(1, 6)
            print(f"computer bowling runs is {Computer_bowling_runs}")

        if  Computer_score > Your_score:
            You_out(Your_score)

        lead_runs = abs(Your_score - Computer_score)

        result(Your_score,Computer_score)
else:
    Computer_choosen = random.randint(0, 1)
    Computer_choice= Computer_decision[Computer_choosen]
    print(f"Computer had  decide to {Computer_choice} first")

    start_game()
    print("\nFIRST INNINGS")

    if Computer_choosen == 0:
        Computer_score = 0

    
        Your_bowling_runs=your_bowling()

        Computer_batting_runs = random.randint(1, 6)
        print(f"The Computer batting runs is {Computer_batting_runs}")

        while Computer_batting_runs != Your_bowling_runs:
            Computer_score += Computer_batting_runs
            
            print(f"\nComputer_Current_Score: {Computer_score}")
            
            Your_bowling_runs=your_bowling()

            Computer_batting_runs = random.randint(1, 6)
            print(f"The Computer batting runs is {Computer_batting_runs}")

        Computer_out(Computer_score)

        print("\nSECOND INNINGS\n")
        print(f"\t\t\t\t TARGET:{Computer_score}")
        Your_score = 0

        Your_batting_runs=your_batting()
        
        Computer_bowling_runs = random.randint(1, 6)
        print(f"computer bowling runs is {Computer_bowling_runs}")

        while Your_batting_runs != Computer_bowling_runs:
            Your_score += Your_batting_runs

            if Your_score>Computer_score:
                break

            print(f"\nYour_Current_score: {Your_score}")

            Your_batting_runs=your_batting()
            
            Computer_bowling_runs = random.randint(1, 6)
            print(f"computer bowling runs is {Computer_bowling_runs}")

        if Your_score<Computer_score:
            You_out(Your_score)

        lead_runs = abs(Your_score - Computer_score)

        result(Your_score,Computer_score)

    else:
        Your_score = 0

        Your_batting_runs=your_batting()
            
        Computer_bowling_runs = random.randint(1, 6)
        print(f"computer bowling runs is {Computer_bowling_runs}")

        while Your_batting_runs != Computer_bowling_runs:
            Your_score += Your_batting_runs

            print(f"\nYour_Current_score: {Your_score}")

            Your_batting_runs=your_batting()

            Computer_bowling_runs = random.randint(1, 6)
            print(f"Computer bowling runs is {Computer_bowling_runs}")

        You_out(Your_score)

        print("\nSECOND INNINGS\n")
        print(f"\t\t\t\t TARGET:{Your_score}")
        Computer_score = 0
        Computer_batting_runs = random.randint(1, 6)

        Your_bowling_runs=your_bowling()

        print(f"The Computer batting runs is {Computer_batting_runs}")

        while Computer_batting_runs != Your_bowling_runs:
            Computer_score += Computer_batting_runs

            if Computer_score > Your_score:
                break


            print(f"\nComputer_Current_Score: {Computer_score}")

            Your_bowling_runs=your_bowling()

            Computer_batting_runs = random.randint(1, 6)
            print(f"The Computer batting runs is {Computer_batting_runs}")

        if Computer_score < Your_score:
            Computer_out(Computer_score)

        lead_runs = abs(Your_score - Computer_score)

        result(Your_score,Computer_score)
            

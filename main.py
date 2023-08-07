
import random

list=["rock","paper","scissor"]
c_count=0
p_count=0
while True:
    try:
        start=int(input('''\nEnter your choice
1 Play
2 Exit\n
'''))
    except ValueError:
        print("Invalid choice, please choose the correct option!")
        continue

    
    if start==2:
        break
    if start==1:
        print("\n*********************\n")
        while True:

            try:
                turns = int(input("Best of: "))
                break
            except ValueError:
                print("Invalid choice, please enter a number!\n")
                continue
        count = 1
        while count < turns+1:
            
            comp_choice=random.choice(list)
            try:
                U_choice=int(input('''Enter your choice
1 rock
2 paper 
3 scissor 
'''))
                count += 1
            except ValueError:
                print("Invalid choice, please choose the correct option!\n")
                continue
            if U_choice==1:
                P_choice="rock" 

            elif U_choice==2:
                P_choice="paper"

            elif U_choice==3:
                P_choice="scissor"

            
                
            print(f'''\nYou chose {P_choice}
Computer chose {comp_choice}''')
            if (comp_choice==P_choice):
                print("The match is drawn!\n")
                print("*********************\n")
                p_count=p_count+1
                c_count=c_count+1

            elif ((comp_choice=="rock" and P_choice=="scissor") or (comp_choice=="scissor" and P_choice=="paper") or (comp_choice=="paper" and P_choice=="rock") ):
                print("Computer won the match!\n")
                print("*********************\n")
                c_count=c_count+2

            else:
                print("You won the match!\n")
                print("*********************\n")
                p_count=p_count+2


        print(f"Computer's total points: {c_count}")
        print(f"Your total points: {p_count}")

        if c_count==p_count:
            print("The game is drawn!\n\nThank you for playing the game!!")

        elif c_count>p_count:
            print("Computer won the game!\n\nThank you for playing the game!!")
        else:
            print('''Congratulations!
You won the game!\n\nThank you for playing the game!!\n''')
            
            print("*********************\n")

                




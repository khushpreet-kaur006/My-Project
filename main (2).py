import random

def play_game():
    print("\n CHOUCES:")
    print("1.Stone")
    print("2.Paper")
    print("3.Scissor")
    
    user=int(input("enter your choice="))
    
    computer=random.randint(1,3)
    
    names=["stone","paper","scissor"]
    
    print("You chose=",names[user-1])
    print("Computer chose=",names[computer-1])
    
    if user==computer:
        print("Its Draw")
    elif(user==1 and computer==3)or(user==2 and computer==1)or(user==3 and computer==2):
        print("HURRAY!!!!...YOU WIN")
    else:
        print("ohhh!!...YOU LOSE")
    


#main
while True:
    print("\n----STONE,PAPER,SCISSORS-----")
    print("1.Play games")
    print("Exit")
    
    choice=int(input("Enetr your choice="))
    
    if choice==1:
        play_game()
    elif choice==2:
        print("OOOPS!!!...Game over")
        break
    else:
        print("Invalid choice...TRY AGAIN!!!")
        
print("Always Write 1st letter in  Capital")
while True:
    user1=input("Choose What you want to Throw:")
    user2=input("Choose what you want to throw:")
    if(user1=="Scissor" and user2=="Paper"):
       print("User 1 wins")
    elif(user1=="Paper" and user2=="Scissor"):
       print("User 1 Wins")
    elif(user1=="Stone" and user2=="Paper"):
       print("User 2 Wins")
    elif(user1=="Paper" and user2=="Stone"):
       print("User 2 Wins")
    elif(user1=="Stone" and user2=="Scissor"):
       print("User 1 Wins")
    elif(user1=="Scissor" and user2=="Stone"):
       print("User 2 Wins")
    elif(user1==user2):
       print("Draw")
    else:
       print("Invalid input. Please enter Stone, Paper, or Scissor as instructed.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if(play_again == "no"):
       print("Thank you for playing!")
       break
    
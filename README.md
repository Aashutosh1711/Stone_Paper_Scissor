## Preview Code

Here is a small preview of the core game logic for the "Rock, Paper, Scissors" game:

```python
while True:
    user1 = input("Choose what you want to throw: ")
    user2 = input("Choose what you want to throw: ")

    if user1 == "Scissor" and user2 == "Paper":
        print("User 1 wins")
    elif user1 == user2:
        print("It's a draw!")
    elif user1 == "Stone" and user2 == "Scissor":
        print("User 1 wins")
    elif user1 == "Paper" and user2 == "Stone":
        print("User 2 wins")
    # More game conditions...

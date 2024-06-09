import random

def get_user_choice():
    while True:
        user_choice = input("Enter 'rock', 'paper', 'scissors', or 'exit' to quit: ").lower()
        if user_choice in ['rock', 'paper', 'scissors', 'exit']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose! Computer chose {}.".format(computer_choice)

def play_game():
    while True:
        user_choice = get_user_choice()
        if user_choice == 'exit':
            print("Thanks for playing!")
            break

        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        print("Computer chose", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            print("Congratulations! You've won!")
            break

if __name__ == "__main__":
    play_game()

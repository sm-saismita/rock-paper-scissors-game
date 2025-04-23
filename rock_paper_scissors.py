import random
user_score = 0;


def play_game():
    global user_score;
    options = ["paper","rock","scissors"];
    while True:
        user_input=input("Enter your option").lower()
        if user_input not in options:
            print("Invalid option. Please enter valid option")
            continue
        computer_input = random.choice(options);
        print(f"Computer chose: {computer_input}")
        if user_input==computer_input:
            print("Its a tie!")
        elif (user_input == "paper" and computer_input == "rock") or (user_input == "rock" and computer_input == "scissors") or (user_input == "scissors" and computer_input == "paper"):
            user_score += 1
            print("Yoho.. You win! :)\n Your score is: ",user_score)
        else:
            print("Oops. Computer win!")
        play_more = input("Do you want to play again? y/n").lower()
        if play_more == "y":
            continue
        else:
            print("Thanks for playing")
            break;

play_game();

import time

print("You have 5 seconds to complete each game")


def countdown(seconds):
    while seconds > 0:
        # Use an f-string and \r (carriage return) so the timer updates on the same line
        print(f"Remaining time: {seconds} seconds", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nTimes up!")


# Initialize score variables
count = 0
wrong = 0

print("Game starts now. Are you ready?")
user_ready = input("(yes/no): ").strip().lower()

if user_ready == "yes":
    # Note: A real-time timer during an input() prompt requires threading,
    # but here we can prompt and then check, or structure it sequentially.
    question1 = input("What goes up but never comes down? ").strip().lower()

    if question1 == "age":
        print("Correct!")
        count += 1  # Add 1 mark
    else:
        print("Wrong!")
        wrong += 1

    question2 = input("What is the capital of Germany? ").strip().lower()

    if question2 == "berlin":
        print("Correct!")
        count += 1  # Add 1 mark
    else:
        print("Wrong!")
        wrong += 1

    # Use f-strings for the final scores
    if count >= 2:
        print(f"Congrats! Your score is: {count}")
    else:
        print(f"You failed. Your score is: {count}")

else:
    print("Maybe next time!")
    quit()

import random

def generate_math_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return num1, num2, operator, result

def hangman():
    word_list = [
        "apple", "banana", "orange", "grape", "kiwi", "melon", "peach", "strawberry", "blueberry", "raspberry",
        "carrot", "broccoli", "cucumber", "potato", "tomato", "onion", "garlic", "lettuce", "spinach", "cabbage",
        "dog", "cat", "rabbit", "hamster", "goldfish", "parrot", "turtle", "monkey", "elephant", "giraffe",
        "house", "car", "bicycle", "boat", "train", "airplane", "bus", "motorcycle", "truck", "helicopter",
        "book", "pen", "pencil", "notebook", "marker", "paper", "scissors", "eraser", "ruler", "glue",
        "computer", "phone", "tablet", "television", "radio", "headphones", "camera", "keyboard", "mouse", "speaker",
        "shoe", "sock", "shirt", "pants", "dress", "jacket", "hat", "glove", "scarf", "umbrella",
        "chair", "table", "couch", "bed", "desk", "lamp", "mirror", "clock", "picture", "vase",
        "tree", "flower", "grass", "bush", "rock", "mountain", "river", "lake", "ocean", "beach",
        "sun", "moon", "star", "cloud", "rain", "snow", "wind", "thunder", "lightning", "rainbow",
        "pizza", "burger", "sandwich", "pasta", "salad", "soup", "steak", "chicken", "fish", "sushi",
        "cake", "cookie", "icecream", "chocolate", "candy", "pie", "donut", "muffin", "popcorn", "pretzel",
        "music", "movie", "game", "sport", "art", "dance", "poetry", "theater", "comedy", "drama"
    ]

    while True:
        word = random.choice(word_list)
        guessed_letters = []
        attempts = 6

        print("Welcome to Hangman!")
        print("Try to guess the word before the hangman is complete.")
        print("You have {} attempts.".format(attempts))

        while True:
            display = ""
            for letter in word:
                if letter in guessed_letters:
                    display += letter
                else:
                    display += "_"
            print(display)

            if display == word:
                print("Congratulations! You guessed the word: {}!".format(word))
                break

            guess = input("Enter a letter (or type 'hint' for a hint): ").lower()

            if guess == "hint":
                num1, num2, operator, result = generate_math_problem()
                print(f"What is {num1} {operator} {num2}?")
                try:
                    answer = int(input("Enter your answer: "))
                    if answer == result:
                        print("Correct! Here's a letter for you.")
                        for i in range(len(word)):
                            if word[i] not in guessed_letters:
                                guessed_letters.append(word[i])
                                break
                    else:
                        print("Incorrect!")
                except ValueError:
                    print("Please enter a valid integer.")
                continue

            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                attempts -= 1
                print("You have {} attempts left.".format(attempts))
                if attempts == 0:
                    print("Sorry, you ran out of attempts. The word was: {}.".format(word))
                    break

        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

hangman()

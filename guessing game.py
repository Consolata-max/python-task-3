import random


print("Hi , Let's play a guessing game.")


def random_game():

    play = True
    while play:

        easy = random.randint(1, 10)
        medium = random.randint(1, 20)
        hard = random.randint(1, 50)
        # prompts the user to select a difficulty to play on
        print("There are 3 levels, easy, medium and hard "
                "\nType 'e' for easy, 'm' for medium, or 'h' for hard!")

        level_selection = True
        while level_selection:
            level = input()
            if level == "e":
                print("\n welcome to easy level!")
                level_selection = not True
                break
            if level == "m":
                print("\n welcome to medium level!")
                level_selection = not True
                break
            if level == "h":
                print("\nwelcome to hard level!")
                level_selection = not True
                break
            else:
                print("Invalid input!\nPlease enter either e, m, or h. ")


    # If the user selects e for Easy - 6tries
        if level == 'e':
            print("Because you selected easy, you'll have 6\nguesses to guess a number between 1-10.")
            guesses_left = 6
            while guesses_left != 0:
                try1 = int(input("what's your guess? \n"))
                if try1 == easy:
                    print("You got it right!" + str(easy))
                    break
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                # If the user runs out of guesses
                if guesses_left == 0:
                    print('Game over')

    # If the user selects m for Medium - 4tries
        if level == 'm':
            print("Because you selected medium, you'll have 4\nguesses to guess a number between 1-20.")
            guesses_left = 4
            while guesses_left != 0:
                try1 = int(input("what's your guess? \n"))
                if try1 == medium:
                    print("You got it right! " + str(medium))
                    break
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

                # If the user runs out of guesses
                if guesses_left == 0:
                    print('Game over')

    # If the user selects h for Hard - 3 tries
        if level == 'h':
            print("Because you selected hard, you'll have 5\nguesses to guess a number between 1-50.")
            guesses_left = 3
            while guesses_left != 0:
                try1 = int(input("what's your guess? \n"))
                if try1 == hard:
                    print("You got it right! " + str(hard))
                    break
                guesses_left -= 1
                print('You now have ' + str(guesses_left) + ' guesses left!')

              # If the user runs out of guesses
                if guesses_left == 0:
                    print('Game over')

        

random_game()



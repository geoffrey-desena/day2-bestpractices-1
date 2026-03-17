from dicegame.runner import GameRunner


def main():
    print("Add the values of the dice")
    print("It's really that easy")
    print("What are you doing with your life.")
    GameRunner.run()


if __name__ == "__main__":
    main()

# %% Debugging notes

# In runner.py:
    # We find where the sum is calculated in the function GameRunner.answer
    # It simply counts the dice
    
    # Change: 1 -> die.value
    
    
    # We find the prompt in line 55, which asks the user to enter [Y/n], but
    # the code only accepts "y" or ""
    
    # Change: Y -> y
    # Change: line 57 accepts Y, y, or nothing
    # Change: line 60 else statement, instead of the useless exception,
        # I call a different function that exits the loops

# In utils.py
    # added more_helpful_exception that prints goodbye message
    
# It's still not counting the score properly, but I'm out of time.
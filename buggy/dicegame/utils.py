class UnnecessaryError(Exception):
    pass


def i_just_throw_an_exception():
    value = 1
    def some_inner_function():
        value += 1

    some_value = "I don't know what you were expecting"
    raise UnnecessaryError("You actually called this function...")

def more_helpful_comment():
    print("Sorry you don't want to play anymore.")

def is_valid(guess_digit) -> bool:
    if guess_digit.isdigit() and 1 <= int(guess_digit) <= 100:
        return True
    return False


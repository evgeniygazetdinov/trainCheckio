import re


def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    result =  ''.join((word if counter != 0 else word.upper() for counter, word in enumerate(text) ))
    if result[-1] != '.':
        result+= '.'
    return result


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    
    print("Coding complete? Click 'Check' to earn cool rewards!")
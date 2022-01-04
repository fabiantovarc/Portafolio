def is_palindrome(string: str) -> bool:
    """
    Checks if a string is a palindrome
    """
    string = string.lower()
    string = string.replace(" ", "")
    string = string.replace(".", "")
    string = string.replace(",", "")
    string = string.replace("!", "")
    string = string.replace("?", "")
    string = string.replace("-", "")
    string = string.replace("'", "")
    string = string.replace("\"", "")
    string = string.replace(";", "")
    string = string.replace(":", "")
    string = string.replace("(", "")
    string = string.replace(")", "")
    string = string.replace("[", "")
    string = string.replace("]", "")
    string = string.replace("{", "")
    string = string.replace("}", "")
    return string == string[::-1]

def run():
    print(is_palindrome("hola"))

if __name__ == "__main__":
    run()
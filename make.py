"""
Describe what the program does.
First Last - Month Year
"""

def main() -> None:
    #input
    first: str = input("First name: ")
    middle: str = input("Middle name: ")
    last: str = input("Last name: ")
    if len(middle) > 0:
        username: str = first[0] + middle[0] + last
    else:
        username: str = first[0] + last
    username = username.lower()
    username = username.replace(" ", "-")
    username = username.replace("'", "")
    print(username)

if __name__ == "__main__":
    main()
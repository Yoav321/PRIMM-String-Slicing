"""
Contains code to teach about string slicing.
First Last - Month Year
"""


def main() -> None:
    word: str = "creative computing"
    
    print(word[1:5:2])
    print(word[:8:3])
    print(word[-2:-6:-1])
    print(word[::-1])

if __name__ == "__main__":
    main()
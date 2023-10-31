print("Welcome to the Letter Counter App")

name = input("Please enter your name: ").title().strip()
print("\nEnter a message and I will count a specific letter for you!")

message = input("enter your message: ").lower()
letter = input("enter a letter: ").lower()

def countLetter(name, message, letter):
    result = message.count(letter)
    print(f"\n{name}, your message has {result} {letter} in it. Thank you!")


countLetter(name, message, letter)
PlayerOne = raw_input("Rock, paper, scissors? ").lower()
PlayerTwo = raw_input("Rock, paper, scissors? ").lower()
x = ('rock')
y = ('paper')
z = ('scissors')
if PlayerOne == x and PlayerTwo == x:
    print("Draw.")
elif PlayerOne == y and PlayerTwo == y:
    print("Draw.")
elif PlayerOne == z and PlayerTwo == z:
    print("Draw.")
elif PlayerOne == y and PlayerTwo == x:
    print("Paper covers rock.")
elif PlayerOne == y and PlayerTwo == z:
    print("Scissors cut paper.")
elif PlayerOne == x and PlayerTwo == y:
    print("Paper covers rock.")
elif PlayerOne == z and PlayerTwo == y:
    print("Scissors cut paper.")
elif PlayerOne == x and PlayerTwo == z:
    print("Rock breaks scissors.")
elif PlayerOne == z and PlayerTwo == x:
    print("Rock breaks scissors.")

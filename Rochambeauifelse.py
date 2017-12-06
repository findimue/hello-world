PlayerOne = raw_input("Rock, paper, scissors? ").lower()
PlayerTwo = raw_input("Rock, paper, scissors? ").lower()
x = ('rock')
y = ('paper')
z = ('scissors')
if PlayerOne == x:
    if PlayerTwo == x:
        print("Draw.")
    else:
        if PlayerOne == y:
            if PlayerTwo == y:
                print("Draw.")
        else:
            if PlayerOne == z:
                if PlayerTwo == z:
                    print("Draw.")
            else:
                if PlayerOne == y:
                    if PlayerTwo == x:
                        print("Paper covers rock.")
                else:
                    if PlayerOne == y:
                        if PlayerTwo == z:
                            print("Scissors cut paper.")
                    else:
                        if PlayerOne == x:
                            if PlayerTwo == y:
                                print("Paper covers rock.")
                        else:
                            if PlayerOne == z:
                                if PlayerTwo == y:
                                    print("Scissors cut paper.")
                            else:
                                if PlayerOne == x:
                                    if PlayerTwo == z:
                                        print("Rock breaks scissors.")
                                else:
                                    if PlayerOne == z:
                                        if PlayerTwo == x:
                                            print("Rock breaks scissors.")
                                        
                 

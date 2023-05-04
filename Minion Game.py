def minion_game(string):
    # your code goes here
    points_vowels = points_consonants = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(string)):
        if string[i] in vowels:
            points_vowels += len(string[i:])
        else:
            points_consonants += len(string[i:])

    if points_vowels > points_consonants:
        print("Kevin", points_vowels)
    elif points_vowels < points_consonants:
        print("Stuart", points_consonants)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
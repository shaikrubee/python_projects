def character_sequence(numbers):
    alpha="abcdefghijklmnopqrstuvwxyz"
    new_alpha=""
    for i in numbers:
        x=alpha[i-1]
        new_alpha+=x
    print(new_alpha)

numbers=list(map(int,input().split()))
character_sequence(numbers)

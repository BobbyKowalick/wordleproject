import random as rand

possiblefinals: list = [
    'bobby',
    'riley',
    'adieu',
    'sleep',
    'booty'
]

finalword = rand.choice(possiblefinals)

charlimit: int = 5
global lives

def guessing() -> str:
    while True:
        guessword = input("")
        if len(guessword) == charlimit:
            return guessword
        else:
            print("invalid guess")
            print(f'guess a word {charlimit} letters long')
            continue

def compareguesstofinal(guess: str, final: str) -> bool:
    standingsreport: list = []
    outputstr: str = ""
    if guess == final:
        return False
    else:
        for i in range(charlimit):
            standingsreport.append(guess[i] == final[i])

        for j in range(charlimit):
            if standingsreport[j]:
                outputstr += finalword[j]
            else:
                outputstr += "_"

        print(outputstr)
        return True

def main():
    lives = 5
    guess = guessing()
    while compareguesstofinal(guess, finalword):
        if lives > 0:
            print(f'youve got {lives} lives left')
            guess = guessing()
            lives -= 1
        else:
            print("youre out of lives fucktard, you lost")
            break

    print(f'final word was {finalword}')

if __name__ == "__main__":
    main()
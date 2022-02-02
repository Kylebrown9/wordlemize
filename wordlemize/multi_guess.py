from typing import List

def info(answer: str, guesses: List[str]) -> str:
    return ''.join(_info(answer, guesses))

def _info(answer: str, guesses):
    letters = set(''.join(guesses))

    for i, letter in enumerate(answer):
        for guess in guesses:
            if letter == guess[i]:
                yield 'p' # position match
                break
        else:
            if letter in letters:
                yield 'l'
            else:
                yield 'n' # no match
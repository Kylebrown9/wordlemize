
from typing import List, Tuple, Dict, Optional
import json


def color(guess: str, word: str) -> str:
    return ''.join(_color(guess, word))

def _color(guess: str, word: str):
    for i, letter in enumerate(word):
        if letter == guess[i]:
            yield 'p' # position match
        elif letter in guess:
            yield 'l' # letter match
        else:
            yield 'n' # no match

def can_distinguish_pair(guess: str, word1: str, word2: str) -> bool:
    return color(guess, word1) != color(guess, word2)

def can_distinguish_group(guess: str, words: set) -> bool:
    return len(set(color(guess, word) for word in words)) == len(words)


def largest_distinguishable_group(
        valid_guesses: List[str],
        valid_answers: List[str]
    ) -> Tuple[Optional[str], Dict[str, str]]:

    largest_group_guess = None
    largest_group = {}
    for guess in valid_guesses:
        group = {}
        for answer in valid_answers:
            answer_color = color(guess, answer)
            if answer_color not in group:
                group[answer_color] = answer

        if len(largest_group) < len(group):
            largest_group_guess = guess
            largest_group = group

            # print(guess, ' ', group)

    return largest_group_guess, largest_group

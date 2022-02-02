from pathlib import Path

def get_legal_answers():
    return (Path.cwd() / 'reference' / 'legal_answers.txt').read_text().split('\n')

def get_legal_guesses():
    return (Path.cwd() / 'reference' / 'legal_guesses.txt').read_text().split('\n')
from . import color, dataset

def main():
    print(color.largest_distinguishable_group(dataset.get_legal_guesses(), dataset.get_legal_answers()))

if __name__ == '__main__':
    main()
def predict_smart_contract_word():
    # List of common four-letter words used in smart contracts
    four_letter_words = ['CODE','NODE', 'DEMO', 'DONE', 'DEAL', 'DEMO', 'DOOR', 'DEBT', 'DEEP', 'EDGE', 'FEND', 'HERO', 'HOLD', 'HOME', 'IDOL', 'JUDO', 'KIND', 'LIED', 'MODE', 'POEM', 'REDO', 'SEND', 'VEND', 'YOND', 'ZEDS']

    # Set of letters to ignore
    ignore_letters = {'A', 'T', 'R', 'L', 'N', 'S', 'F', 'I', 'M'}

    # Initialize an empty list to store potential matches
    potential_matches = []

    # Iterate through each word in the list
    for word in four_letter_words:
        # Check if the word contains the letters D, E, and O
        if 'D' in word and 'E' in word and 'O' in word:
            # Check if the word contains any of the ignored letters
            if not any(letter in ignore_letters for letter in word):
                potential_matches.append(word)

    return potential_matches

# Call the function and print the result
result = predict_smart_contract_word()
print(result)

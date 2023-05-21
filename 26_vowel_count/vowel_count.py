def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    phrase = phrase.lower()
    output = {}

    def is_vowel(char):
       return char in 'aeiou'

    for char in phrase:
        if is_vowel(char):
            output[char] = output.get(char,0) + 1

    return output




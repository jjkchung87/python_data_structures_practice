def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?'
    """
    def is_vowel(char):
       return char in 'aeiouAEIOU'
    
    vowels =[]
    vowel_position = []

    for i,char in enumerate(s) :
        if is_vowel(char):
            vowels.append(char)
            vowel_position.append(i)

    vowels.reverse()

    vowels_dict = dict(zip(vowel_position, vowels))

    new_string = ''

    for i,char in enumerate(s) :
        if i in vowels_dict:
            new_string += vowels_dict[i]
        else:
            new_string += s[i]

    return new_string







    # 1) determine if char is a vowel 
    # 2) determine index of each vowel 
    # 3) Place vowels in a list
    # 4) Place indices in a list
    # 5) reverse vowel_list, then join with indices_list to create vowel_dict
    # 5) splice vowels back into String 


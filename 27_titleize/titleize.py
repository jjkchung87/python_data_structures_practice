def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    listed_phrase = phrase.split(' ')
    for i in range(len(listed_phrase)):
        listed_phrase[i] = listed_phrase[i].capitalize()
    
    new_string = ' '.join(listed_phrase)
    return new_string
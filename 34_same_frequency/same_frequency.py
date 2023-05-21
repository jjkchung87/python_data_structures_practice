def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    list_num1 = list(str(num1))
    list_num2 = list(str(num2))

    list_num1.sort()
    list_num2.sort()

    return list_num1 == list_num2

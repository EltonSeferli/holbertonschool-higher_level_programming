def no_c(my_string):
    """Return a string without characters 'c' and 'C'"""
    new_string = ""

    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string += ch

    return new_string

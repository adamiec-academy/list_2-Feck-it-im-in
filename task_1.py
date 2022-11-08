def remove_parentheses(text):
    result = ""
    is_inside = False
    for letter in text:
        if letter == "(":
            is_inside = True
            text.replace(letter, "")
        elif letter == ")":
            is_inside = True
            text.replace(letter, "")
        else:
            result = result + letter

    return result

# nwm co zrb dalej, sry

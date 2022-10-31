def remove_parentheses(text):
    result = ""
    is_inside = False
    for letter in text:
        if letter == "(":
            is_inside = True
            pass
        elif letter == ")":
            is_inside = True
            pass
        else:
            result = result + letter

    return result


print(remove_parentheses("(Nie) jest tak zle."))
# work in progress

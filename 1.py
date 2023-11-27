def isValid(s):
    stack = []
    bracket_dict = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_dict.values():
            stack.append(char)
        elif char in bracket_dict.keys():
            if not stack or bracket_dict[char] != stack.pop():
                return False
        else:
            return False

    return not stack

# Приклад
example_string = "()[]{}"
print(isValid(example_string))  # Вивід: True

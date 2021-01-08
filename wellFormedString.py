# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

# For example, given the string "()({})", you should return true.

# Given the string "([)]" or "((()", you should return false. 


def wellFormed(myString):
    myStack = []
    for i in myString:
        if i in ["{","(","["]:
            myStack.append(i)

        if i == "}":
            character = myStack.pop()
            if character!= '{':
                return False

        if i == ")":
            character = myStack.pop()
            if character!= '(':
                return False

        if i == "]":
            character = myStack.pop()
            if character!= '[':
                return False
    if myStack:
        return False
    return True

if __name__ == "__main__":
    print(wellFormed("()({})"))

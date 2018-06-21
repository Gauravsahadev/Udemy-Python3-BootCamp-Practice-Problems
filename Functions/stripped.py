# Program to remove the white spaces and reverse the string using slices and compare it to return true of false.
def stripped(string):
    pass
    stripped = string.replace(" ", "")
    stripped = stripped.lower()
    return stripped == stripped[::-1]


s = input("Enter string: ")
print(stripped(s))

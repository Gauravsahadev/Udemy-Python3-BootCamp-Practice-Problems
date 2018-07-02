# Program to change colour of the text

from pyfiglet import figlet_format
from termcolor import colored

valid_colors = ("red", "blue", "green", "white", "cyan", "magenta")

text = input("Enter your text: ")
colour = input("Which color: ")

if colour not in valid_colors:
    colour = "blue"

ascii_text = figlet_format(text)
colour_ascii = colored(ascii_text, color=colour)
print(colour_ascii)

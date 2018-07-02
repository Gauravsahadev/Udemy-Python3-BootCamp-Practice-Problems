from termcolor import colored
t = colored("hello", color="cyan", on_color="on_magenta", attrs=["blink"])
print(t)

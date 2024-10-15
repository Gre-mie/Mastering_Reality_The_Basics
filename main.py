import re

def find_oddities(extract):
    oddities = []

    oddity = False
    odd_arr = []
    for char in extract:
        if char == '(':
            oddity = True

        elif char == ')':
            odd_str = "".join(odd_arr)
            oddities.append(odd_str)
            odd_arr = []
            oddity = False

        else:
            if oddity == True:
                odd_arr.append(char)

    return oddities


def main():
    extract_path = "chapter_1_extract.txt"
    extract = None
    try:
        with open(extract_path) as extract_text:
            extract = extract_text.read()
    except FileNotFoundError:
        print(f"\n\033[31mFile Not Found: \033[38;5;{214}m{extract_path}\033[39m")

    
    oddities = []
    if extract == None:
        print("Exiting programme\n")
        exit()
    else:
        for oddity in find_oddities(extract):
            print(oddity)

    


main()
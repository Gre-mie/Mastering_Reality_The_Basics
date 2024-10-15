

def main():
    extract_path = "chapter_1_extract.txt"
    extract = None
    try:
        with open(extract_path) as extract_text:
            extract = extract_text.read()
    except FileNotFoundError:
        print(f"\n\033[31mFile Not Found: \033[38;5;{214}m{extract_path}\033[39m")

    if extract == None:
        print("Exiting programme\n")
        exit()
    else:
        print(extract) # test

    


main()
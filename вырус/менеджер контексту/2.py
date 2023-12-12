def readfile(file):
    try:
        with open(file, "w") as f:
            print(f.read())
    except FileNotFoundError:
        print("NO FILE")
readfile("input.txt")
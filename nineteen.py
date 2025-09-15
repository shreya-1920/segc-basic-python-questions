#print star pattern of your name
def print_pattern(ch):
    patterns = {
        "A": ["  *  ",
              " * * ",
              "*****",
              "*   *",
              "*   *"],

        "H": ["*   *",
              "*   *",
              "*****",
              "*   *",
              "*   *"],

        "R": ["**** ",
              "*   *",
              "**** ",
              "*  * ",
              "*   *"],

        "S": [" ****",
              "*    ",
              " *** ",
              "    *",
              "**** "],

        "E": ["*****",
              "*    ",
              "**** ",
              "*    ",
              "*****"],

        "Y": ["*   *",
              " * * ",
              "  *  ",
              "  *  ",
              "  *  "]
    }
    return patterns.get(ch.upper(), ["     "]*5)   # blank if letter not found

def print_name(name):
    rows = [""]*5
    for ch in name:
        pattern = print_pattern(ch)
        for i in range(5):
            rows[i] += pattern[i] + "  "   # space between letters
    for row in rows:
        print(row)

# Example
print_name("SHREYA")

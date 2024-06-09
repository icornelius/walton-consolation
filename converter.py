import os

csv = 'line-number-concordance.csv'

def load_data(file_path):
    with open(file_path) as file:
        return {str(index): line.strip().split(",") for index, line in enumerate(file)}

def get_valid_input(prompt, options):
    while True:
        choice = input(prompt)
        if choice in options:
            return choice
        prompt = "Invalid input. Try again. "

print("Welcome to the reference converter for Walton's Boethius.\n")

# Confirm CSV exists
if not os.path.exists(csv):
    print("Source file not found.")
    exit()

# Identify a source to query
print("What reference system do you want to convert from?\n\n"
        "(1) Mark Science's continuous stanza numbering\n"
        "(2) Mark Science's numbering by book, section, and stanza\n"
        "(3) Nicholas Myklebust's numbering by book and line\n"
        "(4) Karl Schümmer's continuous stanza numbering\n")

options = {
        1:"Science (continuous stanzas)",
        2:"Science (stanzas by section)",
        3:"Myklebust (lines by book)",
        4:"Schümmer (continuous stanzas)"
}

prompt = "Enter a number (1)-(4) from the options: "
read_source = get_valid_input(prompt, str(options.keys()))

# Load file as dictionary of lists
data = load_data(csv)

# Load a query-term from input
repeat = True
while repeat:
    if read_source == "1" or read_source == "4":
        input_msg = "Enter a stanza number: "
        query = input(input_msg)
    elif read_source == "2":
        print(" * For the translation proper, use the format, e.g., \"3m9\", for the ninth meter of the third book\n"
              " * For the translator's FIRST PREFACE (preceding the Prologue), enter \"Pref1\"\n"
              " * For the translator's PROLOGUE (preceding Book 1), enter \"Prol\"\n"
              " * For the translator's SECOND PREFACE (preceding Book 4), enter \"Pref2\"\n")
        input_msg = "Enter a section code: "
        section = input(input_msg)
        input_msg = "Enter a stanza number: "
        stanza = input(input_msg)
        query = section + "." + stanza
    elif read_source == "3":
        input_msg = "Enter a book number (for initial prefatory material, enter \"P1\"; for the second preface enter \"P2\"): "
        section = input(input_msg)
        input_msg = "Enter a line number: "
        line = input(input_msg)
        if section == "P1" or section == "1" or section == "2" or section == "3":
            stanza = (int(line)-1) // 8 + 1
            floor_line = int(stanza) * 8 - 7
        elif section == "P2" or section == "4" or section == "5":
            stanza = (int(line)-1) // 7 + 1
            floor_line = int(stanza) * 7 - 6
        query = str(section) + "." + str(floor_line)

    # Run the query
    found=False
    for key in range(len(data)):
        found = data[str(key)][int(read_source)] == query
        if found:
            for i in range(4):
                print("\t" + options[i+1] + ":\t" + data[str(key)][i+1])
            break
    if not found:
        print("Query term not found.")
    print()

    # Offer to query again
    repeat = input("Type 'q' to quit or any key to convert another reference from the same source. ").lower() != 'q'

print("Goodbye")

import os
import pandas as pd

source_csv = 'line-number-concordance.csv'

print("Welcome to the reference converter for Walton's Boethius.\n")

if not os.path.exists(source_csv):
  print("Source file not found.")
  exit()

print("What reference system do you want to convert from?\n\n"
        "(1) Mark Science's continuous stanza numbering\n"
        "(2) Mark Science's numbering by book, section, and stanza\n"
        "(3) Nicholas Myklebust's numbering by book and line\n"
        "(4) Karl Schümmer's continuous stanza numbering\n")

input_msg = "Enter a number (1)-(4) from the options above: "
option_dict = {1:"Science (stanzas continuous)",
        2:"Science (stanzas by section)",
        3:"Myklebust",
        4:"Schümmer"}
valid = False

while valid == False:
  read = input(input_msg)
  if int(read) not in option_dict.keys():
      input_msg = "Try again.\nEnter a numeral between 1 and 4: "
  else:
    print("You have selected " + read + ", " + option_dict[int(read)] + "\n")
    valid = True

dframe = pd.read_csv(source_csv)

repeat = True

while repeat == True:
    if read == "1" or read == "4":
        input_msg = "Enter a stanza number: "
        ref = input(input_msg)
    elif read == "2":
        print(" * For the translation proper, use the format, e.g., \"3m9\", for the ninth meter of the third book\n"
              " * For the translator's FIRST PREFACE (preceding the Prologue), enter \"Pref1\"\n"
              " * For the translator's PROLOGUE (preceding Book 1), enter \"Prol\"\n"
              " * For the translator's SECOND PREFACE (preceding Book 4), enter \"Pref2\"\n")
        input_msg = "Enter a section code: "
        section = input(input_msg)
        input_msg = "Enter a stanza number: "
        stanza = input(input_msg)
        ref = section + "." + stanza
    elif read == "3":
        input_msg = "Enter a book number (for initial prefatory material, enter \"P1\"; for the second preface enter \"P2\"): "
        section = input(input_msg)
        input_msg = "Enter a line number: "
        line = input(input_msg)
        if section == "P" or section == "1" or section == "2" or section == "3":
            stanza = (int(line)-1) // 8 + 1
            floor_line = int(stanza) * 8 - 7
        elif section == "P2" or section == "4" or section == "5":
            stanza = (int(line)-1) // 7 + 1
            floor_line = int(stanza) * 7 - 6
        ref = str(section) + "." + str(floor_line)
    else:
        print("Sorry, that option is not yet available.")
        exit()

    conversion_table = dframe[dframe[dframe.columns[int(read)]] == ref].drop(columns=['logical_ln.'])
    print("Looking for reference point", ref, "in", option_dict[int(read)], "...")
    print("\n", conversion_table, "\n")

    input_msg = "Convert another reference from the same source? (y/n) "
    again = input(input_msg)
    if again == "n":
      print("Goodbye")
      repeat = False

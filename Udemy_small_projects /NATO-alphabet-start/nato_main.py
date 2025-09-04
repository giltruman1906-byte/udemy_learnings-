import pandas as pd

# student_grades = { "students" : ["Alice", "Bob", "Charlie"],
#                    "grades" : [85, 92, 78] }

# pandas_line = pd.DataFrame(student_grades)
# print(pandas_line)

nato = pd.read_csv("/Users/giltruman/giltruman/NATO alphabet project/NATO-alphabet-start/nato_phonetic_alphabet.csv")
# print(nato)
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
# print(nato_dict)



def validate_input():
    word = input("enter a word ").upper()
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError as e:
        print(f"Sorry, only letters in the alphabet please. {e}")
        validate_input()
    else:   
        print(output_list)

validate_input()
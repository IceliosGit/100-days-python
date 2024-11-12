import pandas
# Create a dic from the CSV:
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {}
for (index, row) in nato_df.iterrows():  # need to call index, won't work otherwise
    nato_dict.update({row["letter"]: row["code"] for letter in row})
print(nato_dict)

# Create a list of the phonetic code words from a word that the user inputs:
user_input = input("Enter a word:")
nato_list_user = [nato_dict[letter.upper()] for letter in list(user_input)]
print(nato_list_user)



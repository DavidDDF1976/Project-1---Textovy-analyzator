"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: David Del Favero
email: ddf@centrum.cz
discord: David_DF

"""
from task_template import TEXTS
usernames_passwords = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
user_input = input("username:")
password_input = input("password:")
pocet_slov_malym_pismem = 0
pocet_slov_velkym_pismen = 0
pocet_slov_zac_velkym_pismenem = 0
pocet_cisel = 0
suma_cisel = 0
delka_frekvence = {}

if user_input in usernames_passwords and password_input == usernames_passwords.get(user_input):
    print("-" * 44)
    print(f"Welcome to the app: {user_input}")
    print(f"We have 3 texts to be analyzed.")
    print("-" * 44)
    vyber_textu = input("Enter a number btw. 1 and 3 to select:")
    print("-" * 44)
    index_textu = int(vyber_textu) - 1
    split_text = TEXTS[index_textu].split()
    pocet_slov =  len(split_text) - pocet_cisel
    for i in split_text:
        if(i.islower()):
            pocet_slov_malym_pismem += 1
        if(i[0].isupper()):
            pocet_slov_zac_velkym_pismenem += 1
        elif (i.isupper()):
            pocet_slov_velkym_pismen += 1
    for cisla in split_text:
        if cisla.isnumeric():
            pocet_cisel += 1
    for cislo in split_text:
        if cislo.isdigit():
            suma_cisel += int(cislo)
    print(f"There are {pocet_slov} words in the selected text.")
    print(f"There are {pocet_slov_velkym_pismen} titlecase words.")
    print(f"There are {pocet_slov_zac_velkym_pismenem} uppercase words.")
    print(f"There are {pocet_slov_malym_pismem} lowercase words.")
    print(f"There are {pocet_cisel} numeric strings.")
    print(f"The sum of all the numbers {suma_cisel}")
    print("-" * 44)
    print("LEN | OCCURENCES | NR.")
    print("-" * 44)
    for slovo in split_text:
        pocet_char = len(slovo)
        if len(slovo) in delka_frekvence:
            delka_frekvence[pocet_char] += 1
        else:
            delka_frekvence[pocet_char] = 1
    for delka, frekvence in sorted(delka_frekvence.items()):
        bar = '*' * frekvence
        print(f'{delka:2d}|{bar:15s}|{frekvence}')
else:
    print("username:", user_input)
    print("password:", password_input)
    print("unregistered user, terminating the program")






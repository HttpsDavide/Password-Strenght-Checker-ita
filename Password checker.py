import string
import getpass

def check_password_strength(password):
    lower_alpha_count = upper_alpha_count = number_count = whitespace_count = special_char_count = 0
    for char in list(password):
        if char in string.ascii_lowercase:
            lower_alpha_count += 1
        elif char in string.ascii_uppercase:
            upper_alpha_count += 1
        elif char in string.digits:
            number_count += 1
        elif char == ' ':
            whitespace_count += 1
        else:
            special_char_count += 1
    strength = 0
    remarks = ''

    if lower_alpha_count >= 1:
        strength += 1
    if upper_alpha_count >= 1:
        strength += 1
    if number_count >= 1:

        strength += 1
    if whitespace_count >= 1:
        strength += 1
    if special_char_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "Questa è una pessima password. Cambiala il prima possibile."
    elif strength == 2:
        remarks = "Non è una buona password. Creane una più difficile"
    elif strength == 3:
        remarks = "La tua password va bene, ma può essere migliorata"
    elif strength == 4:
        remarks = "La tua password è difficile da indovinare. Ma puoi renderla ancora più sicura"
    elif strength == 5:
        remarks = "Bravo, questa password ti proteggerà dagli hacker"

    print("La tua password ha:-")
    print(f"{lower_alpha_count} Lettere Minuscole")
    print(f"{upper_alpha_count} Lettere Maiuscole")
    print(f"{number_count} Caratteri")
    print(f'{whitespace_count} Spazi bianchi')
    print(f"{special_char_count} Caratteri speciali")
    print(f"Punteggio Password: {strength}/5")
    print(f"Remarks: {remarks}")
    print("")
    print("")
    print("===== Created By AO BUONGIORNO#2910 ig https_davide_ =====")

print("===== Benvenuto in Password Strength Checker=====")
print("")
print("LA PASSWORD MENTRE VERRÀ SCRITTA NON SARÀ VISIBILE")
print("")
while 1:
    choice = input("Vuoi controllare una password? (s/n) : ")
    if 's' in choice.lower():
        password = getpass.getpass("Inserisci la password: ")
        check_password_strength(password)
    elif 'n' in choice.lower():
        print('Buona giornata...')
        break
    else:
        print('Non valido, riprova')
    print()

    #by @https_davide_
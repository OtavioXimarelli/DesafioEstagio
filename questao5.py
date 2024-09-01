def reverse_string(string):

    reverse = ""
    for i in range(len(string) -1, -1, -1):
        reverse += string[i]
    return reverse

if __name__ == "__main__":
    usr_string = str(input("Digite sua frase para inverter: "))
    result = reverse_string(usr_string)
    print(result)
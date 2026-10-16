texto_cifrado = input("Introduce el texto cifrado: ")

for key in range(26):
    texto_plano = ""

    for caracter in texto_cifrado:

        if caracter.isalpha():

            if caracter.isupper():
                inicio = ord("A")
            else:
                inicio = ord("a")

            posicion = ord(caracter) - inicio
            nueva_posicion = (posicion - key) % 26
            nuevo_caracter = chr(nueva_posicion + inicio)

            texto_plano += nuevo_caracter

        else:
            texto_plano += caracter

    print("Key", key, ":", texto_plano)
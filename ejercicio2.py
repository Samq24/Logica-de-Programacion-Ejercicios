def palindromo(texto):
    texto = texto.lower()
    texto = ''.join(c for c in texto if c.isalnum())
    texto = texto.translate(str.maketrans('áéíóúü', 'aeiouu'))
    invertido = texto[::-1]
    return invertido == texto
print("¿Es un palíndromo?", palindromo("Dábale arroz a la zorra el abad"))

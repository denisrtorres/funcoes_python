def contar_vogais(texto):
    count_vogal = 0
    for letra in texto:
        if letra in "AEIOU":
            count_vogal +=1
    
    return count_vogal

print(contar_vogais("DENIS"))
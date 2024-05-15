import time

meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "CREEPY": "Aterrador, siniestro",
    "RANDOM": "Significa algo aleatorio o al azar.",
    "SHEESH": "Ligera desaprobación"
}

print("Hola")
time.sleep(2)
print("Si estas aqui es porque eres una persona mayor y no entiendes algunas palabras")
time.sleep(2)
print("Pero no te preocupes estoy aqui para ayudarte  ")
time.sleep(2)
for i in  range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("No encontré una definición para ",word)

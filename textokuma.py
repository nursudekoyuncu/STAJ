from collections import Counter

file = open("ödev.txt", "r")
içerik = file.read()
file.close()

kelimeler = içerik.split()
kelime_sayaci = Counter(kelimeler)

for kelime, sayi in kelime_sayaci.items():
    print(f"{kelime}: {sayi}")
 
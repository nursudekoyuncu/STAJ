file = open("odev.txt" , "w", encoding='utf-8')

metinler = [ 
    "nursude koyuncu ostim teknik üniversitesi",
    "nursude yönetim bilişim sistemleri",
    "ostim teknik yönetim bilişim",
    "nursude koyuncu" ]

for metin in metinler:
    file.write(metin + "\n")

file.close()



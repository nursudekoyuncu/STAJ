def kelime_sayisi(dosya_adi, aranan_kelime):

  kelime_sozlugu = {}
  with open(dosya_adi, 'r', encoding='utf-8') as dosya:
    for satir in dosya:
      kelimeler = satir.split()  

      for kelime in kelimeler:
        kelime = kelime.lower() 
        if kelime in kelime_sozlugu:
          kelime_sozlugu[kelime] += 1
        else:
          kelime_sozlugu[kelime] = 1

  if aranan_kelime in kelime_sozlugu:
    return kelime_sozlugu[aranan_kelime]
  else:
    return 0

# Kullanım örneği:
dosya_adi = "odev.txt"
aranan_kelime = "bilişim"
sayi = kelime_sayisi(dosya_adi, aranan_kelime)
print(f"Dosyada '{aranan_kelime}' kelimesi {sayi} kez geçiyor.")
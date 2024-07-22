while True:
    try:
       ilksayi= int(input("ilksayiyi giriniz."))
       ikincisayi= int(input("ikinci sayiyi giriniz."))
       işlem= input("Yapmak İstediğiniz İşlemi Giriniz."
       "toplama: +, çikarma: -, çarpma: *, bölme: /")


       if işlem == "+":
          print("Sonuç: "+ str(ilksayi+ikincisayi))
       elif işlem == "-":
          print("Sonuç: " +str(ilksayi-ikincisayi))
       elif işlem == "*":
          print("Sonuç: " +str(ilksayi*ikincisayi))
       elif işlem == "/":
          if ikincisayi != 0:
             print("Sonuç: " +str(ilksayi/ikincisayi))
          else:
             print("Bir sayiyi sifira bölemezsiniz.")
       else:
          print("geçersiz işlem.")

       cikis = input("Çikmak için q'ya basiniz, devam etmek için başka bir tuşa basiniz: ")
       if cikis == 'q':
            break
    
    except ValueError:
       print("Lütfen geçerli bir sayi giriniz.")
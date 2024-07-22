import random
sayi = random.randint(1,100)
a = 1
ü = 100

while True:
   
   x= int(input("Tahmin et"))
   print(x)
   if x==sayi:
        print("Tebrikler. Doğru tahmin")
        break
   elif x<sayi:
        a=x 
        print(f"{a} ile {ü} arasinda.")
        print("Yukari")
   elif x>sayi:
        ü=x 
        print(f"{a} ile " f"{ü} arasinda")
        print("Aşaği")
  
sayi1 = input("Birinci sayıyı giriniz : ")
islem = input("yapmak istediğiniz işlemi giriniz : ")
sayi2= input("İknici sayıyı giriniz : ")

if islem=="+":
    toplam= int(sayi1) + int(sayi2)
    print(toplam)
elif islem=="-":
    sonuc:int(sayi1)-int(sayi2)
    print(sonuc)
elif islem=="/":
    sonuc=int(sayi1)/int(sayi2)
    print(sonuc)
elif islem=="*":
    sonuc= int(sayi1) * int(sayi2)
else:
    print("yanlış ")
    



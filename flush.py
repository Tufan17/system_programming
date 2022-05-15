#flush() kullanımı

# dosya oluşturma
fileObject = open("text.txt","w+")

# oluşturulan dosyaya yazma
fileObject.write("Merhaba")

# oluşturulan dosyayı kapatma
fileObject.close()



# var olan dosyayı okumak için yolunu giriyoruz
fileObject = open("text.txt", "r")

#yolunu girdiğimiz dosyayı okuyoruz
fileContent = fileObject.read()

# 
print(" flush():\n", fileContent)



# okunan dosyayı kapatma
fileObject.close()


#Sep() Kullanımı 

print("17","11","1999", sep="-")
#17-11-1999 şeklide çıkmasını istiyoruz
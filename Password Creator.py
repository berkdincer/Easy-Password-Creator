#######################################
import random

#######################################

zorluk = 0
passwlist = "abcdefghijklmnopqrstuvwxyz"
passwlist2 = "01234567890"
passwlist3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
passwlist4 = "!@#$%^&*()?"

#######################################

qq = int(input("Şifreniz için bir uzunluk giriniz. "))

qq2 = str(input("Şifrenizde rakam kullanılsın mı ? "))

qq3 = str(input("Şifrenizde büyük harf kullanılsın mı ? "))

qq4 = str(input("Şifrenizde karışık semboller kullanılsın mı ? "))

#######################################   

if qq2 == "Evet":
    passwlist = passwlist+passwlist2
    zorluk +=1
    
if qq3 == "Evet":
    passwlist = passwlist+passwlist3
    zorluk +=1

if qq4 == "Evet":
    passwlist = passwlist+passwlist4
    zorluk +=1

#######################################

if zorluk == 0:
    zorluk = "Basit"
elif zorluk == 1:
    zorluk = "Normal"
elif zorluk == 2:
    zorluk = "Zor"
elif zorluk == 3:
    zorluk = "Çok Zor"

####################################### 

passw =''.join(random.sample(passwlist,qq))
print("Şifre bilgisi\n","------------------")
print("Sifre: %s"%passw)
print("Zorluk: %s"%zorluk)


#######################################




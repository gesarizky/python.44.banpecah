# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# function kpk dan fpb
def fpb(a,b):
    if a<b:
        smaller=a
    else:
        smaller=b
    for i in range (1,smaller+1):
        if a%i==0 and b%i==0:
            fpb=i
        # else:
        #     continue
    return fpb

def kpk(a,b):
    kpk=int(a*b/fpb(a,b))
    return kpk

# Menginput
print('Masukan Nilai dari a/b dengan c/d')
a = int(input("Tuliskan Nilai a : "))
b = int(input("Tuliskan Nilai b: "))
c = int(input("Tuliskan Nilai c: "))
d = int(input("Tuliskan Nilai d: "))

# Mengkonversi
a1 = int(kpk(b,d) / b * a)
c1 = int(kpk(b,d) / d * c)

# Menampilkan Hasil
print('==========================================================')
print('Maka Perbandingan Dari Pecahan ',a,'/',b,' dengan ',c,'/',d)
print('Dengan KPK Pecahan =',kpk(b,d))
print('Setelah disederhanakan menjadi = ',a1,' /',kpk(b,d),' dengan ',c1,'/',kpk(b,d))
if(a1>c1):
   print('maka Kesimpulan ',a1,' /',kpk(b,d),' lebih besar ',c1,'/',kpk(b,d))
elif(a1 < c1):
   print('maka Kesimpulan ',a1,' /',kpk(b,d),' lebih kecil ',c1,'/',kpk(b,d))
else:
   print('maka Kesimpulan ',a1,' /',kpk(b,d),' sama dengan ',c1,'/',kpk(b,d))
print('==========================================================')

print("=========== Prgram Manipulasi String ============")
print("Pilihan Menu :")
print("1. Hitung Kata")
print("2. Ubah Kata")
pilihan=int(input("pilihhan anda :"))


def hitung_kata():
    a = input("masukkan sebuah kalimat/kata : ")
    b = input("masukan kta yang ingin di hitung : ")
    print("terdapat sebanyak",a.count(b),"kata makan di dalam kalimat")

    
def ubah_kata():
    c = input("masukkan sebuah kalimat/kata : ")
    d = input("masukkan kata yang ingin di ubah : ")
    e = input("masukan kata pengganti : ")
    print("string berhasil diubah menjadi : ",c.replace(d,e))


if pilihan==1 :
          hitung_kata()

elif pilihan==2 :
    ubah_kata()
    
else:
    input("masukkan sebuah kalimat/kata : ") 
    print("pilihan yang anda input tidak terdaftar di daftar pilihan")

      
    
            
   
    
            
            

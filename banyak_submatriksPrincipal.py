def faktorial(num) :
    hasil = 1
    for i in range (1, num+1) :
        hasil *= i     
    return hasil

def kombinasi(n,r):
    return int(faktorial(n)/(faktorial(n-r)*faktorial(r)))

def sigmaKombinasi(num):
    sigma = 0
    for i in range (1,num) :
        sigma += kombinasi(num,i)
    return sigma


try:
    ordo = int(input("Masukkan jumlah kolom dan baris matriks : "))    
    print("Jumlah Maksimal submatriks prinsipal yang dapat diperoleh adalah " + str(sigmaKombinasi(ordo)+1))
except Exception as e:
    print(e)
    print("Ada kesalahan!")
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

def jumlahSubmatriks(kolom,baris) :
    kolom = sigmaKombinasi(kolom)
    baris = sigmaKombinasi(baris)
    
    return kolom + baris + (kolom*baris)+1
    
try:
    kolom = int(input("Masukkan jumlah kolom matriks: "))
    baris = int(input("Masukkan jumlah baris matriks: "))
    
    print("Jumlah Maksimal submatriks yang diperoleh adalah " + str(jumlahSubmatriks(kolom, baris)))
except Exception as e:
    print(e)
    print("Ada kesalahan!")
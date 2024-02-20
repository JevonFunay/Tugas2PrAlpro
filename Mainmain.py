# #Latihan Mandiri 1
tinggi = int(input("Berapa Tinggi Anda: "))
BMI = int(input("Berapa BMI anda: "))
x = tinggi/100
berat = BMI*(x**2)
y = round(berat)

print(F"Jadi berat anda sesuai dengan rumus adalah {y}")

#Latihan Mandiri 2
X = int(input("X nya mau berapa? :"))
RUMUS = 2*(X**2) + 2*(X) + 15/X

print(F"Jadi F(X) ={RUMUS}")

# Latihan Mandiri 3
Gaji = int(input("Gaji Perjam:"))
JKerja = int(input("Jam Kerja PerMinggun:"))
TJKerja = JKerja*5
GajiSBP = (Gaji*TJKerja)
Pajak = GajiSBP*(14/100)
GajiSP = GajiSBP-Pajak

Baju = GajiSP*(10/100)
Tulis = GajiSP*(1/100)
TotalBelanja = Baju+Tulis
SisaGaji = GajiSP-TotalBelanja

Sedekah = SisaGaji*(25/100)
Yatim = Sedekah*(30/100)
SisaSedekah = Sedekah - Yatim


print (f"Gaji Sebelum Kena Pajak RP.{GajiSBP}")
print (f"Gaji Setelah Kena Pajak RP.{GajiSP}")
print (f"Total Belanja Pakaiana & Aksesoris RP.{Baju}")
print (f"Total Belanja Alat Tulis RP.{Tulis}")
print (f"Total Sedekah RP.{Sedekah}")
print (f"Total Sedekah untuk Anak Yatim RP.{Yatim}")
print (f"Total Sedekah untuk Dhufa RP.{SisaSedekah}")

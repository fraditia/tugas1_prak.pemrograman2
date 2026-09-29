npm = input ("masukan npm :")
nama = input ("masukan nama :")
umur = input ("masukan umur: ")
tinggi = input ("masukan tinggi :")
prodi = input ("masukan prodi :")

print ("npm : ", npm)
print ("nama : ", nama)
print ("umur : ", umur)
print ("tinggi : ", tinggi)
print ("prodi : ", prodi)

tugas =int(input ("masukan nilai tugas:"))
uts = int(input ("masukan nilai uts:"))
uas = int(input ("masukan nilai uas :"))
nilai_akhir = (tugas + uts + uas) / 3

print("nilai akhir : ", nilai_akhir .__round__(2))
if nilai_akhir >= 75:
    print("selamat anda lulus")

else:
    print("maaf anda tidak lulus")
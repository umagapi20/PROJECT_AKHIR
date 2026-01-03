from pasien import Pasien
from dokter import Dokter
from pendaftaran import Pendaftaran

p1 = Pasien("P01", "Andi", 20)
p2 = Pasien("P02", "Siti", 25)

d1 = Dokter("D01", "Dr. Budi", "Umum")
d2 = Dokter("D02", "Dr. Ani", "Gigi")

pendaftaran = Pendaftaran()

def garis():
    print("=" * 35)

while True:
    garis()
    print("   SISTEM MANAJEMEN KLINIK")
    garis()
    print("1. Lihat Data Pasien")
    print("2. Lihat Data Dokter")
    print("3. Pendaftaran Berobat")
    print("4. Lihat Rekam Medis")
    print("5. Keluar")
    garis()

    pilih = input("Pilih menu: ")

    if pilih == "1":
        print(p1.info())
        print(p2.info())

    elif pilih == "2":
        print(d1.info())
        print(d2.info())

    elif pilih == "3":
        idp = input("Masukkan ID Pasien: ")
        keluhan = input("Masukkan Keluhan: ")
        pasien = p1 if idp == "P01" else p2
        dokter = d1
        pendaftaran.tambah(pasien, dokter, keluhan)
        print("Pendaftaran berhasil!")

    elif pilih == "4":
        pendaftaran.tampilkan()

    elif pilih == "5":
        break
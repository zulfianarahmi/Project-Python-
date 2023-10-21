import random

def permainan_batu_gunting_kertas():
    pilihan = ["Batu", "Gunting", "Kertas"]
    komputer = random.choice(pilihan)
    pemain = input("Mau pilih apa (Batu/Gunting/Kertas): ").capitalize()

    print(f"Komputer pilih: {komputer}")
    print(f"Kamu pilih: {pemain}")

    if pemain in pilihan:
        if pemain == komputer:
            print("Hasil: Seri!")
        elif (pemain == "Batu" and komputer == "Gunting") or \
             (pemain == "Gunting" and komputer == "Kertas") or \
             (pemain == "Kertas" and komputer == "Batu"):
            print("Kamu menang!")
        else:
            print("Komputer menang!")
    else:
        print("Pilihan tidak valid. Silakan pilih Batu, Gunting, atau Kertas.")

permainan_batu_gunting_kertas()

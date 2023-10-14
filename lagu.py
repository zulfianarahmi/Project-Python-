import pygame

# Inisialisasi Pygame
pygame.init()

# Inisialisasi pengaturan pemutar musik
pygame.mixer.init()

# Membuat jendela Pygame kosong (tidak digunakan dalam aplikasi pemutar musik sederhana)
window = pygame.display.set_mode((200, 200))

# Memuat lagu
pygame.mixer.music.load("D:/VIDEO/Belajar/github/python beginner/song/lover.mp3")

# Fungsi untuk memutar musik
def play_music():
    pygame.mixer.music.play()

# Fungsi untuk menghentikan musik
def stop_music():
    pygame.mixer.music.stop()

# Loop utama aplikasi
while True:
    print("Pemutar Musik Sederhana")
    print("1. Putar Musik")
    print("2. Berhenti")
    print("3. Keluar")
    
    # Meminta input dari pengguna
    choice = input("Pilih opsi: ")
    
    # Memproses pilihan pengguna
    if choice == "1":
        play_music()
    elif choice == "2":
        stop_music()
    elif choice == "3":
        stop_music()
        break
    else:
        print("Pilihan tidak valid. Silakan pilih opsi 1, 2, atau 3.")

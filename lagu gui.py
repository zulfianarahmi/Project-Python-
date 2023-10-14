import pygame
import tkinter as tk
from tkinter import filedialog

# Inisialisasi Pygame
pygame.init()
pygame.mixer.init()

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Aplikasi Pemutar Musik")

# Memilih file musik
def choose_music():
    file_path = filedialog.askopenfilename()
    pygame.mixer.music.load(file_path)

# Fungsi untuk memutar musik
def play_music():
    pygame.mixer.music.play()

# Fungsi untuk menghentikan musik
def stop_music():
    pygame.mixer.music.stop()

# Tombol untuk memilih musik
choose_button = tk.Button(root, text="Pilih Musik", command=choose_music)
choose_button.pack(pady=20)

# Tombol untuk memutar musik
play_button = tk.Button(root, text="Putar", command=play_music)
play_button.pack(pady=20)

# Tombol untuk menghentikan musik
stop_button = tk.Button(root, text="Berhenti", command=stop_music)
stop_button.pack(pady=20)

# Fungsi untuk menutup aplikasi
def close_app():
    pygame.mixer.music.stop()
    root.destroy()

# Tombol untuk keluar
exit_button = tk.Button(root, text="Keluar", command=close_app)
exit_button.pack(pady=20)

# Memulai loop Tkinter
root.mainloop()


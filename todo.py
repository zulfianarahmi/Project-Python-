import tkinter as tk
from tkinter import messagebox

# Inisialisasi Tkinter
root = tk.Tk()
root.title("Aplikasi To-Do List")

# Daftar tugas
tasks = []

# Fungsi untuk menambahkan tugas ke daftar
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Peringatan", "Silakan masukkan tugas terlebih dahulu!")

# Fungsi untuk menghapus tugas terpilih dari daftar
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        del tasks[selected_task_index]
        update_listbox()
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih tugas yang ingin dihapus!")

# Fungsi untuk memperbarui daftar tugas di Listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Membuat entry untuk input tugas
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Tombol untuk menambahkan tugas
add_button = tk.Button(root, text="Tambah Tugas", command=add_task)
add_button.pack()

# Listbox untuk menampilkan daftar tugas
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Tombol untuk menghapus tugas terpilih
delete_button = tk.Button(root, text="Hapus Tugas", command=delete_task)
delete_button.pack()

# Memulai loop Tkinter
root.mainloop()


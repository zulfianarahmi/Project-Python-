import tkinter as tk
from tkinter import filedialog, messagebox
import tkinter.ttk as ttk
from ttkthemes import ThemedTk

# Inisialisasi Tkinter dengan tema
root = ThemedTk(theme="plastik")
root.title("Aplikasi To-Do List")

# Daftar tugas
tasks = []

# Fungsi untuk menambahkan tugas beserta berkas
def add_task_with_file():
    task = entry.get()
    if task:
        file_path = filedialog.askopenfilename()
        tasks.append({"task": task, "file": file_path})
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Peringatan", "Silakan masukkan tugas terlebih dahulu!")

# Fungsi untuk menampilkan berkas tugas
def show_task_file():
    try:
        selected_task_index = listbox.curselection()[0]
        selected_task = tasks[selected_task_index]
        file_path = selected_task.get("file")
        if file_path:
            messagebox.showinfo("Berkas Tugas", f"Berkas tugas: {file_path}")
        else:
            messagebox.showinfo("Berkas Tugas", "Tidak ada berkas terkait dengan tugas ini.")
    except IndexError:
        messagebox.showwarning("Peringatan", "Pilih tugas untuk melihat berkas terkait!")

# Fungsi untuk mengubah tema aplikasi
def change_theme():
    selected_theme = theme_combobox.get()
    root.set_theme(selected_theme)

# Membuat entry untuk input tugas
entry_label = tk.Label(root, text="Masukkan Tugas:")
entry_label.pack()
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Tombol untuk menambahkan tugas beserta berkas
add_with_file_button = tk.Button(root, text="Tambah Tugas dengan Berkas", command=add_task_with_file)
add_with_file_button.pack()

# Listbox untuk menampilkan daftar tugas
listbox_label = tk.Label(root, text="Daftar Tugas:")
listbox_label.pack()
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Tombol untuk melihat berkas tugas terpilih
show_file_button = tk.Button(root, text="Lihat Berkas Tugas", command=show_task_file)
show_file_button.pack()

# Pilihan tema
theme_label = tk.Label(root, text="Pilih Tema:")
theme_label.pack()
themes = ["aqua", "clam", "vista", "radiance", "scid themes", "smog", "winxpblue"]
theme_combobox = ttk.Combobox(root, values=themes, state="readonly")
theme_combobox.pack()
theme_combobox.set("radiance")  # Tema awal
theme_button = tk.Button(root, text="Ubah Tema", command=change_theme)
theme_button.pack()

# Fungsi untuk memperbarui daftar tugas di Listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task.get("task"))

# Memulai loop Tkinter
root.mainloop()

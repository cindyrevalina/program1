# OOP-PYTHON

# Data Diri

Nama: cindy revalina simanullang

NIM: 312410417

Kelas: TI.24.A3

# Manajemen Data Mahasiswa

Sebuah aplikasi sederhana berbasis Python untuk mengelola data mahasiswa. Aplikasi ini mendukung operasi CRUD (Create, Read, Update, Delete) yang diimplementasikan dalam antarmuka berbasis teks.

## Struktur Proyek
 <img src="strukturproyek.png">


### Penjelasan File

- **`data/mahasiswa.py`**  
  Berisi class `Mahasiswa` untuk model data mahasiswa dan class `DataMahasiswa` untuk operasi seperti:
  - Menambah data
  - Menghapus data
  - Mengubah data
  - Mencari data
  - Menampilkan data

- **`view/input_form.py`**  
  Berisi class `InputForm` untuk menangani input data dari pengguna.

- **`view/mahasiswa.py`**  
  Berisi class `MahasiswaView` untuk menampilkan daftar dan detail data mahasiswa.

- **`Main.py`**  
  Program utama yang menyatukan semua komponen dan memberikan menu interaktif untuk pengguna.

---

## Fitur Utama

1. **Tambah Data Mahasiswa**  
   Menambahkan data mahasiswa baru dengan atribut NIM, nama, dan jurusan.
   <img src="tambah data.png">

2. **Tampilkan Semua Data Mahasiswa**  
   Menampilkan daftar semua data mahasiswa yang telah disimpan.
   <img src="tampilkan data.png">

3. **Cari Mahasiswa**  
   Mencari mahasiswa berdasarkan NIM dan menampilkan detailnya.
    <img src="cari data.png">

4. **Ubah Data Mahasiswa**  
   Mengubah nama dan jurusan mahasiswa berdasarkan NIM.
    <img src="ubah data.png">

5. **Hapus Data Mahasiswa**  
   Menghapus data mahasiswa berdasarkan NIM.
    

6. **Keluar**  
   Mengakhiri program.

---
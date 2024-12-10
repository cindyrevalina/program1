
from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import TampilkanMahasiswa

def main():
    data_mahasiswa = DataMahasiswa()

    while True:
        print("\nMenu Utama")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Hapus Mahasiswa")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_mahasiswa()
            mahasiswa = Mahasiswa(nim, nama, jurusan)
            data_mahasiswa.tambah_mahasiswa(mahasiswa)
            print("Mahasiswa berhasil ditambahkan!")

        elif pilihan == "2":
            TampilkanMahasiswa.tampilkan_list(data_mahasiswa.semua_mahasiswa())

        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang dicari: ")
            mahasiswa = data_mahasiswa.cari_mahasiswa(nim)
            TampilkanMahasiswa.tampilkan_detail(mahasiswa)

        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
            nama = input("Masukkan nama baru (kosongkan jika tidak diubah): ")
            jurusan = input("Masukkan jurusan baru (kosongkan jika tidak diubah): ")
            if data_mahasiswa.ubah_mahasiswa(nim, nama, jurusan):
                print("Data mahasiswa berhasil diubah!")
            else:
                print("Mahasiswa tidak ditemukan.")

        elif pilihan == "5":
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            data_mahasiswa.hapus_mahasiswa(nim)
            print("Mahasiswa berhasil dihapus.")

        elif pilihan == "6":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()

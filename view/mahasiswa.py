# view/mahasiswa.py

class TampilkanMahasiswa:
    @staticmethod
    def tampilkan_list(data):
        if not data:
            print("Tidak ada data mahasiswa.")
        else:
            print("\nDaftar Mahasiswa:")
            for m in data:
                print(m)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print("\nDetail Mahasiswa:")
            print(f"NIM: {mahasiswa.nim}")
            print(f"Nama: {mahasiswa.nama}")
            print(f"Jurusan: {mahasiswa.jurusan}")
        else:
            print("Mahasiswa tidak ditemukan.")

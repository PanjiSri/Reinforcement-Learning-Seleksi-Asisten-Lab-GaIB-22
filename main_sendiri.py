from game import PermainanSederhana

permainan = PermainanSederhana()
permainan.tampilkan()

while not permainan.permainan_selesai:
    aksi = input("Masukkan aksi ('kiri' atau 'kanan'): ").strip().lower()
    _, _, permainan_selesai = permainan.langkah(aksi)
    permainan.tampilkan()
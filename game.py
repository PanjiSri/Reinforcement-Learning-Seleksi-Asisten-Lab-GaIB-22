import numpy as np

class PermainanSederhana:
    def __init__(self):
        self.panjang_papan = 10
        self.posisi_lubang = 0
        self.posisi_apel = 9
        self.posisi_awal = 2
        self.posisi_pemain = self.posisi_awal
        self.poin = 0
        self.poin_menang = 500
        self.poin_kalah = -200
        self.hadiah = {'lubang': -100, 'apel': 100, 'langkah': -1}
        self.permainan_selesai = False

    def reset(self):
        self.posisi_pemain = self.posisi_awal
        self.poin = 0
        self.permainan_selesai = False
        return self.posisi_pemain
    
    def langkah(self, aksi):
        if aksi == 'kiri':
            self.posisi_pemain -= 1
        elif aksi == 'kanan':
            self.posisi_pemain += 1
        
        self.posisi_pemain = max(0, min(self.posisi_pemain, self.panjang_papan - 1))
        
        if self.posisi_pemain == self.posisi_lubang:
            reward = self.hadiah['lubang']
            self.posisi_pemain = self.posisi_awal
        elif self.posisi_pemain == self.posisi_apel:
            reward = self.hadiah['apel']
            self.posisi_pemain = self.posisi_awal
        else:
            reward = self.hadiah['langkah']
        
        self.poin += reward
        
        if self.poin >= self.poin_menang or self.poin <= self.poin_kalah:
            self.permainan_selesai = True
            reward = self.poin
        
        return self.posisi_pemain, reward, self.permainan_selesai
    
    def tampilkan(self):
        papan = [' '] * self.panjang_papan
        papan[self.posisi_lubang] = 'L'
        papan[self.posisi_apel] = 'A'
        papan[self.posisi_pemain] = 'P'
        
        print("_" * 41)
        print("|", end="")
        for i in papan:
            print(f" {i} |", end="")
        print("\n" + "_" * 41)
        print(f"Poin: {self.poin}\n")

# permainan = PermainanSederhana()
# permainan.tampilkan()

# while not permainan.permainan_selesai:
#     aksi = input("Masukkan aksi ('kiri' atau 'kanan'): ").strip().lower()
#     _, _, permainan_selesai = permainan.langkah(aksi)
#     permainan.tampilkan()

import numpy as np
from game import PermainanSederhana
from q_learning import q_learning, evaluasi_agen
from sarsa import sarsa, evaluasi_agen as evaluasi_agen_sarsa

def algoritma(permainan, fungsi_algoritma, nama_algoritma, random_state=42):
    print(f"Menjalankan {nama_algoritma}...")
    q_table, rewards = fungsi_algoritma(permainan, random_state=random_state)
    
    print(f"\nQ-Table dari {nama_algoritma}:")
    print(q_table)
    
    print(f"\nRata-rata reward selama pelatihan ({nama_algoritma}): {np.mean(rewards):.2f}")
    print(f"Reward tertinggi selama pelatihan ({nama_algoritma}): {np.max(rewards):.2f}")
    print(f"Reward terendah selama pelatihan ({nama_algoritma}): {np.min(rewards):.2f}")
    
    rata_rata_reward = evaluasi_agen(permainan, q_table)
    print(f"\nRata-rata reward setelah evaluasi ({nama_algoritma}): {rata_rata_reward:.2f}\n")
    
    return q_table

if __name__ == "__main__":
    permainan = PermainanSederhana()

    # Jalankan Q-Learning
    q_table_q_learning = algoritma(permainan, q_learning, "Q-Learning")

    # Jalankan SARSA
    q_table_sarsa = algoritma(permainan, sarsa, "SARSA")
    
    # Contoh jalur optimal dari Q-Learning
    # print("\nContoh jalur optimal dari Q-Learning:")
    state = permainan.reset()
    path = [state]
    total_reward = 0
    
    while not permainan.permainan_selesai:
        action = np.argmax(q_table_q_learning[state])
        state, reward, _ = permainan.langkah('kiri' if action == 0 else 'kanan')
        path.append(state)
        total_reward += reward
        # permainan.tampilkan()
    
    print("\nJalur yang diambil oleh pemain (Q-Learning):")
    print(path)
    print(f"Total reward (Q-Learning): {total_reward}")

    if permainan.poin >= permainan.poin_menang:
        print("Pemain menang dengan Q-Learning!")
    elif permainan.poin <= permainan.poin_kalah:
        print("Pemain kalah dengan Q-Learning!")
    else:
        print("Permainan berakhir, pemain tidak menang atau kalah dengan Q-Learning.")

    # Contoh jalur optimal dari SARSA
    # print("\nContoh jalur optimal dari SARSA:")
    state = permainan.reset()
    path = [state]
    total_reward = 0
    
    while not permainan.permainan_selesai:
        action = np.argmax(q_table_sarsa[state])
        state, reward, _ = permainan.langkah('kiri' if action == 0 else 'kanan')
        path.append(state)
        total_reward += reward
        # permainan.tampilkan()
    
    print("\nJalur yang diambil oleh pemain (SARSA):")
    print(path)
    print(f"Total reward (SARSA): {total_reward}")

    if permainan.poin >= permainan.poin_menang:
        print("Pemain menang dengan SARSA!")
    elif permainan.poin <= permainan.poin_kalah:
        print("Pemain kalah dengan SARSA!")
    else:
        print("Permainan berakhir, pemain tidak menang atau kalah dengan SARSA.")

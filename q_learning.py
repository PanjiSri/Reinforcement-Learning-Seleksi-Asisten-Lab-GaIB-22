import numpy as np
from game import PermainanSederhana

def q_learning(permainan, alpha=0.1, gamma=0.9, epsilon_awal=1.0, epsilon_akhir=0.01, epsilon_decay=0.995, jumlah_episodes=10000, random_state=None):
    if random_state is not None:
        np.random.seed(random_state)
    
    q_table = np.zeros((permainan.panjang_papan, 2))
    epsilon = epsilon_awal
    rewards_per_episode = []
    
    for episode in range(jumlah_episodes):
        state = permainan.reset()
        total_reward = 0
        selesai = False
        
        while not selesai:
            if np.random.uniform(0, 1) < epsilon:
                action = np.random.choice([0, 1])
            else:
                action = np.argmax(q_table[state])
            
            next_state, reward, selesai = permainan.langkah('kiri' if action == 0 else 'kanan')
            
            q_value = q_table[state, action]
            max_next_q = np.max(q_table[next_state])
            
            updated_q_value = (1 - alpha) * q_value + alpha * (reward + gamma * max_next_q)
            q_table[state, action] = updated_q_value
            
            state = next_state
            total_reward += reward
        
        rewards_per_episode.append(total_reward)
        
        # Penurunan Epsilon
        epsilon = max(epsilon_akhir, epsilon * epsilon_decay)
        
        if (episode + 1) % 1000 == 0:
            print(f"Episode {episode + 1}/{jumlah_episodes}, Rata-rata Reward: {np.mean(rewards_per_episode[-1000:]):.2f}, Epsilon: {epsilon:.4f}")
    
    return q_table, rewards_per_episode

def evaluasi_agen(permainan, q_table, jumlah_episodes=100):
    total_rewards = []
    for _ in range(jumlah_episodes):
        state = permainan.reset()
        selesai = False
        episode_reward = 0
        while not selesai:
            action = np.argmax(q_table[state])
            state, reward, selesai = permainan.langkah('kiri' if action == 0 else 'kanan')
            episode_reward += reward
        total_rewards.append(episode_reward)
    return np.mean(total_rewards)

# if __name__ == "__main__":
#     permainan = PermainanSederhana()
#     q_table, rewards = q_learning(permainan, random_state=42)
    
#     print("\nQ-Table dari Q-Learning:")
#     print(q_table)
    
#     print(f"\nRata-rata reward selama pelatihan: {np.mean(rewards):.2f}")
#     print(f"Reward tertinggi selama pelatihan: {np.max(rewards):.2f}")
#     print(f"Reward terendah selama pelatihan: {np.min(rewards):.2f}")
    
#     rata_rata_reward = evaluasi_agen(permainan, q_table)
#     print(f"\nRata-rata reward setelah evaluasi: {rata_rata_reward:.2f}")
    
#     print("\nContoh jalur optimal:")
#     state = permainan.reset()
#     path = [state]
#     total_reward = 0
    
#     while not permainan.permainan_selesai:
#         action = np.argmax(q_table[state])
#         state, reward, _ = permainan.langkah('kiri' if action == 0 else 'kanan')
#         path.append(state)
#         total_reward += reward
#         permainan.tampilkan()
    
#     print("\nJalur yang diambil oleh pemain:")
#     print(path)
#     print(f"Total reward: {total_reward}")
    
#     if permainan.poin >= permainan.poin_menang:
#         print("Pemain menang!")
#     elif permainan.poin <= permainan.poin_kalah:
#         print("Pemain kalah!")
#     else:
#         print("Permainan berakhir, pemain tidak menang atau kalah.")

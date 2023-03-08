# Nama : Muhammad Asyrof
# Nim : 21343056
# Prodi : Informatika

import heapq

def dijkstra(graf, titik_mulai, titik_akhir):
    # Inisialisasi jarak ke semua titik sebagai tak terhingga
    jarak = {titik: float('inf') for titik in graf}
    # Jarak ke titik awal diatur sebagai 0
    jarak[titik_mulai] = 0
    # Antrian prioritas yang berisi semua titik dengan jarak terdekat yang diketahui
    antrian = [(0, titik_mulai)]
    while antrian:
        # Ambil titik dengan jarak terdekat dari antrian prioritas
        (jarak_terdekat, titik_saat_ini) = heapq.heappop(antrian)
        # Jika jarak terdekat ke titik saat ini lebih besar dari jarak yang diketahui, lewati titik ini
        if jarak_terdekat > jarak[titik_saat_ini]:
            continue
        # Periksa tetangga dari titik saat ini dan update jarak ke mereka jika lebih pendek
        for tetangga, bobot in graf[titik_saat_ini].items():
            jarak_tetangga = jarak_terdekat + bobot
            if jarak_tetangga < jarak[tetangga]:
                jarak[tetangga] = jarak_tetangga
                heapq.heappush(antrian, (jarak_tetangga, tetangga))
    # Kembalikan jarak terpendek ke titik akhir
    return jarak[titik_akhir]

# Contoh penggunaan
graf = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 3, 'D': 2, 'E': 3},
    'C': {'B': 1, 'D': 4, 'E': 5},
    'D': {'E': 1},
    'E': {}
}
titik_mulai = 'A'
titik_akhir = 'E'
print("Jarak terpendek dari", titik_mulai, "ke", titik_akhir, "adalah", dijkstra(graf, titik_mulai, titik_akhir))

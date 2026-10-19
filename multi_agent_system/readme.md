# Multi-Agent System Sederhana dengan Python

## 1. Deskripsi

Proyek ini merupakan implementasi sederhana **Multi-Agent System (MAS)** menggunakan Python untuk menyelesaikan masalah pencarian jalur pada graf.

Sistem terdiri dari tiga komponen utama, yaitu agen BFS, agen DFS, dan agen koordinator. Kedua agen pencari jalur menggunakan algoritma yang berbeda, kemudian koordinator membandingkan hasil pencarian tersebut.

## 2. Tujuan

- Memahami konsep dasar Multi-Agent System.
- Mengimplementasikan agen dengan strategi pencarian yang berbeda.
- Menggunakan BFS dan DFS untuk mencari jalur pada graf.
- Membandingkan hasil pencarian melalui agen koordinator.

## 3. Struktur Proyek

```text
multi_agent_system/
├── main.py
├── bfs_agent.py
├── dfs_agent.py
├── coordinator.py
└── README.md
```

| File | Fungsi |
|---|---|
| `main.py` | Menentukan graf, titik awal, dan tujuan. |
| `bfs_agent.py` | Menjalankan pencarian menggunakan BFS. |
| `dfs_agent.py` | Menjalankan pencarian menggunakan DFS. |
| `coordinator.py` | Mengatur pencarian dan membandingkan hasil agen. |

## 4. Arsitektur Sistem

```text
             Main Program
                  |
                  v
            Coordinator
             /       \
            v         v
        BFS Agent  DFS Agent
            \         /
             v       v
          Hasil Pencarian
                  |
                  v
       Perbandingan Hasil
```

### Peran setiap agen

**BFS Agent (Breadth-First Search)**

Melakukan pencarian secara melebar, yaitu memeriksa simpul berdasarkan tingkat kedekatannya dari titik awal. Pada graf tak berbobot, BFS dapat menemukan jalur dengan jumlah sisi minimum.

**DFS Agent (Depth-First Search)**

Melakukan pencarian secara mendalam pada satu cabang sebelum mencoba cabang lainnya. DFS dapat menemukan jalur, tetapi tidak menjamin jalur terpendek.

**Coordinator Agent**

Mengatur proses pencarian oleh kedua agen, menerima hasil pencarian, membandingkan panjang jalur, dan menampilkan kesimpulan.

## 5. Cara Kerja

1. Program menentukan graf, titik awal, dan titik tujuan.
2. Koordinator memanggil agen BFS dan DFS.
3. Masing-masing agen mencari jalur dari titik awal ke tujuan.
4. Kedua agen mengembalikan jalur yang ditemukan.
5. Koordinator membandingkan panjang jalur dan menampilkan hasilnya.

Panjang jalur dihitung berdasarkan jumlah sisi yang dilewati, bukan jumlah simpul.

## 6. Cara Menjalankan Program

Pastikan Python telah terpasang di komputer.

Buka terminal pada direktori proyek, lalu jalankan:

```bash
python main.py
```

## 7. Contoh Graf

Graf yang digunakan dalam demonstrasi:

```text
        A
       / \
      B   C
     / \   \
    D   E   F
     \  |  /
        G
```

Titik awal: `A`

Titik tujuan: `G`

Hasil jalur bergantung pada urutan tetangga dalam representasi graf dan strategi pencarian masing-masing agen.

## 8. Contoh Keluaran

```text
Koordinator: memulai pencarian jalur

Hasil Agen BFS: ['A', 'B', 'D', 'G']
Hasil Agen DFS: ['A', 'B', 'D', 'G']

Panjang jalur BFS: 3
Panjang jalur DFS: 3
Koordinator: panjang jalur sama
```

Keluaran tersebut merupakan contoh. Hasil aktual dapat berbeda apabila urutan simpul atau struktur graf diubah.

## 9. Konsep Multi-Agent System

Proyek ini memperagakan pembagian tugas berdasarkan peran:

- Setiap agen menggunakan strategi pencarian yang berbeda.
- Koordinator mengelola pemanggilan agen.
- Hasil dari beberapa agen dibandingkan untuk mendukung pengambilan keputusan.

**Catatan:** Implementasi ini merupakan prototipe awal. Agen BFS dan DFS masih berupa fungsi Python yang dipanggil oleh koordinator, sehingga belum menerapkan komunikasi pesan atau otonomi penuh seperti pada Multi-Agent System yang lebih kompleks.

## 10. Pengembangan Selanjutnya

Beberapa pengembangan yang dapat dilakukan:

- Menambahkan agen pencarian lain, seperti Dijkstra atau A*.
- Menghitung jumlah simpul yang dikunjungi oleh setiap agen.
- Mengukur waktu eksekusi setiap algoritma.
- Membuat koordinator memilih algoritma berdasarkan karakteristik graf.
- Menambahkan mekanisme komunikasi pesan ant aragen.
- Membandingkan performa agen pada beberapa graf yang berbeda.

## 11. Kesimpulan

Proyek ini menunjukkan bagaimana beberapa agen dengan strategi berbeda dapat digunakan untuk menyelesaikan masalah pencarian jalur. Agen BFS dan DFS bertugas mencari jalur, sedangkan agen koordinator membandingkan hasilnya.

Implementasi ini menjadi dasar untuk mempelajari koordinasi agen dan pengembangan Multi-Agent System yang lebih kompleks.

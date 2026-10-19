# Maze Search: BFS and DFS

## Deskripsi

Proyek ini merupakan implementasi algoritma pencarian (search algorithm) menggunakan **Breadth-First Search (BFS)** dan **Depth-First Search (DFS)** untuk menemukan jalur dari titik awal (*Start*) menuju titik tujuan (*End*) pada sebuah maze.

Program menampilkan jalur yang ditemukan menggunakan simbol `*` dan menghitung jumlah langkah dari titik awal ke titik tujuan.

## Tujuan

- Memahami cara kerja algoritma BFS dan DFS.
- Mengimplementasikan algoritma pencarian jalur pada maze.
- Membandingkan hasil pencarian BFS dan DFS.
- Memvisualisasikan jalur yang ditemukan oleh setiap algoritma.

## Struktur Proyek

```text
maze-search/
├── main.py
├── bfs.py
├── dfs.py
└── README.md
```

Keterangan:

- `main.py`: Program utama untuk menjalankan BFS dan DFS.
- `bfs.py`: Implementasi algoritma Breadth-First Search.
- `dfs.py`: Implementasi algoritma Depth-First Search.
- `README.md`: Dokumentasi proyek.

## Simbol Maze

| Simbol | Keterangan |
|---|---|
| `S` | Titik awal (Start) |
| `E` | Titik tujuan (End) |
| `.` | Jalur yang dapat dilewati |
| `#` | Dinding atau penghalang |
| `*` | Jalur hasil pencarian |

## Algoritma yang Digunakan

### 1. Breadth-First Search (BFS)

BFS menelusuri simpul berdasarkan tingkat kedekatan dari titik awal. Algoritma ini menggunakan struktur data **queue (FIFO)**.

Karakteristik:
- Menelusuri simpul berdasarkan tingkat kedalaman.
- Menemukan jalur terpendek jika semua gerakan memiliki biaya yang sama.
- Dapat menggunakan memori lebih besar karena menyimpan banyak simpul yang menunggu diproses.

### 2. Depth-First Search (DFS)

DFS menelusuri satu cabang sedalam mungkin sebelum kembali untuk mencoba cabang lainnya. Implementasinya dapat menggunakan **stack (LIFO)** atau rekursi.

Karakteristik:
- Menelusuri cabang secara mendalam.
- Tidak menjamin jalur terpendek.
- Penggunaan memori dapat lebih kecil, bergantung pada struktur maze dan implementasi.

## Cara Kerja Program

1. Program mendefinisikan maze.
2. Fungsi `find_point()` mencari koordinat `S` dan `E`.
3. Algoritma BFS mencari jalur dari titik awal ke tujuan.
4. Fungsi `show_maze()` menampilkan jalur BFS.
5. Algoritma DFS melakukan pencarian pada maze yang sama.
6. Program menampilkan jalur DFS dan menghitung jumlah langkahnya.

Jumlah langkah dihitung menggunakan:

```python
len(path) - 1
```

Pengurangan satu diperlukan karena jumlah elemen jalur mencakup titik awal, sedangkan titik awal bukan langkah perpindahan.

## Persyaratan

- Python 3
- File `main.py`, `bfs.py`, dan `dfs.py` berada dalam folder yang sama.

## Cara Menjalankan

Buka terminal di folder proyek, kemudian jalankan:

```bash
python main.py
```

Jika sistem menggunakan perintah `python3`, jalankan:

```bash
python3 main.py
```

## Contoh Maze

```text
S...#
.#..#
.#...
...#.
##..E
```

Program akan menampilkan hasil pencarian BFS dan DFS secara terpisah, termasuk visualisasi jalur serta jumlah langkah yang ditemukan.

## Perbandingan BFS dan DFS

| Aspek | BFS | DFS |
|---|---|---|
| Strategi | Melebar per tingkat | Mendalam per cabang |
| Struktur data umum | Queue | Stack atau rekursi |
| Menjamin jalur terpendek | Ya, jika biaya setiap gerakan sama | Tidak |
| Kelengkapan pencarian | Ya, pada maze hingga dengan implementasi yang benar | Bergantung pada implementasi; ya jika ruang pencarian hingga dan simpul ditangani dengan benar |
| Hasil jalur | Jalur terpendek | Jalur pertama yang ditemukan sesuai urutan penelusuran |

## Kesimpulan

Proyek ini menunjukkan penerapan BFS dan DFS dalam menyelesaikan masalah pencarian jalur pada maze. BFS cocok ketika jalur dengan jumlah langkah minimum diperlukan, sedangkan DFS dapat digunakan untuk menjelajahi jalur berdasarkan kedalaman penelusuran.

Hasil kedua algoritma dapat berbeda karena strategi dan urutan penelusurannya berbeda.

---

**Teknologi:** Python 3  
**Kategori:** Artificial Intelligence — Search Algorithms

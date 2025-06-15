# **Laporan Proyek: Implementasi Operasi Dasar Pengolahan Sinyal Digital**

**Kelompok**: 1

**Anggota**:
* Rizky Cahyono Putra       - 442023611012
* Syaifan Noer Iwawan       - 442023611008
* M. Irfansyah              - 442023611004
* Muhammad Galang Fachrezy  - 442023611011
* Achmad Fatich Al-fahmi    - 422021611002

## **Deskripsi Proyek** 📝
Proyek ini merupakan implementasi dari operasi-operasi fundamental dalam Pengolahan Sinyal Digital (PSD) menggunakan Python. Tujuan utama dari proyek ini adalah untuk memahami konsep dasar sinyal dan mempraktikkan manipulasinya secara terprogram, bukan hanya sekadar menggunakan fungsi jadi.

Notebook yang kami sediakan mendemonstrasikan proses dari awal hingga akhir, mulai dari cara merepresentasikan sinyal 1D dan 2D, melakukan operasi dasar, hingga melakukan eksperimen dengan menggabungkan beberapa operasi tersebut. Setiap langkah di dalam notebook disertai dengan penjelasan konseptual, implementasi kode, visualisasi hasil, serta analisis singkat untuk memperkuat pemahaman.

### **Konsep Utama yang Dicakup**
* **Representasi Sinyal 1D**: Pembuatan sinyal sinus dan kosinus menggunakan NumPy.
* **Representasi Sinyal 2D**: Pembuatan gambar/matriks sederhana secara programatik.
* **Operasi Dasar**: Implementasi fungsi untuk Penskalaan (*Scaling*), Penjumlahan (*Addition*), dan Penggeseran Waktu (*Time Shifting*).
* **Visualisasi**: Penggunaan Matplotlib untuk membuat plot sinyal 1D dan menampilkan sinyal 2D (gambar) dengan jelas.
* **Eksperimen**: Menggabungkan beberapa operasi dasar untuk menciptakan sinyal baru yang lebih kompleks dan menganalisis hasilnya.

---

## **⚙️ Panduan Instalasi**

Untuk menjalankan proyek ini di lingkungan lokal Anda, ikuti langkah-langkah persiapan di bawah ini.

### **Prasyarat**
* **Git**: Pastikan Git sudah terinstal di sistem Anda.
* **Python**: Versi Python 3.8 atau yang lebih baru.
* **pip**: Package installer untuk Python (biasanya sudah terinstal bersama Python).

### **Langkah-langkah Instalasi**

**1. Clone Repositori Ini**
Buka terminal atau command prompt, lalu jalankan perintah berikut untuk mengunduh proyek ke komputer Anda:
```bash
git clone https://github.com/rizkycahyono97/pengolahan-sinyal-digital
cd assessment/assesment-week-03
```

**2. (Sangat Direkomendasikan) Buat dan Aktifkan Virtual Environment**
Membuat lingkungan virtual adalah praktik terbaik untuk mengisolasi dependensi proyek dan menghindari konflik dengan library Python lain di sistem Anda.

* **Untuk macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
* **Untuk Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

**3. Instal Semua Library yang Dibutuhkan**
Kami telah menyediakan file `requirements.txt` yang berisi semua library Python yang diperlukan. Jalankan satu perintah berikut untuk menginstal semuanya:
```bash
pip install -r requirements.txt
```
File `requirements.txt` berisi:
* `numpy`: Untuk komputasi numerik dan manipulasi array.
* `matplotlib`: Untuk visualisasi dan plotting sinyal.
* `jupyterlab`: Untuk menjalankan file notebook `.ipynb`.

Setelah langkah ini selesai, lingkungan Anda siap untuk menjalankan proyek.

---

## **▶️ Cara Menjalankan Proyek**

Proyek ini disajikan dalam format Jupyter Notebook (`.ipynb`) yang interaktif.

**1. Aktifkan Virtual Environment**
Pastikan Anda sudah mengaktifkan *virtual environment* yang dibuat pada tahap instalasi (jika Anda membuatnya).

**2. Buka Jupyter Lab atau Jupyter Notebook**
Di terminal yang sama, jalankan salah satu perintah berikut:
```bash
jupyter lab
```
atau
```bash
jupyter notebook
```
Perintah ini akan membuka antarmuka Jupyter di browser web Anda secara otomatis.

**3. Buka dan Jalankan Notebook**
* Dari antarmuka Jupyter, navigasi dan buka file `[Nama_Notebook_Anda].ipynb`.
* Jalankan setiap sel kode secara berurutan dari atas ke bawah dengan menekan `Shift + Enter`.
* Notebook ini dirancang untuk dijalankan secara keseluruhan, di mana setiap sel bergantung pada hasil dari sel sebelumnya. Anda akan melihat penjelasan, kode, dan output visualisasi secara langsung di dalam notebook.

---

## **🤝 Kontribusi dan Kolaborasi Tim**

Proyek ini dikerjakan secara kolaboratif oleh seluruh anggota kelompok. Distribusi tugas dan kontribusi setiap anggota dapat diverifikasi secara transparan melalui **riwayat commit** di repositori GitHub ini.

Untuk memeriksa kontribusi, Anda dapat menggunakan beberapa cara:
1.  **Tab "Insights" di GitHub**: Buka halaman repositori di GitHub, lalu klik tab `Insights > Contributors` untuk melihat grafik kontribusi.
2.  **Perintah `git log`**: Jalankan perintah `git log` di terminal untuk melihat riwayat commit secara detail.
3.  **Perintah `git shortlog`**: Jalankan `git shortlog -sn` untuk mendapatkan ringkasan jumlah commit per anggota.

| Nama Anggota | Tanggung Jawab Utama |
| :--- | :--- |
| Rizky Cahyono Putra | Representasi Sinyal 1D dan Operasi Penjumlahan. |
| Syaifan Noer Iwawan | Operasi Penskalaan dan Penggeseran Sinyal 1D. |
| M. Irfansyah        | Representasi Sinyal 2D, Eksperimen Kombinasi, dan Finalisasi Laporan. |

Untuk melihat riwayat kontribusi, dapat digunakan perintah `git` berikut di terminal:
```bash
git shortlog -sn --all
```

---

## **🛠️ Teknologi yang Digunakan**
* **Python**
* **NumPy**
* **Matplotlib**
* **Jupyter Notebook**
* **Git & GitHub**

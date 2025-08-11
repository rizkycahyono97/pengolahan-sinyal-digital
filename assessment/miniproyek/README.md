# Mini Proyek: Analisis Sinyal Digital Sederhana

Aplikasi ini adalah implementasi dari mini proyek mata kuliah Pengolahan Sinyal Digital. Program ini dibuat menggunakan Python dengan GUI (Graphical User Interface) dari **Tkinter** untuk memvisualisasikan beberapa konsep dasar pengolahan sinyal digital pada citra (gambar) dan audio.

## Fitur Utama

  * **Analisis Frekuensi Suara:** Memvisualisasikan sinyal audio dalam domain waktu (waveform) dan domain frekuensi (spektrogram) menggunakan FFT.
  * **Penjumlahan Citra:** Menggabungkan dua gambar menjadi satu dengan teknik *blending*.
  * **Perbesaran Citra:** Memperbesar ukuran gambar dan menganalisis efek dari proses *scaling*.
  * **Filtering Citra:** Menerapkan filter *high-pass* untuk menonjolkan tepi pada gambar.
  * **Reduksi Noise Audio:** Menambahkan noise buatan pada sinyal audio dan mencoba menguranginya dengan filter sederhana.

## Link Video Youtube
```bash
https://youtu.be/zIUIk0F_ieI
```

## Kebutuhan Sistem (Prerequisites)

Pastikan Anda memiliki Python 3.x terinstal. Untuk menjalankan aplikasi ini, Anda perlu menginstal beberapa pustaka Python. Buka terminal atau command prompt Anda dan jalankan perintah berikut:

```bash
pip install numpy matplotlib pillow scipy opencv-python librosa
```

Tkinter biasanya sudah termasuk dalam instalasi standar Python.

-----

## Cara Menjalankan

1.  **Clone Repositori:**

    ```bash
    git clone https://github.com/rizkycahyono97/pengolahan-sinyal-digital
    cd pengolahan-sinyal-digital
    ```

2.  **Siapkan Data:** Pastikan Anda memiliki beberapa file gambar (`.jpg`, `.png`, `.jpeg`) di dalam direktori proyek atau di folder lain yang mudah diakses.

3.  **Jalankan Aplikasi:** Buka terminal di dalam direktori proyek dan jalankan skrip `main.py`:

    ```bash
    python main.py
    ```

4.  **Gunakan Aplikasi:**

      * Jendela utama akan muncul dengan beberapa pilihan tema.
      * Klik pada salah satu tema untuk membuka jendela baru yang didedikasikan untuk analisis tersebut.
      * Ikuti instruksi di setiap jendela (misalnya, "Pilih Gambar 1 dan 2") untuk memuat data dan melihat hasilnya.
      * Kemudian Pilih `Proses Image`

-----

## Penjelasan Konsep Singkat

### Penjumlahan Citra (Image Addition)

Operasi ini bukan sekadar menumpuk dua gambar. Secara konseptual, setiap gambar digital adalah sebuah matriks di mana tiap selnya (piksel) memiliki nilai warna.

  * **Proses:** Ketika kita menjumlahkan dua gambar, kita sebenarnya menjumlahkan nilai numerik dari setiap piksel yang bersesuaian.
  * **Blending:** Dalam aplikasi ini, kita menggunakan *weighted addition* (`cv2.addWeighted`). Ini seperti mencampur dua "cat" dengan perbandingan tertentu. Misalnya, 50% dari gambar A dicampur dengan 50% dari gambar B. Hasilnya adalah efek gabungan (transparan) yang halus, bukan sekadar penimpaan yang kasar.

### Perbesaran Citra (Image Scaling)

Memperbesar gambar bukan hanya "meregangkan" piksel yang ada. Jika itu dilakukan, hasilnya akan terlihat sangat kotak-kotak (*pixelated*).

  * **Proses:** Untuk menghindari hal tersebut, komputer perlu menciptakan piksel-piksel baru yang sebelumnya tidak ada. Proses "menebak" nilai warna dari piksel-piksel baru ini berdasarkan piksel tetangganya disebut **interpolasi**.
  * **Metode:** Ada banyak metode interpolasi. Dalam proyek ini kita menggunakan `BICUBIC`, sebuah metode canggih yang mempertimbangkan area 4x4 piksel di sekitarnya untuk menghitung nilai piksel baru. Hasilnya adalah gambar yang diperbesar dengan transisi warna yang jauh lebih halus dan tidak terlihat "pecah".

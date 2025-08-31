# Aplikasi Filtering Audio dengan Python

## Ringkasan Proyek

Proyek ini adalah implementasi **Aplikasi Filtering Sinyal Audio** yang dirancang untuk membersihkan rekaman audio dari _noise_ atau frekuensi yang tidak diinginkan. Aplikasi ini dibangun menggunakan Python dengan **GUI berbasis Tkinter**, memungkinkan pengguna untuk mengunggah file audio WAV, menerapkan berbagai jenis filter, dan memvisualisasikan hasilnya secara interaktif. Proyek ini menggabungkan konsep-konsep dasar Pengolahan Sinyal Digital (PSD), seperti analisis domain waktu, analisis domain frekuensi, dan filtering digital.

## Fitur Utama

- **Unggah File Audio**: Memungkinkan pengguna untuk mengunggah file audio dalam format .wav.
- **Visualisasi Sinyal**: Menampilkan visualisasi sinyal audio dalam dua domain:

  - **Domain Waktu**: Grafik gelombang sinyal asli dan yang sudah difilter.
  - **Domain Frekuensi**: Spektrum frekuensi (hasil FFT) dari sinyal asli dan yang sudah difilter, untuk menunjukkan efek filtering secara visual.

- **Filtering Interaktif**: Menerapkan filter **Low-Pass**, **High-Pass**, dan **Band-Pass** ke sinyal audio. Pengguna dapat menentukan frekuensi _cut-off_ secara manual.
- **Pemutar Audio**: Memutar audio asli dan yang sudah difilter untuk perbandingan langsung.

## Pustaka yang Digunakan

Proyek ini menggunakan beberapa pustaka Python utama untuk fungsionalitasnya:

- **Tkinter**: Digunakan untuk membangun antarmuka pengguna grafis (GUI) yang interaktif.
- **NumPy**: Pustaka fundamental untuk komputasi numerik, digunakan untuk manipulasi data sinyal audio.
- **SciPy**: Pustaka inti untuk pengolahan sinyal digital, menyediakan fungsi-fungsi untuk membaca file .wav dan merancang filter digital (menggunakan algoritma Butterworth).
- **Matplotlib**: Digunakan untuk membuat plot dan grafik yang memvisualisasikan sinyal audio dalam domain waktu dan frekuensi.
- **Pydub & FFmpeg**: Digunakan untuk memutar file audio yang sudah dimuat atau difilter, memastikan kompatibilitas dan stabilitas.

## Cara Menjalankan Aplikasi

### 1\. Clone Repositori

```bash
- git clone https://github.com/rizkycahyono97/pengolahan-sinyal-digital

- cd final-proyek
```

### 2\. Buat dan Aktifkan Virtual Environment

Sangat disarankan untuk menggunakan lingkungan virtual agar instalasi pustaka tidak merusak instalasi Python global Anda.

```bash
python3 -m venv venv  source venv/bin/activate
```

### 3\. Instal Dependensi

Pastikan Anda sudah menginstal FFmpeg di sistem Anda sebelum menginstal pydub.

```bash
sudo apt-get install ffmpeg && pip install -r requirements.txt
```

### 4\. Jalankan Aplikasi

```bash
python main.py
```

## Struktur Proyek

- main.py: Berisi seluruh kode program, termasuk GUI, fungsi-fungsi pemrosesan sinyal, dan visualisasi.
- README.md: Dokumen ini.
- requirements.txt: Daftar semua pustaka Python yang diperlukan untuk menjalankan proyek.

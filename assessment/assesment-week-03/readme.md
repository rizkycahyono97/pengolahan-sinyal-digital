# **Laporan Proyek: Implementasi Operasi Dasar Pengolahan Sinyal Digital**

**Kelompok**: 1

**Anggota**:
* Rizky Cahyono Putra       - 442023611012
* Syaifan Noer Iwawan       - 442023611008
* M. Irfansyah              - 442023611004
* Muhammad Galang Fachrezy  - 442023611011
* Achmad Fatich Al-fahmi    - 422021611002

## **1. Pendahuluan**

Proyek ini bertujuan untuk memahami dan mengimplementasikan konsep fundamental dalam pengolahan sinyal digital. Kami menggunakan bahasa pemrograman Python dengan library utama **NumPy** untuk komputasi numerik dan **Matplotlib** untuk visualisasi. Laporan ini akan mencakup representasi sinyal 1D dan 2D, implementasi operasi dasar (penskalaan, penggeseran, penjumlahan), eksperimen kombinasi operasi, serta analisis dan refleksi dari setiap hasil yang diperoleh.

```python
# Setup Awal: Impor Library
import numpy as np
import matplotlib.pyplot as plt

# Konfigurasi plot agar lebih rapi
plt.style.use('seaborn-v0_8-whitegrid')
```

---

## **2. Representasi Sinyal**

### **2.1. Sinyal 1D (Satu Dimensi)**

**Konsep:** Sinyal 1D merepresentasikan suatu kuantitas yang nilainya berubah terhadap satu variabel independen, umumnya adalah **waktu**. Dalam implementasi ini, sinyal 1D direpresentasikan oleh dua array NumPy:
1.  **Sumbu Waktu (`t`)**: Array yang menyimpan titik-titik waktu.
2.  **Sumbu Amplitudo (`x`)**: Array yang menyimpan nilai sinyal pada setiap titik waktu tersebut.

**Implementasi:** Kami membuat dua sinyal periodik sebagai dasar eksperimen: sinyal sinus dan sinyal kotak (*square wave*).

```python
# Membuat sumbu waktu dari t=0 hingga t=2 detik, dengan 1000 titik data
t = np.linspace(0, 2, 1000)

# Sinyal 1: Sinus dengan frekuensi 2 Hz
f1 = 2
x1 = np.sin(2 * np.pi * f1 * t)

# Sinyal 2: Kotak (Square Wave) dengan frekuensi 1 Hz
from scipy import signal
f2 = 1
x2 = signal.square(2 * np.pi * f2 * t)

# Visualisasi Sinyal Awal
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
ax1.plot(t, x1, label='Sinyal Sinus (2 Hz)')
ax1.set_title('Sinyal 1D: $x_1(t)$')
ax1.set_ylabel('Amplitudo')
ax1.legend()

ax2.plot(t, x2, label='Sinyal Kotak (1 Hz)', color='r')
ax2.set_title('Sinyal 1D: $x_2(t)$')
ax2.set_xlabel('Waktu (detik)')
ax2.set_ylabel('Amplitudo')
ax2.legend()

plt.tight_layout()
plt.show()
```

### **2.2. Sinyal 2D (Dua Dimensi)**

**Konsep:** Sinyal 2D merepresentasikan kuantitas yang nilainya bergantung pada dua variabel spasial (posisi `x` dan `y`), contoh paling umum adalah **gambar digital**. Sinyal ini direpresentasikan sebagai matriks (array 2D NumPy) di mana nilai setiap elemen adalah intensitas piksel.

**Implementasi:** Kami membuat sebuah gambar sederhana secara programatik untuk menunjukkan representasi ini.

```python
# Membuat kanvas hitam 100x100 piksel
img = np.zeros((100, 100))

# Menambahkan bentuk "L" berwarna putih (nilai 1)
img[20:80, 20:35] = 1.0
img[65:80, 20:80] = 1.0

# Visualisasi
plt.figure(figsize=(5, 5))
plt.imshow(img, cmap='gray')
plt.title('Representasi Sinyal 2D (Gambar)')
plt.show()
```

---

## **3. Operasi Dasar pada Sinyal 1D**

### **3.1. Penskalaan (Scaling)**

**Konsep:** Operasi penskalaan ($y(t) = a \cdot x(t)$) mengubah amplitudo sinyal sebesar faktor `a`.

**Implementasi & Visualisasi:**

```python
a = 2.5  # Faktor skala
y_scaled = a * x1

plt.figure(figsize=(10, 5))
plt.plot(t, x1, label='Sinyal Asli, $x_1(t)$')
plt.plot(t, y_scaled, label=f'Hasil Penskalaan, $y(t) = {a} \cdot x_1(t)$', linestyle='--')
plt.title('Operasi Penskalaan Sinyal')
plt.legend()
plt.show()
```
**Analisis:** Terlihat jelas bahwa amplitudo sinyal hasil penskalaan menjadi 2.5 kali lebih besar dari sinyal asli, sementara frekuensi dan bentuk gelombangnya tetap terjaga.

### **3.2. Penjumlahan (Addition)**

**Konsep:** Operasi penjumlahan ($y(t) = x_1(t) + x_2(t)$) menggabungkan dua sinyal. Hasilnya adalah superposisi dari kedua sinyal tersebut.

**Implementasi & Visualisasi:**

```python
y_sum = x1 + x2

plt.figure(figsize=(10, 5))
plt.plot(t, x1, label='$x_1(t)$', alpha=0.6)
plt.plot(t, x2, label='$x_2(t)$', alpha=0.6)
plt.plot(t, y_sum, label='$y(t) = x_1(t) + x_2(t)$', color='k', linewidth=2)
plt.title('Operasi Penjumlahan Sinyal')
plt.legend()
plt.show()
```
**Analisis:** Bentuk gelombang hasil penjumlahan menjadi lebih kompleks, merefleksikan gabungan karakteristik dari sinyal sinus dan sinyal kotak.

### **3.3. Penggeseran (Shifting)**

**Konsep:** Operasi penggeseran ($y(t) = x(t - t_0)$) memindahkan sinyal sepanjang sumbu waktu. Implementasinya dilakukan dengan memanipulasi sumbu waktu (`t`), bukan amplitudonya (`x`).

**Implementasi & Visualisasi:**

```python
t0 = 0.3  # Digeser ke kanan sejauh 0.3 detik

plt.figure(figsize=(10, 5))
plt.plot(t, x1, label='Sinyal Asli, $x_1(t)$')
plt.plot(t + t0, x1, label=f'Sinyal Digeser, $x_1(t - {t0})$', linestyle='-.')
plt.title('Operasi Penggeseran Waktu')
plt.legend()
plt.show()
```
**Analisis:** Plot menunjukkan sinyal yang sama persis namun posisinya mundur (delay) atau bergeser ke kanan sejauh 0.3 detik, sesuai dengan teori.

---

## **4. Eksperimen Kombinasi Operasi**

**Tujuan:** Membuktikan bahwa operasi-operasi dasar dapat dikombinasikan untuk membentuk sinyal yang lebih kompleks. Kami akan mengimplementasikan persamaan:

$$y(t) = 2 \cdot x_1(t) + 0.5 \cdot x_2(t - 0.5)$$

**Implementasi & Visualisasi:**

```python
# Komponen 1: Penskalaan pada Sinyal 1
comp1 = 2 * x1

# Komponen 2: Penggeseran dan Penskalaan pada Sinyal 2
t_shift_2 = t + 0.5
comp2 = 0.5 * x2

# Sinyal Akhir (Penjumlahan komponen)
# Untuk visualisasi akurat, kita perlu mendefinisikan ulang sinyal 2 yang digeser pada sumbu waktu t
x2_shifted = signal.square(2 * np.pi * f2 * (t - 0.5))
y_combined = comp1 + (0.5 * x2_shifted)

# Visualisasi
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
ax1.plot(t, comp1, label='$2 \cdot x_1(t)$', color='b')
ax1.set_title('Komponen 1: Penskalaan Sinyal 1')
ax1.legend()

ax2.plot(t, 0.5 * x2_shifted, label='$0.5 \cdot x_2(t - 0.5)$', color='g')
ax2.set_title('Komponen 2: Penggeseran & Penskalaan Sinyal 2')
ax2.legend()

ax3.plot(t, y_combined, label='$y(t)$', color='purple')
ax3.set_title('Hasil Akhir Kombinasi Operasi')
ax3.set_xlabel('Waktu (detik)')
ax3.legend()

plt.tight_layout()
plt.show()
```
**Analisis:** Eksperimen ini berhasil menunjukkan bagaimana sinyal akhir `y(t)` terbentuk dari superposisi dua komponen yang telah dimodifikasi secara individual. Ini membuktikan pemahaman kami dalam mengombinasikan operasi dasar secara bertahap.

---

## **5. Operasi pada Sinyal 2D (Gambar)**

Operasi yang sama dapat diterapkan pada sinyal 2D. Penskalaan memengaruhi kecerahan, dan penjumlahan menggabungkan dua gambar.

```python
# Operasi Penskalaan pada Sinyal 2D (mengubah kecerahan)
img_scaled = 0.6 * img  # Membuat gambar lebih gelap

# Membuat gambar kedua untuk dijumlahkan
img2 = np.zeros((100, 100))
img2[40:60, 10:90] = 1.0 # Garis horizontal

# Operasi Penjumlahan (menumpuk gambar)
img_sum = np.clip(img + img2, 0, 1) # np.clip untuk memastikan nilai tetap di [0,1]

# Visualisasi
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(img_scaled, cmap='gray', vmin=0, vmax=1)
ax1.set_title('Hasil Penskalaan (Lebih Gelap)')
ax2.imshow(img_sum, cmap='gray')
ax2.set_title('Hasil Penjumlahan Gambar')
plt.show()
```

---

## **6. Refleksi dan Kesimpulan**

### **Refleksi Pemahaman**
Melalui proyek ini, kami memahami secara mendalam bahwa konsep sinyal yang abstrak dapat direpresentasikan secara konkret menggunakan struktur data array. Operasi-operasi matematis yang terlihat rumit dalam teori ternyata dapat diimplementasikan dengan manipulasi array yang sederhana dan intuitif menggunakan NumPy. Tantangan utama kami adalah memahami logika penggeseran waktu, di mana yang diubah adalah domain waktu (`t`) itu sendiri, bukan nilai sinyalnya (`x`). Setelah memahami konsep ini, implementasi menjadi jauh lebih mudah.

### **Kesimpulan**
Kelompok kami berhasil mengimplementasikan representasi sinyal 1D dan 2D serta melakukan tiga operasi dasar: penskalaan, penjumlahan, dan penggeseran. Eksperimen kombinasi operasi juga berhasil menunjukkan bagaimana sinyal kompleks dapat dibentuk dari komponen-komponen yang lebih sederhana. Visualisasi di setiap langkah terbukti sangat krusial untuk memvalidasi dan memahami hasil dari setiap operasi yang dilakukan.

---

## **7. Kontribusi Anggota**

Distribusi tugas dan kontribusi setiap anggota dicatat melalui riwayat commit pada repositori GitHub proyek ini.

| Nama Anggota | Tanggung Jawab Utama |
| :--- | :--- |
| Rizky Cahyono Putra | Representasi Sinyal 1D dan Operasi Penjumlahan. |
| Syaifan Noer Iwawan | Operasi Penskalaan dan Penggeseran Sinyal 1D. |
| M. Irfansyah        | Representasi Sinyal 2D, Eksperimen Kombinasi, dan Finalisasi Laporan. |

Untuk melihat riwayat kontribusi, dapat digunakan perintah `git` berikut di terminal:
```bash
git shortlog -sn --all
```
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import numpy as np
import librosa
import librosa.display
from scipy.io.wavfile import write
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import cv2

class DSPMiniProjectApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Proyek: Analisis Sinyal Digital")
        self.root.geometry("500x450")

        #style
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=10)
        style.configure("Header.TLabel", font=("Helvetica", 12, "italic"))

        # widget utama
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(expand=True, fill=tk.BOTH)
        title_label = ttk.Label(main_frame, text="Pilihan Mini Proyek", style="TLabel")
        title_label.pack(pady=(0, 20))

        # tombol setiap tema
        ttk.Button(main_frame, text="3. Operasi Penjumlahan & Perbesaran Citra", command=self.open_project_3).pack(fill=tk.X, pady=5)

    # ===========================
    # fungsi untuk setiap pilihan
    # ===========================
    def open_project_3(self):
        """Membuka jendela untuk Tema 3: Operasi Citra."""
        win = tk.Toplevel(self.root)
        win.title("Tema 3: Penjumlahan & Perbesaran Citra")
        win.geometry("900x500")

        # Variabel untuk menyimpan path dan data gambar
        self.img1_path = None
        self.img2_path = None
        self.img1_display = None
        self.img2_display = None
        
        # Frame utama
        main_frame = ttk.Frame(win, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Kolom untuk Input ---
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # --- Kolom untuk Hasil ---
        result_frame = ttk.Frame(main_frame)
        result_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        lbl_img1 = ttk.Label(input_frame, text="Gambar 1 (Pilih):", style="Header.TLabel")
        lbl_img1.pack()
        panel1 = ttk.Label(input_frame)
        panel1.pack(pady=5)
        
        lbl_img2 = ttk.Label(input_frame, text="Gambar 2 (Pilih):", style="Header.TLabel")
        lbl_img2.pack()
        panel2 = ttk.Label(input_frame)
        panel2.pack(pady=5)

        # --- Label untuk hasil ---
        lbl_result_add = ttk.Label(result_frame, text="Hasil Penjumlahan:", style="Header.TLabel")
        lbl_result_add.pack()
        panel_add = ttk.Label(result_frame)
        panel_add.pack(pady=5, expand=True)

        lbl_result_scale = ttk.Label(result_frame, text="Hasil Perbesaran (Gambar 1):", style="Header.TLabel")
        lbl_result_scale.pack()
        panel_scale = ttk.Label(result_frame)
        panel_scale.pack(pady=5, expand=True)

        def select_image(panel, label_widget, img_var_name):
            filepath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
            if not filepath:
                return

            setattr(self, img_var_name, filepath) # Simpan path
            
            # Tampilkan thumbnail
            img = Image.open(filepath)
            img.thumbnail((200, 200))
            photo = ImageTk.PhotoImage(img)
            
            panel.config(image=photo)
            panel.image = photo # Best practice: simpan referensi agar tidak di-garbage collect
            label_widget.config(text=f"{img_var_name.replace('_path','').upper()} Dipilih")


        def process_images():
            if not self.img1_path or not self.img2_path:
                messagebox.showwarning("Peringatan", "Harap pilih kedua gambar terlebih dahulu.")
                return

            try:
                img1 = Image.open(self.img1_path).convert("RGB")
                img2 = Image.open(self.img2_path).convert("RGB")

                # Samakan ukuran untuk operasi penjumlahan
                size = (400, 400)
                img1_resized = img1.resize(size)
                img2_resized = img2.resize(size)

                # --- Operasi Penjumlahan ---
                arr1 = np.array(img1_resized, dtype=np.uint8)
                arr2 = np.array(img2_resized, dtype=np.uint8)
                
                # Menggunakan cv2.addWeighted untuk blending yang lebih baik
                added_arr = cv2.addWeighted(arr1, 0.5, arr2, 0.5, 0)
                added_img = Image.fromarray(added_arr)

                # --- Operasi Perbesaran (Scaling) ---
                scaled_size = (600, 600)
                scaled_img = img1.resize(scaled_size, Image.Resampling.BICUBIC)
                
                # --- Tampilkan hasil ---
                # Penjumlahan
                added_img.thumbnail((300, 300))
                photo_add = ImageTk.PhotoImage(added_img)
                panel_add.config(image=photo_add)
                panel_add.image = photo_add

                # Perbesaran
                scaled_img.thumbnail((300, 300))
                photo_scale = ImageTk.PhotoImage(scaled_img)
                panel_scale.config(image=photo_scale)
                panel_scale.image = photo_scale
                
            except Exception as e:
                messagebox.showerror("Error", f"Gagal memproses gambar: {e}")


        # --- Tombol-tombol kontrol ---
        control_frame = ttk.Frame(input_frame)
        control_frame.pack(pady=20)
        ttk.Button(control_frame, text="Pilih Gambar 1", command=lambda: select_image(panel1, lbl_img1, "img1_path")).pack(fill=tk.X)
        ttk.Button(control_frame, text="Pilih Gambar 2", command=lambda: select_image(panel2, lbl_img2, "img2_path")).pack(fill=tk.X, pady=5)
        ttk.Button(control_frame, text="Proses Gambar", command=process_images).pack(fill=tk.X)


if __name__ == "__main__":
    root = tk.Tk()
    app = DSPMiniProjectApp(root)
    root.mainloop()
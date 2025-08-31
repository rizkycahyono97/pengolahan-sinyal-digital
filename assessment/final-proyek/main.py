import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import numpy as np
import scipy.io.wavfile
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pydub import AudioSegment
from pydub.playback import play

class AudioFilterApp:
    def __init__(self, root):
        """
        Inisialisasi aplikasi GUI.
        """
        self.root = root
        self.root.title("Aplikasi Filtering Audio")
        self.root.geometry("1000x800")
        self.root.option_add('*tearOff', False)

        self.sample_rate = None
        self.audio_data = None
        self.filtered_data = None
        
        self.filter_type = tk.StringVar(value="lowpass")
        self.cutoff_freq_low = tk.DoubleVar(value=1000.0)
        self.cutoff_freq_high = tk.DoubleVar(value=5000.0)

        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.control_frame = ttk.LabelFrame(self.main_frame, text="Kontrol", padding="10")
        self.control_frame.pack(fill=tk.X, padx=5, pady=5)

        ttk.Button(self.control_frame, text="Unggah Audio", command=self.open_audio_file).pack(side=tk.LEFT, padx=5, pady=5)
        self.play_original_button = ttk.Button(self.control_frame, text="Mainkan Asli", command=lambda: self.play_audio(self.audio_data))
        self.play_original_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.file_label = ttk.Label(self.control_frame, text="Tidak ada file yang dipilih.")
        self.file_label.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.filter_options_frame = ttk.LabelFrame(self.control_frame, text="Pilih Filter")
        self.filter_options_frame.pack(side=tk.LEFT, padx=20, pady=5)

        ttk.Radiobutton(self.filter_options_frame, text="Low-Pass", variable=self.filter_type, value="lowpass", command=self.toggle_freq_entry).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(self.filter_options_frame, text="High-Pass", variable=self.filter_type, value="highpass", command=self.toggle_freq_entry).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(self.filter_options_frame, text="Band-Pass", variable=self.filter_type, value="bandpass", command=self.toggle_freq_entry).pack(side=tk.LEFT, padx=5)

        self.freq_frame = ttk.Frame(self.control_frame)
        self.freq_frame.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.freq_label_low = ttk.Label(self.freq_frame, text="Frekuensi Cutoff Bawah (Hz):")
        self.freq_label_low.pack(side=tk.LEFT)
        self.freq_entry_low = ttk.Entry(self.freq_frame, textvariable=self.cutoff_freq_low, width=10)
        self.freq_entry_low.pack(side=tk.LEFT, padx=5)

        self.freq_label_high = ttk.Label(self.freq_frame, text="Frekuensi Cutoff Atas (Hz):")
        self.freq_label_high.pack_forget()
        self.freq_entry_high = ttk.Entry(self.freq_frame, textvariable=self.cutoff_freq_high, width=10)
        self.freq_entry_high.pack_forget()

        self.apply_button = ttk.Button(self.control_frame, text="Terapkan Filter", command=self.apply_filter)
        self.apply_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.play_filtered_button = ttk.Button(self.control_frame, text="Mainkan Filtered", command=lambda: self.play_audio(self.filtered_data))
        self.play_filtered_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.graph_frame = ttk.LabelFrame(self.main_frame, text="Visualisasi Sinyal", padding="10")
        self.graph_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.figure, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True)

        self.ax1.set_title("Sinyal Audio Asli (Domain Waktu)")
        self.ax2.set_title("Sinyal Audio Asli (Domain Frekuensi)")
        self.figure.tight_layout(pad=3.0)

    def toggle_freq_entry(self):
        if self.filter_type.get() == "bandpass":
            self.freq_label_high.pack(side=tk.LEFT)
            self.freq_entry_high.pack(side=tk.LEFT, padx=5)
        else:
            self.freq_label_high.pack_forget()
            self.freq_entry_high.pack_forget()

    def open_audio_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".wav",
            filetypes=[("WAV files", "*.wav")]
        )
        if file_path:
            self.file_label.config(text=f"File: {file_path.split('/')[-1]}")
            
            try:
                self.sample_rate, self.audio_data = scipy.io.wavfile.read(file_path)
                
                self.audio_data = self.audio_data.astype(np.float64)
                if len(self.audio_data.shape) > 1:
                    self.audio_data = np.mean(self.audio_data, axis=1)

                self.ax1.clear()
                self.ax2.clear()
                self.plot_signal(self.audio_data, self.sample_rate, self.ax1, "Sinyal Audio Asli")
                self.plot_spectrum(self.audio_data, self.sample_rate, self.ax2, "Spektrum Frekuensi Asli")
                self.canvas.draw()
            except Exception as e:
                self.file_label.config(text=f"Error: {e}")
                
    def apply_filter(self):
        if self.audio_data is None:
            self.file_label.config(text="Error: Mohon unggah file audio terlebih dahulu.")
            return

        try:
            filter_type = self.filter_type.get()
            cutoff_low = self.cutoff_freq_low.get()
            cutoff_high = self.cutoff_freq_high.get()
            order = 5  

            nyq = 0.5 * self.sample_rate
            Wn = None
            btype = ""

            if filter_type == "lowpass":
                Wn = cutoff_low / nyq
                btype = 'low'
            elif filter_type == "highpass":
                Wn = cutoff_high / nyq
                btype = 'high'
            elif filter_type == "bandpass":
                Wn = [cutoff_low / nyq, cutoff_high / nyq]
                btype = 'band'

            b, a = butter(order, Wn, btype=btype, analog=False)
            
            self.filtered_data = lfilter(b, a, self.audio_data)

            self.ax1.clear()
            self.ax2.clear()
            self.plot_signal(self.audio_data, self.sample_rate, self.ax1, "Sinyal Audio Asli vs Filtered")
            self.plot_signal(self.filtered_data, self.sample_rate, self.ax1, "Sinyal Audio Asli vs Filtered", filtered=True)
            self.plot_spectrum(self.audio_data, self.sample_rate, self.ax2, "Spektrum Asli vs Filtered")
            self.plot_spectrum(self.filtered_data, self.sample_rate, self.ax2, "Spektrum Asli vs Filtered", filtered=True)
            self.canvas.draw()
            self.file_label.config(text="Filter berhasil diterapkan!")

        except ValueError:
            self.file_label.config(text="Error: Masukkan frekuensi yang valid.")
        except Exception as e:
            self.file_label.config(text=f"Error: {e}")

    def plot_signal(self, data, sample_rate, ax, title, filtered=False):
        time = np.linspace(0, len(data) / sample_rate, num=len(data))
        color = 'blue' if not filtered else 'red'
        label = 'Asli' if not filtered else 'Filtered'
        ax.plot(time, data, color=color, label=label, alpha=0.7)
        ax.set_title(title)
        ax.set_xlabel("Waktu (detik)")
        ax.set_ylabel("Amplitudo")
        ax.grid(True)
        ax.legend()
        self.figure.tight_layout(pad=3.0)

    def plot_spectrum(self, data, sample_rate, ax, title, filtered=False):
        N = len(data)
        T = 1.0 / sample_rate
        xf = np.fft.fftfreq(N, T)[:N//2]
        yf = np.fft.fft(data)
        color = 'orange' if not filtered else 'green'
        label = 'Asli' if not filtered else 'Filtered'
        ax.plot(xf, 2.0/N * np.abs(yf[0:N//2]), color=color, label=label, alpha=0.7)
        ax.set_title(title)
        ax.set_xlabel("Frekuensi (Hz)")
        ax.set_ylabel("Magnitudo")
        ax.set_xlim(0, sample_rate/2)
        ax.grid(True)
        ax.legend()
        self.figure.tight_layout(pad=3.0)
        
    def play_audio(self, audio_data):
        if audio_data is not None:
            try:
                # Normalisasi data ke int16
                audio_data_int16 = audio_data.astype(np.int16)
                
                audio_segment = AudioSegment(
                    audio_data_int16.tobytes(),
                    frame_rate=self.sample_rate,
                    channels=1,
                    sample_width=audio_data_int16.dtype.itemsize
                )
                
                # Putar audio
                play(audio_segment)
            except Exception as e:
                self.file_label.config(text=f"Error saat memutar audio: {e}")
            
if __name__ == "__main__":
    root = tk.Tk()
    app = AudioFilterApp(root)
    root.mainloop()

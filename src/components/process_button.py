import customtkinter as ctk
import tkinter as tk
import os
import time
from tkinter import messagebox
from src.pdf.pdf_processor import process_pdfs as process_pdfs_merge
from src.pdf.pdf_processor_rename import process_pdfs as process_pdfs_rename

class ProcessButtonComponent:
    def __init__(self, parent, colors, input_path_var, output_path_var, mode_var, settings, progress_var, progress_percentage_var, statistics, output_location, mode_selection, gui):
        self.parent = parent
        self.colors = colors
        self.input_path_var = input_path_var
        self.output_path_var = output_path_var
        self.mode_var = mode_var
        self.settings = settings
        self.progress_var = progress_var
        self.progress_percentage_var = progress_percentage_var
        self.statistics = statistics
        self.output_location = output_location
        self.mode_selection = mode_selection
        self.gui = gui  # Referensi ke instance RenamergedGUI

        # Tombol Proses
        self.process_btn = ctk.CTkButton(self.parent, text="Proses", command=self.process,
                                         fg_color="#1E3A8A", text_color="#FFFFFF",
                                         font=("Roboto", 12, "bold"), hover_color="#3B82F6",
                                         width=120, height=35, border_width=0, corner_radius=15)
        self.process_btn.grid(row=14, column=0, columnspan=2, pady=20)

    def process(self):
        input_dir = self.input_path_var.get()
        output_dir = self.output_path_var.get()
        mode = self.mode_var.get()

        # Validasi input
        if not input_dir or not isinstance(input_dir, str):  # Periksa apakah input_dir kosong atau bukan string
            messagebox.showerror("Error", "Pilih folder input terlebih dahulu!")
            return
        if not os.path.isdir(input_dir):
            messagebox.showerror("Error", "Folder input tidak valid! Pilih folder yang benar.")
            return

        # Perbarui pengaturan dengan urutan komponen dari mode_selection
        self.settings["component_order"] = self.mode_selection.get_component_order()

        # Reset statistik dan progress bar
        self.statistics.reset()
        self.progress_var.set(0)
        self.progress_percentage_var.set("0%")
        self.gui.progress_bar.set_progress(0)  # Set progress bar ke 0
        self.parent.update_idletasks()  # Pastikan UI diperbarui

        # Jalankan proses sesuai mode
        try:
            if mode == "Rename dan Merge":
                total, renamed, merged, errors = process_pdfs_merge(input_dir, output_dir, self.progress_callback, self.log_callback, self.settings)
            else:  # Rename Saja
                total, renamed, merged, errors = process_pdfs_rename(input_dir, output_dir, self.progress_callback, self.log_callback, self.settings)

            # Update statistik
            self.statistics.update_statistics(total, renamed, merged, errors)
            self.output_location.set_output_path(output_dir)

        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

    def log_callback(self, message):
        if self.statistics:
            self.statistics.log_message(message)

    def progress_callback(self, stage, current, total_files, total_to_merge, total_to_finalize):
        # Hitung persentase dalam skala 0 hingga 100
        if stage == "reading":
            percentage = (current / total_files) * 40  # 40% untuk tahap membaca
        elif stage == "processing":
            percentage = 40 + (current / total_to_merge) * 40  # 40% untuk tahap pemrosesan (merge)
        else:  # finalizing
            percentage = 80 + (current / total_to_finalize) * 20  # 20% untuk tahap finalisasi

        # Pastikan persentase berada dalam skala 0 hingga 100
        percentage = min(max(percentage, 0), 100)

        # Normalkan ke skala 0 hingga 1 untuk CTkProgressBar
        normalized_progress = percentage / 100

        # Debugging: Log nilai progress
        print(f"[Progress] Stage: {stage}, Current: {current}, Total Files: {total_files}, Total to Merge: {total_to_merge}, Total to Finalize: {total_to_finalize}, Percentage: {percentage}%, Normalized: {normalized_progress}")

        # Update progress bar menggunakan metode set_progress
        self.gui.progress_bar.set_progress(normalized_progress)
        self.progress_var.set(normalized_progress)
        self.progress_percentage_var.set(f"{int(percentage)}%")
        self.parent.update_idletasks()  # Memaksa pembaruan UI untuk progress bar
        self.parent.update()

        # Tambahkan jeda kecil untuk memperlambat pembaruan visual
        time.sleep(0.05)  # Jeda 50ms untuk memperlambat pembaruan

    def update_theme(self, colors):
        self.colors = colors
        self.process_btn.configure(fg_color="#1E3A8A", text_color="#FFFFFF", hover_color="#3B82F6")
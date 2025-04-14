import customtkinter as ctk
import os

class FileListComponent:
    def __init__(self, parent, colors, input_path_var):
        self.parent = parent
        self.colors = colors
        self.input_path_var = input_path_var

        # Total PDF Terdeteksi
        self.total_pdf_var = ctk.StringVar(value="Total PDF Terdeteksi: 0")
        self.total_pdf_label = ctk.CTkLabel(self.parent, textvariable=self.total_pdf_var,
                                            font=("Roboto", 12), text_color=self.colors["fg"])
        self.total_pdf_label.grid(row=6, column=0, columnspan=2, sticky="w", padx=10, pady=(10, 0))

        # Bind input_path_var untuk update jumlah PDF
        self.input_path_var.trace("w", self.update_file_count)

    def update_file_count(self, *args):
        folder = self.input_path_var.get()
        if folder and os.path.isdir(folder):
            pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]
            count = len(pdf_files)
            self.total_pdf_var.set(f"Total PDF Terdeteksi: {count}")
        else:
            self.total_pdf_var.set("Total PDF Terdeteksi: 0")

    def update_theme(self, colors):
        self.colors = colors
        self.total_pdf_label.configure(text_color=self.colors["fg"])
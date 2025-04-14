import customtkinter as ctk
import tkinter as tk
import os
from tkinter import filedialog

class FileInputOutputComponent:
    def __init__(self, parent, colors, input_path_var, output_path_var):
        self.parent = parent
        self.colors = colors
        self.input_path_var = input_path_var
        self.output_path_var = output_path_var

        # Input Folder
        ctk.CTkLabel(self.parent, text="Pilih Folder Input PDF:", font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=4, column=0, sticky="w", padx=10, pady=(10, 0))
        self.input_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.input_frame.grid(row=5, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.input_frame.grid_columnconfigure(0, weight=1)
        self.input_frame.grid_columnconfigure(1, weight=0)
        self.input_entry = ctk.CTkEntry(self.input_frame, textvariable=self.input_path_var,
                                        height=35, fg_color=self.colors["entry_bg"],
                                        text_color=self.colors["entry_fg"], border_width=0,
                                        corner_radius=10, font=("Roboto", 12), width=1000)  # Perbesar lebar menjadi 1000
        self.input_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        self.browse_input_btn = ctk.CTkButton(self.input_frame, text="Browse", command=self.browse_input,
                                              fg_color="#1E3A8A", text_color="#FFFFFF",
                                              font=("Roboto", 12, "bold"), hover_color="#3B82F6",
                                              width=120, height=35, border_width=0, corner_radius=15)
        self.browse_input_btn.grid(row=0, column=1)

        # Output Folder
        ctk.CTkLabel(self.parent, text="Pilih Folder Output PDF (Opsional):", font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=7, column=0, sticky="w", padx=10, pady=(10, 0))
        self.output_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.output_frame.grid(row=8, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        self.output_frame.grid_columnconfigure(0, weight=1)
        self.output_entry = ctk.CTkEntry(self.output_frame, textvariable=self.output_path_var,
                                         height=35, fg_color=self.colors["entry_bg"],
                                         text_color=self.colors["entry_fg"], border_width=0,
                                         corner_radius=10, font=("Roboto", 12), width=1000)  # Perbesar lebar menjadi 1000
        self.output_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        self.browse_output_btn = ctk.CTkButton(self.output_frame, text="Browse", command=self.browse_output,
                                               fg_color="#1E3A8A", text_color="#FFFFFF",
                                               font=("Roboto", 12, "bold"), hover_color="#3B82F6",
                                               width=120, height=35, border_width=0, corner_radius=15)
        self.browse_output_btn.grid(row=0, column=1)

    def browse_input(self):
        # Buat jendela pop-up untuk memilih folder
        popup = ctk.CTkToplevel(self.parent)
        popup.title("Pilih Folder Input PDF")
        popup.geometry("600x400")
        popup.transient(self.parent)  # Membuat pop-up tetap di atas jendela utama
        popup.grab_set()  # Membuat pop-up modal

        # Frame utama di pop-up
        main_frame = ctk.CTkFrame(popup)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame untuk memilih folder
        folder_frame = ctk.CTkFrame(main_frame)
        folder_frame.pack(fill="x", pady=(0, 10))
        folder_path_var = ctk.StringVar()
        folder_entry = ctk.CTkEntry(folder_frame, textvariable=folder_path_var, width=400)
        folder_entry.pack(side="left", padx=(0, 5))
        browse_btn = ctk.CTkButton(folder_frame, text="Browse", command=lambda: self._browse_folder(popup, folder_path_var))
        browse_btn.pack(side="left")

        # Label untuk total PDF terdeteksi
        total_pdf_var = ctk.StringVar(value="Total PDF Terdeteksi: 0")
        total_pdf_label = ctk.CTkLabel(main_frame, textvariable=total_pdf_var, font=("Roboto", 12))
        total_pdf_label.pack(anchor="w", padx=5)

        # Frame untuk pratinjau file PDF
        preview_frame = ctk.CTkFrame(main_frame)
        preview_frame.pack(fill="both", expand=True)
        ctk.CTkLabel(preview_frame, text="Pratinjau File PDF:", font=("Roboto", 12)).pack(anchor="w", padx=5)
        file_list = ctk.CTkTextbox(preview_frame, height=200)
        file_list.pack(fill="both", expand=True, padx=5, pady=5)
        file_list.configure(state="disabled")  # Membuat textbox hanya baca

        # Frame untuk tombol
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(fill="x", pady=(10, 0))
        cancel_btn = ctk.CTkButton(button_frame, text="Batal", command=popup.destroy)
        cancel_btn.pack(side="right", padx=5)
        select_btn = ctk.CTkButton(button_frame, text="Pilih", command=lambda: self._select_folder(popup, folder_path_var))
        select_btn.pack(side="right", padx=5)

        # Bind folder_path_var untuk update pratinjau dan total PDF
        folder_path_var.trace("w", lambda *args: self._update_preview(folder_path_var, file_list, total_pdf_var))

    def _browse_folder(self, popup, folder_path_var):
        folder = filedialog.askdirectory(parent=popup, title="Pilih Folder PDF")
        if folder:
            folder_path_var.set(folder)

    def _update_preview(self, folder_path_var, file_list, total_pdf_var):
        folder = folder_path_var.get()
        file_list.configure(state="normal")
        file_list.delete("1.0", tk.END)
        if folder and os.path.isdir(folder):
            pdf_files = [f for f in os.listdir(folder) if f.endswith('.pdf')]
            count = len(pdf_files)
            total_pdf_var.set(f"Total PDF Terdeteksi: {count}")
            for pdf_file in pdf_files:
                file_list.insert(tk.END, f"{pdf_file}\n")
        else:
            total_pdf_var.set("Total PDF Terdeteksi: 0")
        file_list.configure(state="disabled")

    def _select_folder(self, popup, folder_path_var):
        folder = folder_path_var.get()
        if folder:
            self.input_path_var.set(folder)
        popup.destroy()

    def browse_output(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_path_var.set(folder)

    def update_theme(self, colors):
        self.colors = colors
        for child in self.parent.winfo_children():
            if isinstance(child, ctk.CTkLabel) and child != self.parent.winfo_children()[0]:  # Skip title label
                child.configure(text_color=self.colors["fg"])
        self.input_frame.configure(fg_color="transparent")
        self.input_entry.configure(fg_color=self.colors["entry_bg"], text_color=self.colors["entry_fg"])
        self.browse_input_btn.configure(fg_color="#1E3A8A", text_color=self.colors["button_fg"], hover_color="#3B82F6")
        self.output_frame.configure(fg_color="transparent")
        self.output_entry.configure(fg_color=self.colors["entry_bg"], text_color=self.colors["entry_fg"])
        self.browse_output_btn.configure(fg_color="#1E3A8A", text_color=self.colors["button_fg"], hover_color="#3B82F6")
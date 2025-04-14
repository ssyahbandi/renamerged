import customtkinter as ctk
import os
from tkinter import messagebox

class OutputLocationComponent:
    def __init__(self, parent, colors):
        self.parent = parent
        self.colors = colors

        # Lokasi Output
        self.output_location_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.output_location_frame.grid(row=13, column=0, columnspan=2, sticky="ew", padx=10, pady=(20, 0))  # Tambah padding vertikal (pady)
        self.output_location_frame.grid_columnconfigure(0, weight=1)
        self.output_location_var = ctk.StringVar(value="Hasil disimpan di: -")
        self.output_location_label = ctk.CTkLabel(self.output_location_frame, textvariable=self.output_location_var,
                                                  font=("Roboto", 12), text_color=self.colors["fg"],
                                                  wraplength=600)  # Kurangi wraplength menjadi 600
        self.output_location_label.grid(row=0, column=0, sticky="w")
        self.open_output_btn = ctk.CTkButton(self.output_location_frame, text="Buka Folder Hasil", command=self.open_output_folder,
                                             fg_color="#1E3A8A", text_color="#FFFFFF",
                                             font=("Roboto", 12, "bold"), hover_color="#3B82F6",
                                             width=120, height=35, border_width=0, corner_radius=15)
        self.open_output_btn.grid(row=0, column=1, sticky="e")

    def set_output_path(self, path):
        self.output_location_var.set(f"Hasil disimpan di: {path}")

    def open_output_folder(self):
        output_path = self.output_location_var.get().replace("Hasil disimpan di: ", "")
        if os.path.isdir(output_path):
            os.startfile(output_path)
        else:
            messagebox.showerror("Error", "Folder tidak ditemukan!")

    def update_theme(self, colors):
        self.colors = colors
        self.output_location_frame.configure(fg_color="transparent")
        self.output_location_label.configure(text_color=self.colors["fg"])
        self.open_output_btn.configure(fg_color="#1E3A8A", text_color=self.colors["button_fg"], hover_color="#3B82F6")
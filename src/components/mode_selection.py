import customtkinter as ctk
import tkinter as tk
from src.components.draggable_component import DraggableComponent

class ModeSelectionComponent:
    def __init__(self, parent, colors, mode_var, settings):
        self.parent = parent
        self.colors = colors
        self.mode_var = mode_var
        self.settings = settings
        self.components = []  # Daftar komponen yang dapat digeser
        self.component_order = []  # Urutan komponen
        self.selected_component = None  # Komponen yang sedang dipilih

        # Pemilihan Mode
        self.mode_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.mode_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        ctk.CTkLabel(self.mode_frame, text="Mode Pemrosesan:", font=("Roboto", 12),
                     text_color=self.colors["fg"]).pack(side="left", padx=(0, 10))
        self.mode_menu = ctk.CTkOptionMenu(self.mode_frame, values=["Rename Saja", "Rename dan Merge"],
                                           variable=self.mode_var, command=self.toggle_mode_options,
                                           fg_color="#1E3A8A", text_color="#FFFFFF",
                                           font=("Roboto", 12), width=150, height=35, corner_radius=15)
        self.mode_menu.pack(side="left")

        # Frame untuk opsi komponen nama file (hanya muncul pada mode Rename Saja)
        self.name_components_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.name_components_frame.grid(row=3, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))

        # Label untuk komponen nama file
        ctk.CTkLabel(self.name_components_frame, text="Komponen Nama File (untuk Rename Saja):", font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=0, column=0, sticky="w", padx=(0, 10), pady=(0, 2))

        # Keterangan cara menggeser
        ctk.CTkLabel(self.name_components_frame, text="Bisa digeser dengan klik lalu geser dengan panah keyboard.", font=("Roboto", 10, "italic"),
                     text_color="#BBBBBB").grid(row=1, column=0, sticky="w", padx=(0, 10), pady=(0, 5))

        # Frame untuk komponen yang dapat digeser (menggunakan CTkFrame biasa)
        self.components_container = ctk.CTkFrame(self.name_components_frame, fg_color="transparent")
        self.components_container.grid(row=2, column=0, columnspan=5, sticky="ew", padx=(10, 10))

        # Inisialisasi komponen yang dapat digeser
        self.component_order = [
            ("Nama Lawan Transaksi", self.settings["use_name"]),
            ("Tanggal Faktur Pajak", self.settings["use_date"]),
            ("Referensi", self.settings["use_reference"]),
            ("Nomor Faktur Pajak", self.settings["use_faktur"])
        ]
        self._create_components()

        # Bind tombol panah untuk menggeser komponen
        self.parent.bind("<Left>", self.move_left)
        self.parent.bind("<Right>", self.move_right)

        self.toggle_mode_options(self.mode_var.get())  # Inisialisasi visibilitas

    def _create_components(self):
        """Membuat komponen yang dapat digeser."""
        self.components = []
        for text, var in self.component_order:
            component = DraggableComponent(self.components_container, text, var, self._on_select, self.colors)
            component.pack(side="left", padx=10, pady=5)  # Gunakan pack untuk tata letak horizontal
            self.components.append(component)
        self._update_order()

    def _on_select(self, selected_component):
        """Menangani saat komponen dipilih."""
        # Deselect semua komponen lain
        for component in self.components:
            if component != selected_component:
                component.deselect()
        self.selected_component = selected_component

    def move_left(self, event):
        """Geser komponen yang dipilih ke kiri satu posisi."""
        if self.selected_component and self.mode_var.get() == "Rename Saja":
            current_index = self.components.index(self.selected_component)
            if current_index > 0:  # Pastikan bukan komponen pertama
                # Geser komponen satu posisi ke kiri dalam daftar
                self.components[current_index], self.components[current_index - 1] = self.components[current_index - 1], self.components[current_index]
                self._refresh_layout()
                self._update_order()

    def move_right(self, event):
        """Geser komponen yang dipilih ke kanan satu posisi."""
        if self.selected_component and self.mode_var.get() == "Rename Saja":
            current_index = self.components.index(self.selected_component)
            if current_index < len(self.components) - 1:  # Pastikan bukan komponen terakhir
                # Geser komponen satu posisi ke kanan dalam daftar
                self.components[current_index], self.components[current_index + 1] = self.components[current_index + 1], self.components[current_index]
                self._refresh_layout()
                self._update_order()

    def _refresh_layout(self):
        """Perbarui tata letak visual berdasarkan urutan dalam self.components."""
        # Hapus semua komponen dari tata letak
        for component in self.components:
            component.pack_forget()
        # Tambahkan kembali komponen sesuai urutan dalam self.components
        for component in self.components:
            component.pack(side="left", padx=10, pady=5)

    def _update_order(self):
        """Perbarui urutan komponen setelah digeser."""
        self.component_order = [(comp.text, comp.variable) for comp in self.components]

    def get_component_order(self):
        """Mengembalikan urutan komponen."""
        return [text for text, _ in self.component_order]

    def toggle_mode_options(self, mode):
        """Menampilkan atau menyembunyikan opsi komponen nama file berdasarkan mode."""
        if mode == "Rename Saja":
            self.name_components_frame.grid()
        else:
            self.name_components_frame.grid_remove()

    def update_theme(self, colors):
        self.colors = colors
        for child in self.mode_frame.winfo_children():
            if isinstance(child, ctk.CTkLabel):
                child.configure(text_color=self.colors["fg"])
        self.mode_menu.configure(fg_color="#1E3A8A", text_color="#FFFFFF")
        for child in self.name_components_frame.winfo_children():
            if isinstance(child, ctk.CTkLabel):
                child.configure(text_color="#BBBBBB" if child.cget("text").startswith("Bisa digeser") else self.colors["fg"])
        for component in self.components:
            component.update_theme(colors)
import customtkinter as ctk
import tkinter as tk

class DraggableComponent(ctk.CTkFrame):
    def __init__(self, parent, text, variable, on_select_callback, colors, width=260, height=40):
        super().__init__(parent, fg_color=colors["entry_bg"], border_width=2, border_color="#3B82F6", corner_radius=10, width=width, height=height)
        self.text = text
        self.variable = variable
        self.on_select_callback = on_select_callback
        self.colors = colors
        self.is_selected = False

        # Checkbox untuk mengaktifkan/menonaktifkan komponen
        self.checkbox = ctk.CTkCheckBox(self, text="", variable=self.variable, width=20, height=20)
        self.checkbox.pack(side="left", padx=5)

        # Label untuk teks komponen
        self.label = ctk.CTkLabel(self, text=self.text, font=("Roboto", 12, "bold"), text_color=self.colors["fg"])
        self.label.pack(side="left", padx=5, pady=5)

        # Bind klik untuk memilih komponen (untuk geser dengan keyboard)
        self.bind("<Button-1>", self.select)
        self.checkbox.bind("<Button-1>", self.select)
        self.label.bind("<Button-1>", self.select)

        # Bind efek hover
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.checkbox.bind("<Enter>", self.on_enter)
        self.checkbox.bind("<Leave>", self.on_leave)
        self.label.bind("<Enter>", self.on_enter)
        self.label.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        """Efek hover: ubah warna border saat mouse masuk."""
        if not self.is_selected:
            self.configure(border_color="#60A5FA")  # Biru lebih terang saat hover

    def on_leave(self, event):
        """Efek hover: kembalikan warna border saat mouse keluar."""
        if not self.is_selected:
            self.configure(border_color="#3B82F6")  # Kembalikan warna border awal

    def select(self, event):
        if not self.is_selected:
            self.is_selected = True
            self.configure(fg_color="#3B82F6", border_color="#FFD700")  # Highlight dengan warna kuning untuk border saat dipilih
            self.on_select_callback(self)  # Panggil callback untuk memberi tahu bahwa komponen ini dipilih
        return "break"  # Cegah event bubbling

    def deselect(self):
        self.is_selected = False
        self.configure(fg_color=self.colors["entry_bg"], border_color="#3B82F6")  # Kembalikan warna awal saat tidak dipilih

    def update_theme(self, colors):
        self.colors = colors
        self.configure(fg_color=colors["entry_bg"] if not self.is_selected else "#3B82F6",
                      border_color="#3B82F6" if not self.is_selected else "#FFD700")
        self.label.configure(text_color=colors["fg"])
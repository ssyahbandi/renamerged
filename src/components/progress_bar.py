import customtkinter as ctk

class ProgressBarComponent:
    def __init__(self, parent, colors, progress_var, progress_percentage_var):
        self.parent = parent
        self.colors = colors
        self.progress_var = progress_var
        self.progress_percentage_var = progress_percentage_var

        # Progress Bar
        self.progress_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.progress_frame.grid(row=10, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))

        ctk.CTkLabel(self.progress_frame, text="Progress:", font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=0, column=0, sticky="w", pady=(0, 5))

        # Konfigurasi CTkProgressBar tanpa variable, sesuaikan width untuk ukuran jendela baru
        self.progress_bar = ctk.CTkProgressBar(self.progress_frame,
                                               progress_color="#4CAF50", fg_color=self.colors["entry_bg"],
                                               width=350, height=15, corner_radius=10)  # Sesuaikan width dari 500 ke 350
        self.progress_bar.set(0)  # Set nilai awal ke 0
        self.progress_bar.grid(row=1, column=0, sticky="ew", padx=(0, 10))

        # Label persentase
        ctk.CTkLabel(self.progress_frame, textvariable=self.progress_percentage_var, font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=1, column=1)

    def set_progress(self, value):
        """Mengatur nilai progress bar secara langsung (skala 0 hingga 1)."""
        self.progress_bar.set(value)
        self.parent.update_idletasks()

    def update_theme(self, colors):
        self.colors = colors
        for child in self.progress_frame.winfo_children():
            if isinstance(child, ctk.CTkLabel):
                child.configure(text_color=self.colors["fg"])
        self.progress_bar.configure(fg_color=self.colors["entry_bg"], progress_color="#4CAF50")
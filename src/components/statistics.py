import customtkinter as ctk

class StatisticsComponent:
    def __init__(self, parent, colors):
        self.parent = parent
        self.colors = colors

        # Statistik
        self.stats_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.stats_frame.grid(row=11, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))

        self.total_processed_var = ctk.StringVar(value="Total diproses: 0")
        self.total_moved_var = ctk.StringVar(value="File yang hanya diganti nama: 0")
        self.total_merged_var = ctk.StringVar(value="File yang diganti nama dan digabung: 0")
        self.total_errors_var = ctk.StringVar(value="Total file yang error: 0")

        ctk.CTkLabel(self.stats_frame, textvariable=self.total_processed_var, font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=0, column=0, sticky="w")
        ctk.CTkLabel(self.stats_frame, textvariable=self.total_moved_var, font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=1, column=0, sticky="w")
        ctk.CTkLabel(self.stats_frame, textvariable=self.total_merged_var, font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=2, column=0, sticky="w")
        ctk.CTkLabel(self.stats_frame, textvariable=self.total_errors_var, font=("Roboto", 12),
                     text_color=self.colors["fg"]).grid(row=3, column=0, sticky="w")

    def reset(self):
        """Reset semua statistik ke nilai awal."""
        self.total_processed_var.set("Total diproses: 0")
        self.total_moved_var.set("File yang hanya diganti nama: 0")
        self.total_merged_var.set("File yang diganti nama dan digabung: 0")
        self.total_errors_var.set("Total file yang error: 0")

    def log_message(self, message):
        pass  # Tidak digunakan untuk saat ini

    def update_statistics(self, total_processed, total_moved, total_merged, total_errors):
        self.total_processed_var.set(f"Total diproses: {total_processed}")
        self.total_moved_var.set(f"File yang hanya diganti nama: {total_moved}")
        self.total_merged_var.set(f"File yang diganti nama dan digabung: {total_merged}")
        self.total_errors_var.set(f"Total file yang error: {total_errors}")

    def update_theme(self, colors):
        self.colors = colors
        for child in self.stats_frame.winfo_children():
            if isinstance(child, ctk.CTkLabel):
                child.configure(text_color=self.colors["fg"])
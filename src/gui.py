import customtkinter as ctk
import tkinter as tk
from src.styles import Theme
from src.components.header import HeaderComponent
from src.components.mode_selection import ModeSelectionComponent
from src.components.file_input_output import FileInputOutputComponent
from src.components.file_list import FileListComponent
from src.components.progress_bar import ProgressBarComponent
from src.components.statistics import StatisticsComponent
from src.components.output_location import OutputLocationComponent
from src.components.process_button import ProcessButtonComponent

class RenamergedGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RENAMERGED - Rename & Merge PDFs")
        self.root.geometry("900x800")
        self.root.resizable(True, True)
        self.root.minsize(900, 800)

        # Inisialisasi tema
        self.theme = Theme()
        self.current_theme = "dark"
        ctk.set_appearance_mode(self.current_theme)
        self.colors = self.theme.get_colors(self.current_theme)
        self.root.configure(bg=self.colors["bg"])

        # Pengaturan Kustom
        self.mode_var = ctk.StringVar(value="Rename dan Merge")
        self.settings = {
            "mode": self.mode_var,
            "use_name": tk.BooleanVar(value=True),
            "use_date": tk.BooleanVar(value=True),
            "use_reference": tk.BooleanVar(value=True),
            "use_faktur": tk.BooleanVar(value=True)
        }

        # Variabel untuk input/output
        self.input_path_var = ctk.StringVar()
        self.output_path_var = ctk.StringVar()

        # Variabel untuk progress bar
        self.progress_var = ctk.DoubleVar(value=0.0)
        self.progress_percentage_var = ctk.StringVar(value="0%")

        # Frame utama
        self.main_frame = ctk.CTkFrame(self.root, fg_color=self.colors["bg"])
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Konfigurasi grid untuk layout
        self.main_frame.grid_rowconfigure(0, weight=0)  # Baris judul
        self.main_frame.grid_rowconfigure(1, weight=0)  # Baris tombol donasi/tema
        self.main_frame.grid_rowconfigure(2, weight=0)  # Baris mode
        self.main_frame.grid_rowconfigure(3, weight=0)  # Baris komponen nama file
        self.main_frame.grid_rowconfigure(4, weight=0)  # Baris label input
        self.main_frame.grid_rowconfigure(5, weight=0)  # Baris entry input
        self.main_frame.grid_rowconfigure(6, weight=0)  # Baris total PDF
        self.main_frame.grid_rowconfigure(7, weight=2)  # Baris daftar file
        self.main_frame.grid_rowconfigure(8, weight=0)  # Baris label output
        self.main_frame.grid_rowconfigure(9, weight=0)  # Baris entry output
        self.main_frame.grid_rowconfigure(10, weight=0)  # Baris label progress
        self.main_frame.grid_rowconfigure(11, weight=0)  # Baris progress bar
        self.main_frame.grid_rowconfigure(12, weight=0)  # Baris statistik
        self.main_frame.grid_rowconfigure(13, weight=0)  # Baris lokasi output
        self.main_frame.grid_rowconfigure(14, weight=0)  # Baris tombol proses
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=0)

        # Inisialisasi komponen
        self.header = HeaderComponent(self.main_frame, self.colors, self.toggle_theme)
        self.mode_selection = ModeSelectionComponent(self.main_frame, self.colors, self.mode_var, self.settings)
        self.file_input_output = FileInputOutputComponent(self.main_frame, self.colors, self.input_path_var, self.output_path_var)
        self.file_list = FileListComponent(self.main_frame, self.colors, self.input_path_var)
        self.progress_bar = ProgressBarComponent(self.main_frame, self.colors)
        self.statistics = StatisticsComponent(self.main_frame, self.colors)
        self.output_location = OutputLocationComponent(self.main_frame, self.colors)
        self.process_button = ProcessButtonComponent(self.main_frame, self.colors, self.input_path_var, self.output_path_var,
                                                    self.mode_var, self.settings, self.progress_bar.progress_var,
                                                    self.progress_bar.progress_percentage_var, self.statistics,
                                                    self.output_location)

    def toggle_theme(self):
        if self.current_theme == "dark":
            self.current_theme = "light"
        else:
            self.current_theme = "dark"
        ctk.set_appearance_mode(self.current_theme)
        self.colors = self.theme.get_colors(self.current_theme)
        self.root.configure(bg=self.colors["bg"])
        self.main_frame.configure(fg_color=self.colors["bg"])
        self.header.update_theme(self.colors)
        self.mode_selection.update_theme(self.colors)
        self.file_input_output.update_theme(self.colors)
        self.file_list.update_theme(self.colors)
        self.progress_bar.update_theme(self.colors)
        self.statistics.update_theme(self.colors)
        self.output_location.update_theme(self.colors)
        self.process_button.update_theme(self.colors)

def run_gui():
    root = ctk.CTk()
    app = RenamergedGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
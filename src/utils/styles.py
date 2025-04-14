class Theme:
    def __init__(self):
        # Definisi warna untuk tema dark
        self.dark = {
            "bg": "#333333",
            "fg": "#FFFFFF",
            "entry_bg": "#555555",
            "entry_fg": "#FFFFFF",
            "button_bg": "#0000FF",
            "button_fg": "#FFFFFF",
            "button_hover_bg": "#00008B",
            "listbox_bg": "#555555",
            "listbox_fg": "#FFFFFF",
            "log_bg": "#555555",
            "log_fg": "#FFFFFF",
            "status_fg": "#FFFFFF",
        }

        # Definisi warna untuk tema light
        self.light = {
            "bg": "#F0F0F0",
            "fg": "#000000",
            "entry_bg": "#E0E0E0",
            "entry_fg": "#000000",
            "button_bg": "#0000FF",
            "button_fg": "#FFFFFF",
            "button_hover_bg": "#00008B",
            "listbox_bg": "#E0E0E0",
            "listbox_fg": "#000000",
            "log_bg": "#E0E0E0",
            "log_fg": "#000000",
            "status_fg": "#000000",
        }

        # Font
        self.title_font = ("Helvetica", 24, "bold")
        self.label_font = ("Helvetica", 12)
        self.button_font = ("Helvetica", 12, "bold")
        self.listbox_font = ("Helvetica", 10)

    def get_colors(self, theme):
        """Mengembalikan warna berdasarkan tema yang dipilih."""
        if theme == "dark":
            return self.dark
        else:
            return self.light
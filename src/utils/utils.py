from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)
LOG_FILE = "log.txt"

def log_message(message, color=Fore.WHITE, include_timestamp=True, log_callback=None):
    """Mencetak pesan ke terminal, menyimpannya ke log file, dan mengirimkan ke GUI jika ada callback."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}" if include_timestamp else message
    
    # Cetak ke terminal
    print(f"{color}{log_entry}")
    
    # Simpan ke file log
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")
    
    # Kirim ke GUI melalui callback jika ada
    if log_callback:
        log_callback(log_entry)
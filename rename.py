import pdfplumber
import re
import os
import shutil
import argparse
from datetime import datetime
from colorama import Fore, Style, init
import time

init(autoreset=True)

def welcome_message():
    print(Fore.MAGENTA + "==============================================")
    print(Fore.CYAN + "✨ Selamat Datang di PDF Renamer ✨")
    print(Fore.CYAN + "📜 Script by Syahbandi - PT BBN SURABAYA")
    print(Fore.MAGENTA + "==============================================")
    time.sleep(2)

def extract_info_from_pdf(pdf_path, debug=False):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    
    if debug:
        print(Fore.YELLOW + "========== RAW TEXT ==========")
        print(text)
        print(Fore.YELLOW + "==============================")

    # Ekstrak nama lawan transaksi
    partner_name_match = re.search(r'Pembeli Barang Kena Pajak\s*/\s*Penerima Jasa Kena Pajak:\s*Nama\s*:\s*(.+?)\s*Alamat', text)
    partner_name = partner_name_match.group(1).strip().title() if partner_name_match else "Nama tidak ditemukan"

    # Ekstrak tanggal
    date_match = re.search(r'(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})', text)
    if date_match:
        day, month, year = date_match.groups()
        month_dict = {
            "Januari": "01", "Februari": "02", "Maret": "03", "April": "04",
            "Mei": "05", "Juni": "06", "Juli": "07", "Agustus": "08",
            "September": "09", "Oktober": "10", "November": "11", "Desember": "12"
        }
        month = month_dict.get(month, "00")
        date = f"{day}-{month}-{year}"
    else:
        date = "Tanggal tidak ditemukan"

    # Ekstrak referensi dengan regex yang diperbarui
    reference_match = re.search(r'Referensi:\s*([^)]*)', text)
    if reference_match:
        ref = reference_match.group(1).strip()
        reference = ref if ref else None
    else:
        reference = None

    return partner_name, date, reference

def get_unique_filename(directory, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base} - {counter}{ext}"
        counter += 1
    return new_filename

def rename_pdf_files(input_directory, mode, debug=False):
    output_directory = os.path.join(input_directory, "RenamedPDFs")
    log_file = os.path.join(input_directory, "log.txt")
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    total_files = len([f for f in os.listdir(input_directory) if f.endswith('.pdf')])
    processed_files = 0
    error_files = 0
    
    with open(log_file, "w", encoding="utf-8") as log:
        log.write(f"Log proses pada {datetime.now()}\n")
        log.write("======================================\n")
    
    print(Fore.CYAN + "\n================= Proses Dimulai =================")
    print(f"Total file ditemukan: {total_files}\n")
    
    for filename in os.listdir(input_directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_directory, filename)
            try:
                partner_name, date, reference = extract_info_from_pdf(pdf_path, debug)
                
                # Bangun nama file berdasarkan mode
                parts = [partner_name, date]
                
                if mode == 'X':
                    if reference is not None:
                        parts.append(reference)
                elif mode == 'Y':
                    parts.append(reference if reference is not None else "Tidak Ada Referensi")
                elif mode == 'Z':
                    pass  # Abaikan referensi
                
                new_filename = " ".join(parts) + ".pdf"
                unique_filename = get_unique_filename(output_directory, new_filename)
                new_pdf_path = os.path.join(output_directory, unique_filename)
                
                shutil.copy(pdf_path, new_pdf_path)
                processed_files += 1
                print(Fore.GREEN + f"✔ Berhasil: {filename} -> {unique_filename}")
                with open(log_file, "a", encoding="utf-8") as log:
                    log.write(f"✔ {filename} -> {unique_filename}\n")
            except Exception as e:
                error_files += 1
                print(Fore.RED + f"✖ Error processing {filename}: {e}")
                with open(log_file, "a", encoding="utf-8") as log:
                    log.write(f"✖ Error {filename}: {e}\n")
    
    print(Fore.CYAN + "\n================= Proses Selesai =================")
    print(Fore.YELLOW + f"Total sampel: {total_files}")
    print(Fore.GREEN + f"Total diproses: {processed_files}")
    print(Fore.RED + f"Total error: {error_files}")

def main():
    welcome_message()
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Tampilkan teks mentah dari PDF")
    parser.add_argument("--mode", choices=['X', 'Y', 'Z'], default='Y',
                        help="Mode penanganan referensi: X (hanya jika ada), Y (tambahkan 'Tidak Ada Referensi' jika tidak ada), Z (abaikan referensi)")
    args = parser.parse_args()
    
    input_directory = input(Fore.BLUE + "Masukkan path direktori input: ")
    
    if not os.path.exists(input_directory):
        print(Fore.RED + f"Direktori '{input_directory}' tidak ditemukan.")
        return
    
    rename_pdf_files(input_directory, args.mode, args.debug)

if __name__ == "__main__":
    main()

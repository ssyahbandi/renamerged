import os
from src.utils.utils import log_message, Fore
from src.pdf.pdf_utils import validate_pdf, extract_info_from_pdf, generate_filename, copy_file_with_unique_name

# Debugging: Pastikan impor copy_file_with_unique_name berhasil
log_message("Debug: Impor copy_file_with_unique_name berhasil", Fore.CYAN)

def process_pdfs(input_directory, output_directory=None, progress_callback=None, log_callback=None, settings=None):
    """Memproses file PDF dengan mode Rename Saja."""
    if output_directory is None or output_directory.strip() == "":
        output_directory = os.path.join(input_directory, "ProcessedPDFs")  # Kembali ke ProcessedPDFs
    os.makedirs(output_directory, exist_ok=True)

    # Tahap 1: Perhitungan file PDF
    pdf_files = [f for f in os.listdir(input_directory) if f.endswith('.pdf')]
    total_files = len(pdf_files)
    log_message(f"Total file ditemukan: {total_files}", Fore.CYAN, log_callback=log_callback)

    # Inisialisasi variabel statistik
    processed_files = 0
    error_files = 0
    renamed_files = 0  # Jumlah file yang hanya diganti nama
    merged_files = 0   # Jumlah file yang diganti nama dan digabungkan (0 dalam mode ini)

    # Ambil urutan komponen dari pengaturan
    component_order = settings.get("component_order", None)

    # Proses setiap file secara independen
    for filename in pdf_files:
        pdf_path = os.path.join(input_directory, filename)
        if not validate_pdf(pdf_path):
            error_files += 1
            log_message(f"⚠️ File {filename} korup atau tidak valid, dilewati.", Fore.YELLOW, log_callback=log_callback)
            continue

        try:
            id_tku_seller, partner_name, faktur_number, date, reference = extract_info_from_pdf(pdf_path, log_callback)

            if partner_name == "Nama tidak ditemukan":
                log_message(f"⚠️ Nama tidak ditemukan di {filename}, dilewati.", Fore.YELLOW, log_callback=log_callback)
                continue

            # Buat folder berdasarkan ID TKU
            idtku_folder = os.path.join(output_directory, id_tku_seller)  # IDTKU Penjual di dalam ProcessedPDFs
            os.makedirs(idtku_folder, exist_ok=True)

            # Buat nama file berdasarkan pengaturan
            new_filename = generate_filename(partner_name, faktur_number, date, reference, settings, component_order)
            destination_path = os.path.join(idtku_folder, new_filename)

            # Salin file dengan nama unik
            renamed_files += copy_file_with_unique_name(pdf_path, destination_path, log_callback)

        except Exception as e:
            error_files += 1
            log_message(f"❌ Error membaca {filename}: {str(e)}", Fore.RED, log_callback=log_callback)

        processed_files += 1
        if progress_callback:
            progress_callback("reading", processed_files, total_files, 0, 0)

    # Hitung total file yang akan difinalisasi
    total_to_finalize = renamed_files  # Jumlah file yang berhasil diganti nama
    processed_files_for_finalizing = 0

    # Tahap 2: Finalisasi (simulasi pemindahan file)
    if progress_callback:
        progress_callback("finalizing", 0, total_files, 0, total_to_finalize)

    # Simulasi finalisasi untuk setiap file yang diganti nama
    for _ in range(total_to_finalize):
        processed_files_for_finalizing += 1
        if progress_callback:
            progress_callback("finalizing", processed_files_for_finalizing, total_files, 0, total_to_finalize)

    # Log hasil akhir
    log_message("\n📊 Hasil Akhir:", Fore.CYAN, log_callback=log_callback)
    log_message(f"📝 Total file diproses   : {total_files}", Fore.CYAN, log_callback=log_callback)
    log_message(f"📂 File yang hanya diganti nama: {renamed_files}", Fore.BLUE, log_callback=log_callback)
    log_message(f"✅ File yang diganti nama dan digabung: {merged_files}", Fore.GREEN, log_callback=log_callback)
    log_message(f"❌ Total error           : {error_files}\n", Fore.RED, log_callback=log_callback)
    log_message("✨ Selesai", Fore.GREEN, log_callback=log_callback)

    return total_files, renamed_files, merged_files, error_files
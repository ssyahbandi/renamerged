import os
import shutil
from src.utils.utils import log_message, Fore
from src.pdf.pdf_utils import validate_pdf, extract_info_from_pdf, merge_pdfs

# Debugging: Pastikan impor merge_pdfs berhasil
log_message("Debug: Impor merge_pdfs berhasil", Fore.CYAN)

def process_pdfs(input_directory, output_directory=None, progress_callback=None, log_callback=None, settings=None):
    """Memproses file PDF dengan mode Rename dan Merge."""
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
    renamed_files = 0  # Jumlah file yang hanya diganti nama (gagal digabungkan)
    merged_files = 0   # Jumlah file individual yang diganti nama dan digabungkan

    # Ambil urutan komponen dari pengaturan
    component_order = settings.get("component_order", None)

    # Kelompokkan file berdasarkan ID TKU
    files_by_idtku = {}
    for filename in pdf_files:
        pdf_path = os.path.join(input_directory, filename)
        if not validate_pdf(pdf_path):
            error_files += 1
            renamed_files += 1  # File yang korup dihitung sebagai "hanya diganti nama"
            log_message(f"⚠️ File {filename} korup atau tidak valid, dilewati.", Fore.YELLOW, log_callback=log_callback)
            continue

        try:
            id_tku_seller, partner_name, faktur_number, date, reference = extract_info_from_pdf(pdf_path, log_callback)

            if partner_name == "Nama tidak ditemukan":
                log_message(f"⚠️ Nama tidak ditemukan di {filename}, dilewati.", Fore.YELLOW, log_callback=log_callback)
                renamed_files += 1  # File yang tidak memiliki nama dihitung sebagai "hanya diganti nama"
                continue

            if id_tku_seller not in files_by_idtku:
                files_by_idtku[id_tku_seller] = []
            files_by_idtku[id_tku_seller].append((pdf_path, partner_name, faktur_number, date, reference))
        except Exception as e:
            error_files += 1
            renamed_files += 1  # File yang gagal diproses dihitung sebagai "hanya diganti nama"
            log_message(f"❌ Error membaca {filename}: {str(e)}", Fore.RED, log_callback=log_callback)

        processed_files += 1
        if progress_callback:
            progress_callback("reading", processed_files, total_files, 0, 0)

    # Hitung total file yang akan digabungkan
    total_to_merge = sum(len(files) for id_tku, files in files_by_idtku.items())
    total_to_finalize = total_to_merge  # Jumlah file yang akan difinalisasi sama dengan yang digabungkan
    processed_files_for_merging = 0
    processed_files_for_finalizing = 0

    # Tahap 2: Pemrosesan (merging)
    processed_files = 0
    total_to_process = len(files_by_idtku)
    for id_tku_seller, files in files_by_idtku.items():
        # Buat folder berdasarkan ID TKU
        idtku_folder = os.path.join(output_directory, id_tku_seller)
        os.makedirs(idtku_folder, exist_ok=True)

        # Kelompokkan file berdasarkan Nama Partner
        files_by_partner = {}
        for pdf_path, partner_name, faktur_number, date, reference in files:
            if partner_name not in files_by_partner:
                files_by_partner[partner_name] = []
            files_by_partner[partner_name].append((pdf_path, partner_name, faktur_number, date, reference))

        # Proses setiap file secara individual
        for partner_name, partner_files in files_by_partner.items():
            for file in partner_files:
                pdf_path, _, _, _, _ = file
                processed_files_for_merging += 1
                if progress_callback:
                    progress_callback("processing", processed_files_for_merging, total_files, total_to_merge, total_to_finalize)

            # Buat nama file output (hanya menggunakan Nama Partner)
            output_filename = f"{partner_name}.pdf"
            output_path = os.path.join(idtku_folder, output_filename)

            # Merge file PDF
            merged_files += len(partner_files)  # Hitung jumlah file individual yang digabungkan
            merge_pdfs([file[0] for file in partner_files], output_path, log_callback)

        processed_files += 1

    # Tahap 3: Finalisasi
    if progress_callback:
        progress_callback("finalizing", 0, total_files, total_to_merge, total_to_finalize)

    # Simulasi finalisasi untuk setiap file yang digabungkan
    for i in range(total_to_finalize):
        processed_files_for_finalizing += 1
        if progress_callback:
            progress_callback("finalizing", processed_files_for_finalizing, total_files, total_to_merge, total_to_finalize)

    # Log hasil akhir
    log_message("\n📊 Hasil Akhir:", Fore.CYAN, log_callback=log_callback)
    log_message(f"📝 Total file diproses   : {total_files}", Fore.CYAN, log_callback=log_callback)
    log_message(f"📂 File yang hanya diganti nama: {renamed_files}", Fore.BLUE, log_callback=log_callback)
    log_message(f"✅ File yang diganti nama dan digabung: {merged_files}", Fore.GREEN, log_callback=log_callback)
    log_message(f"❌ Total error           : {error_files}\n", Fore.RED, log_callback=log_callback)
    log_message("✨ Selesai", Fore.GREEN, log_callback=log_callback)

    return total_files, renamed_files, merged_files, error_files
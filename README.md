# Renamerged

Selamat datang di Renamerged! Aplikasi ini adalah solusi praktis untuk mengelola file PDF, terutama dokumen pajak atau transaksi bisnis yang menumpuk. Renamerged (singkatan dari Rename-Merged) dirancang untuk rename dan merge file PDF secara otomatis berdasarkan ID TKU Penjual dan Nama Lawan Transaksi. Dengan Renamerged, dokumen Anda akan terorganisir dengan rapi tanpa perlu kerja manual yang melelahkan.

Renamerged kini hadir dengan GUI modern yang lebih modular, intuitif, dan mendukung kustomisasi nama file. Berikut informasi lebih lanjut tentang apa yang dapat dilakukan Renamerged untuk Anda.

## Apa Itu Renamerged?

Renamerged adalah alat sederhana namun efisien untuk mengelola file PDF. Aplikasi ini sangat membantu ketika Anda memiliki ratusan PDF dengan ID TKU Penjual dan Nama Lawan Transaksi yang berbeda-beda. Renamerged dapat:  
- Rename File PDF Otomatis: Membaca isi PDF, mengambil ID TKU Penjual (22 digit) dan Nama Lawan Transaksi, lalu mengganti nama file PDF sesuai Nama Lawan Transaksi atau komponen lain yang Anda pilih.  
- Merge PDF yang Sama: Menggabungkan semua PDF dengan ID TKU Penjual dan Nama Lawan Transaksi yang sama menjadi satu file (opsi ini dapat dimatikan).  
- Organisasi File: Menyimpan hasil di folder `ProcessedPDFs` (atau folder pilihan Anda), terorganisir berdasarkan ID TKU Penjual, sehingga mudah dicari kapan saja.  

Aplikasi ini sangat cocok untuk Anda yang sering menangani dokumen pajak, transaksi bisnis, atau file PDF yang perlu dirapikan. Renamerged akan mempermudah pekerjaan Anda tanpa perlu proses manual.

## Fitur Unggulan

Renamerged dilengkapi dengan fitur-fitur berikut:  
- GUI Modern dan Modular: Antarmuka grafis yang intuitif dengan desain futuristik, tombol rounded, dan progress bar yang lebih profesional untuk memantau proses.  
- Pilih Mode Pemrosesan: Pilih antara "Rename Saja" (hanya rename tanpa merge) atau "Rename dan Merge" (rename + merge file yang sama).  
- Kustomisasi Nama File: Pada mode "Rename Saja", Anda dapat memilih komponen nama file (Nama Lawan Transaksi, Tanggal Faktur Pajak, Referensi, Nomor Faktur Pajak) untuk hasil yang lebih fleksibel.  
- Pratinjau File PDF: Lihat daftar file PDF yang akan diproses sebelum memulai, sehingga Anda dapat memastikan file yang tepat.  
- Organisasi File: Simpan hasil di folder `ProcessedPDFs` (atau folder pilihan Anda), terorganisir berdasarkan ID TKU Penjual.  
- Validasi File PDF: Aplikasi memeriksa apakah file PDF valid (tidak korup) sebelum diproses, mencegah error selama pemrosesan.  
- Kustomisasi Tema: Pilih tema dark atau light mode untuk pengalaman visual yang lebih nyaman.  
- Versi Executable: Tersedia `renamerged.exe` yang tinggal klik, tanpa perlu instal Python atau library apa pun. Cocok untuk pengguna awam.  
- Tombol Donasi: Dukung pengembangan proyek ini dengan donasi via tombol berwarna merah di GUI.

## Sistem Persyaratan

Untuk versi executable (`renamerged.exe`):  
- Sistem Operasi: Windows 10 atau lebih baru (versi macOS/Linux akan menyusul).  
- RAM: Minimal 2 GB.  
- Penyimpanan: Minimal 50 MB ruang kosong untuk aplikasi dan file log.  
- Catatan: Pastikan antivirus tidak memblokir `renamerged.exe` (lihat bagian "Catatan Penting").  

Untuk menjalankan source code:  
- Python: Versi 3.8 atau lebih baru.  
- Library: `pdfplumber`, `PyPDF2`, `colorama`, `customtkinter`.  
  Instal dengan:  ```pip install pdfplumber PyPDF2 colorama customtkinter```
  
## Download

Download versi terbaru Renamerged di [Releases](https://github.com/ssyahbandi/PDF_Renamer/releases). Atau langsung di [Sini](https://github.com/ssyahbandi/PDF_Renamer/releases/download/v2.0.0/renamerged.exe).

Ada dua pilihan untuk Anda:  
1. `renamerged.exe`: Versi executable dengan GUI, tinggal download dan jalankan. Tidak perlu instal Python atau library apa pun. Cocok untuk pengguna awam.  
2. Source Code: Clone repo ini jika Anda ingin melihat atau mengedit kode. Pastikan Python dan library berikut sudah terinstal:  ```pip install pdfplumber PyPDF2 colorama customtkinter```


## Cara Pakai

Menggunakan Renamerged sangat mudah berkat GUI-nya. Ikuti langkah berikut:  
1. Download `renamerged.exe` dari [Releases](https://github.com/ssyahbandi/PDF_Renamer/releases) atau langsung di [Sini](https://github.com/ssyahbandi/PDF_Renamer/releases/download/v2.0.0/renamerged.exe).  
2. Klik dua kali `renamerged.exe` untuk menjalankan aplikasi.  
    - Catatan: Jika muncul pop-up "Windows protected your PC", klik "More info" lalu pilih "Run anyway" untuk melanjutkan. Ini terjadi karena aplikasi belum ditandatangani secara resmi oleh Windows, tetapi sangat aman digunakan.  
3. Di jendela yang muncul:  
    - Pilih Mode Pemrosesan dari dropdown: "Rename Saja" (hanya rename) atau "Rename dan Merge" (rename + merge file yang sama).  
    - Jika memilih "Rename Saja", centang komponen nama file yang diinginkan (Nama Lawan Transaksi, Tanggal Faktur Pajak, Referensi, Nomor Faktur Pajak).  
    - Klik "Browse" di bagian "Pilih Folder Input PDF", lalu pilih folder tempat file PDF Anda disimpan (contoh: `C:/Dokumen/PDF`).  
    - Lihat pratinjau daftar file PDF yang terdeteksi di bawah "Daftar File PDF".  
    - (Opsional) Klik "Browse" untuk pilih folder output tempat hasil disimpan. Jika tidak dipilih, hasil akan disimpan di `ProcessedPDFs` di folder input.  
    - (Opsional) Klik "Ganti Tema" untuk beralih antara dark dan light mode sesuai preferensi visual Anda.  
4. Klik tombol "Proses" untuk memulai. Progress bar akan menunjukkan kemajuan proses.  
5. Tunggu hingga proses selesai. Renamerged akan:  
    - Memvalidasi file PDF untuk memastikan tidak ada file korup.  
    - Rename file PDF berdasarkan komponen yang dipilih (jika mode "Rename Saja") atau Nama Lawan Transaksi (jika mode "Rename dan Merge").  
    - Merge file PDF dengan ID TKU Penjual dan Nama Lawan Transaksi yang sama (jika mode "Rename dan Merge").  
    - Menyimpan hasil di folder yang terorganisir berdasarkan ID TKU Penjual.  
6. Selesai! Klik "Buka Folder Hasil" untuk melihat hasilnya. Semua PDF Anda sudah rapi terorganisir.

## Contoh Penggunaan

Berikut adalah contoh cara kerja Renamerged:  
Misalnya Anda punya 3 file PDF di folder:  
- `dokumen1.pdf`: ID TKU = `1234567890123456789012`, Nama Lawan Transaksi = `PT ABC`, Nomor Faktur = `123456`, Tanggal = `01-01-2025`.  
- `dokumen2.pdf`: ID TKU = `1234567890123456789012`, Nama Lawan Transaksi = `PT ABC`, Nomor Faktur = `123457`, Tanggal = `02-01-2025`.  
- `dokumen3.pdf`: ID TKU = `9876543210987654321098`, Nama Lawan Transaksi = `PT XYZ`, Nomor Faktur = `123458`, Tanggal = `03-01-2025`.  

### Mode "Rename dan Merge"
Setelah menjalankan Renamerged:  
- `dokumen1.pdf` dan `dokumen2.pdf` digabung menjadi `PT ABC.pdf`, disimpan di `ProcessedPDFs/1234567890123456789012/PT ABC.pdf`.  
- `dokumen3.pdf` di-rename menjadi `PT XYZ.pdf`, disimpan di `ProcessedPDFs/9876543210987654321098/PT XYZ.pdf`.  

### Mode "Rename Saja"
Jika hanya "Nama Lawan Transaksi" dan "Nomor Faktur Pajak" dicentang:  
- `dokumen1.pdf` di-rename menjadi `PT ABC - 123456.pdf`, disimpan di `ProcessedPDFs/1234567890123456789012/PT ABC - 123456.pdf`.  
- `dokumen2.pdf` di-rename menjadi `PT ABC - 123457.pdf`, disimpan di `ProcessedPDFs/1234567890123456789012/PT ABC - 123457.pdf`.  
- `dokumen3.pdf` di-rename menjadi `PT XYZ - 123458.pdf`, disimpan di `ProcessedPDFs/9876543210987654321098/PT XYZ - 123458.pdf`.  

## Catatan Penting

Sebelum menggunakan Renamerged, perhatikan hal berikut:  
- Keamanan File: File ini 100% aman dan bebas virus. Namun, karena dibuat menggunakan PyInstaller, beberapa antivirus (seperti Windows Defender) mungkin mendeteksi sebagai "false positive". Tambahkan ke exclusion:  
- Windows Defender: Settings > Virus & Threat Protection > Manage Settings > Add or Remove Exclusions > Tambah renamerged.exe.  
- Kendala: Jika ada masalah saat menggunakan Renamerged, hubungi saya di [Telegram](https://t.me/ssyahbandi). Saya siap membantu kapan saja.

## Donasi

Membuat Renamerged membutuhkan waktu dan usaha, dari coding hingga testing agar aplikasi ini benar-benar berguna untuk Anda. Jika Anda merasa Renamerged membantu, dukung saya dengan donasi via tombol merah "Donasi" di aplikasi, atau langsung ke link ini: [Donasi via QRIS](https://bit.ly/kiyuris). Donasi Anda akan membantu saya terus mengembangkan proyek ini, mungkin menambah fitur baru yang lebih keren lagi. Terima kasih banyak.

## Kontribusi dan Feedback

Saya sangat terbuka untuk masukan. Jika Anda punya ide fitur baru (misalnya, sortir PDF berdasarkan tanggal) atau menemukan bug, hubungi saya via [Telegram](https://t.me/ssyahbandi). Anda juga bisa membuka issue di repo ini, saya akan merespons secepat mungkin.

## Changelog

### Versi 2.0.1 (14/04/2025)
- GUI: Sekarang ukuran jendela utama menjadi 1000x850 untuk memberikan tampilan yang lebih ringkas dan proporsional
- GUI: Lebar CTkProgressBar disesuaikan dari 500 menjadi 350 untuk menyesuaikan dengan ukuran jendela yang baru (progress_bar.py).
- GUI: Ditambahkan jeda waktu time.sleep(0.05) di progress_callback untuk memperlambat pembaruan visual progress bar agar lebih halus (process_button.py).
- GUI: Pembaruan progress di tahap "processing" dan "finalizing" dilakukan per file individual untuk langkah yang lebih kecil (pdf_processor.py, pdf_processor_rename.py).
- GUI: Menambahkan log debugging di progress_callback untuk mencatat nilai progress di setiap tahap (process_button.py).

### Versi 2.0.0 (11/04/2025)
- Fitur Baru: Sekarang bisa memilih antara "Rename Saja" (tanpa merge) atau "Rename dan Merge".  
- Fitur Baru: Menambahkan fitur kustomisasi komponen nama file untuk mode "Rename Saja" (Nama Lawan Transaksi, Tanggal Faktur Pajak, Referensi, Nomor Faktur Pajak).  
- GUI: Tampilan baru yang lebih modular dengan komponen terpisah.  
- GUI: Membuat teks statistik lebih rapat untuk memberikan lebih banyak ruang pada preview file PDF.  
- GUI: Memperkecil ukuran kotak checkbox dan menyeragamkan font teks checkbox dengan elemen lain.  
- GUI: Memperpanjang progress bar untuk tampilan yang lebih profesional.  
- GUI: Memperbaiki warna teks persentase progress bar di mode light agar lebih terlihat.  
- GUI: Mengubah warna tombol "Donasi" menjadi merah untuk menarik perhatian.  
- Bug Fixing: Memperbaiki bug persentase progress bar yang samar saat di mode light.  
- File: GUI sekarang lebih modular dengan komponen terpisah untuk setiap bagian.

### Versi 1.2.0 (10/04/2025)
- GUI: Fix Bugs

### Versi 1.1.0 (10/04/2025)
- GUI Modern: Ditambahkan antarmuka grafis dengan progress bar untuk memantau proses.  
- Pratinjau File PDF: Menampilkan daftar file PDF yang terdeteksi sebelum diproses.  
- Validasi File PDF: Memeriksa apakah file PDF valid (tidak korup) sebelum diproses.  
- Kustomisasi Tema: Menambahkan opsi untuk beralih antara dark dan light mode.  
- Penghapusan Log Proses di GUI: Log proses di GUI dihapus untuk menyederhanakan tampilan, tetapi tetap disimpan di file log.txt.  
- Penjajaran Tombol: Tombol "Donasi" dan "Ganti Tema" disusun rapi di sisi kanan atas, sejajar dengan tombol "Browse".

### Versi 1.0.0 (09/04/2025)
- Initial Release  
- GUI Based

## Terima Kasih

Terima kasih telah mencoba Renamerged. Semoga aplikasi ini membuat pekerjaan Anda lebih mudah dan dokumen Anda lebih rapi. Jangan lupa share ke teman-teman yang membutuhkan. Saya harap Renamerged bisa menjadi alat yang berguna untuk urusan PDF Anda.

## 🎁BONUS🎁

Aku ketika ngoding dan ga ada BUG bee like :

![image](https://github.com/user-attachments/assets/8c819a28-52f1-4503-9469-e81e467ad619)

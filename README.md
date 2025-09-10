Nama    : Haris Azzahra Lunaaya
NPM     : 2406425930
Kela    : PBP A
Link PWS: https://haris-azzahra-footballshop.pbp.cs.ui.ac.id/


1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a. membuat repository pada github dan membuat proyek baru di PWS
    b. inisiasi proyek django dengan membuat direktori baru
    c. meng-konfigurasikan proyek dengan environment
    d. membuat app django baru bernama main
    e. mengimplementasikan template dan model dengan membuat file main.html dan mengisi file models.py dengan atribut-atribut yang telah ditentukan
    f. mengaplikasikan migrasi model agar django melacak perubahan pada model
    g. mengintegrasikan MVT dengan mengisi file views.py dan return render agar template main.html dapat ditampilkan
    h. meng-konfigurasikann routing url dan melakukan deployment agar app main dapat dilihat menggunakan link PWS


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    image link: https://miro.medium.com/v2/resize:fit:640/format:webp/1*K-o5Vn65A7PJZTSrlsm2rQ.jpeg

    saat client memasukkan suatu tautan pada browser, browser mengirim request ke django. Pada urls.py, django mengecek url mana yang dipanggil dan mengarahkan request terserbut ke fungsi yang sesuai di views.py. Pada views.py, logika program ditangani yang database-nya diambil dari models.py dan views.py juga yang me-render data untuk ditampilkan melalui berkas-berkas html pada template. Hasil tersebut lah yang dikembalikan ke browser sebagai response untuk ditampilkan.


3. Jelaskan peran settings.py dalam proyek Django!
    settings.py berisi semua konfigurasi dari proyek django. Settings menyimpan informasi penting, seperti koneksi database, allowed hosts (daftar domain yang boleh diakses), installed apps (daftar aplikasi django atau third-party yang dipakai di proyek), dan lain-lain.

    referensi: https://docs.djangoproject.com/en/5.2/topics/settings/

    
4. Bagaimana cara kerja migrasi database di Django?
    setelah membuat models.py, lalu menjalankan makemigrations, django akan menge-scan dan membandingkan versi yang saat ini terdapat di dalam file migration. Setelah itu, django akan membuat file 0001_initial.py di folder migrations yang berisi instruksi python yang setara dengan SQL. Setelah dijalankan command migrate, file migrasi akan dieksekusi ke database.

    referensi: https://docs.djangoproject.com/en/5.2/topics/migrations/#workflow
    
    
5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Django dijadikan permulaan, yang pertama karena menggunakan bahasa pemrogramana yang mudah dan ngetren digunakan oleh pemula, yaitu python. Yang kedua, django adalah framework yang sudah menyediakan banyak libraries dan tools untuk kebutuhan-kebutuhan umum sehingga tidak perlu membuat semuanya dari awal yang mendukung DRY (Don't Repeat Yourself) principle. Selain itu django juga open source serta memiliki community support yang besar dan dokumentasi yang baik.

    referensi: https://www.geeksforgeeks.org/blogs/top-10-reasons-to-choose-django-framework-for-your-project/
    
    
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    tidak ada, thank you kakak-kakak asdos untuk tutorialnya.

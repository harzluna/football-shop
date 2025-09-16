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



// TUGAS 3 //

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Data delivery penting dilakukan untuk mengirimkan data dari satu sistem ke sistem yang lain. Data delivery memastikan kita mendapatkan infromasi yang tepat di waktu yang tepat karena data yang akurat adalah bahan baku untuk membuat keputusan yang tepat. Data delivery juga dapat mendeteksi error sehingga dapat mencegah adanya permasalahan yang disebabkan oleh terlambatnya penanganan error. 

    referensi: https://www.fanruan.com/en/glossary/big-data/data-delivery
   

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    JSON lebih populer karena JSON memiliki ukuran file yang lebih kecil, sekitar 24.7% lebih kecil, daripada XML sehingga JSON bekerja lebih cepat untuk transmisi data. Namun, XML lebh baik untuk mengirimkan struktur data yang lebih kompleks dan diverse. Berdasarkan peneitian yang dilakukan oleh Gerrans dan Sherratt, men-deserializing JSON memakan lebih sedikit waktu, lebih sedikit penggunaan RAM, dan memakan lebih sedikit power consumption; sedangkan XML mengambil lebih sedikit flash memory. Kesimpulannya, dalam segi hardware, XML lebih baik untuk sistem yang lebih memerlukan memory flash daripada power, waktu, ataupun penggunaan RAM; dan JSON lebih baik digunakan untuk embedded system yang bekerja secara independen untuk waktu yang lebih lama, mengambil lebih banyak data, atau sistem yang memprioritaskan komunikasi yang cepat antar-sistem.

    referensi: J. Gerrans and R. S. Sherratt, "Comparing XML and JSON Characteristics as Formats for Data Serialization Within Ultralow Power Embedded Systems," in IEEE Embedded Systems Letters, vol. 16, no. 4, pp. 489-492, Dec. 2024, doi: 10.1109/LES.2024.3450576.


3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Method is_valid() digunakan untuk binding data yang masuk ke form dan mem-validasi data, seperti field yang sesuai, tipe data sesuai, atau panjang teks memenuhi. is_valid() digunakan agar request.POST tidak langsung dimasukkan ke database, tetapi dipastikan dulu datanya aman dan sesuai aturan; dan mudah untuk menangani form yang tidak valid dan dapat menimbulkan error.


4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    crsf_token dibutuhkan untuk memproteksi web dari serangan ketika website mengandung link, tombol, atau yang lain yang tujuannya untuk melakukan suatu tindakan pada server kita menggunakan kredensial user yang mengunjungi website berbahaya di browsernya. Jika tidak menambahkan csrf_token di django, server kita akan rentan terkena serangan CSRF (Cross-Site Request Forgery), pemalsuan request seolah-olah penyerang adalah user, yang tak diketahui. Serangan-serangan itu dapat dimanfaatkan oleh penyerang untuk mencuri data atau kredensial milik user yang nantinya dapat digunakan untuk keperluan yang tidak baik atau bahkan pencurian.

    referensi: https://docs.djangoproject.com/en/5.2/ref/csrf/


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a. menambahkan 4 fungsi baru, yaitu: show_xml, show_json, show_xml_by_id, dan show_json_by_id pada file views.py
    b. lalu menambahkan routing url masing-masing pada file urls.py yang berada di folder main.
    c. menambahkan 2 fungsi baru: add_product dan show_description pada views.py dan menambahkan juga routingnya di urls.py pada folder main.
    d. membuat file html pada folder templates di root folder untuk base.html
    e. lalu membuat 2 file html baru yang akan menampilkan add_product dan show_description pada aplikasi main
    f. membuat file form.py untuk menambahkan request objek, yaitu untuk add_product
    g. memperbarui migrations yang sebelumnya belum memakai uuid agar dapat melakukan data delivery dengan lebih mudah
    h. add, commit, dan push pada github dan pws.


6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    tutorial sudah cukup baik dan jelas. thanks kakak-kakak asdos.


7. Link foto screenshot Postman: https://drive.google.com/drive/folders/1mkgKC75KLRqc849uS-4WRVzksAne5Oc-?usp=drive_link
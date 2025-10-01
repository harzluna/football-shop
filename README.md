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




// TUGAS 4 //

1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    AuthenticationForm adalah form bawaan Django yang dipakai untuk login user. Form ini berasal dari django.contrib.auth.forms dan sudah terintegrasi langsung dengan sistem autentikasi Django. Kelebihnnya adalah ketika kita ingin membuat halaman login, cukup pakai AuthenticationForm, Django sudah menyiapkan field dan validasinya tanpa perlu membuat program dari awal sehingga bisa langsung dipakai di template HTML tanpa banyak konfigurasi. Kekurangannya hanya terbatas pada login yang menggunkan username dan password, jika ingin memakai akun email harus override dan malah akan rumit lagi jika menggunakan keamanan yang lebih ketat seperti 2FA/MFA dan OTP.

    referensi:  https://docs.djangoproject.com/en/5.2/topics/auth/default/#authentication-forms


2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    Autentikasi adalah proses meng-konfirmasi identitas user, sedangkan otorisasi adalah proses memberikan user permission pada akses informasi seperti data, dokumen, dll. Autentikasi muncul lebih dulu untuk memvalidasi identitas user yang kemudian dengan otorisasi akan diberikan akses pada informasi-informasi user jika user teridentifikasi. Django menerapkan kedua konsep tersebut dengan "Django auth", yaitu fitur buit-in Django. Autentikasi Django adalah fitur login user yang mencocokkan username dengan password yang telah diregister dan tersimpan dalam bentuk hash, sedangkan sistem otorisasi Django berupa menghubungkan user dengan model yang nantinya akan dipersonalisasi sehingga beberapa infromasi hanya dapat diakses oleh user yang diberikan permission.

    referensi: https://www.fortinet.com/resources/cyberglossary/authentication-vs-authorization, 


3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    Kelebihan cookies: meningkatkan personalisasi, login yan persisten (user tidak perlu login setiap kali membuka web), data management yang ringan karena tidak memakan resource server
    Kekurangan cookies: keamanan yang kurang karena cookies disimpan di client-side atau browser, terbatas pada ukuran data yang kecil, lebih rentan pada serangan siber, pencurian, dan manipulasi data yang diakibatkan oleh unauthorized user.
    Kelebihan session: temporal dan otomatis terhapus ketika user menutup browser atau log out, session menyimpan data pada server sehigga mengurangi risiko manipulasi client-side access, session dapat menyimpan data yang lebih banyak dan beragam (termasuk preferensi user, kredensial login, dan bvariabel session)
    Kekurangan Session: kapasitas penyimpan yang terbatas, penyimpanan pada server yang dapat meningkatkan server load dan biaya pemeliharaan.

    referensi: https://pandectes.io/blog/understanding-the-difference-between-cookies-and-sessions/


4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    Cookies dapat menimbulkan risiko keamanan, terutama pada cookies yang mempunyai informasi yang sensitif. jika cookies yang menyimpan kredensial login dimanipulasi, user yang tidak ter-autentikasi dapat mengakses data atau informasi user. Django mengatasi risiko serangan tersebut dengan menyediakan csrf_token untuk render hidden field beserta token yang telah di-generate secara otomatis

    referensi: https://pandectes.io/blog/understanding-the-difference-between-cookies-and-sessions/, https://madey.medium.com/common-website-security-attacks-dan-cara-mencegahnya-menggunakan-django-framework-bahasa-12729a3251a5


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a. menambahkan pada views.py beberapa import sepeerti UserCreationForm, AuthenticationForm, authenticate, login, dan logout
    b. menambahkan fungsi register, login_user, dan logout_user pada file views.py
    c. membuat file HTML register.html yang akan menampilkan halaman untuk daftar akun dan login.html yang akan menampilkan halaman login
    d. menambahkan login_required untuk merestriksi sehingga halaman main hanya dapat diakses setelah melakukan login
    e. menghubungkan model Product dengan user dengan mengimport user dan menambahkan potongan kode user pada file models.py; lalu melakukan makemigrations dan migrate model yang baru ditambahkan. memodifikasi fungsi add_product dan show_main di file views.py. Lalu menambahkan fitur atau tombol filter pada tampilan halaman depa dengan memodifikasi file template main.html dan show_description.html agar dapat menampilkan user yang menjual produk.
    f. Memodifikasi file views.py dengan import HttpResponseRedirest, reverse, dan datetime; lalu mengubah beberapa baris kode pada fungsi login_user, tepatnya pada if form.is_valid(). Selanjutnya pada fungsi show_main, juga menambahkan kode last_login pada dictionary context.
    g. mengubah funggsi logout_user pada views.py agar dapat menghapus cookie last_login setelah melakukan logout dan menambahkan potongan kode yang akan menampilkan data sesi terakhir login pada template main.html
    h. melakukan git add, commit, dan push pada github dan pws




// TUGAS 5 //

1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    a. !important: Meskipun ini bukan bagian dari specificity secara teknis, menambahkan !important pada aturan CSS akan mengesampingkan semua aturan lain kecuali inline styles yang juga menggunakan !important
    b. Inline Styles — Style yang langsung diberikan pada atribut style dalam elemen HTML, misalnya <h1 style="color: red;">. Ini memiliki nilai specificity tertinggi
    c. ID Selector — Selector yang menggunakan ID, seperti #header.
    d. Class, Pseudo-class, dan Attribute Selector — Selector seperti .container, :hover, atau [type="text"].
    e. Element dan Pseudo-element Selector — Selector berbasis elemen seperti div, p, atau pseudo-elemen seperti ::before.
    f. Universal Selector — Selector universal * memiliki prioritas paling rendah.

    referensi: https://www.easycoding.id/blog/urutan-prioritas-selector-css-specificity-panduan-lengkap-untuk-memahami-dan-menggunakan

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
    Responsive design sangat penting dalam pengembangan aplikasi web karena memastikan bahwa aplikasi atau situs web dapat diakses dan digunakan secara optimal di berbagai perangkat dengan ukuran layar yang berbeda, seperti desktop, tablet, dan smartphone. Dengan responsive design, tampilan dan fungsi aplikasi menyesuaikan secara otomatis, memberikan pengalaman pengguna yang nyaman dan konsisten tanpa harus membuat versi terpisah untuk setiap perangkat.
    Aplikasi yang sudah menerapkan responsive design: Bootstrap, Tailwind
    Yang belum: situs web lama yang hanya didesain untuk desktop
    jika tidak menggunakan responsive web design, aplikasi web akan mengalami berbagai masalah seperti penurunan kualitas pengalaman pengguna, terutama dari pengguna mobile, dan kesulitan dalam pemeliharaan dan pengembangan di masa depan.


3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
    Margin adalah ruang kosong di luar border elemen. Margin mengatur jarak antara elemen satu dengan elemen lain di sekitarnya. Margin bersifat eksternal dan tidak mempengaruhi ukuran konten atau border elemen.
    Border adalah garis tepi atau bingkai yang mengelilingi elemen, tepat di antara padding dan margin. Border memiliki lebar, gaya (seperti solid, dashed), dan warna yang bisa diatur.
    Padding adalah ruang di dalam border elemen yang memisahkan konten elemen dari border tersebut. Padding bersifat internal dan menambah ruang di sekitar konten, sehingga bisa memperbesar ukuran total elemen.

    cara implementasi:
    a. menentukan elemen yang akan diberi margin, padding, atau border
    b. buka berkas CSS
    c. tuliskan selector untuk elemen tersebut
    d. tentukan properti margin, border, dan padding yang ingin digunakan, lalu simpan


4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
    Flexbox (Flexible Box) adalah sistem layout satu dimensi yang berfokus pada pengaturan elemen dalam satu baris (row) atau satu kolom (column). Flexbox memudahkan penyelarasan, distribusi ruang, dan pengaturan ukuran elemen dalam container yang fleksibel. Konsep utama flexbox adalah penggunaan dua sumbu: sumbu utama (main axis) yang merupakan arah pengaturan elemen (horizontal atau vertikal)dan sumbu silang (cross axis) yang tegak lurus terhadap sumbu utama.
    Grid layout adalah sistem layout dua dimensi yang memungkinkan pengaturan elemen secara baris dan kolom sekaligus. Dengan grid, desain layout menjadi lebih terstruktur dan mudah mengontrol posisi dan ukuran setiap elemen secara presisi. Kita menggunakan properti seperti grid-template-columns, grid-template-rows, dan gap untuk mengatur grid. Grid cocok digunakan untuk membuat layout kompleks seperti tata letak halaman web secara keseluruhan yang terdiri dari beberapa bagian berbeda dalam baris dan kolom.

    Kegunaan Flexbox dan Grid:
    - Flexbox digunakan untuk mengelola item dalam satu dimensi, sangat baik untuk navbar, daftar horizontal atau vertikal, tombol yang perlu disejajarkan dan didistribusikan secara fleksibel.
    - Grid digunakan untuk layout dua dimensi, seperti struktur halaman utama, pengaturan foto dalam kolom dan baris, dan tata letak dashboard yang kompleks.
    - Keduanya sering digunakan bersamaan: grid mengatur layout utama, sedangkan flexbox mengelola elemen-elemen di dalam grid untuk fleksibilitas tambahan.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    a. 
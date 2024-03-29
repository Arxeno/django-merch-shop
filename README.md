**Link website**: https://rukomerch88.adaptable.app/

# TUGAS 2

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

Jawaban:

- Pertama-tama saya memulai project Django menggunakan `django-admin startproject inventory_merch`.
- Membuat virtual environment bernama env.
- Lalu saya mengubah konfigurasi db saya menggunakan postgresql. Saya menginstall psycopg2-binary untuk mendukung penggunaan database PostgreSQL.
- Membuat django app bernama "main".
- Membuat models Item (dan model tambahan saya sendiri bernama Category) di `models.py`.
- Membuat url dan template `index.html`.
- Membuat desain card merch yang akan mengakses data dari Item lewat `views.py`.

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jawaban: Untuk penjelasan bagan dapat diakses di link [FigJam](https://www.figma.com/file/kJ66qnnWO3iNRDp56QetQw/Diagram-Tugas-2-PBP?type=whiteboard&node-id=0%3A1&t=ZFTsJmHFOS2rQuyV-1) berikut atau dapat dilihat dibawah ini.

![Bagan Project Django inventory_merch](/Diagram%20Tugas%202%20PBP.png)

## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Jawaban: Virtual environment sebenarnya adalah opsional. Program Django kita dapat berjalan tanpa error walaupun kita tidak menggunakan Virtual Environment sama sekali. Namun, itu berarti kita menggunakan python global interpreter dalam menjalankan Django kita. Permasalahannya terdapat di proses membuat `requirements.txt` dan proses deploy. Karena ketika kita melakukan `pip freeze > requirements.txt` dan kita tidak menggunakan virtual environment, `pip` akan menyimpan semua package-package yang tidak berikatan sama sekali dengan project django yang kita gunakan sehingga hal tersebut hanya membuang-buang waktu proses deploy saja.

## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

Jawaban:

### MVC

MVC atau Model-View-Controller adalah _design pattern_ yang membagi aplikasi menjadi 3 bagian utama, yaitu:

- **Model**: Menyimpan segala logic terkait manipulasi data model di database.
- **View**: Menyimpan komponen-komponen UI yang akan ditampilkan.
- **Controller**: Menjadi penengah antara View dan Model. Disini juga perilaku apa yang akan dilakukan jika client mengakses endpoint tertentu.

Fitur-fitur yang ditawarkan MVC:

- Memisahkan business logic, UI logic, dan input logic lebih jelas.
- Menyediakan full control terhadap HTML dan URLs sehingga dapat lebih mudah dalam mendesain web application architecture
- Mensupport Test Driven Development (TDD)

### MVT

MVT adalah singkatan dari (Model-View-Template). Berikut adalah penjelasan dari setiap komponen dalam MVT:

- **Model**: Bagian pembuatan Schema/Model database kita.
- **View**: Untuk menerima request dari client dan melakukan suatu logic yang kemudian akan dikirimkan sebagai response kepada client.
- **Template**: Terdiri dari file-file static yang akan dikirimkan sebagai response kepada client.

### MVVM

MVVM atau Model-View-Viewmodel adalah design architecture yang biasa digunakan dalam Android Development. Berikut adalah penjelasan lebih lanjut mengenai ketiga komponen diatas:

- **Model**: Berperan dalam manipulasi dan pembuatan model database.
- **View**: Berperan sebagai konfigurasi User Interface.
- **Viewmodel**: Berperan sebagai penghubung antara View dan Model.

# TUGAS 3

## Apa perbedaan antara form POST dan form GET dalam Django?

POST dan GET adalah salah dua method-method HTTP request dalam dunia web. Method GET berfungsi untuk memberitahu server bahwa klien ingin mendapatkan data dari suatu endpoint di server tersebut. GET tidak bisa mengirimkan request body, namun POST tidak bisa mengirimkan request body. POST berfungsi untuk meminta server untuk menerima data request body dari klien dan membuat & menyimpan suatu data dari request body tersebut.

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

XML adalah bahasa markup, mirip seperti HTML, namun tag-tag yang digunakan bukan tag dari HTML namun kolom data yang digunakan. Contoh: data "kota" yang isinya "Bandung" akan tertulis seperti ini `<kota>Bandung</kota>`.

JSON adalah singkatan dari Javascript Object Notation yang merupakan jenis struktur pertukaran data (seperti XML), namun struktur yang digunakan adalah object.

HTML adalah singkatan dari Hypertext Markup Language yang bukan merupakan static file yang tidak digunakan untuk pertukaran data. Ia digunakan untuk menampilkan data-data secara visual.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON lebih sering digunakan ketimbang XML dalam pertukaran data adalah karena pertama, JSON lebih mudah dibaca ketimbang XML karena ia tidak menggunakan tag open dan tag close, melainkan menggunakan skema "key" dan "value" yang membuatnya lebih terasa simple ketimbang XML. Selain itu, karena hampir semua _web app_ menggunakan bahasa Javascript, maka JSON semakin populer digunakan karena sangat cocok dengan environment Javascript.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- membuat file forms.py
- Membuat ModelForm untuk model Item
- Membuat fungsi views untuk menghandle request GET dan POST untuk form Item
- Membuat halaman sukses membuat item
- Membuat tombol `Add Item` di halaman home (`index.html`)
- Mengubah response `HttpResponse('Success!')` dengan `render(request, 'success.html')`
- Membuat url untuk GET XML data
- Menguji endpoint `item/xml`
- Membuat endpoint GET XML data by ID
- Menguji endpoint `item/xml/:id`
- Membuat url untuk GET JSON data
- Menguji endpoint `item/json`
- Membuat endpoint GET JSON data by ID
- Menguji endpoint `item/json/:id`
- Menambahkan bonus: jumlah items di RukoMerch di file `index.html`

Endpoint HTML: /
![SS HTML](/HTML.png)

Endpoint XML: /item/xml
![SS XML](/XML.png)

Endpoint XML by ID: /item/xml/:id
![SS XML by ID](/XML%20by%20ID.png)

Endpoint JSON: /item/json
![SS JSON](/JSON.png)

Endpoint JSON by ID: /item/json/:id
![SS JSON by ID](/JSON%20by%20ID.png)

# TUGAS 4

## Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?

UserCreationForm adalah sebuah kelas dalam django dimana mempermudah para web developer dalam membuat user. Kelebihan dari menggunakan UserCreationForm adalah semua logic autentikasi seperti penggunaan hasing password, pemeriksaan kesediaan user berdasarkan input login dari pengguna dan lain sebagainya sehingga kita sebagai developer tidak perlu membuat fitur autentikasi dari awal. Tapi dengan kelebihan tersebut, yakni 'sudah disiapkan dari django'-nya, terdapat kekurangan dimana apabila kita menginginkan untuk menambah field di login atau registrasi, maka kita tidak bisa menggunakan Django sehingga harus membuat sistem autentikasi secara manual.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

_Authentication_ itu seperti di tahap login, register, dan logout. Sedangkan _Authorization_ itu seperti ketika kita ingin mengakses halaman beranda dari Django app yang menggunakan `@login_required(login_url='[url login]')`, maka disitu Django akan memeriksa apakah client yang merequest tersebut memiliki otorisasi dalam mengakses halaman beranda. Jika iya, maka Django akan mengarahkan user ke halaman beranda. Jika tidak, maka Django akan melakukan sesuatu seperti mengarahkan ke laman login.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah mekanisme untuk menyimpan suatu data dari sisi klien, mirip seperti _Local Storage_ dan _Session Storage_. Bedanya jika Local Storage dan Session Storage disimpan dan diakses menggunakan Web Storage API, Cookies tidak menggunakan Web Storage API dalam menyimpan suatu data, walaupun sama-sama disimpan di sisi klien.

Cara menerapkan cookies di django adalah membuat perintah untuk menyimpan cookies ketika user login.
Contoh: `response.set_cookie('[sebuah key]', [sebuah nilai])`

Kemudian kita dapat mengakses cookie seperti berikut:
Contoh: `request.COOKIES['[sebuah key]']`

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Secara default cookie tidak aman dibandingkan dengan local storage atau session storage. Karena para peretas dapat mengeksploitasi nya menggunakan CSRF sehingga dapat mengakses akun pengguna di web tersebut. Untuk mencegah risiko tersebut, kita dapat menggunakan CSRF token sehingga ketika server menerima request, maka server akan memeriksa terlebih dahulu apakah csrf token yang digunakan valid atau tidak.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Pertama saya membuat fitur register user, membuat fungsi view nya dan menambahkan url endpoint untuk view register. Setelah itu saya menerapkan fungsi view login beserta url endpoint-nya. Setelah login dan register selesai, maka saya mulai membuat view untuk fitur logout. Setelah fungsi autentikasi secara keseluruhan sudah bisa bekerja (tanpa cookie), saya mulai mencoba menerapkan cookie agar user tidak perlu login setiap kali mengunjungi website.

# TUGAS 5

## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

1. Universal Selector => Berfungsi untuk memberi styling kepada semua elemen (tanpa terkecuali). Digunakan ketika kita ingin styling semua elemen yg ada di file html agar memiliki styling yg seragam.

2. Type Selector (Element Selector) => Berfungsi untuk memberi styling kepada tag elemen yg sama. Digunakan ketika kita ingin styling semua tag tersebut agar memiliki style yg seragam.

3. ID Selector (`#id`) => Berfungsi untuk memberi styling kepada elemen html yg memiliki id tersebut. Digunakan ketika kita ingin styling tag unik, yang hanya berlaku pada satu elemen

4. Class Selector (`.class`) => Berfungsi untuk memberi styling kepada elemen html yg memiliki class tersebut. Digunakan ketika kita tidak ingin styling untuk elemen tertentu, melainkan yg memiliki atribut kelas yg kita berikan di dalam html tersebut.

5. Attribute Selector (`[attribute]`, `[attribute=value]`) => Berfungsi untuk memberi styling kepada elemen yang memiliki atribut html tersebut. Digunakan ketika kita ingin memberikan styling kepada elemen yg memiliki atribut html tersebut.

6. Pseudo-Class Selector (`:pseudo-class`) => Berfungsi untuk memberi styling kepada elemen yang berlaku ketika pseudoclass tersebut seperti `:hover`. Digunakan ketika kita ingin memberikan styling ketika suatu event terjadi.

7. Pseudo-Element Selector (`::pseudo-element`) => Berfungsi untuk memberi styling untuk semi element dari suatu html element seperti `::after` dan `::before`. Digunakan ketika kita ingin membuat suatu elemen tanpa membuat elemen di html dengan menggunakan pseudo-element atau semi element ini.

## Jelaskan HTML5 Tag yang kamu ketahui.

1. `<!DOCTYPE html>`: untuk memberitahu bahwa versi html yg digunakan adalah HTML5.
2. `<html>`: sebagai root element bagi semua elemen html.
3. `<head>`: berfungsi sebagai tempat konfigurasi meta web dan import link css atau script js. Bisa juga sebagai tempat untuk edit title web.
4. `<title>`: untuk memberikan judul web yang ditampilkan di tab browser.
5. `<meta>`: untuk memberikan informasi tambahan tentang halaman, seperti karakter encoding, deskripsi, dan kata kunci.
6. `<link>`: untuk mengimport static file css.
7. `<style>`: untuk memberikan styling css langsung di file html nya.
8. `<script>`: untuk menyisipkan atau import kode Javascript ke html.
9. `<body>`: sebagai 'root' content yg ditampilkan dalam user interface.
10. `<div>`: untuk membuat custom element yg tidak memiliki arti/semantic.

## Jelaskan perbedaan antara margin dan padding.

Kalau margin itu sebagai ruang pembatas atau pemberi jarak suatu elemen dengan elemen lainnya. Kalau padding itu sebagai pemberi jarak antara isi konten elemen agar memiliki jarak dengan border elemen tersebut.

## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Kalau Bootstrap itu udah dikasih template nya dan styling sudah disiapkan sedemikian sehingga kita hanya terima hasil jadi styling nya. Sedangkan Tailwind itu tidak memberikan styling hasil jadi namun memberikan hasil jadi inline styling sehingga kita tidak perlu styling secara terpisah di file CSS nya.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Di folder app main, buat file style.css di static/main/style.css.
2. Mengimport file css di index.html
3. Memberikan styling css sehingga menjadi lebih menarik ✨.
4. Memberikan styling untuk last card menggunakan pseudo-class `:last-child`

# TUGAS 6

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

### Synchronous Programming (Programming Sinkron):

Synchronous Programming itu seperti kita sedang makan di restoran cepat saji. Kita memesan burger dan koki pergi membuatnya. Kita harus menunggu sampai koki selesai membuat burger sebelum kita bisa makan. Sistem ini seperti tindakan yang terjadi satu demi satu. Tidak ada yang bisa berjalan bersamaan. Ini berarti kode dijalankan baris per baris secara berurutan. Semua tindakan harus menunggu yang sebelumnya selesai sebelum melanjutkan.

### Asynchronous Programming (Programming Asinkron):

Sedangkan untuk Asynchronous Programming itu seperti kita memesan pizza di restoran lain. Koki di sana tahu bahwa membuat pizza memerlukan waktu, jadi sambil menunggu pizza, kita dapat makan burger di restoran pertama. Ini adalah contoh asinkron. kita tidak harus menunggu satu hal selesai sebelum melakukan yang lain.

Asynchronous programming adalah seperti ini. Ini memungkinkan komputer melakukan beberapa tugas sekaligus tanpa harus menunggu yang satu selesai. Ini sangat berguna ketika kita memiliki tugas yang memerlukan waktu, seperti mengunduh data dari internet atau menunggu tanggapan dari pengguna.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event driven programming adalah bentuk pemrograman dimana program akan menunggu suatu event terjadi, dan ketika suatu event terjadi maka program akan melakukan satu atau serangkaian perintah.

## Jelaskan penerapan asynchronous programming pada AJAX.

Penerapan asynchronous programming pada Javascript dapat dilakukan dalam 3 cara, yaitu:

- menggunakan `XMLHttpRequest`. Ini adalah cara yang old school dan sudah lama tidak digunakan.
- menggunakan fetch-then-catch. Ketika menggunakan cara fetch ini, maka kita dapat menaruh perintah yang harus dilakukan setelah asynchronous atau fetch berhasil atau gagal.
- atau menggunakan async/await. Untuk menggunakan fungsi ini, maka kita harus menaruh keyword async di awal pendeklarasian fungsi dan keyword await ketika kita melakukan perintah fetch.

## Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

| No. | Fetch API                                                                                  | jQuery                                                                                                                     |
| --- | ------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| 1.  | Mudah diaplikasikan                                                                        | Lebih rumit untuk diaplikasikan                                                                                            |
| 2.  | Karena ia adalah library built in javascript, maka tidak perlu memperdulikan sisi size nya | Jika kita menggunakan jQuery hanya untuk AJAX nya saja, maka library jQuery menjadi berat ketimbang menggunakan Fetch API. |

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Langkah-langkah implementasi saya:

1. Mengubah implementasi GET items menjadi menggunakan AJAX.
2. Mengubah implementasi POST add, substract, dan delete menjadi menggunakan AJAX.
3. Mengubah implementasi POST create item menjadi menggunakan AJAX.
4. Membuat views untuk url `create-ajax/` dan menerapkannya untuk POST create item.

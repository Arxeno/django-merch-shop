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

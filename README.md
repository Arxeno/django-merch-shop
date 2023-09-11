# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

Jawaban:

- Pertama-tama saya memulai project Django menggunakan `django-admin startproject inventory_merch`.
- Membuat virtual environment bernama env.
- Lalu saya mengubah konfigurasi db saya menggunakan postgresql. Saya menginstall psycopg2-binary untuk mendukung penggunaan database PostgreSQL.
- Membuat django app bernama "main".
- Membuat models Item (dan model tambahan saya sendiri bernama Category) di `models.py`.
- Membuat url dan template `index.html`.
- Membuat desain card merch yang akan mengakses data dari Item lewat `views.py`.

# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

Jawaban:

# 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Jawaban: Virtual environment sebenarnya adalah opsional. Program Django kita dapat berjalan tanpa error walaupun kita tidak menggunakan Virtual Environment sama sekali. Namun, itu berarti kita menggunakan python global interpreter dalam menjalankan Django kita. Permasalahannya terdapat di proses membuat `requirements.txt` dan proses deploy. Karena ketika kita melakukan `pip freeze > requirements.txt` dan kita tidak menggunakan virtual environment, `pip` akan menyimpan semua package-package yang tidak berikatan sama sekali dengan project django yang kita gunakan sehingga hal tersebut hanya membuang-buang waktu proses deploy saja.

# 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

Jawaban:

## MVC

MVC adalah singkatan dari (Model-View-Controller).

## MVT

MVT adalah singkatan dari (Model-View-Template).

## MVVM

MVVM adalah singkatan dari (Model-View-Viewmodel).

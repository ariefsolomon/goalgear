# GoalGear

## Muhammad Arief Solomon - 2406343092

## Link Aplikasi Web

goalgear [PWS]: https://muhammad-arief41-goalgear.pbp.cs.ui.ac.id

## Penjelasan Implementasi MVT

1. **Membuat Proyek Django Baru:**

-   Buat direktori `goalgear` dan virtual environtment.
-   Install depedensi lewat `requirements.txt` yang dibutuhkan.
-   Buat proyek Django dengan `django-admin startproject goalgear`.

2. **Membuat Aplikasi `main`:**

-   Jalankan `python manage.py startapp main`.
-   Daftarkan aplikasi `main` di `INSTALLED_APPS` di dalam `settings.py`.

3. **Routing Proyek:**

-   Tambahkan `include('main.urls')` di dalam `goalgear/urls.py` agar proyek dapat menjangkau aplikasi `main`.

4. **Implementasi Model `Product`:**

-   Definisikan model `Product` di dalam `main/models.py` dengan atribut yang sudah ditentukan.
-   Jalankan migrasi dengan `python manage.py makemigrations` lalu `python manage.py migrate`.

5. **Implementasi Views dan Template:**

-   Buat folder `main/template` yang berisi `main.html`.
-   Buat tampilan di `main.html` yang akan dipanggil oleh request.
-   Buat fungsi `show_main` di `main/views.py` untuk merender `main.html` dengan data `context`.

6. **Routing Aplikasi `main`:**

-   Buat `main/urls.py` untuk menjangkau fungsi `show_main` di dalam `main/views.py` agar dapat menampilkan `main.html` yang sudah dirender.

7. **PWS Deployment:**

-   Atur `.env` dan `.env.prod` untuk development dan production.
-   Tambahkan `ALLOWED_HOSTS` di dalam `goalgear/settings.py` agar dapat diakses lewat akun PWS yang terdaftar.
-   Push proyek ke GitHub dengan `git commit -m "<commit message>"`, `add .`, dan `push origin master` dan PWS dengan `git push pws master`.

## Alur Request-Respones Django GoalGear

<img width="669" height="512" alt="image" src="https://github.com/user-attachments/assets/06bdd8ad-50e3-4edb-a84d-65f09d70edfc" />

**Sumber:** Tim Dosen PBP. (2024). MTV Django Architecture. Universitas Indonesia.

### Penjelasan lebihlanjut:

1. **Client Request**: Pengguna mengakses URL, misalnya https://muhammad-arief41-goalgear.pbp.cs.ui.ac.id atau http://127.0.0.1:8000/ yang meminta root url dari proyek.
2. **Django Development Server**: Menangkap dan meneruskan request root url ke `goalgear/urls.py`.
3. **goalgear/urls.py**: Menerima lalu mengarahkan request root url ke `main/urls.py` dengan `include('main.urls')`.
4. **main/urls.py**: Menerima lalu memetakan root URL ke `show_main` di dalam `views.py`.
5. **main/views.py**: Merender `main.html` dengan data dari `context` yang ada di dalam `main/views.py`.
6. **main/models.py**: Mendefinisikan struktur data `Product`.
7. **main/template/main.html**: Menampilkan tampilan `main.html` dan data dari `main/views.py` sebagai response dari request pengguna.
8. **Django Response**: Mengembalikan page HTML yang sudah dijelaskan sebelumnya ke browser client.

## Peran goalgear/settings.py

Mengatur konfigurasi proyek keseluruhan seperti aplikasi terinstall, database, middleware, environtment variables, dan allowed hosts untuk mengakses web.

## Cara Kerja Migrasi Django

-   `python manage.py makemigrations`: Ketika kita selesai membuat/mengubah model di `models.py` (misalnya `Product`), Django membaca perubahannya lalu membuat file migrasi di folder `migrations/` yang berisi instruksi python untuk mengubah database, misalnya membuat tabel baru, menambah kolom, menghapus kolom, dll, sehingga kita tidak perlu menulis SQL manual.
-   `python manage.py migrate`: Django mengeksekusi file migrasi tadi, hasilnya akan diubah jadi perintah SQL sesuai dengan database yang diimplementasikan (misalnya PostgreSQL)
-   Setelah migrate, struktur berubah sesuai dengan model di dalam `models.py`. Misalnya kita menambah field baru untuk `Product` dengan `stock = models.IntegerField()` lalu `makemigrations` -> `migrate` seperti yang dijelaskan sebelumnya, Django akan menambah kolom `stock` ke tabel `Product`.

## Mengapa Django untuk Pemula

-   **Struktur MVT yang jelas dan terstruktur** memudahkan sekaligus melatih pengembang pemula mengenai konsep _separation of concerns_ yang memisahkan sub proyek/aplikasi berdasarkan fungsionalitasnya, seperti `models.py` untuk data, `views.py` untuk logika aplikasi, dan `template` untuk tampilan.
-   **Menggunakan bahasa Python** yang banyak dipelajari oleh programmer pemula.
-   **Aman secara Security** untuk framework yang mudah dipelajari dibandingkan dengan menggunakan bahasa pemrograman atau framework lain.

## Feedback untuk Asisten Dosen

Tutorial yang diberikan sudah sangat baik, namun bisa dijelaskan lebih lanjut di kelas, karena awalnya saya sedikit bingung dan menghabiskan waktu di pre-tutorial dikarenakan saya menganggap hal tersebut wajib dikerjakan sebelum tutorial.

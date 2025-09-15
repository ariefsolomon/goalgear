# GoalGear

## Muhammad Arief Solomon - 2406343092

## Link Aplikasi Web

goalgear [PWS]: https://muhammad-arief41-goalgear.pbp.cs.ui.ac.id

# Tugas 3 | Data Delivery

## Mengapa perlu _data delivery_ dalam sebuah platform?

*Data delivery* adalah proses mengirimkan data dari server ke client agar data dapat ditampilkan, digunakan, atau diolah lebih lanjut. Data yang dikirimkan ke client berbentuk HTML, JSON, XML, dll.

Django sendiri melakukan _data delivery_ dengan alur mekanisme *request -> view -> response*:
1. User kirim request, misalnya `url/product/<id product>/` atau menekan tombol `See Detail` pada salah satu product di page `main.html`.
2. `urls.py` mengarahkan ke fungsi `show_product` yang berada di `views.py`.
3. `show_product` menerima `request` dan `id` product untuk mengangkap objek product dengan variable `product` menggunakan `get_object_or_404(Product, pk=id)` dari `models.py` dan database.
4. `show_product` mengembalikan data di dalam variable `context` dan merendernya dengan `product_detail.html`, lalu menampilkannya ke user.

Berdasarkan alur tersebut, _data delivery_ diperlukan untuk membuat aplikasi kita menjadi lebih dinamis, serta dapat menampilkan data yang sesuai dengan _request_ dari user.

## JSON atau XML yang lebih baik?

Menurut saya JSON lebih baik dan lebih banyak digunakan karena:
-   Ukuran file lebih kecil, sehingga dapat menghemat bandwidth.
-   Struktur kode yang lebih mudah, menggunakan _maplike_ _key-value pairs_, dibanding dengan _markup language_ XML dengan struktur berbasis HTML dengan syntax yang _verbose_ yang dapat memberatkan bandwidth.
-   Lebih aman terhadap jenis serangan seperti yang terjadi di XML (XXE: XML External Entity dan Billion Laughs).

Namun demikian, jika diperlukan data dengan aturan schema yang kuat, maka XML akan lebih kompatibel digunakan, seperti pada lingkungan enterprise, dengan resiko keamanan spesifik yang juga harus di-_manage_.

Sumber: https://aws.amazon.com/compare/the-difference-between-json-xml/ 

## Fungsi Method `is_valid()` di `views.py`

`is_valid()` digunakan untuk menerima dan melakukan validasi input user, biasanya dalam data form. Misalnya, `is_valid()` yang berada di dalam method `create_product` di `views.py` dengan penjelasan:
1. Variable `form` menangkap `ProductForm(request.POST or None)` -> form diisi dengan input dari user.
2. `if form.is_valid()` mengecek apakah input sesuai dengan fields yang didefinisikan di `ProductForm` di `forms.py` (berdasarkan `Product` di `models.py`) serta `request.method == "POST"` memastikan memang ada pengiriman form (bukan hanya akses page). 
3. Jika hasil `True` -> `form.save` dan `return redirect("main:show_main")` untuk kembali ke page utama. Jika hasil `False` -> kalau pertama kali akses page (GET) -> form kosong ditampilkan; kalau submit tapi ada error (_invalid input_) -> menampilkan _error message_ dari `form`.

## Kenapa perlu `csrf_token` saat membuat form di Django?

-   `{% csrf_token %}`, misalnya yang ada di dalam `create_product.html`, mencegah CSRF (Cross-Site Request Forgery), yaitu serangan di mana penyerang membuat browser korban mengirim request ke situs yang korban sudah login
-   `csrf_token` adalah token unik yang harus disisipkan di setiap form HTML yang butuh aksi: POST/PUT/DELETE. 
-   Saat form disubmit, token itu dikirim ke server. Django memeriksa token tersebut cocok dengan token di cookie/session. Hasilnya: hanya permintaan yang berasal dari page asli yang memiliki token valid yang akan diterima.
-   Karena penyerang tidak dapat membaca token itu dari domain korban (_same-origin policy_), dia tidak dapat menyertakan token valid dalam form palsunya, sehingga permintaan palsu akan ditolak.

## Penjelasan Implementasi Tugas 3

1. *Pembuatan 4 Fungsi `views.py`*: Mebuat fungsi `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` untuk mengakses dan menampilkan data dalam format `JSON` dan `XML` di browser berdasarkan `Tutorial 2` yang diberikan.
2. *Membuat Routing 4 Fungsi Show*: Membuat routing url untuk masing-masing fungsi show di dalam `views.py` sebelumnya di dalam `main/urls.py` agar user dapat melakukan request dan mengakses masing-masing page data sesuai dengan `Tutorial 2` yang diberikan.

## Feedback Asdos

Tidak ada.

## Dokumentasi Postman

- ![alt text](<Screenshot 2025-09-15 130736.png>)
- ![alt text](<Screenshot 2025-09-15 130753.png>)

# Tugas 2 | MVT Implementation

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

<img width="1188" height="787" alt="image" src="https://github.com/user-attachments/assets/c8409280-f90f-42fb-8bba-16a437b4b4c5" />

**Referensi:** Tim Dosen PBP. (2024). MTV Django Architecture. Universitas Indonesia.

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

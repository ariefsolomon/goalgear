# GoalGear

**Muhammad Arief Solomon - 2406343092 - PBP E**

**Link Aplikasi Web**: https://muhammad-arief41-goalgear.pbp.cs.ui.ac.id

# Tugas 5 | Data Edit, Delete & Styling

## Urutan Prioritas CSS Selector

Ketika ada lebih dari satu aturan CSS yang menargetkan elemen yang sama, browser menentukan gaya yang diterapkan berdasarkan urutan prioritas (specificity & cascade).

**Aturan prioritas:**

1. `!important` → Paling tinggi.
2. Asal aturan → User Agent < User < Author.
3. Spesifisitas → ID > Class > Elemen.
4. Urutan deklarasi → Aturan terakhir akan menang jika spesifisitas sama.
5. Warisan (inheritance) → Properti diwarisi dari parent jika tidak didefinisikan.

**Contoh:**

```html
<style>
  p { color: blue; }
  .highlight p { color: red; }
  #main p { color: green; }
</style>

<div id="main" class="highlight">
  <p>Contoh teks</p>
</div>
```

Hasil akhirnya teks berwarna **hijau** (aturan dengan ID lebih spesifik).

---

## Responsive Design

**Apa itu?**
Konsep desain web yang memastikan tampilan aplikasi tetap rapi dan nyaman digunakan di berbagai ukuran layar (mobile, tablet, desktop).

**Mengapa penting?**

- Banyak perangkat dengan resolusi berbeda.
- UX lebih baik (tidak perlu zoom/scroll horizontal).
- SEO lebih bagus (Google mendukung mobile-friendly).
- Efisien: cukup satu kode untuk semua perangkat.
- Konsistensi tampilan dan fungsi.

**Contoh:**

- **Sudah responsif** → The Boston Globe, e-commerce modern, blog dengan Bootstrap/Tailwind.
- **Belum responsif** → Situs lama dengan layout fixed width, tidak menggunakan meta viewport.

---

## Margin, Border, dan Padding

Ketiganya adalah bagian dari **CSS Box Model**.

- **Margin** → Jarak luar antar elemen.
- **Border** → Garis tepi di sekeliling elemen.
- **Padding** → Jarak dalam, antara konten dan border.

**Contoh:**

```css
.box {
  margin: 20px;
  padding: 10px;
  border: 2px solid black;
}
```

---

## Flexbox

**Apa itu?**
Model layout satu dimensi untuk mengatur elemen dalam baris atau kolom.

**Properti penting:**

- `display: flex;`
- `flex-direction` (row/column)
- `justify-content` (atur horizontal)
- `align-items` (atur vertikal)
- `flex-wrap` (membungkus ke baris baru)

**Kegunaan:**
Navbar, centering elemen, daftar item responsif.

**Contoh:**

```css
.container {
  display: flex;
  flex-wrap: wrap;
}
.item {
  flex: 1 1 200px;
}
```

---

## Grid Layout

**Apa itu?**
Model layout dua dimensi (baris & kolom).

**Properti penting:**

- `display: grid;`
- `grid-template-columns` / `grid-template-rows`
- `gap`
- `grid-area`

**Kegunaan:**
Dashboard, layout halaman penuh, struktur kompleks.

**Contoh:**

```css
.container {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 10px;
}
```

---

## Perbandingan Flexbox & Grid

- **Flexbox** → Satu arah (row/column).
- **Grid** → Dua arah (baris + kolom).
- Bisa digabung: Grid untuk struktur besar, Flexbox untuk detail isi.

---

## Referensi

- [MDN – Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascade/Specificity?utm_source=chatgpt.com)
- [CSS Tricks – Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/?utm_source=chatgpt.com)
- [CSS Tricks – Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/?utm_source=chatgpt.com)
- [MDN – Box Model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model?utm_source=chatgpt.com)
- [Web.dev – Responsive Web Design Basics](https://web.dev/articles/responsive-web-design-basics?utm_source=chatgpt.com)
- [Wikipedia – Responsive Web Design](https://en.wikipedia.org/wiki/Responsive_web_design?utm_source=chatgpt.com)

---

# Tugas 4 | Autentikasi, Session, dan Cookies

## Apa itu Django AuthenticationForm?

`AuthenticationForm` pada Django adalah form bawaan dari `django.contrib.auth.forms` yang memudahkan dalam men-develop proses login aplikasi web. 

**Kelebihan**: 
- Terintegrasi dengan method `authenticate()` dan `login()`.
- 'get_user()' untuk pengecekan username atau password sehingga tidak perlu membuat validasi lagi.

**Kekurangan**:
- Hanya melakukan validasi kredensial dasar, untuk aturan password, dsb. harus ditambahkan sendiri.
- Kurang fleksibel jika ingin menambahkan field input tambahan.

---

## Autentikasi dan Otorisasi

**Authentication**: Melakukan verifikasi pengguna, biasanya dengan login (meminta username dan password).
1. Fungsi `login_user` di dalam `views.py` menangani proses login ketika user mengakses halaman login.
    ```python
    def login_user(request):
    if request.method == 'POST':
        ...
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})

2. Decorator `@login_required(login_url='/login')` biasanya dipasang di view selain `login_user` (seperti `show_main` dan `show_product`) untuk memastikan hanya user yang sudah login yang bisa mengakses page tersebut. Jika belum login, user akan diarahkan ke halaman login.
    ```python
    @login_required(login_url='/login')
    def show_main(request):
        ...
        return render(request, 'main.html', context)

3. User mengisi *username* dan *password* yang diproses oleh `AuthenticationForm` dalam objek `form`.
    ```python
    form = AuthenticationForm(data=request.POST)

4. `form.is_valid()` akan memanggil `authenticate()` untuk memverifikasi objek `User` di database (melalui model `User` bawaan Django atau custom user model).
   - Jika user valid, objek `User` disimpan di `user_cache`, dan bisa diambil lewat `form.get_user()`.
   - Jika tidak valid, `form.get_user()` mengembalikan `None`.
    ```python
    if form.is_valid():
        user = form.get_user()

5. `login(request, user)` kemudian menyimpan informasi user ke dalam session (dengan menyimpan `user.id`), dan mengirim cookie `sessionid` ke browser.  
   Dengan cara ini, Django bisa mengenali user yang sedang login pada request berikutnya.
    ```python
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response

**Authorization**: Mengizinkan user dengan identitas tertentu (username dan password, atau atribut lainnya) untuk mengakses page atau fungsi tertentu di dalam aplikasi web. 
1. Setelah user login melalui `login_user`, Django menyimpan informasi user ke dalam session (`sessionid`).
2. Middleware `AuthenticationMiddleware` otomatis menambahkan atribut `request.user` ke setiap request.
   - Jika user sudah login -> `request.user` berisi objek `User`.
   - Jika belum login -> `request.user` adalah `AnonymousUser`.
3. Fungsi view yang diproteksi dengan `@login_required` hanya bisa diakses oleh user yang sudah login, seperti pada pembahasan pada _Authentication_ poin ke-2.

---

## Sessions dan Cookies

**Cookies**: Data (ukurannya cenderung kecil) yang tersimpan di browser user untuk mengingat hal-hal seperti status logged atau preferensi user di dalam suatu web app di server.

- Kelebihan: 
    - Kecepatan load data di browser client lebih cepat.
    - Umur data bisa di manage sendiri.
    - Data masih ada setelah browser di-close.

- Kekurangan:
    - Keamanan data kurang selama berada di dalam browser user.
    - Ada limit data tersimpan, biasanya 4KB.

- Contoh: Google, Facebook, Amazon, YouTube, Netflix, dsb.

**Sessions**: Sama seperti cookies, tetapi data di simpan di dalam server.

- Kelebihan:
    - Keamanan data yang tersimpan lebih terjamin.
    - Bisa menyimpan data dalam ukuran yang besar.

- Kekurangan:
    - Kecepatan load data lebih lambat.
    - Data biasanya otomatis hilang jika tidak digunakan dalam jangka waktu tertentu.
    - Data hilang ketika sesi expired atau server melakukan restart.

- Contoh: Banking App, Platform E-Learning, Website Pemerintahan, dsb.

Sumber: https://www.geeksforgeeks.org/javascript/difference-between-session-and-cookies/

---

## Keamanan Cookies dalam Django
    
```python
def login_user(request):
    if request.method == 'POST':
        ...
        if form.is_valid():
            ...
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        ...
```

Pada bagian `response.set_cookies('last_login', ...)`, berfungsi untuk mendaftarkan cookie `last_login` di `response`. 

```python
def show_main(request):
    ...
    context = {
        ...
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
```

Sementara di dalam `show_main`, `.get()` mengambil cookie `last_login`, jika tidak ditemukan -> akan mengembalikan nilai default `Never`.

Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Permasalahan security mengenai cookie di Django adalah sebagai berikut: 

**Cross Site Scripting (XSS)**: Jika sesi cookie dikirim melalui HTTP yang tidak aman, _attacker_ dapat mencegatnya dan memperoleh akses tidak sah ke sesi pengguna.
- Solusi: Tetapkan `SESSION_COOKIE_HTTPONLY = True`, `SESSION_COOKIE_SECURE = True` di `settings.py` yang memastikan sesi cookie hanya dikirim melalui HTTPS yang lebih aman.

**HTTP Problem**
_Attacker_ dapat melacak sesi cookie melalui jaringan publik seperti WIFI.
- Solusi: Tetapkan `SESSION_COOKIE_SECURE = True` dengan alasan sama seerti poin sebelumnya.

---

## Implementasi Tugas 4

Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
Menghubungkan model Product dengan User.
Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.

1. **Implementasi Fungsi Registrasi, Login, dan Logout**
    - Registrasi menggunakan `UserCreationForm` untuk membuat akun baru.
    - Login menggunakan `AuthenticationForm`, jika valid maka user diarahkan ke halaman utama, serta disimpan cookie `last_login`.
    - Logout menghapus session user dan cookie `last_login`, lalu diarahkan ke halaman login.
2. **Menghubungkan Model `Product` dengan `User`**
    Pada model `Product` ditambahkan:
    ```python
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ```
3. **Menampilkan Informasi User berdasarkan Cookie**

   Pada fungsi `show_main`, disertakan data bernama `last_login` di dalam `context`:
    ```python
    @login_required(login_url='/login')
    def show_main(request):
        ...
        context = {
            ...
            'last_login': request.COOKIES.get('last_login', 'Never'),
        }
        ...
    ```
    Lalu di dalam `main.html`, data tersebut ditampilkan dengan:
    ```html
    <h5>Nama: </h5>
    <p>{{ student_name }}</p>
    
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ```

---

# Tugas 3 | Data Delivery

## Mengapa perlu _data delivery_ dalam sebuah platform?

*Data delivery* adalah proses mengirimkan data dari server ke client agar data dapat ditampilkan, digunakan, atau diolah lebih lanjut. Data yang dikirimkan ke client berbentuk HTML, JSON, XML, dll.

Django sendiri melakukan _data delivery_ dengan alur mekanisme *request -> view -> response*:
1. User kirim request, misalnya `url/product/<id product>/` atau menekan tombol `See Detail` pada salah satu product di page `main.html`.
2. `urls.py` mengarahkan ke fungsi `show_product` yang berada di `views.py`.
3. `show_product` menerima `request` dan `id` product untuk mengangkap objek product dengan variable `product` menggunakan `get_object_or_404(Product, pk=id)` dari `models.py` dan database.
4. `show_product` mengembalikan data di dalam variable `context` dan merendernya dengan `product_detail.html`, lalu menampilkannya ke user.

Berdasarkan alur tersebut, _data delivery_ diperlukan untuk membuat aplikasi kita menjadi lebih dinamis, serta dapat menampilkan data yang sesuai dengan _request_ dari user.

---

## JSON atau XML yang lebih baik?

Menurut saya JSON lebih baik dan lebih banyak digunakan karena:
-   Ukuran file lebih kecil, sehingga dapat menghemat bandwidth.
-   Struktur kode yang lebih mudah, menggunakan _maplike_ _key-value pairs_, dibanding dengan _markup language_ XML dengan struktur berbasis HTML dengan syntax yang _verbose_ yang dapat memberatkan bandwidth.
-   Lebih aman terhadap jenis serangan seperti yang terjadi di XML (XXE: XML External Entity dan Billion Laughs).

Namun demikian, jika diperlukan data dengan aturan schema yang kuat, maka XML akan lebih kompatibel digunakan, seperti pada lingkungan enterprise, dengan resiko keamanan spesifik yang juga harus di-_manage_.

---

Sumber: https://aws.amazon.com/compare/the-difference-between-json-xml/ 

## Fungsi Method `is_valid()` di `views.py`

`is_valid()` digunakan untuk menerima dan melakukan validasi input user, biasanya dalam data form. Misalnya, `is_valid()` yang berada di dalam method `create_product` di `views.py` dengan penjelasan:
1. Variable `form` menangkap `ProductForm(request.POST or None)` -> form diisi dengan input dari user.
2. `if form.is_valid()` mengecek apakah input sesuai dengan fields yang didefinisikan di `ProductForm` di `forms.py` (berdasarkan `Product` di `models.py`) serta `request.method == "POST"` memastikan memang ada pengiriman form (bukan hanya akses page). 
3. Jika hasil `True` -> `form.save` dan `return redirect("main:show_main")` untuk kembali ke page utama. Jika hasil `False` -> kalau pertama kali akses page (GET) -> form kosong ditampilkan; kalau submit tapi ada error (_invalid input_) -> menampilkan _error message_ dari `form`.

---

## Kenapa perlu `csrf_token` saat membuat form di Django?

-   `{% csrf_token %}`, misalnya yang ada di dalam `create_product.html`, mencegah CSRF (Cross-Site Request Forgery), yaitu serangan di mana _attacker_ membuat browser korban mengirim request ke situs yang korban sudah login
-   `csrf_token` adalah token unik yang harus disisipkan di setiap form HTML yang butuh aksi: POST/PUT/DELETE. 
-   Saat form disubmit, token itu dikirim ke server. Django memeriksa token tersebut cocok dengan token di cookie/session. Hasilnya: hanya permintaan yang berasal dari page asli yang memiliki token valid yang akan diterima.
-   Karena _attacker_ tidak dapat membaca token itu dari domain korban (_same-origin policy_), dia tidak dapat menyertakan token valid dalam form palsunya, sehingga permintaan palsu akan ditolak.

---

## Implementasi Tugas 3

1. *Pembuatan 4 Fungsi `views.py`*: Mebuat fungsi `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` untuk mengakses dan menampilkan data dalam format `JSON` dan `XML` di browser berdasarkan `Tutorial 2` yang diberikan.
2. *Membuat Routing 4 Fungsi Show*: Membuat routing url untuk masing-masing fungsi show di dalam `views.py` sebelumnya di dalam `main/urls.py` agar user dapat melakukan request dan mengakses masing-masing page data sesuai dengan `Tutorial 2` yang diberikan.

---

## Feedback Asdos

Tidak ada.

---

## Dokumentasi Postman

- XML
<img width="2879" height="1797" alt="Screenshot 2025-09-15 130736" src="https://github.com/user-attachments/assets/16146497-ded0-4059-b5dd-4756ab0e79d7" />

- JSON
<img width="2879" height="1799" alt="Screenshot 2025-09-15 131412" src="https://github.com/user-attachments/assets/7796ca96-2559-4e44-89fa-b5b6a9fa74df" />

---

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

---

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

---

## Peran goalgear/settings.py

Mengatur konfigurasi proyek keseluruhan seperti aplikasi terinstall, database, middleware, environtment variables, dan allowed hosts untuk mengakses web.

---

## Cara Kerja Migrasi Django

-   `python manage.py makemigrations`: Ketika kita selesai membuat/mengubah model di `models.py` (misalnya `Product`), Django membaca perubahannya lalu membuat file migrasi di folder `migrations/` yang berisi instruksi python untuk mengubah database, misalnya membuat tabel baru, menambah kolom, menghapus kolom, dll, sehingga kita tidak perlu menulis SQL manual.
-   `python manage.py migrate`: Django mengeksekusi file migrasi tadi, hasilnya akan diubah jadi perintah SQL sesuai dengan database yang diimplementasikan (misalnya PostgreSQL)
-   Setelah migrate, struktur berubah sesuai dengan model di dalam `models.py`. Misalnya kita menambah field baru untuk `Product` dengan `stock = models.IntegerField()` lalu `makemigrations` -> `migrate` seperti yang dijelaskan sebelumnya, Django akan menambah kolom `stock` ke tabel `Product`.

---

## Mengapa Django untuk Pemula

-   **Struktur MVT yang jelas dan terstruktur** memudahkan sekaligus melatih pengembang pemula mengenai konsep _separation of concerns_ yang memisahkan sub proyek/aplikasi berdasarkan fungsionalitasnya, seperti `models.py` untuk data, `views.py` untuk logika aplikasi, dan `template` untuk tampilan.
-   **Menggunakan bahasa Python** yang banyak dipelajari oleh programmer pemula.
-   **Aman secara Security** untuk framework yang mudah dipelajari dibandingkan dengan menggunakan bahasa pemrograman atau framework lain.

---

## Feedback untuk Asisten Dosen

Tutorial yang diberikan sudah sangat baik, namun bisa dijelaskan lebih lanjut di kelas, karena awalnya saya sedikit bingung dan menghabiskan waktu di pre-tutorial dikarenakan saya menganggap hal tersebut wajib dikerjakan sebelum tutorial.



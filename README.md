# 🚀 Marvel Comic Search Using Vertex AI Search

Proyek ini membangun sistem pencarian komik Marvel berbasis **Vertex AI Search** dengan data dari **BigQuery** dan antarmuka pencarian berbasis prompt. Sistem ini mencakup pipeline dari pre-processing data, pembuatan aplikasi pencarian, hingga deployment menggunakan **Cloud Run**.

---

## 🧱 Langkah-langkah Pengembangan

### 1. 🧹 Retrieve Data dan Pre-processing

- Siapkan data komik Marvel dan simpan ke dalam **Google Cloud Storage (GCS)**.
- Di dalam **Vertex AI Workbench**, tarik data dari bucket untuk dilakukan pre-processing.
- Tahapan pre-processing:
  - **Isi nilai null** berdasarkan tipe data:
    - `integer`: diganti dengan `0`
    - `object/string`: diganti dengan `"Not Provided"`
  - Contoh implementasi ada di notebook:
    ```
    development code --> 1_preprocessing.ipynb
    ```

- Setelah data bersih, **upload ke BigQuery** agar bisa digunakan dalam tahap berikutnya.

---

### 2. 🏗️ Create AI Application

- Di halaman utama GCP, ketik `AI Application` di search bar lalu buka halaman tersebut.
- Buat **datastore baru**:
  - **Source**: BigQuery
  - **Type**: Structured
- Setelah datastore berhasil dibuat, buat aplikasi baru:
  - Pilih **Custom Search**
  - Hubungkan aplikasi dengan datastore yang sudah dibuat tadi.

---

### 3. 🧠 Prompting and Configuring

- Buat notebook baru di Workbench untuk melakukan konfigurasi dan pengujian model.
- Hal yang dilakukan:
  - **Memberi prompt** kepada model untuk mengarahkan perilaku pencarian.
  - Melakukan **konfigurasi model** sesuai dengan struktur data dan skema di AI Application.
  - Uji hasil pencarian melalui notebook.
  - **Catatan**: Dalam tahap ini, **chat history** akan dicatat dan disimpan sebagai bahan untuk evaluasi model di tahap selanjutnya.

- Contoh dan template dapat dilihat di notebook:
    ```
    development code --> 2_Prompting model.ipynb
    ```
---

### 4. 🧪 Evaluasi (Opsional)

- Buat notebook evaluasi untuk mengecek performa model.
- Menggunakan pendekatan **pointwise evaluation** dengan kriteria yang kamu tentukan sendiri.
- Setiap kriteria memiliki **rating rubric** (misal: 1–5).
- Hasil evaluasi dapat dilihat di:
- Notebook referensi:
  ```
  development code --> 3_Evaluation Model.ipynb
  ```

---

### 5. 🚀 Deployment

- Gabungkan seluruh fungsi penting ke dalam satu file Python: `function.py`.
- Buat juga:
- `app.py` untuk frontend/servis utama
- `Dockerfile` untuk build container
- `requirements.txt` untuk dependensi

- **Langkah deploy:**
1. Upload semua file ke GitHub.
2. Buka **Cloud Run** > klik **Deploy container** > pilih **Services**.
3. Hubungkan ke **GitHub** repository kamu.
4. Lanjutkan proses deployment hingga aplikasi online.

---
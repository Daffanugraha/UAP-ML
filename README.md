# Prediksi Stunting
Stunting adalah kondisi gagal tumbuh pada anak balita akibat kekurangan gizi kronis, infeksi berulang, dan stimulasi psikososial yang tidak memadai. Deteksi penyakit stunting sangat penting untuk mencegah dampak jangka panjang pada kesehatan, pertumbuhan, dan perkembangan anak. Anak yang mengalami stunting berisiko menghadapi masalah kesehatan seperti gangguan kognitif, penurunan produktivitas di masa dewasa. Ada beberapa indikator yang menyebabkan anak balita terkena penyakit stunting seperti usia , tinggi badan , dan jenis kelamin
## Dataset
Proyek ini menggunakan dataset dari *[Kaggle](https://www.kaggle.com/datasets/rendiputra/stunting-balita-detection-121k-rows)*  ini didasarkan pada formula z-score untuk menentukan stunting menurut WHO (World Health Organization), yang berfokus pada deteksi stunting pada anak di bawah usia lima tahun. Dataset ini terdiri dari 121.000 baris data yang memuat informasi mengenai usia, jenis kelamin, tinggi badan, dan status gizi balita. Dataset ini bertujuan untuk membantu peneliti, ahli gizi, dan pembuat kebijakan dalam memahami dan menangani masalah stunting pada anak di bawah usia lima tahun.
Pada dataset akan diolah menggunakan 2 algoritma yaitu : Feedforward Neural Network (FFNN) dan Random Forest, analisis data dapat dilakukan dengan lebih cepat dan akurat.  Proyek ini bertujuan untuk memprediksi apakah seseorang teridentifikasi Berisiko atau Mengalami Stunting dengan memasukan data input seperti usia , tinggi badan, dan jenis kelamin. Hasil dari inputan akan mengetahui status gizi dari balita tersebut yaitu dengan 4 kelas normal , stunted, tinggi , severly stunted. Hasil dari prediksi tersebut diharapkan dapat mengurangi resiko stunting di indonesia.
## Feedforward Neural Network architecture
![FNN](https://github.com/user-attachments/assets/29da4cf4-d78b-40fc-9fb4-854d81c96b6f)

## Random Forest architecture
![Random-forest-architecture-Breiman-2001](https://github.com/user-attachments/assets/3edef549-a281-4b08-a68c-5027e9f5ef74)

## Modelling
### Feedforward Neural Network
#### Preprocessing
Preprocessing data melibatkan beberapa langkah penting untuk menyiapkan dataset agar siap digunakan dalam model machine learning. Langkah pertama adalah pengecekan missing value, yang bertujuan untuk mengidentifikasi dan menangani data yang kosong. Setelah itu, dilakukan encoding label menggunakan LabelEncoder untuk mengubah data kategori menjadi numerik, sehingga model dapat memprosesnya. Selanjutnya, normalisasi dilakukan menggunakan MinMaxScaler, yang menskalakan data numerik ke rentang [0, 1], untuk menghindari bias akibat perbedaan skala antar fitur. Terakhir, data dibagi menjadi dua bagian, yaitu 80% untuk pelatihan dan 20% untuk pengujian.

#### Layer yang digunakan untuk FFNN
![Layer FFNN](https://github.com/user-attachments/assets/6f8c3ff0-8389-4a64-8dc9-8b417428d6ec)

#### Kurva
![Kurva](https://github.com/user-attachments/assets/f2e1466d-f0e7-4097-812d-b242d6e9a87c)

#### Classification Report
![Classification Report FFNN](https://github.com/user-attachments/assets/3d77f0bf-cb38-4d27-b132-5318391f2511)

#### Confusion Matrix
![Confusion Matrix](https://github.com/user-attachments/assets/9946505e-c584-453b-bb8e-e4bb7af98623)


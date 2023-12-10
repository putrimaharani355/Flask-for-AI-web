# Klasifikasi Gunting, Batu dan Kertas

Project klasifikasi gunting, batu dan kertas ini menggunakan model pretrained Restnet101. Dataset Project ini menggunakan dataset rock paper scissor dengan jumlah data sebanyak 2520 file. Load image menggunakan image_dataset_from_directory dari pustaka tensorflow dengan pembagian train 70%, validation 25% dan test 5%. 

<h3>Cara menggunakan project ini</h3>

1. Melakukan clone repository ini dengan perintah sebagai berikut `git clone putrimaharani355/Flask-for-AI-web.git`

2. Masuk ke repository 
3. Membuat sebuah env dengan perintah `python -m venv ./rpsvenv`   
4. Mengaktifkan env 
    * Command Prompt `./rpesvenv/Scripts/activate.bat`
    * Powershell `./rpesvenv/Scripts/activate.ps`

5. Lakukan install library yang diperlukan dengan perintah berikut `pip install -r requirements`
6. Melakukan perintah `python main.py`
7. Akses web pada url `http://192.168.1.15:2000/`

<h3>Pembuatan Model</h3>

Model dibuat dengan model ResNet101. Berikut adalah summary model: 


<img width="374" alt="image" src="https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/90ae86d5-e133-4508-a343-956f13f4585f">

Model menggunakan optimizer `adam ` dengan learning rate `0.001` dan `CategoricalCrossentropy loss`. Setelah itu, train data dilakukan dengan `10 epoch`. 
Akurasi yang didapatkan adalah `0.78` dan loss `0.54`.
Berikut adalah plot hasil dari accuracy, val accuracy, loss dan val loss. 
![image](https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/7ff2b0cb-0dcf-4f6a-a111-8d5b2bd7743c)

Setelah dilakukan train data, maka model disimpan dalam format `h5`.

<h3>Web AI</h3>

File pada halaman awal bernama `select.html`
File pada halaman kedua bernama `result_select.html`

Step pada halaman awal: 
1. User akan memilih model apa yang ingin digunakan.
2. Lalu, user mengupload gambar yang ingin diuji.
3. Setelah itu, user melakukan execute. 
![image](https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/522e9e2e-07dc-4e13-bc6e-2e8405e7c9eb)

Tampilan halaman predict. 
![image](https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/14af6949-c7b4-449f-bc5d-40b8bca24ca7)

Pada halaman predict / halaman kedua terdapat Prediction result yang terdiri dari :
1. Predicted Label dari gambar
2. Akurasi
3. Waktu prediksi
   

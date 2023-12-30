# Klasifikasi Gunting, Batu dan Kertas
## Overview Dataset 
***Link Dataset yang digunakan :*** [Rock Paper Scissors Dataset](https://laurencemoroney.com/datasets.html).
Rock Paper Scissors berisi gambar dari berbagai tangan, dari berbagai ras, usia, dan jenis kelamin, yang diposisikan menjadi Batu/Kertas atau Gunting dan diberi label seperti itu. Dataset tersebut memiliki jumlah data sebanyak 2520. 

## Preprocessing and Modelling
Berikut adalah preprocesing pada model ini:

<img width="191" alt="image" src="https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/fc26cb55-092f-424a-ae17-3507f9e73e61">

### Model 1 
Pada model 1, metode yang digunakan merupakan metode CNN dengan arsitekur sebagai berikut : 

![image](https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/d9daefcc-3027-44d3-b00b-4dea08eaf6a2)

Model menggunakan optimizer `adam ` dan `CategoricalCrossentropy loss`. Setelah itu, train data dilakukan dengan `10 epoch`. Akurasi yang didapatkan adalah `13%` dan loss `95%`.
Berikut adalah plot hasil dari accuracy, val accuracy, loss dan val loss. 
![image](https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/c25d262c-022d-4382-a1d5-7b7af24beaf0)

### Model 2 
Pada model 2, metode yang digunakan merupakan metode pre-trained RestNet101 dengan arsitektur sebagai berikut:

<img width="374" alt="image" src="https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/90ae86d5-e133-4508-a343-956f13f4585f">

Model menggunakan optimizer `adam ` dengan learning rate `0.001` dan `CategoricalCrossentropy loss`. Setelah itu, train data dilakukan dengan `10 epoch`. 
Akurasi yang didapatkan adalah `0.78` dan loss `0.54`.
Berikut adalah plot hasil dari accuracy, val accuracy, loss dan val loss. 
![image](https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/7ff2b0cb-0dcf-4f6a-a111-8d5b2bd7743c)

## Predict data
### Model 1 
Berikut adalah hasil predict data menggunakan model CNN :
![image](https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/4e3f1d2e-8db6-4b68-a351-1ff961e40cec)

### Model 2 
Berikut adalah hasil predict data menggunakan model Restnet101 :
![image](https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/79e37317-166a-4d60-9d3e-3042617a18f8)

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


<h3>Web AI</h3>
Model yang digunakan dalam deploy website adalah model RestNet101.

File pada halaman awal bernama `select.html`
File pada halaman kedua bernama `result_select.html`

Step pada halaman awal: 
1. User akan memilih model apa yang ingin digunakan.
2. Lalu, user mengupload gambar yang ingin diuji.
3. Setelah itu, user melakukan execute. 
<img width="960" alt="image" src="https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/06c0eb93-e19a-43c1-9742-cd2453b519d1">

Tampilan halaman predict. 
<img width="960" alt="image" src="https://github.com/putrimaharani355/Flask-for-AI-web/assets/71591898/3655ab23-69c5-419e-b62a-1915e17e1269">

Pada halaman predict / halaman kedua terdapat Prediction result yang terdiri dari :
1. Predicted Label dari gambar
2. Akurasi
3. Waktu prediksi
   

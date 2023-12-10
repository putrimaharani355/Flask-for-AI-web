# Mengimpor modul dan library yang diperlukan
from pyexpat import model
import time
import os
import cv2
import numpy as np
from PIL import Image
from flask import Flask, request, redirect, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.models import model_from_json

# Menetapkan ekstensi file yang diizinkan dan membuat aplikasi Flask
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

# Menetapkan header Cache-Control untuk menonaktifkan penyimpanan cache
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

# Menentukan route utama untuk merender template select.html
@app.route("/")
def index():
    return render_template('/select.html', )

# Menentukan route untuk menangani prediksi gambar
@app.route('/predict', methods=['POST'])
def predict():
    # Memperoleh model yang dipilih
    chosen_model = request.form['select_model']
    
    # Memuat model dari file 'model5.h5'
    model = load_model("model5.h5")

    # Menyimpan file yang diunggah dan memproses gambar untuk prediksi
    file = request.files["file"]
    file.save(os.path.join('static', 'temp.jpg'))
    img = cv2.cvtColor(np.array(Image.open(file)), cv2.COLOR_BGR2RGB)
    img = np.expand_dims(cv2.resize(img, model.layers[0].input_shape[0][1:3] \
        if not model.layers[0].input_shape[1:3] else model.layers[0].input_shape \
        [1:3]).astype('float32') / 255, axis=0)

    # Melakukan prediksi dan mengukur waktu eksekusi
    start = time.time()
    pred = model.predict(img)[0]
    labels = (pred > 0.5).astype(int)
    print(labels)
    runtimes = round(time.time()-start,4)

    # Mengonversi probabilitas prediksi menjadi persentase
    respon_model = [round(elem * 100, 2) for elem in pred]

    # Memanggil fungsi predict_result untuk merender template hasil
    return predict_result(chosen_model, runtimes, respon_model, 'temp.jpg')

# Fungsi untuk merender template hasil prediksi
def predict_result(model, run_time, probs, img):
    # Mendefinisikan kelas-kelas untuk prediksi
    class_list =  {'paper':0, 'rock':1, 'scissor':2}
    idx_pred = probs.index(max(probs))
    labels = list(class_list.keys())
    
    # Merender template hasil dengan informasi prediksi
    return render_template('/result_select.html', labels=labels,
                           probs=probs, model=model, pred=idx_pred,
                           run_time=run_time, img=img)

# Menjalankan aplikasi Flask
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=2000)

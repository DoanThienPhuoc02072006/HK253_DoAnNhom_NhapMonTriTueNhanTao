from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os
from datetime import datetime
from expert_system.diagnosis import run_diagnosis

app = Flask(__name__)
app.secret_key = 'super_secret_key'  # Dùng cho session
DATABASE = 'database/respiratory.db'


def init_db():
    if not os.path.exists('database'):
        os.makedirs('database')
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            phone TEXT,
            address TEXT,
            symptoms TEXT,
            suspected_diseases TEXT,
            date_created TEXT
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/diagnose', methods=['POST'])
def diagnose():
    # Lấy thông tin bệnh nhân
    patient_info = {
        'name': request.form['name'],
        'age': request.form['age'],
        'gender': request.form['gender'],
        'phone': request.form['phone'],
        'address': request.form['address']
    }

    # Lấy danh sách triệu chứng
    symptoms = request.form.getlist('symptoms')

    # Chạy hệ chuyên gia suy diễn (đã bao gồm % khả năng mắc bệnh)
    diagnosis_result = run_diagnosis(symptoms)

    # Chuỗi tên bệnh kèm % để lưu vào database (dạng: "Viêm phổi (66.67%), ...")
    if diagnosis_result['diseases']:
        diseases_str = ", ".join(
            f"{d['disease']} ({d['probability']}%)" for d in diagnosis_result['diseases']
        )
    else:
        diseases_str = diagnosis_result['no_result_message']

    # Lưu vào database
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO patients (name, age, gender, phone, address, symptoms, suspected_diseases, date_created)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (patient_info['name'], patient_info['age'], patient_info['gender'], patient_info['phone'],
          patient_info['address'], ", ".join(symptoms), diseases_str, date_now))
    conn.commit()
    conn.close()

    # Lưu kết quả vào session để hiển thị
    session['result'] = {
        'patient': patient_info,
        'symptoms': symptoms,
        'diagnosis': diagnosis_result,
        'date': date_now
    }

    return redirect(url_for('result'))


@app.route('/result')
def result():
    if 'result' not in session:
        return redirect(url_for('index'))
    return render_template('result.html', data=session['result'])


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

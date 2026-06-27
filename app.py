from flask import Flask, render_template, request, redirect, url_for, session, send_file
import sqlite3
import os
from datetime import datetime
from expert_system.diagnosis import run_diagnosis
from pdf.pdf_generator import generate_pdf

app = Flask(__name__)
app.secret_key = 'super_secret_key' # Dùng cho session
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

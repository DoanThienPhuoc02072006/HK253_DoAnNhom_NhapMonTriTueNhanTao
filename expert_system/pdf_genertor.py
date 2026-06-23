from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import textwrap

def remove_accents(input_str):
    """ Hàm hỗ trợ bỏ dấu tiếng Việt để tránh lỗi font ReportLab mặc định khi không có font Unicode """
    s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
    s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
    s = ''
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s

def generate_pdf(data, filepath):
    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Bao cao Chan doan Benh Ho hap (Tham khao)")
    y -= 30
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Ngay tao: {data['date']}")
    y -= 30

    # Thông tin bệnh nhân
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "1. Thong tin benh nhan")
    y -= 20
    c.setFont("Helvetica", 12)
    patient = data['patient']
    c.drawString(70, y, f"Ho ten: {remove_accents(patient['name'])} - Tuoi: {patient['age']} - Gioi tinh: {remove_accents(patient['gender'])}")
    y -= 20
    c.drawString(70, y, f"SDT: {patient['phone']} - Dia chi: {remove_accents(patient['address'])}")
    y -= 30

    # Triệu chứng
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "2. Trieu chung ghi nhan")
    y -= 20
    c.setFont("Helvetica", 12)
    symptoms_text = ", ".join(data['symptoms'])
    c.drawString(70, y, remove_accents(symptoms_text))
    y -= 30
    
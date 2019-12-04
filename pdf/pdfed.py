from PyPDF2 import PdfFileWriter, PdfFileReader
import io
import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from datetime import datetime


def pdf_money(fio, group, addr, reason, daymonth, year, ser, num, pas_date, pas_place, phone):

    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    pdfmetrics.registerFont(TTFont('TNR', 'pdf/TNR.ttf'))

    can.setFont('TNR', 13)
    can.drawString(103, 573, fio)
    can.drawString(405, 556, group)
    can.setFont('TNR', 11)
    can.drawString(263, 541, addr)
    can.setFont('TNR', 13)
    can.drawString(103, 510, reason)
    can.setFont('TNR', 14)
    can.drawString(152, 478, daymonth)
    can.drawString(295, 478, year)
    can.setFont('TNR', 13)
    can.drawString(226, 462, ser)
    can.drawString(396, 462, num)
    can.drawString(296, 446, pas_date)
    can.setFont('TNR', 12)
    can.drawString(103, 430, pas_place)
    can.setFont('TNR', 13)
    can.drawString(173, 414, phone)
    can.drawString(233, 350, (datetime.now()).strftime("%d.%m"))

    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    existing_pdf = PdfFileReader(open("pdf/original.pdf", "rb"))
    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    mills = str(int(round(time.time() * 1000)))
    outputStream = open("pdf/"+ mills + ".pdf", "wb")
    output.write(outputStream)
    outputStream.close()
    return "pdf/" + mills + ".pdf"


# pdf_money("Иванов Иван Иванович", "ПИН-12", "г.Москва, г.Зеленоград, ул.Юности, д.9, ком.000", "тяжелое материальное положение", "01.01", "18", "0000", "000000", "10.01.2014", "Отделом УФМС России по г.Иваново Центрального Района", "8(800)555-35-35")
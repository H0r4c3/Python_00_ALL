from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

pdf_path = "/mnt/data/top_alimente_fibre_fier_calciu_omega3_COLOR_no_diacritics.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4)

styles = getSampleStyleSheet()
title = styles["Title"]

data = [
    ["Categorie", "Aliment", "Valoare / 100g"],
    ["Fibre", "Psyllium husk", "85 g"],
    ["Fibre", "Seminte de chia", "34-35 g"],
    ["Fibre", "Seminte de in", "27 g"],
    ["Calciu", "Seminte de susan", "970 mg"],
    ["Calciu", "Chia", "630 mg"],
    ["Calciu", "Migdale", "260 mg"],
    ["Fier", "Cacao pudra", "11 mg"],
    ["Fier", "Seminte de dovleac", "8-9 mg"],
    ["Fier", "Linte / naut", "6-7 mg"],
    ["Omega-3", "Seminte de in", "22 g"],
    ["Omega-3", "Chia", "17 g"],
    ["Proteine", "Seminte de dovleac", "30 g"],
    ["Proteine", "Arahide", "26 g"],
]

table = Table(data, colWidths=[100, 200, 100])

table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#4A90E2")),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('BOTTOMPADDING', (0,0), (-1,0), 8),

    ('BACKGROUND', (0,1), (0,-1), colors.HexColor("#ECECEC")),
    ('GRID', (0,0), (-1,-1), 0.3, colors.grey)
]))

story = []
story.append(Paragraph("Top alimente bogate in fibre, calciu, fier si omega-3 (fara diacritice)", title))
story.append(Spacer(1, 12))
story.append(table)

doc.build(story)

pdf_path

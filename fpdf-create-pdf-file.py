from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font('Arial', style = 'B', size = 16)
pdf.cell(200, 10, txt = 'My First PDF in Python', align = 'C')

pdf.set_font('Arial', size = 12)
pdf.multi_cell(0, 10, txt = 'This is created in Python')

pdf.output('./data/fpdf.pdf')
print('PDF created!')

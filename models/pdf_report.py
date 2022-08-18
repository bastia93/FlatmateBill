from fpdf import FPDF
from models.flatmate import Flatmate
from models.bill import Bill


class PdfReport:

    def __init__(self, name):
        self.name = name

    def generate_report(self, flatmates: list[Flatmate], curr_bill: Bill, total_days):

        # Heading
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.image('files/house.png', w=30, h=30)
        pdf.set_font(family='Times', style='B', size=20)
        pdf.cell(w=0, h=60, txt=curr_bill.period, border=0, ln=1, align='C')

        # Adding the flatmates details
        pdf.set_font(family='Times', style='B', size=14)
        for flatmate in flatmates:
            pdf.cell(w=100, h=20, txt=flatmate.name, border=0, align='L')
            pdf.cell(w=100, h=20, txt=str(flatmate.to_pay(curr_bill, total_days)), border=0, align='L', ln=1)

        pdf.output(self.name)





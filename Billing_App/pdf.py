import webbrowser
import os
from fpdf import FPDF


class PdfGenerate:

    def __init__(self,filename):
        self.filename=filename

    def generate(self,person1, person2, bill):
        person1_pay= round(person1.pays(bill,person2),2)
        person2_pay= round(person2.pays(bill,person1),2)

        pdf=FPDF(orientation='P',format='A4',unit='pt')
        pdf.add_page()
        pdf.image("./files/house.png",w=30,h=40)

        #insert Title
        pdf.set_font(family='Times',size=20,style='B')
        pdf.cell(w=100,h=40,txt="Flatmate Bill",align ='c',ln=1)

        pdf.set_font(family='Times',size=15,style='B')
        pdf.cell(w=100,h=40,txt="Period",border=1)
        pdf.cell(w=150,h=40,txt=bill.date,border=1,ln=1)

        pdf.set_font(family='Times',size=12)
        pdf.set_text_color(255,0,0)
        # inserting persion 1 detail
        pdf.cell(w=100,h=40,txt=person1.name,border=1)
        pdf.cell(w=150,h=40,txt=str(person1_pay),border=1,ln=1)

        # inserting persion 2 detail
        pdf.cell(w=100,h=40,txt=person2.name,border=1)
        pdf.cell(w=150,h=40,txt=str(person2_pay),border=1,ln=1)



        os.chdir("files")
        pdf.output(self.filename)
        #automatically open the file
        webbrowser.open(self.filename)

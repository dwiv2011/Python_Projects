from flat import Bill, Flatmate
from pdf import PdfGenerate

bill= Bill(120, "Dec 2021")

person1 = Flatmate("John", 20)
person2 = Flatmate("Merry", 25)

p1=person1.pays(bill,person2)

report= PdfGenerate(f"bill_due_{bill.date}.pdf")
report.generate(person1,person2,bill)
print(person1.pays(bill,person2))

"""
An app that gets as input the amount of a bill for a particular period
and the days that each of the flatmates stayed in the house for that period
and returns how much each flatmate has to pay. It also generates a PDF report
stating the names of the flatmates, the period, and how much each of them had to pay.
"""

class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and
    pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = (self.days_in_house / (self.days_in_house + flatmate2.days_in_house))
        to_pay = bill.amount  * weight
        return to_pay


class PdfReport:
    """
    Creates a PDF file that contains data about
    the flatmates and their names and their bills
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass

bill = Bill(amount=120, period="March 2021")
john = Flatmate(name="John", days_in_house=20)
mary = Flatmate(name="Mary", days_in_house=25)

print("John pays:", john.pays(bill=bill, flatmate2=mary))
print("Mary pays:", mary.pays(bill=bill, flatmate2=john))
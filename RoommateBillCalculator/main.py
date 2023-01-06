from fpdf import FPDF

class Bill(object):
    """
    Class defining the amount to be paid (bill) by both roommates over the given rental period (month, year)

    Paramters
    ----------
    amount: float - total amount of money owed by the roommates for the given pay period

    period: str - period the amount is to be paid for (month, year)

    Methods
    ----------

    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Roommate(object):
    """
    Class defining the roommate who lives in the apartment for the rental period.

    Parameters
    -----------
    name : str - name of roommate in apartment

    days_in_unit : int - number of whole days the given roommate was in the unit

    Methods
    -----------
    pay_bill : arg: bill object - method of calculating how much the roommates have to pay based upon the bill (Bill instance)
    """

    def __init__(self, name, days_in_unit):
        self.name = name
        self.days_in_unit = days_in_unit

    def pay_bill(self, bill_instance, other_roommate) -> float:
        """
        Assigns a bill to be paid by the roommate

        Parameters
        -----------
        bill_instance: Bill obj - the bill to be split and paid by roommates for given pay period and fractional occupancy

        other_roommate: Roommate obj - instance of other roommate sharing the apartment

        Returns
        -----------
        bill_amount: float - fractional bill to be paid by roommate instance based upon number of days in unit and number of days
        other roommate occupied house

        """
        # bill amount per user depends on their fractional time spent in the unit and the total occupancy for that pay period 
        bill_fraction = self.days_in_unit / (self.days_in_unit + other_roommate.days_in_unit)

        bill_amount = bill_fraction * bill_instance.amount

        return bill_amount

class PdfReport(object):
    """
    Class defining the pdf report that will be outputted to the selected directory containing the amount owed by each roommate
    for the given rental pay period.

    Parameters
    -----------
    file_name: str - user defined name for the generated pdf report

    rommate_name: str - name of the roommate also staying in the unit

    rental_period: tuple (str, int) - rental period for the bill to be paid (month, year)

    bill: Bill obj - the bill object for the bill to be paid for the given rental period

    Methods
    -----------
    generate_pdf: - creates the pdf containing the fraction of the bill to be paid by each roommate for the given period

    """

    def __init__(self, file_name) -> None:
        self.file_name = file_name
    
    def generate_pdf(self, roommate1, roommate2, bill):
        """
        Generates the pdf report containing the fraction of the bill to be paid by each roommate for the given rental period.

        Parameters
        -----------
        roommate1: Roommate obj - person 1 living in the rental unit for the given rental period

        roommate2: Roommate obj - person 2 living in the rental unit for the given rental period

        bill: Bill obj - the bill instance to be paid by the two roommates living in the unit for the given period

        Returns
        -----------
        pdf_bill: pdf file - file containing the fraction of the bill to be paid by each roommate for the given period
        """
        # Generate the pdf object and add a page to edit
        pdf_bill = FPDF(orientation='P', unit='pt', format='A4')
        pdf_bill.add_page()

        # Add house image to header
        pdf_bill.image("house.png", x= 60, y=52, w=30, h=30)
        pdf_bill.image("house.png", x= 507, y=52, w=30, h=30)


        # Add desired bold title text and image to the pdf based upon user input
        pdf_bill.set_font(family='Times', size=24, style='B')
        pdf_bill.cell(w=0, h=80, txt="Roommate's Bill", border=1, align='C', ln=1)

        # Add text box for the rental period
        pdf_bill.cell(w=160, h=40, txt="Rental Period:", border=0)
        pdf_bill.cell(w=150, h=40, txt=str(bill.period), border=0, ln=1)

        # Add text box for total monthly bill
        pdf_bill.set_font(family='Times', size=18, style='B')
        pdf_bill.cell(w=110, h=40, txt="Total Bill ($):", border=0)
        pdf_bill.cell(w=40, h=40, txt="{:.2f}".format(bill.amount), align='L', border=0, ln=1)
        pdf_bill.cell(w=250, h=40, txt="Cumulative Occupancy (Days):", border=0)
        pdf_bill.cell(w=40, h=40, txt=str(roommate1.days_in_unit + roommate2.days_in_unit), align='L', border=0, ln=1)

        # Text block headers for amount roommates have to pay
        pdf_bill.set_font(family='Times', size=18, style='I')
        pdf_bill.cell(w=120, h=40, txt="Roommate ", align='C', border=0)
        pdf_bill.cell(w=160, h=40, txt="Days Occupied ", align='C', border=0)
        pdf_bill.cell(w=120, h=40, txt="Owes ($) ", align='C', border=0, ln=1)

        # Text block for amount roommate 1 has to pay
        pdf_bill.set_font(family='Times', size=18, style='')
        pdf_bill.cell(w=120, h=40, txt=str(roommate1.name), align='C', border=0)
        pdf_bill.cell(w=160, h=40, txt=str(roommate1.days_in_unit), align='C', border=0)
        pdf_bill.cell(w=110, h=40, txt="{:.2f}".format(roommate1.pay_bill(bill, roommate2)), align='C', border=0, ln=1)

        # Text block for amount roommate 2 has to pay
        pdf_bill.cell(w=120, h=40, txt=str(roommate2.name), align='C', border=0)
        pdf_bill.cell(w=160, h=40, txt=str(roommate2.days_in_unit), align='C', border=0)
        pdf_bill.cell(w=110, h=40, txt="{:.2f}".format(roommate2.pay_bill(bill, roommate1)), align='C', border=0, ln=1)

        # Save file to current directory
        if ".pdf" not in str(self.file_name):
            self.file_name = str(self.file_name)+".pdf"
        else:
            pass
        pdf_bill.output(self.file_name)

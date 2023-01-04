class Bill(object):
    """
    Class defining the amount to be paid (bill) by both roommates over the given rental period (month, year)

    Paramters
    ----------
    amount: float - total amount of money owed by the roommates for the given pay period

    period: tuple (str, int) - period the amount is to be paid for (month, year)

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
    roommate_name : str - name of roommate in apartment

    days_in_unit : int - number of whole days the given roommate was in the unit

    Methods
    -----------
    pay_bill : arg: bill object - method of calculating how much the roommates have to pay based upon the bill (Bill instance)
    """

    def __init__(self, roommate_name, days_in_unit):
        self.roommate_name = roommate_name
        self.days_in_unit = days_in_unit

    def pay_bill(self, bill_instance, days_in_unit) -> float:
        """
        Assigns a bill to be paid by the roommate

        Parameters
        -----------
        bill_instance: Bill obj - the bill to be split and paid by roommates for given pay period and fractional occupancy

        days_in_unit: int - number of days roommate spent in the unit, used to calculate fraction of total bill to pay

        Returns
        -----------
        bill_amount: float - fraction of bill to be paid by roommate based upon number of days in unit

        """
        pass

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

    def __init__(self, file_name, roommate_name, rental_period, bill) -> None:
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
        bill_pdf: pdf file - file containing the fraction of the bill to be paid by each roommate for the given period
        """
        pass

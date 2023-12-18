class Bill:
    """
    Docstring : to update comments for functionality
    """
    def __init__(self, amount, date):
        self.amount = amount
        self.date = date


class Flatmate:
    """
    Docstring : to update comments for functionality
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, person2):
        to_pay= bill.amount * (self.days_in_house/(self.days_in_house
                                                +person2.days_in_house ))
        return to_pay

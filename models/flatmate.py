from models.bill import Bill


class Flatmate:

    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_in_house = days_in_house

    def to_pay(self, curr_bill: Bill, total_days: int) -> float:
        amount = (curr_bill.amount / total_days) * self.days_in_house
        return round(amount, 2)


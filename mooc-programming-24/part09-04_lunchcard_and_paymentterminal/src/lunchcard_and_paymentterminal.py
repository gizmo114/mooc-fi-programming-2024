# WRITE YOUR SOLUTION HERE:


class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        if payment >= 2.5:
            if payment > 2.5:
                self.funds += 2.5
                self.lunches += 1
                return payment - 2.5
            else:
                self.funds += 2.5
                self.lunches += 1
        else:
            return payment

    def eat_special(self, payment: float):
        if payment >= 4.3:
            if payment > 4.3:
                self.funds += 4.3
                self.specials += 1
                return payment - 4.3
            else:
                self.funds += 4.3
                self.specials += 1
        else:
            return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.balance >= 2.5:
            card.subtract_from_balance(2.5)
            self.funds += 2.5
            self.lunches += 1
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard):
        if card.balance >= 4.3:
            card.subtract_from_balance(4.3)
            self.funds += 4.3
            self.specials += 1
            return True
        else:
            return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)


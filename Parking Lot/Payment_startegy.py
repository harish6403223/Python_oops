from Payment_type import *


class Payment_strategy:
    def __init__(s):
        pass

    def payment_service(s, total_cost):
        # Switch case will be their to select payment among UPI, Cash, Online banking
        payment_type = UPI()
        payment_type.payment(total_cost)
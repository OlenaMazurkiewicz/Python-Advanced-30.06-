import uuid
from user import User

class Administrator(User):
    def __init__(self, username, userpass, email):
        super().__init__(username, userpass, email)
        self.supply = list()
        self.orders = list()
        self.reviews = list()

    def update_supply(self, suppliers_list):
        self.supply.clear()
        for supplier in suppliers_list:
            self.supply.extend(supplier.supply)

    def update_orders(self, customers_list):
        self.orders.clear()
        for customer in customers_list:
            self.orders.extend(customer.orders)

    def check_order(self, order):
        print(f"Checking order {order.id}")
        if not order.status == 'New':
            return order
        for supply in self.supply:
            if supply.item == order.item and supply.amount >= order.amount:
                order.status = 'Confirmed'
                return order
        order.status = 'On hold'
        return order


    def approve_review(self, review):
        print(f"approving review {review.customer}")
        if not review.status == 'Moderation':
            return reviews_list
        for review in reviews_list:
            if review.score <= 5:
                review.status = 'Published'
                return reviews_list
        review.status = 'Published'
        return review



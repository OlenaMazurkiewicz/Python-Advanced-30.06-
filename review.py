import uuid


class Review:
    def __init__(self, text, customer, score):
        self.text = list()
        self.customer = customer
        self.score = int(score)
        self.status = 'Moderation'

    def __str__(self):
        return f"Review {self.customer}: score {self.score}, {self.text}"

    def __repr__(self):
        return f"{self.customer}: score {self.score}, {self.text}"
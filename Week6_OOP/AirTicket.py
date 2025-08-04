
class AirTicket:
    """AirTicket class
    attributes passenger, departing airport, arriving airport, class, price
    """

    def __init__(self, passenger, depart, arrive, seat_class, price):
        self.passenger = passenger
        self.depart = depart
        self.arrive = arrive
        self.seat_class = seat_class
        self.price = price

    def __str__(self):
        out = f"{self.passenger} is flying from {self.depart} to {self.arrive}"
        out = out + f" in {self.seat_class} class for ${self.price}"
        return out


    def change_price(self, new_price, new_class):
        self.price = new_price
        self.seat_class = new_class


def tester():
    ticket1 = AirTicket("Suzy Que", "BOS", "LAX", "First", 1000)
    print(ticket1)
    ticket1.change_price(2000, "Business")
    print(ticket1)

if __name__ == "__main__":
    tester()

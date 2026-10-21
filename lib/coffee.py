#!/usr/bin/env python3

class Coffee:
    """Models a coffee sold at the bookstore."""

    SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, price):
        self.size = size  # goes through the setter below
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Only accept Small, Medium, or Large
        if value in Coffee.SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1  # tipping raises the price by 1

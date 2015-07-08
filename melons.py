"""This file should have our melon-type classes in it."""





class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 5.00 * qty   
        if qty >= 3:
            total *= 0.75
        return total

class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 5.00 * qty   
        if qty >= 5:
            total *= 0.5
        return total

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = (1.00 + 5.00) * 1.5 * qty  

        return total


class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 5.00 * 1.5 * qty  

        return total

class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 5.00 * 1.5 * qty  

        return total

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 5.00 * qty  

        return total

class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 5.00 * 1.5 * qty  

        return total

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 5.00 * 2 * 1.5 * qty  

        return total

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring','Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = (5.00 + 1.00) * qty  

        return total
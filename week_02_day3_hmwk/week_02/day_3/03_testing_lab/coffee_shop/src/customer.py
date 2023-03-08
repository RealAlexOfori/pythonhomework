class Customer:
    
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        # self.age = age

    def reduce_cash(self,amount):
        self.wallet -= amount

    


# A Customer should be able to buy
# a Drink from the Coffee Shop, reducing 
# the money in its wallet (-=)
# and increasing the money in the Coffee Shop's till (+=)
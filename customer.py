class Customer:
    def __init__(self, first_name, last_name, account_no, rented_dvd=None):
        self.first_name = first_name
        self.last_name = last_name
        self.account_no = account_no
        self.rented = rented_dvd  # list

    def get_customer_all(self):
        return [self.account_no, self.first_name, self.last_name, f'{", ".join(self.rented)}']

    def get_name(self):
        return self.first_name + ' ' + self.last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_account(self):
        return self.account_no

    def get_rented(self):
        return self.rented

    def set_first_name(self, name):
        self.first_name = name

    def set_last_name(self, name):
        self.last_name = name

    def set_account_no(self, number):
        self.account_no = number

    def add_rented(self, dvd):
        return self.rented.append(dvd)

    #overloads
    def __lt__(self, other):
        return self.account_no < other.account_no

    def __gt__(self, other):
        return self.account_no > other.account_no

    def __le__(self, other):
        return self.account_no <= other.account_no

    def __ge__(self, other):
        return self.account_no >= other.account_no

    def __str__(self):
        return (f' Name: {self.first_name} {self.last_name}\n'
                f' Account number: {self.account_no}\n'
                f' DVDs rented: {", ".join(self.rented)}\n'
                )


# if __name__ == '__main__':
#
#     custo = Customer("frank", "Nathaniel", "1234", ["The last of us", "The conjuring"])
#     print(custo)
#     print(custo.set_last_name("finnegan"))
#     print(custo.get_name())
class Account:
    def __init__(self, owner, balance):
        self.owner = owner        # public
        self._type = "Savings"    # protected (convention)
        self.__balance = balance  # private (name mangled)

    def show_balance(self):
        print(f"{self.owner}'s balance is ₹{self.__balance}")
    def _protected_method(self):
        pass


a = Account("Alice", 5000)

print(a.owner)       
print(a._type)       
  


print(a._Account__balance)  
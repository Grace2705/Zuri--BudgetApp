class Budget:
    category_record = []
    def __init__(self, category , balance = 0):
        self.category = category
        self.balance = balance
        Budget.category_record.append(self)
        
    
    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited {amount} into your {self.category} Budget, your balance is {self.balance}")
        return

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient Balance, unable to withdraw')
        else:
            self.balance -= amount
        print(f"You have withdrawn {amount} from your {self.category} Budget, your balance is {self.balance}")
        return 
    
    def category_balance(self):
        print(f'Your balance is {self.balance} for your {self.category} budget')


    def transfer(self, to_category, amount):
        if (isinstance(to_category, Budget)):
            if amount > self.balance:
                print('Insufficient Fund, Transfer failed.')    
            else:
                to_category.balance += amount
                self.balance -= amount
                print(f'You have transferred {amount} from {self.category} budget')
                print(f'Your balance in {self.category} budget is {self.balance}')
                
        else:
            print('Please instantiate budget')
        return


   # A class method that returns the list of budget already instantiated 
    @classmethod
    def budget_list(cls):
        if len(Budget.category_record)== 0:
            print("No budgets created")
        else:
            print("Budget Categories:")
            for item in Budget.category_record:
                print(item.category)


    # A class method that returns the list of budget already instantiated and their balance 
    # and the total amount in the budget
    @classmethod
    def full_report(cls):
        if len(Budget.category_record)== 0:
            print("No budgets created")
        else:
            total = 0
            print("Budget Balances:")
            for item in Budget.category_record:
                total += item.balance
                print(f"{item.category} : {item.balance}")
            print('----------')
            print(f'Total : {total}')




# Instantiate Food budget 
food = Budget('food')

# deposit 200 into food budget
food.deposit(200)

# withdraw 100 from food budget
food.withdraw(100)

#instantaite rent budget
rent = Budget('house', 5000)

# check balance of rent budget
rent.category_balance()

# Transfer from rent to food budget
rent.transfer(food, 1500)

# check balance again
food.category_balance()

#  give list of all budgets
Budget.budget_list()
# give full report of buget(balance and total)
Budget.full_report()
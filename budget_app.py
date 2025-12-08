#Build a Budget App that tracks spending in different categories and can show the relative spending percentage.
class Category: #Category class that accepts the name as an argument
    def __init__(self, name):
        self.name = name
        self.ledger = [] #instance attribute ledger, contains a list of transactions

    def __str__(self):
        print(self.name.center(30, '*')) #display a title line of 30 characters with the category name centered between * characters.
        total = 0
        for l in self.ledger:
            print(f'{l[1][:23]} {str(l[0]).rjust(29 - len(l[1]), ' ')}') #display the description left-aligned with a limit of 23 characters and the amount right-aligned
            total += l[0]
        return (f'Total: {total}') #return a final line with the total balance

    def deposit(self, amount, description = ' '): #deposit method with an amount and a optional description (empty string by default)
        regis = [amount, description] #create a list that represent a new register
        self.ledger.append(regis) #the new register is append to the ledger list
        print(f'Amount: {amount}, Description: {description} has been registered')
        return
    
    def get_balance(self): #A get_balance method that returns the current category balance based on ledger.
        total = 0
        for a in self.ledger: #a iterates in the ledger list of lists
            total += a[0] #sum to total the amount of each list inside of ledger, indexing in position 0
        print(f'The total amount is {total}.') #print a message with the total balance
        return

    def check_funds(self, amount): #check_funds method that accepts an amount and return a boolean if it exceeds the total balance
        total = 0
        for a in self.ledger: #a iterates in the ledger list of lists
            total += a[0] #sum the total amount of each list inside of ledger, indexing in position 0
        if amount < total: #check if the amount input by the user exceeds or not the total balance
            return True
        return False

    def withdraw(self, amount, description = ' '): #withdraw method with an amount and a optional description (empty string by default)
        withdrawal = False
        if self.check_funds(amount): #call the check_funds for verify if the amount exceeds or not the total
            withdrawal = True #change the value of the boolean variable
            regis = [-abs(amount), description] #the register should have the amount expressed as a negative number
            self.ledger.append(regis) #append to the ledger the new register with the withdrawal
            print(f'{amount} withdrawal succesfully.')
        return withdrawal #return a boolean if the withdrawal was succesfully or not

    def transfer(self, amount, category): #transfer method receive an amount and a category instance
        auth_transf = False
        if self.check_funds(amount): #call the check_funds for verify if the amount exceeds or not the total
            self.withdraw(amount, (f'Transfer to {category.name}')) #call the withdraw method with amount and a description including the category name
            category.deposit(amount, (f'Transfer from {self.name} to {category.name}')) #call the deposit method with amount and a description with the source name and the destination name
            auth_transf = True
        return auth_transf #return a boolean if the transfer was succesfully or not

food = Category('Food') #Total spend: 760
clothing = Category('Clothing') #Total spend: 225
electronics = Category('Electronics') #Total spend: 800
medicines = Category('Medicines') #580

food.deposit(750, 'breakfast')
food.deposit(850, 'lunch')
food.deposit(250, 'dinner')
food.withdraw(350, 'restaurant')
food.transfer(410, medicines)

clothing.deposit(450, 'shoes')
clothing.deposit(200, 'T-Shirts and Jackets')
clothing.withdraw(75, 'spend in a local store')
clothing.transfer(150, electronics)

electronics.deposit(550, 'smartphone and accesories')
electronics.deposit(450, 'PC components')
electronics.withdraw(800, 'PC repair')

medicines.deposit(1000)
medicines.withdraw(195, 'personal medical-kit')
medicines.transfer(385, food)

#Solution one
def withdrawals(category): #withdrawals function obtain the total whitdrawals for each category (receive a category object, return a negative number)
    return sum([w[0] for w in category.ledger if w[0] < 0])
#spend_by_category function print a message with each category followed by the percentage of spent
def spend_by_category(category, categoryTwo, categoryThree, categoryFour):
    total = withdrawals(category) + withdrawals(categoryTwo) + withdrawals(categoryThree) + withdrawals(categoryFour) #contains the total value of withdrawals between all categories (negative number)
    print(('Percentage spent by category').center(30, '*')) #title string limited by 30 characters centered by *
    #obtain and print the category name and the percentage of spent for each category (round value, right aligned)
    print(f'{category.name}: {str(round(abs(withdrawals(category)) / abs(total) * 100)).rjust(27 - len(category.name), ' ')}%')
    print(f'{categoryTwo.name}: {str(round(abs(withdrawals(categoryTwo)) / abs(total) * 100)).rjust(27 - len(categoryTwo.name), ' ')}%')
    print(f'{categoryThree.name}: {str(round(abs(withdrawals(categoryThree)) / abs(total) * 100)).rjust(27 - len(categoryThree.name), ' ')}%')
    print(f'{categoryFour.name}: {str(round(abs(withdrawals(categoryFour)) / abs(total) * 100)).rjust(27 - len(categoryFour.name), ' ')}%')
    return ''

#Solution two (less efficient)
def percentage_spend_category(food, clothing, electronics, medicines): #function that calculates the percentage of spent by category (withdrawals and transfers)
    food_w, cloth_w, electr_w, medi_w = 0, 0, 0, 0 #variable that contains the total value of withdrawals for each category (negative number)
    for fw in food.ledger:
        if fw[0] < 0: #check if a value inside the category ledger is a negative number
            food_w += fw[0] #sum that value to the variable
    for ch in clothing.ledger:
        if ch[0] < 0:
            cloth_w += ch[0]
    for ew in electronics.ledger:
        if ew[0] < 0:
            electr_w += ew[0]
    for mw in medicines.ledger:
        if mw[0] < 0:
            medi_w += mw[0]
    total = food_w + cloth_w + electr_w + medi_w #obtain the total value of withdrawals for all the categories (negative number)
    print(('Percentage spent by category').center(30, '*'))
    print(f'{food.name}: {str(round(abs(food_w) / abs(total) * 100)).rjust(27 - len(food.name), ' ')}%') #obtain and print the percentage of spent for each category (round value)
    print(f'{clothing.name}: {str(round(abs(cloth_w) / abs(total) * 100)).rjust(27 - len(clothing.name), ' ')}%')
    print(f'{electronics.name}: {str(round(abs(electr_w) / abs(total) * 100)).rjust(27 - len(electronics.name), ' ')}%')
    print(f'{medicines.name}: {str(round(abs(medi_w) / abs(total) * 100)).rjust(27 - len(medicines.name), ' ')}%')
    return ''


print(spend_by_category(food, clothing, electronics, medicines))
print(percentage_spend_category(food, clothing, electronics, medicines))

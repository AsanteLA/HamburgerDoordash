#AGroup 12
#Group Work 1
#Hamburger Doordash
#Caleb Kamalu
#Omar Aburouss
#Asante Laryea-Akrong
#Ryan Hafen 
#Logan Stone

#Import Random
import random

# Create an Order class
class Order:
    def __init__(self):
        self.burger_count = self.randomBurgers()

    def randomBurgers(self):
        return random.randint(1, 20)

# Create a Person class
class Person:
    def __init__(self):
        self.customer_name = self.randomName()

    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(asCustomers)

# Create a Customer class that inherits from the Person class
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()

# Create a queue to hold customers
customer_queue = []

# Add 100 customers to the queue
for i in range(100):
    customer = Customer()
    customer_queue.append(customer)

# Create a dictionary to hold customer information
customer_info = {}

# Loop over each customer in the queue and update their total burgers ordered in the dictionary
for customer in customer_queue:
    customer_name = customer.customer_name
    burger_count = customer.order.burger_count
    if customer_name in customer_info:
        customer_info[customer_name] += burger_count
    else:
        customer_info[customer_name] = burger_count

# Convert the dictionary to a list of tuples and sort by value in descending order
sorted_customers = sorted(customer_info.items(), key=lambda x: x[1], reverse=True)

# Print out each customer and their total burgers ordered
for customer in sorted_customers:
    # Pad the customer name with spaces to make it 19 characters long
    customer_name = customer[0].ljust(19)
    # Get the total number of burgers ordered
    total_burgers = customer[1]
    # Print out the customer name and total burgers ordered
    print(f"{customer_name} {total_burgers} burgers consumed")

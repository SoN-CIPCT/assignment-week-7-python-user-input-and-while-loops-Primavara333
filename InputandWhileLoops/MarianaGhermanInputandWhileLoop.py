pizza_orders = ['Margherita', 'Pepperoni', 'BBQ Chicken', 'Hawaiian', 'Vegetarian']
finished_pizzas = []
for pizza in pizza_orders:
    print(f"Your pizza pie {pizza} is finished!")
    finished_pizzas.append(pizza)
for finished_pizza in finished_pizzas:
    print(f"The pizza {finished_pizza} was made.")
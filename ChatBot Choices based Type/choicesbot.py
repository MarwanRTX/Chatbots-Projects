from flask import Flask, render_template, request
from markupsafe import escape  # Correct import for escaping

app = Flask(__name__)

class ShopBot:
    menu = {
        "Lemon": 3,
        "Tea": 2,
        "Coffee": 5,
        "Pizza": 10,
        "Burger": 15
    }
    address = "123 Main Street, Cityville"
    delivery_available = True
    delivery_cities = ["Cityville", "Townsburg", "Villageton"]
    
    def get_menu(self):
        return self.menu.items()

    def get_price(self, item):
        if item in self.menu:
            return f"The price of {item} is ${self.menu[item]}"
        return "Sorry, we don't have that item. Please check the menu."
    
    def get_shop_info(self):
        delivery_status = "Yes" if self.delivery_available else "No"
        cities = ", ".join(self.delivery_cities)
        return f"Address: {self.address}<br>Delivery Available: {delivery_status}<br>Delivery Cities: {cities}"

bot = ShopBot()

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    response = None
    if request.method == 'POST':
        name = escape(request.form.get("name", "").strip())
        choice = escape(request.form.get("choice", "").strip())
        
        # Handle first-time name submission
        if not choice:
            return render_template('index.html', name=name, menu=bot.get_menu())
        
        # Handle choices after name is established
        # Change the menu response generation to use <li> elements
        if choice == "menu":
            menu_items = [f"<li>{item}: ${price}</li>" for item, price in bot.get_menu()]
            response = f"<ul>{''.join(menu_items)}</ul>"
        elif choice == "shop_info":
            response = bot.get_shop_info()
        else:
            response = bot.get_price(choice)
        
        return render_template('index.html', name=name, response=response, menu=bot.get_menu())
    
    return render_template('index.html', menu=bot.get_menu())

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html", title="The Pizza Patch")

@app.get("/menu/")
def menu():
    pizzas = [
        {
            "name": "mozzarella",
            "price": "200 UAH",
            "ingredients": "flour, eggs, sugar, salt, water, oil, yeast, Fresh or low-moisture mozzarella, Extra virgin olive oil, Salt & pepper, Fresh basil, garlic, chili flakes"
        },
        {
            "name": "pepperoni",
            "price": "250 UAH",
            "ingredients": "flour, eggs, sugar, salt, water, oil, yeast, tomato sauce, pepperoni, cheese mozzarella, chili pepper"
        },
        {
            "name": "four cheese",
            "price": "300 UAH",
            "ingredients": "flour, eggs, sugar, salt, water, oil, yeast, cheese mozzarella, cheese parmesan, cheese dor bleu, cheese cheddar"
        }
    ]
    context = {
        "pizzas": pizzas,
        "title": "Mega menu"
    }
    return render_template("menu.html", **context)

if __name__ == "__main__":
    app.run(debug=True)

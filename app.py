from groq import Groq

products = {}

# ------------------------
# Load Dummy Data
# ------------------------

def load_dummy_data():
    products.clear()

    products[1] = {"name": "Laptop", "price": 40000}
    products[2] = {"name": "Smartphone", "price": 25000}
    products[3] = {"name": "Tablet", "price": 18000}
    products[4] = {"name": "Smart Watch", "price": 7000}
    products[5] = {"name": "Wireless Earbuds", "price": 3500}
    products[6] = {"name": "Bluetooth Speaker", "price": 4500}
    products[7] = {"name": "Gaming Mouse", "price": 1200}
    products[8] = {"name": "Mechanical Keyboard", "price": 3200}
    products[9] = {"name": "Monitor", "price": 15000}
    products[10] = {"name": "Printer", "price": 8500}
    products[11] = {"name": "External Hard Drive", "price": 6000}
    products[12] = {"name": "SSD 1TB", "price": 7500}
    products[13] = {"name": "USB Flash Drive", "price": 800}
    products[14] = {"name": "Power Bank", "price": 2000}
    products[15] = {"name": "WiFi Router", "price": 2800}
    products[16] = {"name": "Webcam", "price": 3000}
    products[17] = {"name": "Projector", "price": 28000}
    products[18] = {"name": "DSLR Camera", "price": 55000}
    products[19] = {"name": "Graphics Card", "price": 42000}
    products[20] = {"name": "Gaming Console", "price": 48000}

    return "Dummy data loaded successfully."

# ------------------------
# View Products
# ------------------------

def display_products():

    if not products:
        return "No products available."

    text = ""

    for pid, p in products.items():
        text += f"ID : {pid}\n"
        text += f"Name : {p['name']}\n"
        text += f"Price : ₹{p['price']}\n"
        text += "-" * 35 + "\n"

    return text

# ------------------------
# Add Product
# ------------------------

def add_product(pid, name, price):

    try:
        pid = int(pid)
        price = float(price)

        if pid in products:
            return "Product ID already exists."

        products[pid] = {
            "name": name,
            "price": price
        }

        return "Product Added Successfully."

    except:
        return "Invalid Input."

# ------------------------
# Search Product
# ------------------------

def search_product(pid):

    try:
        pid = int(pid)

        if pid in products:

            p = products[pid]

            return f"""
Product Found

ID : {pid}
Name : {p['name']}
Price : ₹{p['price']}
"""

        return "Product Not Found."

    except:
        return "Invalid Product ID."

# ------------------------
# Update Product
# ------------------------

def update_product(pid, name, price):

    try:
        pid = int(pid)
        price = float(price)

        if pid not in products:
            return "Product Not Found."

        products[pid]["name"] = name
        products[pid]["price"] = price

        return "Product Updated Successfully."

    except:
        return "Invalid Input."

# ------------------------
# Delete Product
# ------------------------

def delete_product(pid):

    try:
        pid = int(pid)

        if pid in products:
            del products[pid]
            return "Product Deleted Successfully."

        return "Product Not Found."

    except:
        return "Invalid Product ID."

# ------------------------
# Groq AI
# ------------------------

client = Groq(api_key="Your_Groq_API_Key")

def ai_product_details(query):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are an Electronics Product Expert."
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return response.choices[0].message.content
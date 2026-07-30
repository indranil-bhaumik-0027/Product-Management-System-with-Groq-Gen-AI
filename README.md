# 🛒 Product Management System with Groq Gen AI

An AI-powered **Product Management System** built using **Python** and **Gradio**. The application allows users to perform CRUD (Create, Read, Update, Delete) operations on product data and interact with an AI assistant for product-related queries using **Groq LLM**.

---

## 🚀 Features

- 📦 Load Dummy Product Data
- 📋 View All Products
- ➕ Add New Product
- 🔍 Search Product by ID
- ✏️ Update Existing Product
- ❌ Delete Product
- 🤖 AI Product Assistant using Groq LLM
- 🎨 Interactive Gradio Web Interface

---

## 🛠️ Tech Stack

- Python
- Gradio
- Groq LLM API
- Pandas
- Google GenAI
- OpenAI SDK
- python-dotenv

---

## 📂 Project Structure

```
Product-Management-System/
│
├── gui.py              # Gradio User Interface
├── app.py              # Backend Logic
├── requirements.txt    # Required Python Packages
├── .env                # API Keys (Not uploaded to GitHub)
├── README.md
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Product-Management-System.git
```

Move into the project folder

```bash
cd Product-Management-System
```

---

### 2. Create a Virtual Environment (Recommended)

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a **.env** file inside the project folder.

Example

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key
```

> **Note:** Only include the API keys that your implementation actually uses.

---

## ▶️ Run the Project

```bash
python gui.py
```

Gradio will launch the application in your browser.

Example

```
Running on local URL:
http://127.0.0.1:7860
```

---

## 💻 Application Modules

### 📦 Load Dummy Data

Loads predefined product records into the application.

---

### 📋 View Products

Displays all available products.

---

### ➕ Add Product

Add a new product by entering

- Product ID
- Product Name
- Price

---

### 🔍 Search Product

Search any product using its Product ID.

---

### ✏️ Update Product

Update

- Product Name
- Product Price

using Product ID.

---

### ❌ Delete Product

Remove a product permanently using Product ID.

---

### 🤖 AI Product Assistant

Ask natural language questions such as

- Tell me about Product 101
- Which product is the most expensive?
- Suggest a product under ₹1000
- Explain the specifications of Product X

The response is generated using the Groq Large Language Model.

---

## 📸 Screenshot

Add screenshots of the application here.

Example

```
images/
    home.png
    add_product.png
    ai_assistant.png
```

---

## 📋 Requirements

```
groq
python-dotenv
notebook
pandas
openai
google-genai
```

Or install directly

```bash
pip install groq python-dotenv notebook pandas openai google-genai
```

---

## 🎯 Learning Outcomes

This project demonstrates

- CRUD Operations
- Python Programming
- List and Dictionary Manipulation
- Gradio GUI Development
- AI Integration using Groq LLM
- Prompt Engineering Basics
- Environment Variable Management
- API Integration
- Generative AI Applications

---

## 🔮 Future Enhancements

- SQLite/MySQL Database Integration
- User Authentication
- Product Image Upload
- Inventory Management
- Sales Dashboard
- PDF Report Generation
- Excel Export
- Voice-enabled AI Assistant
- Barcode Scanner
- Cloud Deployment

---

## 👨‍💻 Author

**INDRANIL BHAUMIK**

- GitHub: https://github.com/indranil-bhaumik-0027

---

## 📄 License

This project is developed for educational and learning purposes.

Feel free to fork, modify, and enhance it.

---

## ⭐ Support

If you found this project helpful,

⭐ Star this repository

🍴 Fork it

🛠️ Contribute to improve it

Happy Coding! 🚀

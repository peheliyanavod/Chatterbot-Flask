# 💬 ChatBot — AI Conversational Assistant

A simple yet powerful **AI ChatBot** built using **Flask**, **ChatterBot**, and **jQuery**, designed to simulate human-like conversations directly in your browser.  
This application demonstrates how to integrate a machine learning–based chatbot with a clean and responsive front-end interface.

> “Talk with your AI assistant — built with Python and Flask!”

---

## 🚀 Features

✅ Interactive chat interface (no page reloads)  
✅ AI-powered responses using **ChatterBot**  
✅ Trained with **English corpus** for general conversations  
✅ Real-time message exchange using **AJAX (jQuery)**  
✅ Lightweight front-end with clean UI & CSS styling  
✅ Flask-powered backend for simplicity and scalability  

---

## 🧠 Tech Stack

### 🖥️ Frontend
- **HTML5**  
- **CSS3** (Custom responsive design)  
- **jQuery** for AJAX requests  

### ⚙️ Backend
- **Python 3**  
- **Flask** — web framework  
- **ChatterBot** — AI chatbot logic  
- **ChatterBot Corpus** — pre-trained English conversation dataset  

---

## ⚙️ Installation & Setup

Follow these steps to run the ChatBot locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/chatbot-app.git
cd chatbot-app
```
### 2️⃣ Create and activate a virtual environment
```
python -m venv venv
venv\Scripts\activate      # For Windows
# OR
source venv/bin/activate   # For macOS/Linux
```
### 3️⃣ Install dependencies
```
pip install flask chatterbot chatterbot_corpus
pip freeze > requirements.txt
```
### 4️⃣ Run the Flask app
```
python app.py
```
### 5️⃣ Access the ChatBot

Open your browser and visit 👉 http://127.0.0.1:5000

---


### 💡 Example Usage

User: Hello
Bot: Hi there! How are you?

User: What is your name?
Bot: You can call me ChatBot.

User: Who created you?
Bot: I was created by Peheliya Dhanuka Navod using Python and Flask! 😄


### 🧩 How It Works

The frontend (index.html) provides a clean chat interface.
When the user types a message and hits “Send”, jQuery sends it to Flask via an AJAX request (/get_response).
Flask passes the message to ChatterBot, which processes it and generates a relevant response.
The response is returned as JSON and displayed in the chat interface.


### 🎨 UI Preview

<img width="730" height="762" alt="image" src="https://github.com/user-attachments/assets/7dc5d866-bfb9-4676-90ba-841febc222e1" />


### 🔮 Future Enhancements

🧠 Add contextual memory to improve conversation continuity
🌍 Train with domain-specific datasets (e.g., healthcare, education, tourism)
💬 Integrate with a modern frontend (React or Vue.js)
🔊 Enable speech recognition and text-to-speech
☁️ Deploy on Vercel, Render, or AWS

### 👨‍💻 Author

Peheliya Dhanuka Navod
Trainee Software Engineer | Software Engineering Undergraduate at the University of Kelaniya

📧 Email: hwpeheliya@gmail.com
🌐 Portfolio: https://react-portfolio-gray-chi.vercel.app
💼 LinkedIn: linkedin.com/in/peheliya-danuka
✍️ Medium: medium.com/@hwpeheliya


⭐ If you found this project interesting, please give it a star!




# 🌿 AI-Powered Carbon Footprint Calculator

A **Streamlit-based web application** that calculates your annual carbon footprint based on your lifestyle habits — including transportation, electricity use, dietary preferences, and household waste. Built with **Google Gemini AI** integration for smart eco tips and real-time climate insights.

[🌐 Live Demo → Click to try the app](https://carbon-app.streamlit.app)

## 💡 What This App Does

🔍 **Estimate your CO₂ emissions** across key areas:
- 🚗 **Transportation**: Based on daily commute distance  
- 💡 **Electricity**: Based on average kWh usage  
- 🍽️ **Diet**: Type of meals and frequency  
- 🗑️ **Waste**: Approximate household waste levels
  
📊 **Visual Insights:**
- Pie charts for emissions by category
- Tree equivalence (how many trees needed to offset)
- Gemini AI-powered personalized sustainability suggestions
  
🌦️ **Extra Features:**
- Real-time climate change data
- Downloadable emission reports
- Built-in Gemini chatbot for eco-advice
---
## 🛠️ Tech Stack

| Component      | Technology            |
|----------------|------------------------|
| Frontend       | Streamlit              |
| AI Integration | Google Gemini via `generativeai` |
| ML Model       | `MLPRegressor` (Scikit-learn) |
| Data Handling  | CSV, Pandas, Matplotlib |
| Styling        | Custom CSS & HTML      |
---
## 🚀 How to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/chinmayeegithubid/carbon-footprint-calculator.git
   cd carbon-footprint-calculator
2.Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate    # Windows
3.Install Dependencies
pip install -r requirements.txt
4.Set Google API Key
Create a .env file with:
GOOGLE_API_KEY=your_actual_key_here
5.Run the App
streamlit run app.py

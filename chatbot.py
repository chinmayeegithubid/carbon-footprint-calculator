import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load Gemini API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def chatbot_ui():
    # 💬 Button aligned to the left
    st.markdown("""
        <div style='margin-top: 30px; margin-bottom: -10px; text-align: left;'>
            <button style="
                background-color: #007F5F;
                border: none;
                color: white;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: 600;
                border-radius: 30px;
                cursor: pointer;
                box-shadow: 0px 4px 12px rgba(0,0,0,0.2);">
                💬 Need Assistance?
            </button>
        </div>
    """, unsafe_allow_html=True)

    with st.expander("🤖 Eco-Chatbot Assistant", expanded=False):
        st.markdown("Type your question below to get eco-friendly tips, guidance, or help using the app.")

        user_input = st.text_input("🌍 Ask a question:", placeholder="e.g., How to reduce carbon emissions?")
        if user_input:
            with st.spinner("Generating answer..."):
                try:
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    response = model.generate_content(user_input)
                    st.markdown("**🧠 EcoBot:**")
                    st.success(response.text)
                except Exception as e:
                    st.error("⚠️ Sorry! The chatbot couldn't respond.")
                    st.exception(e)
# -------------------- 🌿 Personalized Tips Generator --------------------
def generate_personalized_tips(transport, electricity, diet, waste):
    prompt = f"""
The user's yearly carbon emissions are:
- 🚗 Transportation: {transport:.2f} kgCO₂
- ⚡ Electricity: {electricity:.2f} kgCO₂
- 🍽️ Diet: {diet:.2f} kgCO₂
- 🗑️ Waste: {waste:.2f} kgCO₂

Based on this, suggest 3 beginner-friendly and personalized sustainability tips to reduce their footprint.
Keep them positive, practical, and actionable.
"""

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        if hasattr(response, 'text'):
            return response.text.strip()
        else:
            return "⚠️ Gemini returned an unexpected format."

    except Exception as e:
        return f"❌ Gemini AI failed to generate tips.\n\n**Error:** {str(e)}"
import streamlit as st

# --- 1. THE FUTURISTIC THEME ---
def set_futuristic_theme():
    st.markdown("""
    <style>
    .stApp { background-color: #0a0e14; color: #00ff41; font-family: 'Courier New', monospace; }
    h1 { color: #00d4ff; text-shadow: 0 0 10px #00d4ff; text-align: center; }
    .stButton > button { border: 1px solid #00ff41; background: transparent; color: #00ff41; width: 100%; }
    .stButton > button:hover { background: #00ff41; color: #0a0e14; }
    </style>
    """, unsafe_allow_html=True)

set_futuristic_theme()

# --- 2. CALCULATOR LOGIC ---
def addition(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "ERROR: DIV_BY_ZERO"

# --- 3. UI LAYOUT ---
st.title("⚡ CALCULATOR")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("INPUT_A", value=0)
with col2:
    num2 = st.number_input("INPUT_B", value=0)

operation = st.radio("SELECT_PROTOCOL", ["ADD", "SUBTRACT", "MULTIPLY", "DIVIDE"])

if st.button("EXECUTE_CALCULATION"):
    if operation == "ADD": result = addition(num1, num2)
    elif operation == "SUBTRACT": result = subtract(num1, num2)
    elif operation == "MULTIPLY": result = multiply(num1, num2)
    else: result = divide(num1, num2)
    
    st.success(f"OUTPUT_STREAM: {result}")
    st.balloons() # Just for extra flair!
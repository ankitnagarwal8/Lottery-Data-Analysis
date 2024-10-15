import streamlit as st
import time
import plotly.graph_objects as go

# Define a function to style the app
def set_page_style():
    st.markdown(
        """
        <style>
        body {
            background-color: #f4f4f4;
        }
        .stButton>button {
            color: white;
            background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%);
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #ff6f61;
        }
        .stSlider {
            color: #FF416C !important;
        }
        </style>
        """, unsafe_allow_html=True
    )

# Call the style function
set_page_style()

# Animated loading bar function
def show_loading_bar(duration=2):
    with st.spinner('Calculating...'):
        time.sleep(duration)

# Create Plotly chart for enhanced visualization
def display_probability_chart(probability, n_tickets):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = probability,
        title = {'text': f"Winning Probability ({n_tickets} tickets)"},
        delta = {'reference': 0.00001},
        gauge = {
            'axis': {'range': [0, 1], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "lightblue"},
            'steps': [
                {'range': [0, 0.5], 'color': 'lightgray'},
                {'range': [0.5, 1], 'color': 'blue'}]
        }
    ))
    st.plotly_chart(fig)

# Define the factorial and combination functions as before
def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i
    return final_product

def combinations(n, k):
    numerator = factorial(n)
    denominator = factorial(n - k)
    return numerator / denominator

# Main app logic
st.title("🎨 Colorful Lottery Probability Dashboard")
st.markdown('---')

# One ticket probability calculation with animation
user_numbers_input = st.text_input("🎫 Enter your 6 chosen numbers (comma-separated):", '2, 43, 22, 23, 11, 5')
user_numbers = [int(num) for num in user_numbers_input.split(',')]

if st.button('🎰 Calculate One Ticket Probability'):
    show_loading_bar()
    n_combinations = combinations(49, 6)
    probability_one_ticket = 1 / n_combinations
    percentage_form = probability_one_ticket * 100
    st.success(f"Your chances of winning the lottery with the numbers {user_numbers} are {percentage_form:.7f}%")
    display_probability_chart(probability_one_ticket, 1)

# Multiple tickets probability
n_tickets = st.number_input("🎟️ Enter the number of tickets you want to buy:", min_value=1, step=1)
if st.button('🎰 Calculate Multiple Ticket Probability'):
    show_loading_bar()
    probability = n_tickets / combinations(49, 6)
    st.success(f"Your chances of winning with {n_tickets} tickets are {probability * 100:.6f}%")
    display_probability_chart(probability, n_tickets)

# Probability of matching fewer than 6 numbers
n_winning_numbers = st.slider("🔢 Select how many winning numbers to match (from 2 to 5):", 2, 5)
if st.button('🎯 Calculate Probability of Matching Fewer Than 6 Numbers'):
    show_loading_bar()
    n_combinations_ticket = combinations(6, n_winning_numbers)
    n_combinations_remaining = combinations(43, 6 - n_winning_numbers)
    successful_outcomes = n_combinations_ticket * n_combinations_remaining
    probability = successful_outcomes / combinations(49, 6)
    st.success(f"Your chances of having {n_winning_numbers} winning numbers are {probability * 100:.6f}%")

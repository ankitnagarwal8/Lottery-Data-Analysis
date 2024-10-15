import streamlit as st

# Define the factorial function
def factorial(n):
    final_product = 1
    for i in range(n, 0, -1):
        final_product *= i  # Fix the typo in variable name
    return final_product

# Define the combinations function
def combinations(n, k):
    numerator = factorial(n)
    denominator = factorial(n - k)
    return numerator / denominator

# Define the function for one ticket probability
def one_ticket_probability(user_numbers):
    n_combinations = combinations(49, 6)
    probability_one_ticket = 1 / n_combinations
    percentage_form = probability_one_ticket * 100
    
    st.write(f'''Your chances to win the big prize with the numbers {user_numbers} are {percentage_form:.7f}%.
In other words, you have a 1 in {int(n_combinations):,} chances to win.''')

# Define the function for multiple tickets probability
def multi_ticket_probability(n_tickets):
    n_combinations = combinations(49, 6)
    probability = n_tickets / n_combinations
    percentage_form = probability * 100
    
    if n_tickets == 1:
        st.write(f'''Your chances to win the big prize with one ticket are {percentage_form:.6f}%.
In other words, you have a 1 in {int(n_combinations):,} chances to win.''')
    else:
        combinations_simplified = round(n_combinations / n_tickets)
        st.write(f'''Your chances to win the big prize with {n_tickets:,} different tickets are {percentage_form:.6f}%.
In other words, you have a 1 in {combinations_simplified:,} chances to win.''')

# Define the function for less than 6 winning numbers probability
def probability_less_6(n_winning_numbers):
    n_combinations_ticket = combinations(6, n_winning_numbers)
    n_combinations_remaining = combinations(43, 6 - n_winning_numbers)
    successful_outcomes = n_combinations_ticket * n_combinations_remaining
    
    n_combinations_total = combinations(49, 6)
    probability = successful_outcomes / n_combinations_total
    probability_percentage = probability * 100
    combinations_simplified = round(n_combinations_total / successful_outcomes)
    
    st.write(f'''Your chances of having {n_winning_numbers} winning numbers with this ticket are {probability_percentage:.6f}%.
In other words, you have a 1 in {int(combinations_simplified):,} chances to win.''')

# Streamlit app logic
st.title('Lottery Probability Calculator')

# Input for one ticket probability
user_numbers_input = st.text_input("Enter your 6 chosen numbers (comma-separated):", '2, 43, 22, 23, 11, 5')
user_numbers = [int(num) for num in user_numbers_input.split(',')]
if st.button('Calculate One Ticket Probability'):
    one_ticket_probability(user_numbers)

# Input for multiple ticket probability
n_tickets = st.number_input("Enter the number of tickets you want to buy:", min_value=1, step=1)
if st.button('Calculate Multiple Ticket Probability'):
    multi_ticket_probability(n_tickets)

# Input for probability of matching fewer than 6 numbers
n_winning_numbers = st.slider("Select how many winning numbers to match (from 2 to 5):", 2, 5)
if st.button('Calculate Probability of Matching Fewer Than 6 Numbers'):
    probability_less_6(n_winning_numbers)

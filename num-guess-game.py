# import streamlit as st
# import random

# # Initialize session state variables if they don't exist
# if 'random_number' not in st.session_state:
#     st.session_state.random_number = random.randint(1, 100)
# if 'attempts' not in st.session_state:
#     st.session_state.attempts = 0
# if 'max_attempts' not in st.session_state:
#     st.session_state.max_attempts = None
# if 'game_over' not in st.session_state:
#     st.session_state.game_over = False
# if 'custom_range' not in st.session_state:
#     st.session_state.custom_range = (1, 100)

# # Streamlit page settings
# st.set_page_config(page_title="Number Guessing Game", page_icon="🎯", layout="centered")




# # Custom styles with an attractive game-related background
# st.markdown("""
#     <style>
            
#             .stApp {
#             background: url('https://i.makeagif.com/media/3-17-2021/Vi_2gH.gif');

#             background-size: cover;
#         }
#             /* Change Title Text Color */
#         h1 {
#             color: white !important; 
#             font-size: 32px;
#             font-weight: bold;
#         }
#             h3 {
#             color: white !important; /* Change this to any color you like */
#             font-size: 24px;
#             font-weight: bold;
#             }

#             h4{
#             color: white !important; /* Change this to any color you like */
#             }

          
#        /* Style for Buttons */
#        .stButton>button {
#             background: linear-gradient(to left, #fc4a1a, #f7b733);
#             color: white;
#             font-size: 18px;
#             border-radius: 10px;
#             padding: 10px;
#             transition: all 0.3s ease-in-out;
#             border: none;
#         }

#        /* Hover Effect */
#        .stButton>button:hover {
#             background: #4CAF50 !important;
#             color: white !important;
#             font-weight: bold; 
#             transform: scale(1.1); 
#             box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
#         }

#        /* Input Field Styling */
#        .stTextInput>div>div>input,
#        .stNumberInput>div>div>input {
#             font-size: 18px;
#             border: 2px solid blue;
#             border-radius: 5px;
#         }

       

    #    /* Sidebar Styling */
    #    .stSidebar {
    #         background: linear-gradient(to left, #355c7d, #6c5b7b, #c06c84);
    #         color: white;
    #     }

            
            
    #    /* Change Sidebar Label Colors */
    #    div[data-testid="stSidebar"] label {
    #         color: #FF5733 !important; 
    #         font-size: 20px;
    #         font-weight: bold;
    #     }

       
#     </style>
    
           
# """, unsafe_allow_html=True)




# st.sidebar.title("🎮 Game Settings")

# # Difficulty selection
# difficulty = st.sidebar.selectbox("Select Difficulty", ["Easy", "Medium", "Hard", "Unlimited Attempts"], index=3)
# if difficulty == "Easy":
#     st.session_state.max_attempts = 5
# elif difficulty == "Medium":
#     st.session_state.max_attempts = 10
# elif difficulty == "Hard":
#     st.session_state.max_attempts = 3
# else:
#     st.session_state.max_attempts = None

# # Custom range selection
# st.sidebar.subheader("🔢 Choose Your Number Range")
# min_val, max_val = st.sidebar.slider("Select a range", 1, 1000, (1, 100))
# if (min_val, max_val) != st.session_state.custom_range:
#     st.session_state.custom_range = (min_val, max_val)
#     st.session_state.random_number = random.randint(min_val, max_val)
#     st.session_state.attempts = 0
#     st.session_state.game_over = False

# st.title("🎯 Number Guessing Game")
# st.markdown("<h3>Can you guess the secret number? Try your luck!</h3>", unsafe_allow_html=True)
# st.write(f"<h4>Guess the number between {min_val} and {max_val}</h4>", unsafe_allow_html=True)

# # Guessing input and feedback
# if not st.session_state.game_over:
#     guess = st.number_input("Enter your guess:", min_value=min_val, max_value=max_val, step=1, key='guess')
#     if st.button("Submit Guess"):
#         st.session_state.attempts += 1
#         if guess < st.session_state.random_number:
#             st.warning("❌ Too low! Try again.")
#         elif guess > st.session_state.random_number:
#             st.warning("❌ Too high! Try again.")
#         else:
#             st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts.")
#             st.balloons()
#             st.session_state.game_over = True
        
#         if st.session_state.max_attempts and st.session_state.attempts >= st.session_state.max_attempts:
#             st.error(f"💀 Game Over! The number was {st.session_state.random_number}.")
#             st.session_state.game_over = True

# st.write(f"**Attempts:** {st.session_state.attempts}")


# # Reset button with confirmation
# if st.button("🔄 Reset Game"):
#     st.session_state.random_number = random.randint(st.session_state.custom_range[0], st.session_state.custom_range[1])
#     st.session_state.attempts = 0
#     st.session_state.game_over = False
#     st.rerun()  # Use st.rerun() instead of deprecated st.experimental_rerun()
import streamlit as st
import random

# Initialize session state variables
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'max_attempts' not in st.session_state:
    st.session_state.max_attempts = None
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'custom_range' not in st.session_state:
    st.session_state.custom_range = (1, 100)

# Streamlit page settings
st.set_page_config(page_title="Number Guessing Game", page_icon="🎯", layout="centered")

# Custom styles
st.markdown("""
    <style>
        .stApp {
            background: url('https://i.makeagif.com/media/3-17-2021/Vi_2gH.gif');
            background-size: cover;
        }
        h1, h3, h4 {
            color: white !important;
        }
            h5{
            color: black !important; /* Change this to any color you like */}
        .stButton>button {
            background: linear-gradient(to left, #fc4a1a, #f7b733);
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px;
            margin: 10px;
            transition: all 0.3s ease-in-out;
            border: none;
        }
        .stButton>button:hover {
            background: #4CAF50 !important;
            transform: scale(1.1);
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3);
        }
        .stTextInput>div>div>input, .stNumberInput>div>div>input {
            font-size: 18px;
            border: 2px solid blue;
            border-radius: 5px;
        }
        div[data-testid="stSidebar"] {
            background: linear-gradient(to left, #355c7d, #6c5b7b, #c06c84);
            color: white;
        }
        div[data-testid="stSidebar"] label {
            color: #FF5733 !important;
            font-size: 20px;
            font-weight: bold;
        }
                   /* Sidebar Styling */
       .stSidebar {
            background: linear-gradient(to left, #355c7d, #6c5b7b, #c06c84);
            color: white;
        }

            
            
       /* Change Sidebar Label Colors */
       div[data-testid="stSidebar"] label {
            color: #FF5733 !important; 
            font-size: 20px;
            font-weight: bold;
        }
        .custom-warning {
            color: white;
            background-color: #FF5733;
            padding: 12px;
            margin-top: 12px;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }
        .custom-success {
            color: white;
            background-color: #28a745;
            padding: 12px;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Settings
st.sidebar.title("🎮 Game Settings")

difficulty = st.sidebar.selectbox("Select Difficulty", ["Easy", "Medium", "Hard", "Unlimited Attempts"], index=3)
if difficulty == "Easy":
    st.session_state.max_attempts = 5
elif difficulty == "Medium":
    st.session_state.max_attempts = 10
elif difficulty == "Hard":
    st.session_state.max_attempts = 3
else:
    st.session_state.max_attempts = None

st.sidebar.subheader("🔢 Choose Your Number Range")
min_val, max_val = st.sidebar.slider("Select a range", 1, 1000, (1, 100))
if (min_val, max_val) != st.session_state.custom_range:
    st.session_state.custom_range = (min_val, max_val)
    st.session_state.random_number = random.randint(min_val, max_val)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Game Title
st.title("🎯 Number Guessing Game")
st.markdown("<h3>Can you guess the secret number? Try your luck!</h3>", unsafe_allow_html=True)
st.write(f'<h5> Guess the number between: {min_val} and {max_val} </h5>', unsafe_allow_html=True)

# Guessing Input and Feedback
if not st.session_state.game_over:
    st.markdown("<h5>Enter your guess:</h5>", unsafe_allow_html=True)
guess = st.number_input("", min_value=min_val, max_value=max_val, step=1, key='guess')

if st.button("Submit Guess"):
        st.session_state.attempts += 1
        
        if guess < st.session_state.random_number:
            st.markdown('<div class="custom-warning">❌ Too low! Try again.</div>', unsafe_allow_html=True)
        elif guess > st.session_state.random_number:
            st.markdown('<div class="custom-warning">❌ Too high! Try again.</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="custom-success">🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts.</div>', unsafe_allow_html=True)
            st.balloons()
            st.session_state.game_over = True

        if st.session_state.max_attempts and st.session_state.attempts >= st.session_state.max_attempts:
            st.markdown(f'<div class="custom-warning">💀 Game Over! The number was {st.session_state.random_number}.</div>', unsafe_allow_html=True)
            st.session_state.game_over = True

st.write(f'<h5>Attempts: {st.session_state.attempts}</h5>', unsafe_allow_html=True)

# Reset Button
if st.button("🔄 Reset Game"):
    st.session_state.random_number = random.randint(st.session_state.custom_range[0], st.session_state.custom_range[1])
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.rerun()

import streamlit as st
import random

st.set_page_config(
    page_title="Rock Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

st.title("🎮 Rock Paper Scissors")

st.write("Choose your move!")

choices = ["Rock", "Paper", "Scissors"]

col1, col2, col3 = st.columns(3)

player_choice = None

with col1:
    if st.button("🪨 Rock"):
        player_choice = "Rock"

with col2:
    if st.button("📄 Paper"):
        player_choice = "Paper"

with col3:
    if st.button("✂️ Scissors"):
        player_choice = "Scissors"

if player_choice:
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "🤝 Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"
        st.session_state.player_score += 1
    else:
        result = "💻 Computer Wins!"
        st.session_state.computer_score += 1

    st.subheader(result)

    st.write(f"**Your Choice:** {player_choice}")
    st.write(f"**Computer Choice:** {computer_choice}")

st.markdown("---")

st.metric("Your Score", st.session_state.player_score)
st.metric("Computer Score", st.session_state.computer_score)

if st.button("🔄 Reset Score"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.rerun()
import streamlit as st
import random
from streamlit_extras.let_it_rain import rain

st.set_page_config(
    page_title="가위바위보 대결 💕",
    page_icon="✊",
    layout="centered"
)

st.title("✊ 가위바위보 게임")

# 세션 상태 초기화
if "player_score" not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.com_score = 0

choices = ["가위", "바위", "보"]

st.subheader("선택하세요!")
player = st.radio("👇 당신의 선택", choices)

if st.button("대결하기!"):
    com = random.choice(choices)

    st.write(f"👤 당신: {player}")
    st.write(f"🤖 컴퓨터: {com}")

    if player == com:
        result = "비김 😐"
    elif (
        (player == "가위" and com == "보") or
        (player == "바위" and com == "가위") or
        (player == "보" and com == "바위")
    ):
        result = "승리 🎉"
        st.session_state.player_score += 1
        rain(emoji="🎉", font_size=40, falling_speed=5)
    else:
        result = "패배 😭"
        st.session_state.com_score += 1

    st.subheader(f"결과: {result}")

st.write("---")
st.write(f"🏆 당신 점수: {st.session_state.player_score}")
st.write(f"💻 컴퓨터 점수: {st.session_state.com_score}")

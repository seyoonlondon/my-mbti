import random

import streamlit as st

from pokemon_data import MBTI_COMPATIBILITY, MBTI_POKEMON, pokemon_image_url

st.set_page_config(page_title="MBTI 궁합 포켓몬 추천", page_icon="💞", layout="centered")


def show_pokemon_card(mbti, pokemon, title):
    st.markdown(f"#### {title}")
    col1, col2 = st.columns([1, 1.4])
    with col1:
        st.image(pokemon_image_url(pokemon), width=200)
    with col2:
        st.markdown(f"**{mbti}**")
        st.markdown(f"## {pokemon['emoji']} {pokemon['name']}")
        st.write(pokemon["desc"])


st.title("💞 MBTI 궁합 포켓몬 추천기")
st.write("내 포켓몬의 MBTI와 가장 궁합이 좋은 MBTI의 포켓몬을 확인해보세요!")

mbti_list = list(MBTI_POKEMON.keys())
selected_mbti = st.selectbox("내 포켓몬의 MBTI를 선택하세요", mbti_list)

if st.button("궁합 포켓몬 확인하기 💞"):
    my_pokemon = random.choice(MBTI_POKEMON[selected_mbti])
    best_mbti = MBTI_COMPATIBILITY[selected_mbti]["best"]
    reason = MBTI_COMPATIBILITY[selected_mbti]["reason"]
    best_pokemon = random.choice(MBTI_POKEMON[best_mbti])

    st.markdown("---")
    show_pokemon_card(selected_mbti, my_pokemon, "🧑 내 포켓몬")

    st.markdown("<h2 style='text-align:center;'>💘</h2>", unsafe_allow_html=True)

    show_pokemon_card(best_mbti, best_pokemon, "💞 궁합 최고 포켓몬")

    st.markdown("---")
    st.info(f"**{selected_mbti} × {best_mbti} 궁합 이유:** {reason}")
    st.balloons()

st.markdown("---")
st.caption("Made with Streamlit 🐍")

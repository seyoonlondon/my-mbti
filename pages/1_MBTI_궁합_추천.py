import random

import streamlit as st

st.set_page_config(page_title="MBTI 궁합 포켓몬 추천", page_icon="💞", layout="centered")

# MBTI별 추천 포켓몬 데이터
MBTI_POKEMON = {
    "INTJ": [
        {"name": "메타몽", "dex": 132, "emoji": "🟣", "desc": "전략적이고 치밀한 계획가, 조용히 목표를 향해 나아가는 타입"},
        {"name": "팬텀", "dex": 94, "emoji": "👻", "desc": "신비롭고 독립적인 성향, 깊은 통찰력을 가진 타입"},
    ],
    "INTP": [
        {"name": "무우마", "dex": 200, "emoji": "🔮", "desc": "논리적 사고와 호기심이 강한 탐구가 타입"},
        {"name": "슈터할로트", "dex": 168, "emoji": "🕷️", "desc": "독창적인 아이디어를 가진 분석가 타입"},
    ],
    "ENTJ": [
        {"name": "리자몽", "dex": 6, "emoji": "🔥", "desc": "타고난 리더십과 강한 추진력을 가진 지휘관 타입"},
        {"name": "갸라도스", "dex": 130, "emoji": "🐉", "desc": "카리스마 넘치는 강력한 통솔자 타입"},
    ],
    "ENTP": [
        {"name": "또가스", "dex": 110, "emoji": "💨", "desc": "기발하고 도전적인 발상가, 논쟁을 즐기는 타입"},
        {"name": "치렁이", "dex": 114, "emoji": "🌿", "desc": "재치있고 임기응변에 강한 타입"},
    ],
    "INFJ": [
        {"name": "뮤", "dex": 151, "emoji": "💫", "desc": "신비롭고 이상주의적인, 깊은 통찰을 지닌 타입"},
        {"name": "라티아스", "dex": 380, "emoji": "💗", "desc": "따뜻하지만 신중한 감성을 가진 조언자 타입"},
    ],
    "INFP": [
        {"name": "이브이", "dex": 133, "emoji": "🦊", "desc": "순수하고 감성적인, 무한한 가능성을 지닌 몽상가 타입"},
        {"name": "고디모아젤", "dex": 282, "emoji": "💃", "desc": "예술적 감각과 깊은 내면세계를 지닌 타입"},
    ],
    "ENFJ": [
        {"name": "루카리오", "dex": 448, "emoji": "🦴", "desc": "정의롭고 타인을 이끄는 카리스마 있는 멘토 타입"},
        {"name": "가디안", "dex": 475, "emoji": "🥋", "desc": "우아하고 배려심 깊은 지도자 타입"},
    ],
    "ENFP": [
        {"name": "피카츄", "dex": 25, "emoji": "⚡", "desc": "밝고 에너지 넘치는, 사람들과 어울리기 좋아하는 타입"},
        {"name": "브케인", "dex": 255, "emoji": "🔥", "desc": "열정적이고 자유분방한 모험가 타입"},
    ],
    "ISTJ": [
        {"name": "딱구리", "dex": 50, "emoji": "🕳️", "desc": "성실하고 책임감 강한, 원칙을 중시하는 타입"},
        {"name": "강철톤", "dex": 208, "emoji": "⚙️", "desc": "신뢰할 수 있고 꾸준한 실무형 타입"},
    ],
    "ISFJ": [
        {"name": "라프라스", "dex": 131, "emoji": "🌊", "desc": "따뜻하고 헌신적인, 남을 잘 돌보는 타입"},
        {"name": "마릴리", "dex": 183, "emoji": "💙", "desc": "다정하고 안정감을 주는 수호자 타입"},
    ],
    "ESTJ": [
        {"name": "딱정곤", "dex": 14, "emoji": "🪲", "desc": "체계적이고 실행력 강한 관리자 타입"},
        {"name": "무장조", "dex": 227, "emoji": "🦅", "desc": "엄격하지만 확실한 결과를 내는 타입"},
    ],
    "ESFJ": [
        {"name": "폴리곤", "dex": 137, "emoji": "🖥️", "desc": "사교적이고 조화를 중시하는 협력자 타입"},
        {"name": "치코리타", "dex": 152, "emoji": "🌱", "desc": "다정하고 배려 깊은 분위기 메이커 타입"},
    ],
    "ISTP": [
        {"name": "이상해씨", "dex": 1, "emoji": "🌱", "desc": "차분하고 실용적인 문제 해결사 타입"},
        {"name": "코일", "dex": 81, "emoji": "🔌", "desc": "독립적이고 손재주 좋은 만능 재주꾼 타입"},
    ],
    "ISFP": [
        {"name": "푸린", "dex": 39, "emoji": "🎀", "desc": "온화하고 예술적 감성이 풍부한 자유로운 영혼 타입"},
        {"name": "아르코", "dex": 234, "emoji": "🦌", "desc": "감성적이고 자연을 사랑하는 조용한 타입"},
    ],
    "ESTP": [
        {"name": "윈디", "dex": 59, "emoji": "🐕", "desc": "활동적이고 대담한 행동파 타입"},
        {"name": "야도란", "dex": 80, "emoji": "🦀", "desc": "즉흥적이고 순발력 있는 승부사 타입"},
    ],
    "ESFP": [
        {"name": "파이리", "dex": 4, "emoji": "🔥", "desc": "밝고 재미있는, 무대를 즐기는 엔터테이너 타입"},
        {"name": "또도가스", "dex": 109, "emoji": "🎉", "desc": "활발하고 사람들의 이목을 끄는 타입"},
    ],
}

# MBTI 성격 궁합 데이터 (가장 잘 맞는 유형)
MBTI_COMPATIBILITY = {
    "INTJ": {"best": "ENFP", "reason": "INTJ의 논리와 ENFP의 상상력이 만나 서로의 부족한 부분을 채워주는 환상의 궁합이에요."},
    "INTP": {"best": "ENTJ", "reason": "INTP의 아이디어를 ENTJ의 추진력이 현실로 만들어주는 최고의 시너지 궁합이에요."},
    "ENTJ": {"best": "INTP", "reason": "ENTJ의 리더십과 INTP의 창의적 사고가 만나면 못할 일이 없어요."},
    "ENTP": {"best": "INFJ", "reason": "ENTP의 도전정신과 INFJ의 통찰력이 서로를 성장시키는 궁합이에요."},
    "INFJ": {"best": "ENTP", "reason": "INFJ의 깊이와 ENTP의 발랄한 에너지가 균형을 이루는 조합이에요."},
    "INFP": {"best": "ENFJ", "reason": "INFP의 감성을 ENFJ가 따뜻하게 이해하고 이끌어주는 편안한 궁합이에요."},
    "ENFJ": {"best": "INFP", "reason": "ENFJ의 배려심이 INFP의 마음을 가장 잘 헤아려줄 수 있어요."},
    "ENFP": {"best": "INTJ", "reason": "ENFP의 자유로움과 INTJ의 안정감이 서로에게 신선한 자극이 돼요."},
    "ISTJ": {"best": "ESFP", "reason": "ISTJ의 꾸준함과 ESFP의 즉흥성이 만나 삶에 활력을 더해줘요."},
    "ISFJ": {"best": "ESFP", "reason": "ISFJ의 세심함과 ESFP의 밝은 에너지가 서로를 편안하게 해줘요."},
    "ESTJ": {"best": "ISFP", "reason": "ESTJ의 추진력과 ISFP의 유연함이 좋은 균형을 이뤄요."},
    "ESFJ": {"best": "ISFP", "reason": "ESFJ의 다정함과 ISFP의 감성이 서로 잘 통하는 궁합이에요."},
    "ISTP": {"best": "ESTJ", "reason": "ISTP의 실용성과 ESTJ의 조직력이 만나 안정적인 관계를 만들어요."},
    "ISFP": {"best": "ESTJ", "reason": "ISFP의 자유로운 감성을 ESTJ가 든든하게 받쳐줄 수 있어요."},
    "ESTP": {"best": "ISFJ", "reason": "ESTP의 모험심과 ISFJ의 차분함이 서로를 보완해줘요."},
    "ESFP": {"best": "ISTJ", "reason": "ESFP의 즉흥성과 ISTJ의 안정감이 만나 균형잡힌 관계가 돼요."},
}

def pokemon_image_url(pokemon):
    """포켓몬 딕셔너리를 받아 공식 아트워크 이미지 URL을 반환합니다."""
    return f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{pokemon['dex']}.png"


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

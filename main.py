import streamlit as st
import random

st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="✨", layout="centered")

# MBTI별 추천 포켓몬 데이터
MBTI_POKEMON = {
    "INTJ": [
        {"name": "메타몽", "emoji": "🟣", "desc": "전략적이고 치밀한 계획가, 조용히 목표를 향해 나아가는 타입"},
        {"name": "팬텀", "emoji": "👻", "desc": "신비롭고 독립적인 성향, 깊은 통찰력을 가진 타입"},
    ],
    "INTP": [
        {"name": "무우마", "emoji": "🔮", "desc": "논리적 사고와 호기심이 강한 탐구가 타입"},
        {"name": "슈터할로트", "emoji": "🕷️", "desc": "독창적인 아이디어를 가진 분석가 타입"},
    ],
    "ENTJ": [
        {"name": "리자몽", "emoji": "🔥", "desc": "타고난 리더십과 강한 추진력을 가진 지휘관 타입"},
        {"name": "갸라도스", "emoji": "🐉", "desc": "카리스마 넘치는 강력한 통솔자 타입"},
    ],
    "ENTP": [
        {"name": "또가스", "emoji": "💨", "desc": "기발하고 도전적인 발상가, 논쟁을 즐기는 타입"},
        {"name": "치렁이", "emoji": "🌿", "desc": "재치있고 임기응변에 강한 타입"},
    ],
    "INFJ": [
        {"name": "뮤", "emoji": "💫", "desc": "신비롭고 이상주의적인, 깊은 통찰을 지닌 타입"},
        {"name": "라티아스", "emoji": "💗", "desc": "따뜻하지만 신중한 감성을 가진 조언자 타입"},
    ],
    "INFP": [
        {"name": "이브이", "emoji": "🦊", "desc": "순수하고 감성적인, 무한한 가능성을 지닌 몽상가 타입"},
        {"name": "고디모아젤", "emoji": "💃", "desc": "예술적 감각과 깊은 내면세계를 지닌 타입"},
    ],
    "ENFJ": [
        {"name": "루카리오", "emoji": "🦴", "desc": "정의롭고 타인을 이끄는 카리스마 있는 멘토 타입"},
        {"name": "가디안", "emoji": "🥋", "desc": "우아하고 배려심 깊은 지도자 타입"},
    ],
    "ENFP": [
        {"name": "피카츄", "emoji": "⚡", "desc": "밝고 에너지 넘치는, 사람들과 어울리기 좋아하는 타입"},
        {"name": "브케인", "emoji": "🔥", "desc": "열정적이고 자유분방한 모험가 타입"},
    ],
    "ISTJ": [
        {"name": "딱구리", "emoji": "🕳️", "desc": "성실하고 책임감 강한, 원칙을 중시하는 타입"},
        {"name": "강철톤", "emoji": "⚙️", "desc": "신뢰할 수 있고 꾸준한 실무형 타입"},
    ],
    "ISFJ": [
        {"name": "라프라스", "emoji": "🌊", "desc": "따뜻하고 헌신적인, 남을 잘 돌보는 타입"},
        {"name": "마릴리", "emoji": "💙", "desc": "다정하고 안정감을 주는 수호자 타입"},
    ],
    "ESTJ": [
        {"name": "딱정곤", "emoji": "🪲", "desc": "체계적이고 실행력 강한 관리자 타입"},
        {"name": "무장조", "emoji": "🦅", "desc": "엄격하지만 확실한 결과를 내는 타입"},
    ],
    "ESFJ": [
        {"name": "폴리곤", "emoji": "🖥️", "desc": "사교적이고 조화를 중시하는 협력자 타입"},
        {"name": "치코리타", "emoji": "🌱", "desc": "다정하고 배려 깊은 분위기 메이커 타입"},
    ],
    "ISTP": [
        {"name": "이상해씨", "emoji": "🌱", "desc": "차분하고 실용적인 문제 해결사 타입"},
        {"name": "코일", "emoji": "🔌", "desc": "독립적이고 손재주 좋은 만능 재주꾼 타입"},
    ],
    "ISFP": [
        {"name": "푸린", "emoji": "🎀", "desc": "온화하고 예술적 감성이 풍부한 자유로운 영혼 타입"},
        {"name": "아르코", "emoji": "🦌", "desc": "감성적이고 자연을 사랑하는 조용한 타입"},
    ],
    "ESTP": [
        {"name": "윈디", "emoji": "🐕", "desc": "활동적이고 대담한 행동파 타입"},
        {"name": "야도란", "emoji": "🦀", "desc": "즉흥적이고 순발력 있는 승부사 타입"},
    ],
    "ESFP": [
        {"name": "파이리", "emoji": "🔥", "desc": "밝고 재미있는, 무대를 즐기는 엔터테이너 타입"},
        {"name": "또도가스", "emoji": "🎉", "desc": "활발하고 사람들의 이목을 끄는 타입"},
    ],
}

st.title("✨ MBTI 포켓몬 추천기")
st.write("당신의 MBTI를 선택하면 어울리는 포켓몬을 추천해드려요!")

mbti_list = list(MBTI_POKEMON.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

if st.button("포켓몬 추천받기 🎁"):
    pokemon = random.choice(MBTI_POKEMON[selected_mbti])
    st.markdown("---")
    st.subheader(f"{selected_mbti} 유형에게 어울리는 포켓몬은...")
    st.markdown(f"## {pokemon['emoji']} {pokemon['name']}")
    st.write(pokemon["desc"])
    st.balloons()

st.markdown("---")
st.caption("Made with Streamlit 🐍")

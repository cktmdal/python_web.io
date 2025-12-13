
import streamlit as st
st.title('나의 첫 웹 서비스 만들기!!')
name = st.text_input('이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 음식을 선택해주세요:', ['망고빙수','아몬드봉봉'])
if st.button('인사말 생성') : 
  st.write(name+'님! 당신이 좋아하는 음식은 '+menu+'이군요?! 저도 좋아요!!')

import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="⚡", layout="centered")

# MBTI별 포켓몬 추천 데이터
mbti_pokemon = {
    "INTJ": {
        "name": "뮤츠",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "reason": "전략적이고 독립적인 성향을 가진 뮤츠는 INTJ처럼 지적이고 미래지향적입니다. 강력한 정신력과 목표 달성을 위한 집요함이 INTJ의 특성과 완벽하게 일치합니다."
    },
    "INTP": {
        "name": "포리곤",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/137.png",
        "reason": "논리적이고 분석적인 포리곤은 INTP의 호기심 많고 이론적인 성향을 대표합니다. 끊임없이 데이터를 분석하고 새로운 가능성을 탐구하는 모습이 INTP와 닮았습니다."
    },
    "ENTJ": {
        "name": "망나뇽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/149.png",
        "reason": "카리스마 넘치는 리더십을 가진 망나뇽은 ENTJ의 야심차고 결단력 있는 성격을 반영합니다. 강력하면서도 목표 지향적인 모습이 ENTJ의 특징입니다."
    },
    "ENTP": {
        "name": "로토무",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/479.png",
        "reason": "창의적이고 변화를 즐기는 로토무는 ENTP의 혁신적이고 적응력 높은 성격을 나타냅니다. 다양한 형태로 변신하며 새로운 시도를 즐기는 모습이 ENTP와 같습니다."
    },
    "INFJ": {
        "name": "가디안",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png",
        "reason": "공감능력이 뛰어나고 이상주의적인 가디안은 INFJ의 깊은 통찰력과 타인을 돕고자 하는 열망을 상징합니다. 신비롭고 지혜로운 모습이 INFJ와 닮았습니다."
    },
    "INFP": {
        "name": "이브이",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "reason": "순수하고 감성적인 이브이는 INFP의 이상주의적이고 개성 있는 성향을 대표합니다. 다양한 진화 가능성처럼 무한한 잠재력을 가진 모습이 INFP와 일치합니다."
    },
    "ENFJ": {
        "name": "루카리오",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "reason": "정의롭고 타인을 이끄는 루카리오는 ENFJ의 카리스마와 공감능력을 나타냅니다. 파동으로 감정을 읽고 사람들을 돕는 모습이 ENFJ의 특성과 같습니다."
    },
    "ENFP": {
        "name": "피카츄",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "reason": "활발하고 사교적인 피카츄는 ENFP의 열정적이고 긍정적인 에너지를 상징합니다. 호기심 많고 새로운 모험을 즐기는 모습이 ENFP와 완벽하게 맞습니다."
    },
    "ISTJ": {
        "name": "메타그로스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/376.png",
        "reason": "체계적이고 신뢰할 수 있는 메타그로스는 ISTJ의 책임감 있고 논리적인 성향을 보여줍니다. 정확한 계산과 안정적인 전략으로 목표를 달성하는 모습이 ISTJ와 닮았습니다."
    },
    "ISFJ": {
        "name": "행복란",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/242.png",
        "reason": "헌신적이고 배려심 깊은 행복란은 ISFJ의 보살피는 성격과 타인을 위한 희생정신을 대표합니다. 치유와 돌봄을 제공하는 모습이 ISFJ의 특징입니다."
    },
    "ESTJ": {
        "name": "보스로라",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/306.png",
        "reason": "강력하고 조직적인 보스로라는 ESTJ의 실용적이고 리더십 있는 성향을 나타냅니다. 규칙을 중시하고 효율적으로 목표를 달성하는 모습이 ESTJ와 같습니다."
    },
    "ESFJ": {
        "name": "푸크린",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/40.png",
        "reason": "사교적이고 배려심 많은 푸크린은 ESFJ의 친절하고 협조적인 성격을 상징합니다. 사람들을 즐겁게 하고 조화를 중시하는 모습이 ESFJ의 특성입니다."
    },
    "ISTP": {
        "name": "리자몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "reason": "독립적이고 실용적인 리자몽은 ISTP의 문제해결 능력과 모험심을 대표합니다. 순간의 판단력과 유연한 대처가 뛰어난 모습이 ISTP와 닮았습니다."
    },
    "ISFP": {
        "name": "나비나",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/12.png",
        "reason": "예술적이고 자유로운 영혼을 가진 나비나는 ISFP의 감성적이고 평화로운 성향을 나타냅니다. 아름다움을 추구하며 자신만의 길을 가는 모습이 ISFP와 일치합니다."
    },
    "ESTP": {
        "name": "번치코",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/257.png",
        "reason": "활동적이고 대담한 번치코는 ESTP의 에너지 넘치고 현실적인 성격을 상징합니다. 빠른 행동력과 순간적 판단으로 도전을 즐기는 모습이 ESTP의 특징입니다."
    },
    "ESFP": {
        "name": "파이리",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/4.png",
        "reason": "열정적이고 활발한 파이리는 ESFP의 즉흥적이고 사교적인 성향을 대표합니다. 주변을 즐겁게 하고 현재를 즐기는 모습이 ESFP와 완벽하게 맞습니다."
    }
}

# 제목
st.title("⚡ MBTI 포켓몬 추천")
st.write("당신의 MBTI 유형과 가장 닮은 포켓몬을 찾아보세요!")

# MBTI 선택
mbti_types = list(mbti_pokemon.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types, index=0)

# 추천 버튼
if st.button("포켓몬 찾기!", type="primary"):
    pokemon = mbti_pokemon[selected_mbti]
    
    st.success(f"**{selected_mbti}** 유형 분석 완료!")
    
    # 포켓몬 이미지
    st.subheader(f"🎯 당신과 닮은 포켓몬: {pokemon['name']}")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(pokemon['image'], width=300)
    
    # 이유 설명
    st.subheader("💡 왜 비슷한가요?")
    st.info(pokemon['reason'])
    
    # 추가 메시지
    st.markdown("---")
    st.caption("🎮 포켓몬 이미지는 PokeAPI에서 제공됩니다.")

# 푸터
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")

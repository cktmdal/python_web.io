# streamlit_app.py
# 전반적인 학교생활 만족도 (메뉴별 그래프)
# 표준 라이브러리 + Streamlit 내장 그래프만 사용

import streamlit as st
import csv

st.set_page_config(page_title="학교생활 만족도 분석", layout="centered")

st.title("전반적인 학교생활 만족도 분석")
st.write("메뉴(구분)별 만족도 데이터를 선택하여 그래프로 확인합니다.")

# ---------------------------------
# 1. 데이터 파일 설정 (같은 폴더)
# ---------------------------------
DATA_FILE = "전반적인_학교생활_만족도_20251213143754_분석(전년_대비_증감,증감률).txt"

# ---------------------------------
# 2. 데이터 읽기 (탭 구분 텍스트)
# ---------------------------------
# 컬럼 구조 (실제 데이터 기준)
# 구분, 항목, 전년대비증감, 증감률, 원데이터, 전년대비증감2, 증감률2

rows = []

try:
    with open(DATA_FILE, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter='\t')
        header = next(reader)  # 첫 줄은 헤더
        for row in reader:
            if len(row) < 6:
                continue
            rows.append(row)
except FileNotFoundError:
    st.error("데이터 파일을 찾을 수 없습니다. 같은 폴더에 업로드했는지 확인하세요.")
    st.stop()

# ---------------------------------
# 3. 메뉴(구분) 목록 생성
# ---------------------------------
categories = sorted(set(r[0].replace('"', '') for r in rows))

selected_category = st.selectbox("분석할 메뉴(구분)를 선택하세요", categories)

# ---------------------------------
# 4. 선택한 메뉴 데이터 추출
# ---------------------------------
labels = []
values = []

for r in rows:
    category = r[0].replace('"', '')
    if category == selected_category:
        labels.append(r[1])          # 항목 (예: 남자, 여자, 초등학교 등)
        values.append(float(r[4]))   # 원데이터(만족도)

# ---------------------------------
# 5. 원본 데이터 표 출력
# ---------------------------------
st.subheader("선택한 메뉴의 원본 데이터")
st.write({"항목": labels, "만족도": values})

# ---------------------------------
# 6. Streamlit 내장 그래프
# ---------------------------------
st.subheader("메뉴별 학교생활 만족도 그래프")

chart_data = {
    "만족도": values
}

st.bar_chart(chart_data)

# ---------------------------------
# 7. 그래프 안내
# ---------------------------------
st.info(
    """
    • 본 그래프는 Streamlit 내장 bar_chart를 사용하여
      별도 라이브러리 설치 없이 Streamlit Cloud에서 안정적으로 동작합니다.

    • 항목 간 만족도 비교에는 막대그래프가 가장 적합합니다.

    • 추이(연도 변화) 분석이 필요한 경우 line_chart 사용을 권장합니다.
    """
)


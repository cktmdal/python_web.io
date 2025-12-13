# streamlit_app.py
# Plotly 인터랙티브 그래프를 활용한 학교생활 만족도 웹앱

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="학교생활 만족도 분석", layout="wide")

st.title("전반적인 학교생활 만족도 분석 (인터랙티브)")
st.write("메뉴별 만족도를 인터랙티브 그래프로 확인할 수 있습니다.")

# ---------------------------------
# 1. 데이터 파일 설정 (같은 폴더)
# ---------------------------------
DATA_FILE = "전반적인_학교생활_만족도_20251213143754_분석(전년_대비_증감,증감률).txt"

# ---------------------------------
# 2. 데이터 불러오기
# ---------------------------------
# 탭(\t)으로 구분된 텍스트 파일

df = pd.read_csv(DATA_FILE, sep="\t", header=None)

# 컬럼 재정의
# [구분, 항목, 전년증감, 증감률, 만족도, 전년증감2, 증감률2]
df = df.iloc[:, :7]
df.columns = ["구분", "항목", "전년대비증감", "증감률", "만족도", "전년대비증감2", "증감률2"]

# 큰따옴표 제거 및 결측치 처리
df["구분"] = df["구분"].str.replace('"', '')
df = df.dropna(subset=["만족도"])

# ---------------------------------
# 3. 메뉴 선택
# ---------------------------------
categories = sorted(df["구분"].unique())
selected_category = st.selectbox("분석할 메뉴(구분) 선택", categories)

filtered_df = df[df["구분"] == selected_category]

# ---------------------------------
# 4. 원본 데이터 표시
# ---------------------------------
st.subheader("선택한 메뉴의 데이터")
st.dataframe(filtered_df[["항목", "만족도", "전년대비증감", "증감률"]])

# ---------------------------------
# 5. Plotly 인터랙티브 그래프
# ---------------------------------
st.subheader("메뉴별 학교생활 만족도 그래프")

fig = px.bar(
    filtered_df,
    x="항목",
    y="만족도",
    text="만족도",
    title=f"{selected_category} 학교생활 만족도",
)

fig.update_traces(texttemplate="%{text}", textposition="outside")
fig.update_layout(
    xaxis_title="항목",
    yaxis_title="만족도",
    uniformtext_minsize=8,
    uniformtext_mode="hide",
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------
# 6. 안내
# ---------------------------------
st.info(
    """
    • 본 그래프는 Plotly를 사용한 인터랙티브 그래프입니다.
    • 마우스 오버 시 값 확인, 확대/축소, 이미지 저장이 가능합니다.
    • Streamlit 내장 그래프보다 보고서·설명회·연수 자료에 적합합니다.
    """
)

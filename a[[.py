# 1.
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.title("Heart Failure")

df_a = pd.read_json("heart_failure_a.json")
df_b = pd.read_json("heart_failure_b.json")

df = pd.merge(df_a, df_b, on="person_id", how="inner")

dropped_num = len(df_a) - len(df) + len(df_b) - len(df)

drop_a = set(df_a["person_id"]) - set(df["person_id"])
drop_b = set(df_b["person_id"]) - set(df["person_id"])

st.subheader("1. 데이터 병합 결과")
st.write("df_a 행 개수:", len(df_a))
st.write("df_b 행 개수:", len(df_b))
st.write("병합 후 df 행 개수:", len(df))
st.write("병합하면서 사라진 데이터 수:", dropped_num)

st.write("df_a에만 있고 병합 후 사라진 person_id")
st.write(drop_a)

st.write("df_b에만 있고 병합 후 사라진 person_id")
st.write(drop_b)

st.dataframe(df)

#2.
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("jointplot")

joint = sns.jointplot(
    data=df,
    x='ejection_fraction',
    y='age',
    hue='DEATH_EVENT'
)

st.pyplot(joint.fig)

plt.close(joint.fig)

#3.
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Violin Plot")
smoking_select = st.radio(
    "흡연 여부 선택",
    options=["Yes", "No"]
)

if smoking_select == "Yes":
    filter_df = df[df["smoking"] == "Yes"]
else:
    filter_df = df[df["smoking"] == "No"]

fig, ax = plt.subplots()

sns.violinplot(
    data=filter_df,
    x='DEATH_EVENT',
    y='platelets',
    ax=ax
)

ax.set_title(f"Smoking : {smoking_select}")

st.pyplot(fig)

plt.close(fig)

#4.
min_value = int(df['ejection_fraction'].min())
max_value = int(df['ejection_fraction'].max())

ef_range = st.slider(
    "심박출 범위 선택",
    min_value=min_value,
    max_value=max_value,
    value=(min_value, max_value)
)

filter_df = df[
    (df['ejection_fraction'] >= ef_range[0]) &
    (df['ejection_fraction'] <= ef_range[1])
]

fig, ax = plt.subplots()

sns.histplot(
    data=filter_df,
    x='time',
    bins=20,
    hue='DEATH_EVENT',
    ax=ax
)

st.pyplot(fig)


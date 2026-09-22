import streamlit as st

st.set_page_config(
    page_title="ทายซิทอนเท่าไหร่",
    page_icon="💰"
)

st.header("💰 ทายซิทอนเท่าไหร่")

price = st.number_input(
    "ราคาสินค้า",
    min_value=0.0,
    value=0.0,
    step=1.0
)

paid = st.number_input(
    "เงินที่จ่าย",
    min_value=0.0,
    value=0.0,
    step=1.0
)

if st.button("คำนวณ"):
    if paid < price:
        st.error("เงินที่จ่ายไม่เพียงพอ")
    else:
        change = paid - price

        st.success(
            f"เงินทอน {change:,.2f} บาท"
        )

if st.button("ล้าง"):
    st.rerun()

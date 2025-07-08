import streamlit as st
import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

st.set_page_config(page_title="Billing", layout="centered")
st.title("💰 Client Billing Dashboard")

client_id = st.text_input("Enter Client ID")
tier = st.selectbox("Tier", ["Basic - $50/mo", "Pro - $200/mo", "Enterprise - Custom"])

if st.button("Create Checkout Session"):
    price_lookup = {
        "Basic": "price_basic_id",
        "Pro": "price_pro_id"
    }
    selected = tier.split(" - ")[0]
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{"price": price_lookup[selected], "quantity": 1}],
        mode="subscription",
        success_url="https://yourdomain.com/success",
        cancel_url="https://yourdomain.com/cancel",
        metadata={"client_id": client_id}
    )
    st.success("✅ Checkout session created:")
    st.write(session.url)
    
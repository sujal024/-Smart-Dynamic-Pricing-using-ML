import streamlit as st
from scraper import get_competitor_price
from utils import load_model, simulate_inventory_and_demand

st.set_page_config(page_title="Dynamic Pricing Engine", layout="wide")
st.title("🛒 Real‑Time Dynamic Pricing Engine")

model = load_model()

product = st.text_input("Enter product name:", value="wireless mouse")
inventory_input = st.number_input("Inventory on hand:", min_value=0, max_value=1000, value=50)

if st.button("Suggest Optimal Price"):
    try:
        comp_price = get_competitor_price(product)
        inventory, demand = simulate_inventory_and_demand()
        X_live = [[comp_price, demand, inventory_input or inventory]]
        suggested = model.predict(X_live)[0]

        st.success(f" Suggested Price: ₹{suggested:.2f}")
        st.markdown(
            f"- **Competitor Avg Price:** ₹{comp_price:.2f}  \n"
            f"- **Forecasted Demand (next day):** {demand} units  \n"
            f"- **Inventory Used:** {inventory_input or inventory} units"
        )
    except Exception as e:
        st.error(f"Error: {e}")

import streamlit as st
import pandas as pd
from datetime import datetime

# 1. App Title
st.title("📦 Product Inventory Snapper")

# 2. Camera Input - This activates the phone's camera
photo = st.camera_input("Take a picture of the product")

# 3. Form for Details
with st.form("product_form", clear_on_submit=True):
    name = st.text_input("Product Name")
    description = st.text_area("Description")
    
    # Currency set to Indian Rupee (₹)
    price = st.number_input("Price (₹)", min_value=0.0, step=100.0, format="%.2f")
    
    submitted = st.form_submit_button("Save Product")

    if submitted:
        if photo and name:
            # In a real app, you would save 'photo' to a folder/database here
            
            # Create a simple confirmation
            st.success(f"✅ Saved **{name}** for **₹{price}**!")
            
            # Display what we "saved" (Preview)
            st.image(photo, caption=name, width=200)
            
            # Just for demo: Show the data record
            data = {
                "Name": name,
                "Price": f"₹{price}",
                "Desc": description,
                "Captured": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            st.json(data)
            
        else:
            st.error("⚠️ Please take a photo and add a name.")


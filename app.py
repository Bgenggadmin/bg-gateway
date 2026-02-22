import streamlit as st

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="B&G Digital HQ", page_icon="🏗️", layout="centered")

# --- 2. THE GATEWAY INTERFACE ---
st.title("🏗️ B&G Engineering Industries")
st.subheader("Digital Shopfloor Control Center")
st.write("Select a module below to begin logging or viewing reports.")

st.divider()

# --- 3. APP LINKS ---
# Replace the URLs below with your actual live Streamlit links
c1, c2, c3 = st.columns(3)

with c1:
    st.info("### 📝 Production")
    st.write("Man-hours, Worker logs, & Daily Output Tracking.")
    st.link_button("Open Shopfloor Monitor", "https://bg-engineering-monitor.streamlit.app")
    st.write("**Password:** `BG2026`")

with c2:
    st.success("### ✅ Quality")
    st.write("PMI, Hydrotest, FAT, & Photo Evidence Logs.")
    st.link_button("Open Quality Master", "https://bg-quality-master.streamlit.app")
    st.write("**Password:** `BGQUALITY`")

with c3:
    st.warning("### 🔧 Maintenance")
    st.write("Crane, CNC, & TIG Machine Service Records.")
    st.link_button("Open Maintenance App", "https://bg-maintenance-master.streamlit.app")
    st.write("**Password:** `BGMAINT`")

st.divider()
st.caption("Developed for B&G Engineering Industries Shopfloor Management.")

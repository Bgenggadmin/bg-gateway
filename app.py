import streamlit as st
from datetime import datetime, timedelta
import extra_streamlit_components as cookie_manager

# --- COOKIE LOGIC ---
controller = cookie_manager.CookieManager()

if "auth" not in st.session_state:
    st.session_state["auth"] = False

all_cookies = controller.get_all()
if not all_cookies:
    st.stop()

if controller.get("bg_gateway_login") == "true":
    st.session_state["auth"] = True

if not st.session_state["auth"]:
    st.title("🏗️ B&G Digital HQ")
    pwd = st.text_input("Admin Password", type="password")
    if st.button("Access Gateway"):
        if pwd == "BG2026": # Master Admin Password
            st.session_state["auth"] = True
            controller.set("bg_gateway_login", "true", expires_at=datetime.now() + timedelta(days=30))
            st.rerun()
    st.stop()

# --- GATEWAY BUTTONS ---
st.title("🏗️ B&G Engineering Industries")
st.write("Select a department to continue.")

c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("📝 Production", "https://bg-engineering-monitor.streamlit.app")
with c2:
    st.link_button("✅ Quality", "https://bg-quality-master.streamlit.app")
with c3:
    st.link_button("🔧 Maintenance", "https://bg-maintenance-master.streamlit.app")

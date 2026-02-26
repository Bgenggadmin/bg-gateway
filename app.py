import streamlit as st

# --- 1. CONFIG ---
st.set_page_config(page_title="B&G Engineering Gateway", layout="centered")

# --- 2. STYLING ---
st.markdown("""
    <style>
    .main-button {
        display: block;
        width: 100%;
        padding: 20px;
        margin: 10px 0;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        color: white !important;
        border-radius: 10px;
        border: none;
    }
    .prod { background-color: #2E7D32; } /* Green */
    .qual { background-color: #1565C0; } /* Blue */
    .maint { background-color: #C62828; } /* Red */
    .logis { background-color: #EF6C00; } /* Orange */
    </style>
""", unsafe_allow_html=True)

# --- 3. UI ---
st.image("https://raw.githubusercontent.com/Bgenggadmin/bg-production-master/main/logo.png", width=200) # Optional: Add your logo link
st.title("🏗️ B&G Engineering Industries")
st.subheader("Digital Management Gateway")

st.info("Select a department below to start logging data.")

# --- 4. THE FOUR PILLARS ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<a href="https://bg-production-master.streamlit.app/" target="_blank" class="main-button prod">⚙️ PRODUCTION</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://bg-maintenance-master.streamlit.app/" target="_blank" class="main-button maint">🔧 MAINTENANCE</a>', unsafe_allow_html=True)

with col2:
    st.markdown('<a href="https://bg-quality-master.streamlit.app/" target="_blank" class="main-button qual">🧪 QUALITY</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://bg-logistics-master.streamlit.app/" target="_blank" class="main-button logis">🚛 LOGISTICS</a>', unsafe_allow_html=True)

st.divider()
st.caption("© 2026 B&G Engineering Industries | Developed for Shopfloor Excellence")

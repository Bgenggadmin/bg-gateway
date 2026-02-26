import streamlit as st

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="B&G Engineering Gateway", layout="centered", page_icon="🏗️")

# --- 2. STYLING (Mobile-Friendly Buttons) ---
st.markdown("""
    <style>
    .master-btn {
        display: block;
        width: 100%;
        padding: 25px;
        margin-bottom: 20px;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        color: white !important;
        border-radius: 15px;
        background-color: #4527A0; /* Deep Purple */
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    .dept-btn {
        display: block;
        width: 100%;
        padding: 20px;
        margin: 10px 0;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        color: white !important;
        border-radius: 10px;
    }
    .prod { background-color: #2E7D32; } /* Green */
    .qual { background-color: #1565C0; } /* Blue */
    .maint { background-color: #C62828; } /* Red */
    .logis { background-color: #EF6C00; } /* Orange */
    </style>
""", unsafe_allow_html=True)

# --- 3. UI LAYOUT ---
st.title("🏗️ B&G Engineering Industries")
st.subheader("Smart Factory Management Suite")

# --- 4. MASTER ANALYTICS (Top Priority) ---
st.markdown('<a href="https://bg-analytics-master.streamlit.app/" target="_blank" class="master-btn">📊 MASTER ANALYTICS DASHBOARD</a>', unsafe_allow_html=True)

st.divider()
st.info("Select a department below to log data:")

# --- 5. DEPARTMENT BUTTONS (2x2 Grid) ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<a href="https://bg-production-master.streamlit.app/" target="_blank" class="dept-btn prod">⚙️ PRODUCTION</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://bg-maintenance-master.streamlit.app/" target="_blank" class="dept-btn maint">🔧 MAINTENANCE</a>', unsafe_allow_html=True)

with col2:
    st.markdown('<a href="https://bg-quality-master.streamlit.app/" target="_blank" class="dept-btn qual">🧪 QUALITY</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://bg-logistics-master.streamlit.app/" target="_blank" class="dept-btn logis">🚛 LOGISTICS</a>', unsafe_allow_html=True)

st.divider()
st.caption(f"© 2026 B&G Engineering Industries | Shopfloor Control v2.0")

import streamlit as st

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="B&G Engineering Gateway", layout="centered", page_icon="🏗️")

# --- 2. STYLING ---
st.markdown("""
    <style>
    .master-btn {
        display: block; width: 100%; padding: 25px; margin-bottom: 20px;
        font-size: 24px; font-weight: bold; text-align: center;
        text-decoration: none; color: white !important; border-radius: 15px;
        background-color: #4527A0; box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    .dept-btn {
        display: block; width: 100%; padding: 20px; margin: 10px 0;
        font-size: 18px; font-weight: bold; text-align: center;
        text-decoration: none; color: white !important; border-radius: 10px;
    }
    .prod { background-color: #2E7D32; }
    .qual { background-color: #1565C0; }
    .maint { background-color: #C62828; }
    .logis { background-color: #EF6C00; }
    </style>
""", unsafe_allow_html=True)

st.title("🏗️ B&G Engineering Industries")
st.subheader("Smart Factory Management Suite")

# --- 3. MASTER ANALYTICS (Top Priority) ---
# Using your active long-link for Analytics to avoid access errors
st.markdown('<a href="https://bg-analytics-master-p3xgwancmxryycn3gcsbsm.streamlit.app/" target="_blank" class="master-btn">📊 MASTER ANALYTICS DASHBOARD</a>', unsafe_allow_html=True)

st.divider()

# --- 4. DEPARTMENT BUTTONS (Fixed 2x2 Grid) ---
import streamlit as st

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="B&G Engineering Gateway", layout="centered", page_icon="🏗️")

# --- 2. STYLING ---
st.markdown("""
    <style>
    .master-btn {
        display: block; width: 100%; padding: 25px; margin-bottom: 20px;
        font-size: 24px; font-weight: bold; text-align: center;
        text-decoration: none; color: white !important; border-radius: 15px;
        background-color: #4527A0; box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    .dept-btn {
        display: block; width: 100%; padding: 20px; margin: 10px 0;
        font-size: 18px; font-weight: bold; text-align: center;
        text-decoration: none; color: white !important; border-radius: 10px;
    }
    .kishore { background-color: #1565C0; } /* API Blue */
    .ammu { background-color: #2E7D32; }    /* ZLD Green */
    .santhoshi { background-color: #EF6C00; } /* Purchase Orange */
    .founder { background-color: #C62828; }  /* Master Red */
    </style>
""", unsafe_allow_html=True)

st.title("🏗️ B&G Engineering Industries")
st.subheader("Smart Factory Management Suite")

# --- 3. MASTER ANALYTICS ---
# Replace 'your-portal-url' with: bg-anchor-portal.streamlit.app (or your actual URL)
portal_url = "https://bg-anchor-portal.streamlit.app/" 

st.markdown(f'<a href="{portal_url}?role=Founder" target="_blank" class="master-btn">📊 MASTER FOUNDER DASHBOARD</a>', unsafe_allow_html=True)

st.divider()

# --- 4. ANCHOR ENTRY BUTTONS (The Grid) ---
st.write("### 🔑 Anchor Reporting Access")
col1, col2 = st.columns(2)

with col1:
    # Kishore - API
    st.markdown(f'<a href="{portal_url}?role=API" target="_blank" class="dept-btn kishore">🏢 API ENTRY (KISHORE)</a>', unsafe_allow_html=True)
    # Santhoshi - Purchase
    st.markdown(f'<a href="{portal_url}?role=Purchase" target="_blank" class="dept-btn santhoshi">📦 PURCHASE (SANTHOSHI)</a>', unsafe_allow_html=True)

with col2:
    # Ammu - ZLD
    st.markdown(f'<a href="{portal_url}?role=ZLD" target="_blank" class="dept-btn ammu">💧 ZLD ENTRY (AMMU)</a>', unsafe_allow_html=True)
    # Maintenance or other future department
    st.markdown('<a href="#" class="dept-btn founder">🛠️ MAINTENANCE</a>', unsafe_allow_html=True)

st.divider()
st.caption(f"© 2026 B&G Engineering Industries | Shopfloor Control v3.0")

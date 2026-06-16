from database import (
    save_campaign,
    get_campaigns,
    save_volunteer,
    get_volunteers
)

import streamlit as st
from content_agent import generate_campaign_content
from poster_generator import create_poster
from datetime import date
import re
import html as html_module

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="NayePankh Foundation",
    page_icon="🌍",
    layout="wide"
)

# =========================
# HELPER FUNCTIONS
# =========================

def clean_text(value):
    if value is None:
        return ""
    cleaned = re.sub(r"<[^>]+>", "", str(value))
    cleaned = html_module.unescape(cleaned)
    return cleaned.strip()

# =========================
# SESSION STATE
# =========================

if "page" not in st.session_state:
    st.session_state.page = "Home"

page = st.session_state.page

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main { background-color: #050816; }

.block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}

.hero-section {
    background-image: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
        url('https://images.unsplash.com/photo-1529156069898-49953e39b3ac');
    background-size: cover;
    background-position: center;
    padding: 120px 50px;
    border-radius: 25px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

.hero-title   { font-size: 72px; font-weight: 800; margin-bottom: 20px; color: white !important; }
.hero-subtitle { font-size: 30px; margin-bottom: 20px; color: white !important; }
.hero-slogan  { font-size: 24px; color: #FFD166 !important; margin-bottom: 30px; }

.feature-card {
    background: linear-gradient(135deg, #141E30, #243B55);
    padding: 40px;
    border-radius: 25px;
    text-align: center;
    min-height: 320px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.3);
}
.feature-card * { color: white !important; }
.feature-icon  { font-size: 55px; margin-bottom: 20px; }
.feature-title { font-size: 30px; font-weight: bold; margin-bottom: 15px; }
.feature-text  { font-size: 18px; line-height: 1.6; }

/* ── FORCE dark text inside every white card ── */
.white-card {
    background: #ffffff !important;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.12);
}
.white-card h1,
.white-card h2,
.white-card h3,
.white-card h4,
.white-card p,
.white-card b,
.white-card span {
    color: #1E3A5F !important;
}

/* metric card variant — centred */
.metric-card {
    background: #ffffff !important;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 15px;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.12);
}
.metric-card h1,
.metric-card h2,
.metric-card p {
    color: #1E3A5F !important;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #FF6B35, #FF8E53);
    color: white !important;
    border: none;
    border-radius: 12px;
    height: 52px;
    font-size: 18px;
    font-weight: bold;
    margin-top: 10px;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #E85D2A, #FF6B35);
    color: white !important;
}

section[data-testid="stSidebar"] * { color: white !important; }

.stApp h1, .stApp h2, .stApp h3 { color: white; }

label,
.stSelectbox label,
.stTextInput label,
.stDateInput label,
.stTimeInput label,
.stMultiSelect label { color: white !important; }

.stAlert { border-radius: 12px; }

</style>
""", unsafe_allow_html=True)

# =========================
# HOME PAGE
# =========================

if page == "Home":

    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">🌍 NayePankh Foundation</div>
        <div class="hero-subtitle">AI Powered NGO Campaign & Volunteer Management Platform</div>
        <div class="hero-slogan">"Together We Rise, Together We Change Lives ❤️"</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📢</div>
            <div class="feature-title">Create Campaign</div>
            <div class="feature-text">Generate AI powered NGO campaigns, donor appeals and posters instantly.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Campaign Generator"):
            st.session_state.page = "Create Campaign"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🙋</div>
            <div class="feature-title">Volunteer Hub</div>
            <div class="feature-text">Register volunteers and manage campaign participation smartly.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Volunteer Management"):
            st.session_state.page = "Volunteer Management"
            st.rerun()

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">NGO Dashboard</div>
            <div class="feature-text">Track campaigns, volunteers, analytics and NGO growth.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Dashboard"):
            st.session_state.page = "Dashboard"
            st.rerun()

# =========================
# CREATE CAMPAIGN PAGE
# =========================

elif page == "Create Campaign":

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("📢 AI Campaign Generator")

    campaign_options = [
        "Blood Donation Drive", "Cloth Donation", "Food Distribution",
        "Tree Plantation", "Women Empowerment", "Menstrual Hygiene Awareness",
        "Child Education Support", "Health Checkup Camp",
        "Animal Welfare Campaign", "Environmental Awareness", "Other"
    ]

    selected_campaign = st.selectbox("Select Campaign", campaign_options)
    topic = st.text_input("Enter Custom Campaign") if selected_campaign == "Other" else selected_campaign

    india_cities = ["Mumbai", "Pune", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata"]
    location   = st.selectbox("Select City", india_cities)
    event_date = st.date_input("Select Date", min_value=date.today())
    event_time = st.time_input("Select Time")
    venue      = st.text_input("Venue Name")

    if st.button("Generate Campaign 🚀"):
        if venue.strip() == "":
            st.warning("Please enter venue.")
        else:
            with st.spinner("Generating AI Campaign..."):
                content = generate_campaign_content(topic, location, str(event_date), str(event_time), venue)
                poster  = create_poster(topic, location, str(event_date), str(event_time), venue)
                save_campaign(topic, location, str(event_date), str(event_time), venue, content)

            st.success("Campaign Generated Successfully ✅")
            col1, col2 = st.columns([2, 1])
            with col1:
                st.subheader("📢 Campaign Content")
                st.markdown(content)
            with col2:
                st.subheader("🎨 AI Poster")
                st.image(poster, use_container_width=True)

# =========================
# VOLUNTEER PAGE
# =========================

elif page == "Volunteer Management":

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🙋 Volunteer Management")

    campaigns      = get_campaigns()
    campaign_names = [c[1] for c in campaigns]

    col1, col2 = st.columns(2)

    with col1:
        vol_name  = st.text_input("Volunteer Name")
        vol_email = st.text_input("Email Address")
        vol_phone = st.text_input("Phone Number")

    with col2:
        india_cities = ["Mumbai", "Pune", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata"]
        vol_city = st.selectbox("City", india_cities)
        skills   = st.multiselect("Skills", ["Teaching", "Designing", "Photography",
                                             "Social Media", "Event Management", "Fundraising"])

        if len(campaign_names) == 0:
            st.warning("No campaigns available.")
        else:
            selected_campaign = st.selectbox("Select Campaign", campaign_names)

    if st.button("Register Volunteer"):
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if vol_name.strip() == "":
            st.error("Enter volunteer name.")
        elif not re.match(email_pattern, vol_email):
            st.error("Invalid email address.")
        elif not vol_phone.isdigit() or len(vol_phone) != 10:
            st.error("Phone number must contain 10 digits.")
        elif len(skills) == 0:
            st.error("Select at least one skill.")
        else:
            save_volunteer(vol_name, vol_email, vol_phone, vol_city, ", ".join(skills), selected_campaign)
            st.success("Volunteer Registered Successfully ✅")

# =========================
# DASHBOARD PAGE
# =========================

elif page == "Dashboard":

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.markdown("""
    <div style="background:linear-gradient(135deg,#1e3c72,#2a5298);
                padding:35px; border-radius:20px; text-align:center;
                color:white; margin-bottom:30px;">
        <h1 style="color:white;">📊 NGO Impact Dashboard</h1>
        <h3 style="color:white;">Track Campaigns, Volunteers & Community Impact</h3>
    </div>
    """, unsafe_allow_html=True)

    campaigns  = get_campaigns()
    volunteers = get_volunteers()

    total_campaigns  = len(campaigns)
    total_volunteers = len(volunteers)
    today            = str(date.today())

    upcoming     = []
    completed    = []
    today_events = []

    for campaign in campaigns:
        cd = campaign[3]
        if cd > today:
            upcoming.append(campaign)
        elif cd < today:
            completed.append(campaign)
        else:
            today_events.append(campaign)

    # ── Metric cards ──────────────────────────────────────────
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h2>📢</h2>
            <h1>{total_campaigns}</h1>
            <p>Total Campaigns</p>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h2>🙋</h2>
            <h1>{total_volunteers}</h1>
            <p>Total Volunteers</p>
        </div>""", unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h2>📅</h2>
            <h1>{len(today_events)}</h1>
            <p>Today's Events</p>
        </div>""", unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h2>🚀</h2>
            <h1>{len(upcoming)}</h1>
            <p>Upcoming</p>
        </div>""", unsafe_allow_html=True)

    st.divider()

    # ── Upcoming Campaigns ────────────────────────────────────
    st.subheader("🚀 Upcoming Campaigns")

    if upcoming:
        for campaign in upcoming:
            t  = clean_text(campaign[1])
            lo = clean_text(campaign[2])
            d  = clean_text(campaign[3])
            ti = clean_text(campaign[4])
            v  = clean_text(campaign[5])

            st.markdown(f"""
            <div class="white-card">
                <h3>{t}</h3>
                <p>📍 {lo}</p>
                <p>📅 {d}</p>
                <p>⏰ {ti}</p>
                <p>🏢 {v}</p>
            </div>""", unsafe_allow_html=True)
    else:
        st.info("No upcoming campaigns.")

    st.divider()

    # ── Volunteers per Campaign ───────────────────────────────
    st.subheader("📊 Volunteers Per Campaign")

    campaign_counts = {}
    for volunteer in volunteers:
        cn = volunteer[6]
        campaign_counts[cn] = campaign_counts.get(cn, 0) + 1

    if campaign_counts:
        st.bar_chart(campaign_counts)
        for campaign, count in campaign_counts.items():
            st.markdown(f"""
            <div class="white-card">
                <p>✅ <b>{clean_text(campaign)}</b> → {count} Volunteers</p>
            </div>""", unsafe_allow_html=True)
    else:
        st.info("No volunteer analytics available.")

    st.divider()

    # ── Registered Volunteers ─────────────────────────────────
    st.subheader("🙋 Registered Volunteers")

    if volunteers:
        for volunteer in volunteers:
            nm = clean_text(volunteer[1])
            em = clean_text(volunteer[2])
            ph = clean_text(volunteer[3])
            ci = clean_text(volunteer[4])
            sk = clean_text(volunteer[5])
            ca = clean_text(volunteer[6])

            st.markdown(f"""
            <div class="white-card">
                <h3>{nm}</h3>
                <p>📧 {em}</p>
                <p>📱 {ph}</p>
                <p>🌆 {ci}</p>
                <p>🛠️ {sk}</p>
                <p>🎯 {ca}</p>
            </div>""", unsafe_allow_html=True)
    else:
        st.info("No volunteers registered yet.")
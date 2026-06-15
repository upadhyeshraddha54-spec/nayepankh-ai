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

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="NayePankh Foundation",
    page_icon="🌍",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1, h2, h3 {
    color: #1E3A5F;
    font-weight: 700;
}

.stButton>button {
    background-color: #ff6b35;
    color: white;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    border: none;
    width: 100%;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #e85d2a;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #1E3A5F;
}

[data-testid="stSidebar"] * {
    color: white;
}

.block-container {
    padding-top: 2rem;
}

.metric-box {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 2px 12px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

st.sidebar.markdown("""
# 🌍 NayePankh Foundation

### AI NGO Platform ❤️
""")

page = st.sidebar.radio(
    "Navigation",
    [
        "Create Campaign",
        "Volunteer Management",
        "Dashboard"
    ]
)

# =========================
# HERO SECTION
# =========================

st.markdown("""
# 🌍 NayePankh Foundation

### Empowering Communities Through AI & Volunteerism ❤️

---
""")

# =========================
# CREATE CAMPAIGN PAGE
# =========================

if page == "Create Campaign":

    st.title("📢 AI Campaign Generator")

    campaign_options = [
        "Blood Donation Drive",
        "Cloth Donation",
        "Food Distribution",
        "Tree Plantation",
        "Women Empowerment",
        "Menstrual Hygiene Awareness",
        "Child Education Support",
        "Health Checkup Camp",
        "Animal Welfare Campaign",
        "Environmental Awareness",
        "Other"
    ]

    selected_campaign = st.selectbox(
        "Select Campaign",
        campaign_options
    )

    # CUSTOM CAMPAIGN

    if selected_campaign == "Other":

        topic = st.text_input(
            "Enter Custom Campaign"
        )

    else:

        topic = selected_campaign

    # CITY

    india_cities = [
        "Mumbai",
        "Pune",
        "Delhi",
        "Bangalore",
        "Hyderabad",
        "Chennai",
        "Kolkata"
    ]

    location = st.selectbox(
        "Select City",
        india_cities
    )

    # DATE

    event_date = st.date_input(
        "Select Date",
        min_value=date.today()
    )

    # TIME

    event_time = st.time_input(
        "Select Time"
    )

    # VENUE

    venue = st.text_input(
        "Venue Name"
    )

    # GENERATE BUTTON

    if st.button("Generate Campaign 🚀"):

        if venue.strip() == "":

            st.warning("Please enter venue.")

        else:

            with st.spinner("Generating AI Campaign..."):

                content = generate_campaign_content(
                    topic,
                    location,
                    str(event_date),
                    str(event_time),
                    venue
                )

                poster = create_poster(
                    topic,
                    location,
                    str(event_date),
                    str(event_time),
                    venue
                )

                save_campaign(
                    topic,
                    location,
                    str(event_date),
                    str(event_time),
                    venue,
                    content
                )

            st.success("Campaign Generated Successfully ✅")

            col1, col2 = st.columns([2,1])

            with col1:

                st.subheader("📢 Campaign Content")
                st.markdown(content)

            with col2:

                st.subheader("🎨 AI Poster")
                st.image(
                    poster,
                    use_container_width=True
                )

# =========================
# VOLUNTEER MANAGEMENT
# =========================

elif page == "Volunteer Management":

    st.title("🙋 Volunteer Management")

    campaigns = get_campaigns()

    campaign_names = []

    for campaign in campaigns:

        campaign_names.append(campaign[1])

    col1, col2 = st.columns(2)

    with col1:

        vol_name = st.text_input(
            "Volunteer Name"
        )

        vol_email = st.text_input(
            "Email Address"
        )

        vol_phone = st.text_input(
            "Phone Number"
        )

    with col2:

        india_cities = [
            "Mumbai",
            "Pune",
            "Delhi",
            "Bangalore",
            "Hyderabad",
            "Chennai",
            "Kolkata"
        ]

        vol_city = st.selectbox(
            "City",
            india_cities
        )

        skills = st.multiselect(
            "Skills",
            [
                "Teaching",
                "Designing",
                "Photography",
                "Social Media",
                "Event Management",
                "Fundraising"
            ]
        )

        if len(campaign_names) == 0:

            st.warning(
                "No campaigns available. Create campaign first."
            )

        else:

            selected_campaign = st.selectbox(
                "Select Campaign",
                campaign_names
            )

    # REGISTER BUTTON

    if st.button("Register Volunteer"):

        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if vol_name.strip() == "":

            st.error("Please enter volunteer name.")

        elif not re.match(email_pattern, vol_email):

            st.error("Invalid email address.")

        elif not vol_phone.isdigit() or len(vol_phone) != 10:

            st.error("Phone number must contain 10 digits.")

        elif len(skills) == 0:

            st.error("Please select at least one skill.")

        else:

            save_volunteer(
                vol_name,
                vol_email,
                vol_phone,
                vol_city,
                ", ".join(skills),
                selected_campaign
            )

            st.success(
                "Volunteer Registered Successfully ✅"
            )

            # =========================
            # AI VOLUNTEER MATCHING
            # =========================

            st.subheader("🤖 AI Volunteer Matching")

            if "Teaching" in skills and "Education" in selected_campaign:

                st.success(
                    "Perfect Match: Teaching Volunteer for Education Campaign 🎓"
                )

            elif "Event Management" in skills and "Tree" in selected_campaign:

                st.success(
                    "Perfect Match: Event Coordinator for Plantation Drive 🌱"
                )

            elif "Social Media" in skills:

                st.success(
                    "Recommended Role: Social Media Promotion 📱"
                )

            else:

                st.info(
                    "Volunteer added successfully to campaign."
                )

# =========================
# DASHBOARD
# =========================

elif page == "Dashboard":

    st.title("📊 NGO Dashboard")

    st.info("""
    NayePankh Foundation is a student-led NGO working towards:

    • Food Distribution  
    • Child Education  
    • Women Empowerment  
    • Animal Welfare  
    • Environmental Awareness
    """)

    campaigns = get_campaigns()
    volunteers = get_volunteers()

    # =========================
    # METRICS
    # =========================

    total_campaigns = len(campaigns)
    total_volunteers = len(volunteers)

    today = str(date.today())

    upcoming = []
    completed = []
    today_events = []

    for campaign in campaigns:

        campaign_date = campaign[3]

        if campaign_date > today:

            upcoming.append(campaign)

        elif campaign_date < today:

            completed.append(campaign)

        else:

            today_events.append(campaign)

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📢 Total Campaigns",
            total_campaigns
        )

    with col2:

        st.metric(
            "🙋 Total Volunteers",
            total_volunteers
        )

    with col3:

        st.metric(
            "📅 Today's Events",
            len(today_events)
        )

    st.divider()

    # =========================
    # IMPACT METRICS
    # =========================

    st.subheader("🌍 NGO Impact")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Lives Impacted", "2 Lakh+")

    with col2:
        st.metric("Cities Reached", "10+")

    with col3:
        st.metric("Active Volunteers", total_volunteers)

    st.divider()

    # =========================
    # UPCOMING CAMPAIGNS
    # =========================

    st.subheader("🚀 Upcoming Campaigns")

    if upcoming:

        for campaign in upcoming:

            st.markdown(f"""
            ### {campaign[1]}

            📍 {campaign[2]}

            📅 {campaign[3]}

            ⏰ {campaign[4]}

            🏢 {campaign[5]}
            """)

            st.divider()

    else:

        st.info("No upcoming campaigns.")

    # =========================
    # TODAY EVENTS
    # =========================

    st.subheader("📅 Today's Campaigns")

    if today_events:

        for campaign in today_events:

            st.success(f"""
            {campaign[1]}
            | 📍 {campaign[2]}
            | ⏰ {campaign[4]}
            """)

    else:

        st.info("No events today.")

    # =========================
    # COMPLETED CAMPAIGNS
    # =========================

    st.subheader("✅ Completed Campaigns")

    if completed:

        for campaign in completed:

            st.markdown(
                f"• {campaign[1]} — {campaign[3]}"
            )

    else:

        st.info("No completed campaigns.")

    st.divider()

    # =========================
    # VOLUNTEERS PER CAMPAIGN
    # =========================

    st.subheader("📊 Volunteers Per Campaign")

    campaign_counts = {}

    for volunteer in volunteers:

        campaign_name = volunteer[6]

        if campaign_name in campaign_counts:

            campaign_counts[campaign_name] += 1

        else:

            campaign_counts[campaign_name] = 1

    if campaign_counts:

        st.bar_chart(campaign_counts)

        for campaign, count in campaign_counts.items():

            st.markdown(
                f"✅ {campaign} → {count} Volunteers"
            )

    else:

        st.info("No volunteer analytics available.")

    st.divider()

    # =========================
    # REGISTERED VOLUNTEERS
    # =========================

    st.subheader("🙋 Registered Volunteers")

    if volunteers:

        for volunteer in volunteers:

            st.markdown(f"""
            ### {volunteer[1]}

            📧 {volunteer[2]}

            📱 {volunteer[3]}

            🌆 {volunteer[4]}

            🛠️ {volunteer[5]}

            🎯 {volunteer[6]}
            """)

            st.divider()

    else:

        st.warning("No volunteers registered yet.")

# =========================
# FOOTER
# =========================

st.markdown("""
---
<center>
Made with ❤️ for NayePankh Foundation
</center>
""", unsafe_allow_html=True)
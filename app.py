import streamlit as st
import pandas as pd
import numpy as np
import time

# Page Configuration
st.set_page_config(
    page_title="Hasnain Shaikh | Business & AI Intelligence Suite",
    page_icon="📊",
    layout="wide"
)

# Sidebar - Professional Profile
st.sidebar.title("Hasnain Shaikh")
st.sidebar.caption("BBA - International Business & Applied AI")
st.sidebar.markdown("""
- **Focus:** Business Development, Growth Strategy, CRM & Market Expansion
- **Education:** BBA (CSMU) | IIMB Executive Cert. (In Progress)
- **Email:** 20comeback26@gmail.com
""")

st.sidebar.divider()
st.sidebar.subheader("Navigation")
app_mode = st.sidebar.radio("Select Intelligence Tool:", [
    "1. Market Expansion Simulator",
    "2. AI CRM & Acquisition Engine",
    "3. Financial & CAC Diagnostics",
    "4. Interactive Resume & Portfolio"
])

# TOOL 1: Market Expansion Simulator
if app_mode == "1. Market Expansion Simulator":
    st.title("🌐 Cross-Border Market Expansion Simulator")
    st.write("Quantitative model evaluating market entry feasibility and regulatory friction.")

    col1, col2, col3 = st.columns(3)
    with col1:
        origin = st.selectbox("Origin Market", ["India", "UAE", "Singapore"])
    with col2:
        target = st.selectbox("Target Market", ["UAE", "United States", "United Kingdom", "Germany"])
    with col3:
        sector = st.selectbox("Industry Sector", ["E-Commerce", "Digital Services", "Export/Import Trade"])

    budget = st.slider("Initial Market Entry Budget ($USD)", 5000, 100000, 25000, step=5000)

    st.subheader("Feasibility Analysis")
    
    # Calculate simulated metrics
    est_cac = int(budget * 0.12 / 100) + 45
    est_payback = round(budget / (est_cac * 150), 1)
    compliance_score = "High" if target in ["UAE", "Singapore"] else "Moderate"

    m1, m2, m3 = st.columns(3)
    m1.metric("Est. Customer Acquisition Cost (CAC)", f"${est_cac}")
    m2.metric("Projected Payback Period", f"{est_payback} Months")
    m3.metric("Regulatory Compliance Complexity", compliance_score)

    st.markdown("### Strategic Roadmap")
    st.info(f"**Action Plan for Entry into {target}:**\n"
            f"1. **Market Validation:** Deploy localized test campaigns in {target} focusing on high-intent B2B audiences.\n"
            f"2. **Regulatory Setup:** Fulfill cross-border compliance and trade documentation requirements.\n"
            f"3. **CRM Integration:** Automate multi-touch email and channel outreach to minimize SLA turnaround.")

# TOOL 2: AI CRM Engine
elif app_mode == "2. AI CRM & Acquisition Engine":
    st.title("⚡ AI-Driven CRM & Campaign Generator")
    st.write("Demonstration of prompt engineering and automated client communication workflows.")

    client_type = st.selectbox("Target Client Profile", [
        "Private Banking / High-Net-Worth Individual",
        "B2B E-Commerce Retailer",
        "Cross-Border Trade Client"
    ])
    
    objective = st.selectbox("Campaign Objective", [
        "Portfolio Diversification Offer",
        "CRM & Workflow Optimization Pitch",
        "International Market Entry Strategy"
    ])

    if st.button("Generate Automated Campaign Sequence"):
        with st.spinner("Processing workflow automation..."):
            time.sleep(1)

        st.success("Campaign Strategy Generated!")
        st.subheader("Automated Lead Outreach Sequence")

        if "Private Banking" in client_type:
            st.code(f"""
Subject: Strategic Portfolio Review & Sustainable Wealth Allocation

Dear [Client Name],

Following our initial consultation regarding your long-term wealth objectives—specifically around retirement structuring and sustainable allocations—I have outlined a streamlined overview of product alignment for your review.

Key Highlights:
- Custom liquidity structuring matching your 3-year timeline.
- ESG-aligned investment channels targeting balanced yield.

Would you be open to a brief 15-minute sync this Thursday to review the comparative analysis?

Best regards,
Hasnain Shaikh
Client Strategy Specialist
            """, language="markdown")
        else:
            st.code(f"""
Subject: Operational Scaling: Reducing CRM Turnaround & CAC

Dear [Partner Name],

In analyzing recent market benchmarks for {client_type}s, operational delays in client onboarding consistently increase overall acquisition costs.

By implementing AI-driven automated workflows, organizations in your sector have reduced campaign turnaround times by up to 30% while increasing qualified pipeline lead flow.

Let's discuss how we can apply these operational efficiencies to your upcoming acquisition campaigns.

Best regards,
Hasnain Shaikh
Business Development Specialist
            """, language="markdown")

# TOOL 3: Financial & CAC Diagnostics
elif app_mode == "3. Financial & CAC Diagnostics":
    st.title("📈 Growth Analytics & Financial Modeling")
    
    st.subheader("Simulated Campaign Performance & ROI")
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    df = pd.DataFrame({
        "Month": months,
        "Ad Spend ($)": [2000, 2500, 3000, 3500, 4200, 5000],
        "Acquired Clients": [18, 26, 35, 42, 58, 72],
        "Revenue ($)": [5400, 7800, 10500, 12600, 17400, 21600]
    })
    df["CAC ($)"] = round(df["Ad Spend ($)"] / df["Acquired Clients"], 2)
    df["ROI (x)"] = round(df["Revenue ($)"] / df["Ad Spend ($)"], 2)

    st.dataframe(df, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.line_chart(df.set_index("Month")[["Ad Spend ($)", "Revenue ($)"]])
    with col2:
        st.line_chart(df.set_index("Month")["CAC ($)"])

# TOOL 4: Interactive Resume
elif app_mode == "4. Interactive Resume & Portfolio":
    st.title("📄 Candidate Overview & Credentials")
    
    st.markdown("""
    ### **SHAIKH HASNAIN ROSHAN**
    *Mumbai, Maharashtra | 20comeback26@gmail.com | +91 9892107389*
    
    #### **Professional Summary**
    Business Administration student specializing in International Business and Marketing Technology, with entrepreneurial experience across independent ventures spanning digital marketing, e-commerce operations, and CRM execution[cite: 1].
    
    #### **Core Capabilities**
    - **Strategic Planning & BD:** Market research, market entry analysis, financial reporting[cite: 1].
    - **Applied AI & CRM:** Automating workflows, reducing campaign lead times, and optimizing ROI[cite: 1].
    - **Certifications:** NISM, Skill India / NASSCOM AI Analyst, upGrad Marketing, IIMB Executive Cert. (In Progress)[cite: 1].
    """)

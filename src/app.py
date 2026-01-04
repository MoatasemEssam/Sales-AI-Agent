import streamlit as st
import requests

st.set_page_config(page_title="SAB AI Sales Agent", page_icon="🏦")

st.title("🏦 SAB AI Sales Automation")
st.markdown("Automated Research & Personalized Outreach for Saudi Corporate Banking.")

company = st.text_input("Target Company Name", placeholder="e.g. Saudi Aramco or STC")

if st.button("Start Automation"):
    if company:
        with st.status("🤖 Agent at work...", expanded=True) as status:
            st.write("Searching Saudi business news...")
            # Calling the FastAPI Backend
            try:
                response = requests.post(
                    "http://localhost:8000/generate-sales-lead", 
                    json={"company": company}
                )
                if response.status_code == 200:
                    data = response.json()
                    status.update(label="✅ Analysis Complete", state="complete", expanded=False)
                    
                    st.subheader("Personalized Sales Pitch")
                    st.info(data["pitch"])
                    
                    with st.expander("View AI Research Source"):
                        st.write(data["raw_research"])
                else:
                    st.error("Backend Error: Is the FastAPI server running?")
            except Exception as e:
                st.error(f"Connection Failed: {e}")
    else:
        st.warning("Please enter a company name.")
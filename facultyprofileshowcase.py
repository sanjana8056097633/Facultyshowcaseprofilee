import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyBHzx-k_9qtFuxcJAX1GG6FbH3KdR7vDzQ")

st.title("🎓 Faculty Profile Showcase + Email Generator")

with st.form("faculty_form"):
    name = st.text_input("Faculty Name")
    department = st.text_input("Department")
    qualification = st.text_input("Qualifications")
    expertise = st.text_area("Areas of Expertise")
    achievements = st.text_area("Achievements")
    contact_email = st.text_input("Contact Email")

    submitted = st.form_submit_button("Generate Email")

if submitted:
    prompt = f"""
    Generate a formal introductory email for a faculty profile:
    Name: {name}
    Department: {department}
    Qualification: {qualification}
    Areas of Expertise: {expertise}
    Achievements: {achievements}
    Contact Email: {contact_email}

    The email should introduce the faculty to students or collaborators and summarize the expertise.
    """

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    st.subheader("📧 AI-Generated Email")
    st.write(response.text)

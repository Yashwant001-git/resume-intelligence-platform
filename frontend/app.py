"""
Resume Intelligence Platform
"""

import streamlit as st

from components.upload import UploadComponent
from components.personal_info import PersonalInfoComponent
from components.skills import SkillsComponent
from components.education import EducationComponent
from components.experience import ExperienceComponent
from components.projects import ProjectsComponent
from components.certifications import CertificationsComponent

from services.api import APIService

from utils.constants import (
    APP_TITLE,
    APP_DESCRIPTION,
)

# Page Configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📄",
    layout="wide",
)

# Sidebar
with st.sidebar:

    st.title("Resume Intelligence")

    st.write(APP_DESCRIPTION)

    st.divider()

    st.success("Backend Connected")

    st.divider()

    st.caption("Version 1.0.0")

# Header
st.title(APP_TITLE)

st.write(
    "Upload a resume to extract structured candidate information."
)

st.divider()

# Upload Resume
response = UploadComponent.render()

# Display Candidate Information
if response:

    candidate = response["candidate"]

    # Personal Information
    st.divider()

    PersonalInfoComponent.render(candidate)

    # Skills
    st.divider()

    SkillsComponent.render(candidate)

    # Education
    st.divider()

    EducationComponent.render(candidate)

    # Experience
    st.divider()

    ExperienceComponent.render(candidate)

    # Projects
    st.divider()

    ProjectsComponent.render(candidate)

    # Certifications
    st.divider()

    CertificationsComponent.render(candidate)

    st.divider()

    st.success("Resume processed successfully.")

    # st.divider()
    try:

        excel_data = APIService.download_excel()

        st.download_button(
            label="📥 Download Excel",
            data=excel_data,
            file_name="resumes.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )

    except Exception:

        st.warning("Excel file is not available.")
# import streamlit as st

# from services.api import APIService


# class UploadComponent:

#     @staticmethod
#     def render():

#         st.subheader("Upload Resume")

#         uploaded_file = st.file_uploader(
#             "Choose a PDF Resume",
#             type=["pdf"],
#         )

#         if uploaded_file is None:
#             return None

#         if st.button(
#             "Process Resume",
#             use_container_width=True,
#         ):

#             with st.spinner("Processing Resume..."):

#                 try:

#                     response = APIService.upload_resume(
#                         uploaded_file
#                     )

#                     st.success(
#                         "Resume processed successfully!"
#                     )

#                     return response

#                 except Exception as e:

#                     st.error(str(e))

#         return 




"""
Upload component for uploading resumes.
"""

import streamlit as st

from services.api import APIService
from utils.constants import SUPPORTED_FILE_TYPES


class UploadComponent:
    """
    Handles resume upload.
    """

    @staticmethod
    def render() -> dict | None:
        """
        Render the upload component.

        Returns
        -------
        dict | None
            API response if successful,
            otherwise None.
        """

        st.subheader("Upload Resume")

        uploaded_file = st.file_uploader(
            label="Choose a Resume",
            type=SUPPORTED_FILE_TYPES,
            key="resume_upload",
        )

        if uploaded_file is None:
            return None

        st.success(f"Selected: {uploaded_file.name}")

        if st.button(
            "Process Resume",
            use_container_width=True,
            key="process_resume",
        ):

            with st.spinner("Processing Resume..."):

                try:

                    response = APIService.upload_resume(
                        uploaded_file
                    )

                    st.success(
                        "Resume processed successfully!"
                    )

                    return response

                except Exception as error:

                    st.error(
                        f"Failed to process resume.\n\n{error}"
                    )

        return None
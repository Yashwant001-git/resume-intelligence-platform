# import streamlit as st


# class CertificationsComponent:

#     @staticmethod
#     def render(candidate: dict):

#         st.subheader("📜 Certifications")

#         certifications = candidate["certifications"]

#         if not certifications:

#             st.info("No certifications found.")

#             return

#         for certification in certifications:

#             st.success(certification)



"""
Displays candidate certifications.
"""

import streamlit as st


class CertificationsComponent:
    """
    Renders candidate certifications.
    """

    @staticmethod
    def render(candidate: dict) -> None:
        """
        Display candidate certifications.
        """

        certifications = candidate.get(
            "certifications",
            [],
        )

        st.subheader("Certifications")

        if not certifications:

            st.info("No certifications found.")

            return

        with st.container(border=True):

            for certification in certifications:

                st.write(f"{certification}")
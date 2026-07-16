# import streamlit as st


# class EducationComponent:

#     @staticmethod
#     def render(candidate: dict):

#         st.subheader("🎓 Education")

#         education = candidate["education"]

#         if not education:

#             st.info("No education found.")

#             return

#         for record in education:

#             with st.container(border=True):

#                 st.markdown(f"### {record['degree']}")

#                 st.write(f"**Institute:** {record['institute']}")

#                 st.write(f"**Duration:** {record['duration']}")

#                 st.write(f"**CGPA:** {record['cgpa']}")




"""
Displays candidate education information.
"""

import streamlit as st


class EducationComponent:
    """
    Renders candidate education details.
    """

    @staticmethod
    def render(candidate: dict) -> None:
        """
        Display candidate education.
        """

        education = candidate.get("education", [])

        st.subheader("🎓 Education")

        if not education:

            st.info("No education records found.")

            return

        for record in education:

            with st.container(border=True):

                st.markdown(
                    f"### {record.get('degree', '-')}"
                )

                st.write(
                    f"**Institute:** {record.get('institute', '-')}"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        f"**Duration:** {record.get('duration', '-')}"
                    )

                with col2:

                    st.write(
                        f"**CGPA:** {record.get('cgpa', '-')}"
                    )
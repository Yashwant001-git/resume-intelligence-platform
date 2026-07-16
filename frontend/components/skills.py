# import streamlit as st


# class SkillsComponent:

#     @staticmethod
#     def render(candidate: dict):

#         st.subheader("🛠 Skills")

#         skills = candidate["skills"]

#         if not skills:

#             st.info("No skills found.")

#             return

#         cols = st.columns(3)

#         for index, skill in enumerate(skills):

#             cols[index % 3].success(skill)


"""
Displays candidate skills.
"""

import streamlit as st


class SkillsComponent:
    """
    Renders candidate skills.
    """

    @staticmethod
    def render(candidate: dict) -> None:
        """
        Display candidate skills.
        """

        skills = candidate.get("skills", [])

        st.subheader("🛠 Technical Skills")

        if not skills:

            st.info("No skills found.")

            return

        with st.container(border=True):

            columns = st.columns(3)

            for index, skill in enumerate(skills):

                column = columns[index % 3]

                with column:

                    st.info(skill)
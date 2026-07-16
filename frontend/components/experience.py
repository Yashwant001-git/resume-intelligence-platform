# import streamlit as st


# class ExperienceComponent:

#     @staticmethod
#     def render(candidate: dict):

#         st.subheader("💼 Experience")

#         experiences = candidate["experience"]

#         if not experiences:

#             st.info("No experience found.")

#             return

#         for exp in experiences:

#             with st.container(border=True):

#                 st.markdown(f"### {exp['designation']}")

#                 st.write(exp["company"])

#                 st.caption(exp["duration"])

#                 st.write(exp["description"])


"""
Displays candidate work experience.
"""

import streamlit as st


class ExperienceComponent:
    """
    Renders candidate work experience.
    """

    @staticmethod
    def render(candidate: dict) -> None:
        """
        Display candidate experience.
        """

        experiences = candidate.get("experience", [])

        st.subheader("💼 Experience")

        if not experiences:

            st.info("No experience found.")

            return

        for experience in experiences:

            title = (
                f"{experience.get('designation', '-')}"
                f" | "
                f"{experience.get('company', '-')}"
            )

            with st.expander(title, expanded=False):

                st.write(
                    f"**Duration:** "
                    f"{experience.get('duration', '-')}"
                )

                st.divider()

                description = experience.get(
                    "description",
                    "",
                )

                if description:

                    for line in description.split("\n"):

                        line = line.strip()

                        if line:

                            st.write(line)

                else:

                    st.write("No description available.")
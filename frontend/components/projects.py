# import streamlit as st


# class ProjectsComponent:

#     @staticmethod
#     def render(candidate: dict):

#         st.subheader("🚀 Projects")

#         projects = candidate["projects"]

#         if not projects:

#             st.info("No projects found.")

#             return

#         for project in projects:

#             with st.container(border=True):

#                 st.markdown(f"### {project['title']}")

#                 if project["technologies"]:

#                     st.write(
#                         "**Technologies:** "
#                         + ", ".join(project["technologies"])
#                     )

#                 st.write(project["description"])

"""
Displays candidate projects.
"""

import streamlit as st


class ProjectsComponent:
    """
    Renders candidate projects.
    """

    @staticmethod
    def render(candidate: dict) -> None:
        """
        Display candidate projects.
        """

        projects = candidate.get("projects", [])

        st.subheader("🚀 Projects")

        if not projects:

            st.info("No projects found.")

            return

        for project in projects:

            title = project.get("title", "Untitled Project")

            with st.expander(title, expanded=False):

                technologies = project.get(
                    "technologies",
                    [],
                )

                if technologies:

                    st.write(
                        "**Technologies:** "
                        + ", ".join(technologies)
                    )

                    st.divider()

                description = project.get(
                    "description",
                    "",
                )

                if description:

                    for line in description.split("\n"):

                        line = line.strip()

                        if line:

                            st.write(line)

                else:

                    st.write(
                        "No description available."
                    )
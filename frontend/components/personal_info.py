# import streamlit as st


# class PersonalInfoComponent:

#     @staticmethod
#     def render(candidate: dict):

#         info = candidate["personal_info"]

#         social = candidate["social_links"]

#         st.subheader("👤 Personal Information")

#         col1, col2 = st.columns(2)

#         with col1:

#             st.write(f"**Name** : {info['name']}")

#             st.write(f"**Email** : {info['email']}")

#             st.write(f"**Phone** : {info['phone']}")

#         with col2:

#             st.write(f"**LinkedIn** : {social['linkedin'] or '-'}")

#             st.write(f"**GitHub** : {social['github'] or '-'}")

#             st.write(f"**Portfolio** : {social['portfolio'] or '-'}")



"""
Displays candidate personal information.
"""

import streamlit as st


class PersonalInfoComponent:
    """
    Renders candidate personal information.
    """

    @staticmethod
    def render(candidate: dict) -> None:
        """
        Display personal information.
        """

        info = candidate.get("personal_info", {})
        social = candidate.get("social_links", {})

        st.subheader("👤 Personal Information")

        with st.container(border=True):

            left, right = st.columns(2)

            with left:

                st.markdown("##### Basic Information")

                st.write(
                    f"**Name:** {info.get('name', '-')}"
                )

                st.write(
                    f"**Email:** {info.get('email', '-')}"
                )

                st.write(
                    f"**Phone:** {info.get('phone', '-')}"
                )

            with right:

                st.markdown("##### Social Links")

                st.write(
                    f"**LinkedIn:** {social.get('linkedin') or '-'}"
                )

                st.write(
                    f"**GitHub:** {social.get('github') or '-'}"
                )

                st.write(
                    f"**Portfolio:** {social.get('portfolio') or '-'}"
                )
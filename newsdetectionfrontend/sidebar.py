import streamlit as st
from streamlit_option_menu import option_menu

def show_sidebar(current_page):
    with st.sidebar:
        st.markdown("""
            <style>

            /* Sidebar */
            [data-testid="stSidebar"]{
                background: linear-gradient(
                    180deg,
                    #1F2937 0%,
                    #111827 50%,
                    #0F172A 100%
                );
                border-right: 2px solid #8B5CF6;
                box-shadow: 5px 0px 25px rgba(139, 92, 246, 0.35);
            }

            </style>
            """, unsafe_allow_html=True)
        
        # Profile Section
        st.markdown("""
        <div style="text-align:center;">
            <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
                width="100" style="border-radius:50%;">
            <h3 style="color:white; margin-top:10px;">Welcome!</h3>
            <p style="color:white;">AI Fake News Detector</p>
        </div>
        <hr>
        """, unsafe_allow_html=True)

        # Navigation Menu
        selected = option_menu(
            menu_title=None,
            options=[
                "Home",
                "Prediction",
                "History",
                "About",
                "Logout"
            ],
            icons=[
                "house-fill",
                "search",
                "clock-history",
                "person-circle",
                "info-circle",
                "box-arrow-right"
            ],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {
                    "padding": "5!important",
                    "background-color": "#111827",
                },
                "icon": {
                    "color": "#C084FC",
                    "font-size": "20px",
                },
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#7E22CE",
                    "color": "white",
                    "border-radius": "10px",
                },
                "nav-link-selected": {
                    "background-color": "#8B5CF6",
                    "color": "white",
                    "border-radius": "10px",
                },
            },
        )

    # ---------------- Main Page ----------------
    if selected == "Home":
        st.title("🏠 Home")
        st.switch_page("app.py")


    elif selected == "Prediction":
        st.title("📰 Fake News Prediction")
        st.switch_page("pages/03_Predict.py")


    elif selected == "History":
        st.title("📜 Prediction History")
        st.switch_page("pages/04_history.py")


    elif selected == "About":
        st.title("ℹ️ About")
        st.switch_page("05_About.py")


    elif selected == "Logout":
        st.success("Logged Out Successfully")

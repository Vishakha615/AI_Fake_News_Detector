
import streamlit as st
import requests
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import pandas as pd


st.set_page_config(
    page_title="Predict News",
    page_icon="🔍",
    layout="wide"
)



st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #000000,
        #120024,
        #3A0CA3,
        #7209B7
    );
}
</style>
""", unsafe_allow_html=True)



# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Redirect to login if not logged in
if not st.session_state.logged_in:
    st.switch_page("pages/01_Login.py")



st.markdown("""
<style>

/* =========================
   GLOBAL TEXT COLOR
========================= */

/* Main app */
.stApp{
    color: white;
}

/* Headings */
h1, h2, h3, h4, h5, h6{
    color: white !important;
}

/* Normal text */
p, span, div, label{
    color: white !important;
}

/* Markdown */
[data-testid="stMarkdownContainer"]{
    color: white !important;
}

/* Sidebar */
[data-testid="stSidebar"] *{
    color: white !important;
}

/* Tabs */
button[data-baseweb="tab"]{
    color: white !important;
}

/* Radio */
.stRadio label{
    color: white !important;
}

/* Checkbox */
.stCheckbox label{
    color: white !important;
}

/* Selectbox Label */
.stSelectbox label{
    color: black !important;
}

/* Text Input Label */
.stTextInput label{
    color: white !important;
}

/* Text Area Label */
.stTextArea label{
    color: white !important;
}

/* Number Input Label */
.stNumberInput label{
    color: white !important;
}

/* File Uploader */
.stFileUploader label{
    color: white !important;
}

/* Metric */
[data-testid="stMetricLabel"],
[data-testid="stMetricValue"]{
    color: white !important;
}

/* Success / Warning / Error */
.stAlert{
    color: white !important;
}

/* =========================
   INPUT BOXES
========================= */

.stTextInput input,
.stTextArea textarea,
.stNumberInput input{
    color: black !important;
    background-color: white !important;
}



/* =========================
   BUTTON
========================= */

.stButton > button{
    background: linear-gradient(135deg,#A855F7,#C084FC);
    color: black ;
    font-weight: bold;
    border: none;
    border-radius: 10px;
    padding: 10px 24px;
    transition: 0.3s ease;
}

.stButton > button:hover{
    background: linear-gradient(135deg,#9333EA,#A855F7);
    color: black;
    transform: scale(1.03);
    box-shadow: 0 0 20px rgba(168,85,247,0.5);
}

/* =========================
   EXPANDER
========================= */

.streamlit-expanderHeader{
    color: white !important;
}

</style>
""", unsafe_allow_html=True)





st.markdown("""
<style>

/* Login and Register Button */
div.stButton > button {
   background: linear-gradient(
        135deg,
        #E9D5FF 0%,
        #C084FC 30%,
        #A855F7 65%,
        #7E22CE 100%
    );
    color: white !important;
    font-size: 17px;
    font-weight: 700;
    border: none;
    border-radius: 12px;
    padding: 12px 28px;
    cursor: pointer;
    transition: all 0.35s ease;
    box-shadow: 0 5px 18px rgba(168, 85, 247, 0.45);
}

/* Force text inside button to black */
div.stButton > button * {
    color: black !important;
    fill: black !important;
}

/* Hover */
div.stButton > button:hover {
    background: linear-gradient(135deg, #A855F7, #9333EA);
    color: black !important;
}

div.stButton > button:hover * {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)




# ---------------------------------
# Check Login
# ---------------------------------

# if not st.session_state.get("logged_in", False):
#     st.warning("Please login first.")
#     st.switch_page("pages/01_Login.py")

# ---------------------------------
# Backend URL
# ---------------------------------

BASE_URL = "http://127.0.0.1:5000"

PREDICT_URL = f"{BASE_URL}/predict/predict_news1"

# ---------------------------------
# Page
# ---------------------------------



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
            "Predict",
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


# Main Content
if selected == "Home":
    st.title("🛡️ TruthLens AI")
    st.write("Welcome to AI Fake News Detector")
    # if "logged_in" not in st.session_state:
    #     st.session_state.logged_in = False

    # Redirect to login if not logged in
    
    # Home Page (shown only after login)
   # st.title("📰 AI Fake News & Misinformation Detector")

    st.success(f"Welcome, {st.session_state.get('username', '')} 👋")

    st.markdown("""
    ### Features
    - 🔐 User Login & Registration
    - 🌍 Multi-language News Support
    - 🤖 AI Fake News Detection
    - 💬 AI Explanation
    - 📜 Prediction History

    Use the sidebar to navigate through the application.
    """)


    st.subheader("⚙️ How It Works")

    st.write("""
    1. Enter a news article.
    2. The text is preprocessed.
    3. The news is translated if required.
    4. TF-IDF converts the text into numerical features.
    5. The Machine Learning model predicts Fake or Real.
    6. The confidence score is calculated.
    7. The prediction is stored in the database.
    8. AI can provide an explanation of the result.
    """)

    st.markdown("---")

    st.caption(
        "AI Fake News & Misinformation Detector | "
        "Machine Learning + Flask + Streamlit + MySQL"
    )


elif selected == "Predict":
    
    st.title("🔍 Fake News Detection")

    st.write(
        "Enter a news article below to check whether "
        "it is likely to be Fake or Real."
    )

    st.markdown("---")

    # ---------------------------------
    # Input
    # ---------------------------------

    title = st.text_input(
        "News Title",
        placeholder="Enter the news title"
    )

    news_text = st.text_area(
        "News Content",
        placeholder="Paste the complete news article here...",
        height=300
    )



    language = option_menu(
        menu_title="Language",
        options=["English", "Hindi", "Marathi"],
        icons=["translate", "translate", "translate"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {
                "background-color": "#FFFFFF",
                "border-radius": "8px",
            },
            "nav-link": {
                "color": "black",
                "font-size": "12px",
                "text-align": "center",
                "--hover-color": "#E9D5FF",
            },
            "nav-link-selected": {
                "background-color": "#8B5CF6",
                "color": "white",
            },
        }
    )

    st.write("Selected:", language)




    # language = st.selectbox(
    #     "Language",
    #     [
    #         "English",
    #         "Hindi",
    #         "Marathi"
    #     ]
    # )

    # ---------------------------------
    # Prediction
    # ---------------------------------

    if st.button("🔍 Predict News"):

        if not news_text.strip():

            st.warning("Please enter news content.")

        else:

            data = {
                "user_id": st.session_state["user_id"],
                "title": title,
                "news_text": news_text,
                "language": language
            }

            try:

                with st.spinner("Analyzing news..."):

                    response = requests.post(
                        PREDICT_URL,
                        json=data,
                        timeout=60
                    )

                result = response.json()

                if response.status_code == 200 and result.get("status"):

                    prediction = result.get("prediction")
                    confidence = result.get("confidence")

                    st.markdown("---")

                    st.subheader("📊 Prediction Result")

                    if str(prediction).lower() == "fake":

                        st.error(
                            f"🚨 Prediction: {prediction}"
                        )

                    else:

                        st.success(
                            f"✅ Prediction: {prediction}"
                        )

                        c1,c2 = st.columns(2)

                        with c1:
                            st.metric(
                                        "Confidence",
                                        f"{float(confidence):.2f}%"
                                                            )

                        with c2:    
                            confidence = float(confidence)

                            # Change color according to prediction
                            if prediction == "Fake":
                                color = "#EF4444"   # Red
                            else:
                                color = "#22C55E"   # Green

                            fig = go.Figure(go.Pie(
                                values=[confidence, 100 - confidence],
                                hole=0.75,
                                marker_colors=[color, "#2D3748"],
                                textinfo="none"
                            ))

                            fig.update_layout(
                                width=180,          # Smaller width
                                height=180,         # Smaller height
                                annotations=[
                                    dict(
                                        text=f"{confidence:.1f}%",
                                        showarrow=False,
                                        font=dict(size=18, color="white")  # Smaller text
                                    )
                                ],
                                showlegend=False,
                                paper_bgcolor="rgba(0,0,0,0)",
                                plot_bgcolor="rgba(0,0,0,0)",
                                margin=dict(t=5, b=5, l=5, r=5)
                            )

                            st.plotly_chart(fig, use_container_width=False)
                    
                    # LLM explanation if backend returns it
                    explanation = result.get("explanation")

                    if explanation:

                        st.subheader("🤖 AI Explanation")
                        st.write(explanation)

                else:

                    st.error(
                        result.get(
                            "message",
                            "Prediction failed."
                        )
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to Flask backend. "
                    "Please make sure the Flask server is running."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The server took too long to respond."
                )

            except Exception as e:

                st.error(f"Error: {e}")


elif selected == "History":
    
    # if st.session_state.get("logged_in", False):
    #     st.switch_page("login.py")

    # -----------------------------
    # Register UI
    # # -----------------------------
    # st.title("📝 Create Account")

    # username = st.text_input("Username")

    # email = st.text_input("Email")

    # password = st.text_input(
    #     "Password",
    #     type="password"
    # )

    # confirm_password = st.text_input(
    #     "Confirm Password",
    #     type="password"
    # )

    # if st.button("Register"):

    #     if username == "" or email == "" or password == "" or confirm_password == "":
    #         st.warning("Please fill all fields.")

    #     elif password != confirm_password:
    #         st.error("Passwords do not match.")

    #     else:

    #         data = {
    #             "username": username,
    #             "email": email,
    #             "password": password
    #         }

    #         try:

    #             response = requests.post(
    #                 REGISTER_URL,
    #                 json=data
    #             )

    #             result = response.json()

    #             if response.status_code == 201 and result["status"]:

    #                 st.success(result["message"])

    #                 st.info("Registration successful. Please login.")

    #                 st.switch_page("pages/01_Login.py")

    #             else:

    #                 st.error(result["message"])

    #         except Exception as e:

    #             st.error(f"Server Error: {e}")

    # st.markdown("---")

    # st.write("Already have an account?")

    # if st.button("Go to Login"):
    #     st.switch_page("pages/01_Login.py")








    # ---------------------------------
    # Check Login
    # ---------------------------------

    if not st.session_state.get("logged_in", False):
        st.warning("Please login first.")
        st.switch_page("pages/01_Login.py")

    # ---------------------------------
    # Backend URL
    # ---------------------------------

    BASE_URL = "http://127.0.0.1:5000"

    user_id = st.session_state["user_id"]

    HISTORY_URL = f"{BASE_URL}/history/{user_id}"

    # ---------------------------------
    # Page
    # ---------------------------------

    st.title("📜 Prediction History")

    st.write(
        f"Here you can view the previous predictions "
        f"for user ID: {user_id}"
    )

    st.markdown("---")

    # ---------------------------------
    # Get History
    # ---------------------------------

    try:

        response = requests.get(
            HISTORY_URL,
            timeout=30
        )

        result = response.json()

        if response.status_code == 200 and result.get("status"):

            history = result.get("history", [])

            if history:

                st.success(
                    f"{len(history)} prediction(s) found."
                )

                # Convert to DataFrame
                df = pd.DataFrame(history)

                # Select useful columns
                columns = [
                    "id",
                    "title",
                    "language",
                    "prediction",
                    "confidence",
                    "created_at"
                ]

                available_columns = [
                    col for col in columns
                    if col in df.columns
                ]

                if available_columns:

                    st.dataframe(
                        df[available_columns],
                        use_container_width=True,
                        hide_index=True
                    )

                else:

                    st.dataframe(
                        df,
                        use_container_width=True,
                        hide_index=True
                    )

                # ---------------------------------
                # Detailed History
                # ---------------------------------

                st.markdown("---")

                st.subheader("📰 Prediction Details")

                for item in history:

                    prediction = item.get(
                        "prediction",
                        "Unknown"
                    )

                    title = item.get(
                        "title",
                        "No title"
                    )

                    confidence = item.get(
                        "confidence",
                        0
                    )

                    with st.expander(
                        f"{title} — {prediction}"
                    ):

                        st.write(
                            "**Prediction:**",
                            prediction
                        )

                        st.write(
                            "**Confidence:**",
                            f"{float(confidence):.2f}%"
                        )

                        st.write(
                            "**Language:**",
                            item.get("language", "Unknown")
                        )

                        st.write(
                            "**Date:**",
                            item.get("created_at", "Unknown")
                        )

                        st.write(
                            "**News:**"
                        )

                        st.write(
                            item.get(
                                "news_text",
                                "No news content available."
                            )
                        )

            else:

                st.info(
                    "No prediction history found."
                )

        else:

            st.error(
                result.get(
                    "message",
                    "Could not retrieve history."
                )
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "Cannot connect to Flask backend. "
            "Please make sure the Flask server is running."
        )

    except requests.exceptions.Timeout:

        st.error(
            "The server took too long to respond."
        )

    except Exception as e:

        st.error(f"Error: {e}")


elif selected == "About":


    st.title("About TruthLens AI")
    st.markdown("__________________")

    st.markdown("""
    ## 🛡️ AI Fake News & Misinformation Detector

    TruthLens AI is an intelligent web application designed to identify whether
    a news article is **Fake** or **Real** using Machine Learning techniques.

    The system helps users verify the authenticity of news articles and
    reduce the spread of misinformation across digital platforms.
    """)

    st.markdown("---")

    st.subheader("🎯 Project Objectives")

    st.markdown("""
    - Detect fake news accurately using Machine Learning.
    - Reduce the spread of misinformation.
    - Support multiple languages.
    - Provide confidence score for every prediction.
    - Store prediction history for users.
    - Offer a simple and user-friendly interface.
    """)

    st.markdown("---")

    st.subheader("⚙️ Technologies Used")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **Frontend**
        - Streamlit
        - HTML
        - CSS
        """)

        st.markdown("""
        **Backend**
        - Flask
        - REST API
        """)

    with col2:
        st.markdown("""
        **Machine Learning**
        - Python
        - Scikit-learn
        - TF-IDF Vectorizer
        - Passive Aggressive Classifier
        """)

        st.markdown("""
        **Database**
        - MySQL
        """)

    st.markdown("---")

    st.subheader("🚀 Key Features")

    st.markdown("""
    ✅ Secure Login & Registration

    ✅ AI-Based Fake News Detection

    ✅ Multi-Language News Support

    ✅ Confidence Score Visualization

    ✅ Prediction History

    ✅ Fast and Accurate Results

    ✅ Modern & Interactive User Interface
    """)

    st.markdown("---")

    st.subheader("📊 Workflow")

    st.markdown("""
    1. User enters a news article.
    2. News text is preprocessed.
    3. Text is translated (if required).
    4. TF-IDF converts text into numerical features.
    5. Machine Learning model predicts Fake or Real.
    6. Confidence score is generated.
    7. Prediction is stored in the database.
    8. User can review prediction history.
    """)

    st.markdown("---")

    st.subheader("👩‍💻 Developer")

    st.info("""
    **Project:** TruthLens AI - Fake News & Misinformation Detector

    Developed using Machine Learning, Flask, Streamlit and MySQL
    as an academic project to help users verify the authenticity of online news.
    """)

    st.markdown("---")

    st.caption("© 2026 TruthLens AI | AI Fake News & Misinformation Detector")
    
elif selected=="Logout":

    # Clear login/session information
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.username = ""
    st.session_state.email = ""

    # Go back to Login page
    st.switch_page("pages/01_Login.py")

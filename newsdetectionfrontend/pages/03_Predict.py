'''import streamlit as st
import requests

st.set_page_config(
    page_title="Predict News",
    page_icon="🔍",
    layout="wide"
)

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

PREDICT_URL = f"{BASE_URL}/predict/predict_news1"

# ---------------------------------
# Page
# ---------------------------------


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

language = st.selectbox(
    "Language",
    [
        "English",
        "Hindi",
        "Marathi"
    ]
)

# ---------------------------------
# Prediction
# ---------------------------------

if st.button("🔍 Predict News", use_container_width=True):

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

                st.metric(
                    "Confidence",
                    f"{float(confidence):.2f}%"
                )

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
            
  ''' 
   
   
   
   
import streamlit as st
import requests
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from sidebar import show_sidebar



st.set_page_config(
    page_title="Predict News",
    page_icon="🔍",
    layout="wide"
)


show_sidebar(2)

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

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.switch_page("pages/01_Login.py")

# ---------------------------------
# Backend URL
# ---------------------------------

BASE_URL = "http://127.0.0.1:5000"

PREDICT_URL = f"{BASE_URL}/predict/predict_news1"

# ---------------------------------
# Page
# ---------------------------------

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

'''import streamlit as st
import requests

st.set_page_config(
    page_title="Login",
    page_icon="🔐"
)

# -----------------------------
# Backend URL
# -----------------------------

BASE_URL = "http://127.0.0.1:5000"

LOGIN_URL = f"{BASE_URL}/auth/login"

# -----------------------------
# Already Logged In
# -----------------------------

if st.session_state.get("logged_in", False):
    st.switch_page("app.py")

# -----------------------------
# Login UI
# -----------------------------

st.title("🔐 Login")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if email == "" or password == "":

        st.warning("Please enter Email and Password.")

    else:

        data = {
            "email": email,
            "password": password
        }

        try:

            response = requests.post(
                LOGIN_URL,
                json=data
            )

            result = response.json()

            if response.status_code == 200 and result["status"]:

                st.session_state.logged_in = True

                st.session_state.user_id = result["user"]["id"]

                st.session_state.username = result["user"]["username"]

                st.session_state.email = result["user"]["email"]

                st.success(result["message"])

                st.switch_page("app.py")

            else:

                st.error(result["message"])

        except Exception as e:

            st.error(f"Server Error : {e}")

st.markdown("---")

st.write("Don't have an account?")

if st.button("Register"):

    st.switch_page("pages/02_Register.py")
    
    
'''



import streamlit as st
import requests

st.set_page_config(
    page_title="Login",
    page_icon="🔐"
)

# -----------------------------
# Backend URL
# -----------------------------

BASE_URL = "http://127.0.0.1:5000"

LOGIN_URL = f"{BASE_URL}/auth/login"

# -----------------------------
# Already Logged In
# -----------------------------

if st.session_state.get("logged_in", False):
    st.switch_page("app.py")

# -----------------------------
# Login UI
# -----------------------------


st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #000000,
        #120024,
        #3A0CA3,
        #B9A0DE
    );
}
</style>
""", unsafe_allow_html=True)





import streamlit as st

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
    color: white !important;
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

.stSelectbox div[data-baseweb="select"] > div{
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





st.title("🔐 Login")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if email == "" or password == "":

        st.warning("Please enter Email and Password.")

    else:

        data = {
            "email": email,
            "password": password
        }

        try:

            response = requests.post(
                LOGIN_URL,
                json=data
            )

            result = response.json()

            if response.status_code == 200 and result["status"]:

                st.session_state.logged_in = True

                st.session_state.user_id = result["user"]["id"]

                st.session_state.username = result["user"]["username"]

                st.session_state.email = result["user"]["email"]

                st.success(result["message"])

                st.switch_page("app.py")

            else:

                st.error(result["message"])

        except Exception as e:

            st.error(f"Server Error : {e}")

st.markdown("---")

st.write("Don't have an account?")

if st.button("Register"):

    st.switch_page("pages/02_Register.py")

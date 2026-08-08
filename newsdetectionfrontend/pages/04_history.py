import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Prediction History",
    page_icon="📜",
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
        #B9A0DE
    );
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
# app.py 

import streamlit as st
from components.navbar import navbar
from features import Learn, Assignment, Chat, Mock_Interview, Practice

# Main function to run the app
def main():
    st.set_page_config(page_title="Streamlit App", layout="wide")

    # Navbar with logo, search bar, and profile picture (top of the page)
    navbar()

    # Sidebar feature selection (Streamlit native)
    st.sidebar.title("Features")
    feature = st.sidebar.selectbox(
        "Choose a feature",
        ["Learn", "Practice", "Mock Interview", "Assignment", "Chat"],
        index=0
    )

    # Feature mapping
    feature_mapping = {
        "Learn": Learn.show,
        "Practice": Practice.show,
        "Mock Interview": Mock_Interview.show,
        "Assignment": Assignment.show,
        "Chat": Chat.show   
    }
    
    # Call the function to show the selected feature
    if feature in feature_mapping:
        feature_mapping[feature]()

if __name__ == "__main__":
    main()

# features/Assignment.py

import streamlit as st

def show():
    st.title("Assignment Page")

    # Adding the Recommendations Section
    st.subheader("Recommendations for you:")
    st.markdown("""
        <style>
        .recommendations-section {
            display: flex;
            gap: 20px;
            margin-bottom: 40px;
        }
        .recommendation-card {
            flex-grow: 1;
            background-color: #e0e0e0;
            height: 150px;
            border-radius: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 20px;
            font-weight: bold;
            color: #666;
        }
        </style>
        <div class="recommendations-section">
            <div class="recommendation-card">Recommendation 1</div>
            <div class="recommendation-card">Recommendation 2</div>
            <div class="recommendation-card">Recommendation 3</div>
        </div>
    """, unsafe_allow_html=True)

    # Adding the MCQ Section
    st.subheader("MCQs:")
    st.markdown("""
        <style>
        .mcq-section {
            display: flex;
            gap: 20px;
            margin-bottom: 40px;
        }
        .mcq-card {
            flex-grow: 1;
            background-color: #e0e0e0;
            height: 100px;
            border-radius: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 18px;
            font-weight: bold;
            color: #666;
        }
        </style>
        <div class="mcq-section">
            <div class="mcq-card">MCQ Test 1</div>
            <div class="mcq-card">MCQ Test 2</div>
            <div class="mcq-card">MCQ Test 3</div>
        </div>
    """, unsafe_allow_html=True)

    # Adding the DSA Rounds Section
    st.subheader("DSA Rounds:")
    st.markdown("""
        <style>
        .dsa-section {
            display: flex;
            gap: 20px;
            margin-bottom: 40px;
        }
        .dsa-card {
            flex-grow: 1;
            background-color: #e0e0e0;
            height: 100px;
            border-radius: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 18px;
            font-weight: bold;
            color: #666;
        }
        </style>
        <div class="dsa-section">
            <div class="dsa-card">DSA Round 1</div>
            <div class="dsa-card">DSA Round 2</div>
            <div class="dsa-card">DSA Round 3</div>
        </div>
    """, unsafe_allow_html=True)

# Call the function to display the assignment page
show()
# features/Practice.py

import streamlit as st
from features.ProblemPage import show_problem_page

def show():
    st.title("Practice")

    # Section 1: "Recommended for you"
    st.subheader("Recommended for you")

    st.markdown("""
    <style>
    .scroll-container {
        display: flex;
        gap: 10px;
        padding: 10px 0;
        overflow: hidden;
    }
    .scroll-container img {
        width: 250px;
        height: 150px;
        object-fit: cover;
        border-radius: 8px;
    }

    @keyframes scroll-left {
        0% { transform: translateX(0); }
        100% { transform: translateX(calc(-250px * 5)); }
    }

    .scroll-left {
        display: flex;
        gap: 10px;
        animation: scroll-left 20s linear infinite;
    }

    /* Styling for DSA problems table */
    .dsa-container {
        padding: 20px 0;
        margin-top: 20px;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
    }

    th, td {
        border: 1px solid #ddd;
        padding: 10px;
        text-align: center;
    }

    th {
        font-weight: bold;
        font-size: 16px;
    }

    td {
        font-size: 14px;
    }

    .checkbox-col {
        width: 5%;
    }

    .prob-no-col {
        width: 10%;
    }

    .name-col {
        width: 35%;
    }

    .tags-col {
        width: 30%;
    }

    .difficulty-col {
        width: 20%;
    }

    .difficulty-easy {
        color: green;
    }

    .difficulty-medium {
        color: orange;
    }

    .difficulty-hard {
        color: red;
    }

    /* Style for checkbox */
    .checkbox-input {
        width: 18px;
        height: 18px;
        cursor: pointer;
    }

    .button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Image scrolling section
    st.markdown("""
    <div class="scroll-container">
        <div class="scroll-left">
            <img src="https://via.placeholder.com/250x150?text=Recommended+1" alt="Recommended 1">
            <img src="https://via.placeholder.com/250x150?text=Recommended+2" alt="Recommended 2">
            <img src="https://via.placeholder.com/250x150?text=Recommended+3" alt="Recommended 3">
            <img src="https://via.placeholder.com/250x150?text=Recommended+4" alt="Recommended 4">
            <img src="https://via.placeholder.com/250x150?text=Recommended+5" alt="Recommended 5">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Section 2: "DSA Problems"
    st.subheader("DSA Problems")

    # DSA problems data
    problems = [
        {"id": 1, "title": "Two Sum", "difficulty": "Easy", "tags": ["Array", "Hash Table"]},
        {"id": 2, "title": "Longest Substring Without Repeating Characters", "difficulty": "Medium", "tags": ["String", "Sliding Window"]},
        {"id": 3, "title": "Median of Two Sorted Arrays", "difficulty": "Hard", "tags": ["Array", "Binary Search"]},
        {"id": 4, "title": "Merge Two Sorted Lists", "difficulty": "Easy", "tags": ["Linked List"]},
        {"id": 5, "title": "Container With Most Water", "difficulty": "Medium", "tags": ["Array", "Two Pointers"]},
        {"id": 6, "title": "Word Ladder", "difficulty": "Hard", "tags": ["Graph", "BFS"]},
    ]

    # Initialize session state for checkboxes and problem ID
    if 'completed_problems' not in st.session_state:
        st.session_state['completed_problems'] = [False] * len(problems)
    
    if 'current_problem_id' not in st.session_state:
        st.session_state['current_problem_id'] = None

    # Render problem buttons
    for problem in problems:
        problem_id = problem['id']
        button_label = f"{problem['title']} (ID: {problem['id']}) - Tags: {', '.join(problem['tags'])}"
        
        if st.button(button_label, key=f"button_{problem_id}"):
            st.session_state['current_problem_id'] = problem_id
            st.rerun()

    # If a problem is selected, show the problem page
    if st.session_state['current_problem_id']:
        show_problem_page(st.session_state['current_problem_id'])

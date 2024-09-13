import streamlit as st
import json
import time

# Load the JSON data
with open("test1_data.json", "r") as f:
    questions_data = json.load(f)

# Sample questions from topic 1, easy level
questions = questions_data['topic_1']['questions']

# Variables to store current question, answers, and timer
current_question_idx = st.session_state.get('current_question_idx', 0)
if 'selected_answers' not in st.session_state:
    st.session_state['selected_answers'] = [None] * len(questions)
selected_answers = st.session_state['selected_answers']
timer_end_time = st.session_state.get('timer_end_time', time.time() + 30 * 60)  # 30 minutes timer

# Timer logic
time_left = max(0, int(timer_end_time - time.time()))
if time_left == 0:
    st.warning("Time's up! Submitting automatically.")
    st.session_state['submit'] = True

# Show timer at the top
st.write(f"⏳ **Time left: {time_left // 60}:{time_left % 60:02d}**")

# Function to navigate through questions
def navigate(direction):
    if direction == "next" and current_question_idx < len(questions) - 1:
        st.session_state['current_question_idx'] = current_question_idx + 1
    elif direction == "prev" and current_question_idx > 0:
        st.session_state['current_question_idx'] = current_question_idx - 1
    else:
        st.session_state['current_question_idx'] = direction  # For question number navigation

# Function to clear answer for the current question
def clear_answer():
    selected_answers[current_question_idx] = None

# Layout for question and answer
st.write(f"### Question {current_question_idx + 1}: {questions[current_question_idx]['question']}")

# Display answer options
selected_answer = st.radio(
    f"Select answer for question {current_question_idx + 1}", 
    questions[current_question_idx]['options'], 
    index=questions[current_question_idx]['options'].index(selected_answers[current_question_idx]) if selected_answers[current_question_idx] else 0,
    key=f"question_{current_question_idx}"
)

# Store selected answer
if selected_answer:
    selected_answers[current_question_idx] = selected_answer

# Layout for right-side question number grid
col1, col2 = st.columns([4, 1])  # Left column for question, right column for number grid
with col1:
    # Navigation buttons
    st.button("Previous", on_click=navigate, args=("prev",))
    st.button("Next", on_click=navigate, args=("next",))
    st.button("Clear", on_click=clear_answer)

with col2:
    # Display question numbers as clickable buttons
    for idx in range(len(questions)):
        if idx % 5 == 0:
            st.write("")  # Add some space every 5 buttons
        button_label = f"Q{idx + 1}"
        if st.button(button_label):
            navigate(idx)

# Submit button to check all answers
if st.button("Submit"):
    correct_count = 0
    for idx, question in enumerate(questions):
        if selected_answers[idx] == question['answer']:
            correct_count += 1
        else:
            st.write(f"Question {idx + 1}: {question['question']}")
            st.write(f"Your Answer: {selected_answers[idx]}")
            st.write(f"Correct Answer: {question['answer']}")
            st.write(f"Explanation: {question['incorrect_explanation'].get(selected_answers[idx], 'N/A')}")
    st.write(f"Score: {correct_count} / {len(questions)}")

# Timer countdown and submission handling
if time_left == 0:
    st.rerun()  # Restart to auto-submit when time is up

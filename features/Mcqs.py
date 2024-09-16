import streamlit as st
import json
import time

# Load the JSON data
with open("test1_data.json", "r") as f:
    questions_data = json.load(f)

# Sample questions from easy level
questions = questions_data['questions']

# Variables to store current question, answers, and timer
current_question_idx = st.session_state.get('current_question_idx', 0)
if 'selected_answers' not in st.session_state:
    st.session_state['selected_answers'] = [None] * len(questions)
selected_answers = st.session_state['selected_answers']

# Timer setup (30 minutes countdown)
if 'timer_end_time' not in st.session_state:
    st.session_state['timer_end_time'] = time.time() + 30 * 60  # 30 minutes

# Timer logic
timer_end_time = st.session_state['timer_end_time']
time_left = max(0, int(timer_end_time - time.time()))
if time_left == 0:
    st.warning("Time's up! Submitting automatically.")
    st.session_state['submit'] = True

# Display countdown timer at the top
minutes, seconds = divmod(time_left, 60)
st.markdown(f"⏳ **Time left: {minutes}:{seconds:02d}**")

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

# Layout for navigation buttons (Single row for 'Prev', 'Next', 'Clear', and 'Submit')
col1, col2, col3, col4 = st.columns(4)

# Conditionally show or disable the 'Previous' button
with col1:
    if current_question_idx > 0:
        st.button("Previous", on_click=navigate, args=("prev",))

# Conditionally show or disable the 'Next' button
with col2:
    if current_question_idx < len(questions) - 1:
        st.button("Next", on_click=navigate, args=("next",))

# Clear button to clear the selected answer
with col3:
    st.button("Clear", on_click=clear_answer)

# Submit button to submit the answers
with col4:
    st.button("Submit")

# Layout for right-side question number grid (5x6 grid)
st.write("### Question Navigator")
cols = st.columns(5)
for idx, question in enumerate(questions):
    with cols[idx % 5]:
        button_label = f"Q{idx + 1}"
        if st.button(button_label, key=f"q_btn_{idx}"):
            navigate(idx)

# Submit button handling
if st.session_state.get('submit', False):
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
    st.session_state['submit'] = True
    st.rerun()  # Restart to auto-submit when time is up
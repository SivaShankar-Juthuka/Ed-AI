# features/Mock_Interview.py

import streamlit as st
import cv2
import threading
import time

def start_video_feed():
    """Function to start capturing video feed from the webcam."""
    cap = cv2.VideoCapture(0)  # 0 is the default camera
    while st.session_state['video_feed_visible']:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture webcam feed.")
            break
        
        # Convert the image from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        st.session_state['current_frame'] = frame_rgb
        
        # Sleep for a short time to allow the main thread to refresh
        time.sleep(0.03)

    cap.release()

def stop_video_feed():
    """Function to stop the video feed."""
    st.session_state['video_feed_visible'] = False
    st.rerun()

def show():
    st.title("Mock Interview")

    # Initialize session state for storing messages and video feed visibility
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    if 'video_feed_visible' not in st.session_state:
        st.session_state['video_feed_visible'] = False  # Initialize video_feed_visible
    if 'current_frame' not in st.session_state:
        st.session_state['current_frame'] = None  # Initialize current_frame

    # Define columns for the avatar and chat sections
    col1, col2 = st.columns([3, 1])  # 3/4 for avatar, 1/4 for chat

    # Avatar section
    with col1:
        st.subheader("Interview Avatar")

        # Add custom CSS for overlaying video feed (small rectangle at bottom-right)
        st.markdown("""
            <style>
            .avatar-container {
                position: relative;
                width: 100%;
                height: auto;
            }
            .avatar {
                width: 100%;
                border-radius: 8px;
            }
            .video-feed {
                position: absolute;
                bottom: 10px;
                right: 10px;
                width: 150px;
                height: 100px;
                border: 2px solid #ccc;
                border-radius: 8px;
                background-color: black;
            }
            </style>
        """, unsafe_allow_html=True)

        # Display the avatar image (replace with the actual avatar or use a placeholder)
        st.image("https://via.placeholder.com/600x400.png?text=Avatar+Placeholder", caption="Interview Avatar", use_column_width=True)

        # Display the webcam feed area (show webcam if enabled)
        video_container = st.empty()  # This will be used to display the video dynamically
        if st.session_state['video_feed_visible']:
            while st.session_state['video_feed_visible']:
                if st.session_state['current_frame'] is not None:
                    video_container.image(st.session_state['current_frame'], caption="Your Camera Feed", width=150, use_column_width=True)
                time.sleep(0.03)  # Small delay to allow video updates
        else:
            st.markdown("""
                <div class="video-feed">
                     Your webcam feed will appear here
                </div>
            """, unsafe_allow_html=True)

        # Button to start the video feed
        if st.button("Start Video Feed") and not st.session_state['video_feed_visible']:
            st.session_state['video_feed_visible'] = True  # Set the flag to True
            threading.Thread(target=start_video_feed).start()

        # Button to stop the video feed
        if st.session_state['video_feed_visible'] and st.button("Stop Video Feed"):
            stop_video_feed()

    # Chat section
    with col2:
        st.subheader("Chat")
        
        # Apply custom CSS to style the chat section
        st.markdown("""
            <style>
            .chat-message {
                color: white;
                padding: 5px;
                border-radius: 5px;
                margin-bottom: 5px;
            }
            .chat-input-container input {
                border: none;
                flex-grow: 1;
                outline: none;
            }
            .chat-input-container button {
                background-color: white;
                border: none;
                outline: none;
                cursor: pointer;
                margin-left: 10px;
            }
            </style>
        """, unsafe_allow_html=True)

        # Display previous messages
        for msg in st.session_state['messages']:
            st.markdown(f'<div class="chat-message">You: {msg}</div>', unsafe_allow_html=True)

        # Create the text input and a submit button
        chat_input = st.text_input("Type your message here:")
        submit_button = st.button("Send")

        # Append new message when submit button is pressed
        if submit_button and chat_input:
            st.session_state['messages'].append(chat_input)
            st.rerun()

    # Transcription section
    st.subheader("Video Transcription")
    # Placeholder for video transcription
    st.text_area("Video Transcription:", height=300)

# Call the function to display the interface
show()

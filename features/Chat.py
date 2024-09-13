# features/Chat.py

import streamlit as st

def show():
    st.title("Chat")

    # Initialize session state to hold messages
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # Define layout: sidebar for history and main chat area
    col1, col2 = st.columns([1, 3])

    # Sidebar for chat history
    with col1:
        st.subheader("History")
        if st.session_state['messages']:
            for idx, msg in enumerate(st.session_state['messages']):
                st.write(f"Message {idx + 1}: {msg}")  # Show the full message in history
        else:
            st.write("No chat history yet.")

    # Main chat area
    with col2:
        st.subheader("Recommendation for you:")

        # Display avatar in the center
        st.markdown("""
            <style>
            .avatar-container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 400px;
                background-color: #f0f0f0;
                border-radius: 10px;
            }
            .avatar {
                width: 80px;
                height: 80px;
                border-radius: 50%;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            }
            </style>
            <div class="avatar-container">
                <img src='https://via.placeholder.com/80.png' alt='Avatar' class='avatar'/>
            </div>
        """, unsafe_allow_html=True)

        # Message input at the bottom
        st.markdown("""
            <style>
            .message-input-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #f5f5f5;
                border-radius: 25px;
                padding: 10px;
            }
            .message-input {
                flex-grow: 1;
                border: none;
                padding: 10px;
                font-size: 16px;
                outline: none;
            }
            .message-send-btn {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 25px;
                cursor: pointer;
                font-size: 16px;
            }
        """, unsafe_allow_html=True)

        # Input handling: Send message via the input field or send button
        new_message = st.text_input("Type your message here", key="chat_input")

        # Add button to send the message
        if st.button("Send") and new_message:
            st.session_state['messages'].append(new_message)

# Call the function to display the chat interface
show()

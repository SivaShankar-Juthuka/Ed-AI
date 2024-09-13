import streamlit as st

def navbar():
    # Navbar HTML with logo, search bar, and profile picture
    st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #333;
        padding: 10px;
    }
    .navbar-logo img {
        height: 50px;
    }
    .navbar-elements {
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .navbar-search input {
        padding: 6px;
        border-radius: 4px;
        border: none;
        width: 200px;
    }
    .navbar-profile img {
        height: 40px;
        width: 40px;
        border-radius: 50%;
        object-fit: cover;
    }
    </style>
    
    <div class="navbar">
        <div class="navbar-logo">
            <img src="person_logo.png" alt="Logo">
        </div>
        <div class="navbar-elements">
            <div class="navbar-search">
                <input type="text" placeholder="Search...">
            </div>
            <div class="navbar-profile">
                <img src="person_image.png" alt="Profile Picture">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

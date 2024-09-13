import streamlit as st

def show():
    st.title("Learn")
    
    # Add CSS for scrolling containers with circular scrolling
    st.markdown("""
    <style>
    .scroll-container {
        display: flex;
        gap: 10px;
        padding: 10px 0;
        overflow: hidden;
        position: relative;
    }
    .scroll-container img {
        width: 250px;
        height: 150px;
        object-fit: cover;
        border-radius: 8px;
    }

    /* Circular scrolling animation (Left to Right) */
    @keyframes scroll-left-circular {
        0% { transform: translateX(0); }
        100% { transform: translateX(calc(-250px * 10)); } /* 5 images * 2 (duplicated) */
    }

    .scroll-left-circular {
        display: flex;
        gap: 10px;
        animation: scroll-left-circular 120s linear infinite;
    }

    /* Circular scrolling animation (Right to Left) */
    @keyframes scroll-right-circular {
        0% { transform: translateX(0); }
        100% { transform: translateX(calc(250px * 10)); } /* 5 images * 2 (duplicated) */
    }

    .scroll-right-circular {
        display: flex;
        gap: 10px;
        animation: scroll-right-circular 120s linear infinite;
    }

    /* Circular scrolling animation for Section 3 (Left to Right, faster) */
    @keyframes scroll-left-circular-fast {
        0% { transform: translateX(0); }
        100% { transform: translateX(calc(-250px * 10)); }
    }

    .scroll-left-circular-fast {
        display: flex;
        gap: 10px;
        animation: scroll-left-circular-fast 120s linear infinite;
    }
    </style>
    """, unsafe_allow_html=True)

    # Section 1: No heading, auto-scrolling images (Left to Right, Circular)
    st.markdown("""
    <div class="scroll-container">
        <div class="scroll-left-circular">
            <img src="https://via.placeholder.com/250x150?text=Image+1" alt="Image 1">
            <img src="https://via.placeholder.com/250x150?text=Image+2" alt="Image 2">
            <img src="https://via.placeholder.com/250x150?text=Image+3" alt="Image 3">
            <img src="https://via.placeholder.com/250x150?text=Image+4" alt="Image 4">
            <img src="https://via.placeholder.com/250x150?text=Image+5" alt="Image 5">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Section 2: "Recommendation for you" (Right to Left, Circular)
    st.subheader("Recommendation for you")
    
    st.markdown("""
    <div class="scroll-container">
        <div class="scroll-right-circular">
            <img src="https://via.placeholder.com/250x150?text=Recommendation+1" alt="Recommendation 1">
            <img src="https://via.placeholder.com/250x150?text=Recommendation+2" alt="Recommendation 2">
            <img src="https://via.placeholder.com/250x150?text=Recommendation+3" alt="Recommendation 3">
            <img src="https://via.placeholder.com/250x150?text=Recommendation+4" alt="Recommendation 4">
            <img src="https://via.placeholder.com/250x150?text=Recommendation+5" alt="Recommendation 5">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Section 3: "All Courses" (Left to Right, Faster, Circular)
    st.subheader("All Courses")

    st.markdown("""
    <div class="scroll-container">
        <div class="scroll-left-circular-fast">
            <img src="https://via.placeholder.com/250x150?text=Course+1" alt="Course 1">
            <img src="https://via.placeholder.com/250x150?text=Course+2" alt="Course 2">
            <img src="https://via.placeholder.com/250x150?text=Course+3" alt="Course 3">
            <img src="https://via.placeholder.com/250x150?text=Course+4" alt="Course 4">
            <img src="https://via.placeholder.com/250x150?text=Course+5" alt="Course 5">
        </div>
    </div>
    """, unsafe_allow_html=True)

# features/ProblemPage.py 

import streamlit as st
import subprocess
import os

# Function to write code to a file
def write_code_to_file(code, language):
    file_extension = {'cpp': 'cpp', 'python': 'py', 'java': 'java'}
    filename = f"temp_code.{file_extension[language]}"
    
    with open(filename, "w") as f:
        f.write(code)
    
    return filename

# Function to compile and run C++ code
def compile_and_run_cpp(filename):
    # Compile the C++ code
    compile_cmd = f"C:\\MinGW\\bin\\g++.exe {filename} -o temp_cpp_executable.exe"
    compile_process = subprocess.run(compile_cmd.split(), capture_output=True, text=True)

    # Check for compilation errors
    if compile_process.returncode != 0:
        return f"Compilation error:\n{compile_process.stderr}"
    
    # Run the compiled executable
    run_cmd = "temp_cpp_executable.exe"  # Correct for Windows
    run_process = subprocess.run(run_cmd.split(), capture_output=True, text=True)
    
    # Return the output or runtime errors
    return run_process.stdout if run_process.returncode == 0 else run_process.stderr


# Function to run Python code
def run_python(filename):
    run_cmd = f"python3 {filename}"
    run_process = subprocess.run(run_cmd.split(), capture_output=True, text=True)
    
    return run_process.stdout if run_process.returncode == 0 else run_process.stderr

# Function to compile and run Java code
def compile_and_run_java(filename):
    # Compile the Java code
    compile_cmd = f"javac {filename}"
    compile_process = subprocess.run(compile_cmd.split(), capture_output=True, text=True)
    
    if compile_process.returncode != 0:
        return f"Compilation error:\n{compile_process.stderr}"
    
    # Run the Java code
    classname = filename.replace(".java", "")
    run_cmd = f"java {classname}"
    run_process = subprocess.run(run_cmd.split(), capture_output=True, text=True)
    
    return run_process.stdout if run_process.returncode == 0 else run_process.stderr

# Main function to handle code compilation and execution based on the language
def compile_and_run_code(code, language):
    filename = write_code_to_file(code, language)
    
    if language == "cpp":
        return compile_and_run_cpp(filename)
    elif language == "python":
        return run_python(filename)
    elif language == "java":
        return compile_and_run_java(filename)
    else:
        return "Unsupported language"

# Show the problem page with a compiler area
def show_problem_page(problem_id):
    # Fetch problem data based on problem_id (hardcoded example)
    problems = {
        1: {"title": "Two Sum", "difficulty": "Easy", "description": "Find two numbers that add up to a target."},
        2: {"title": "Longest Substring Without Repeating Characters", "difficulty": "Medium", "description": "Find the longest substring without repeating characters."},
    }

    problem = problems.get(problem_id, {"title": "Unknown", "difficulty": "Unknown", "description": "No problem found."})

    st.title(f"Problem: {problem['title']}")

    # Split into two columns: Problem description (left) and Code Editor (right)
    col1, col2 = st.columns(2)

    # Left column: Problem description
    with col1:
        st.subheader("Problem Description")
        st.write(f"**Difficulty:** {problem['difficulty']}")
        st.write(problem['description'])

    # Right column: Code editor, language selection, and submit button
    with col2:
        st.subheader("Code Editor")

        # Select the language
        language = st.selectbox("Select Language", ["cpp", "python", "java"])

        # Code editor
        code = st.text_area("Write your code here", height=300)

        # Submit button
        if st.button("Submit"):
            # Run the code based on selected language
            result = compile_and_run_code(code, language)

            # Display the result
            st.subheader("Output")
            st.code(result)

            # Show result analysis (this could be expanded with real test cases)
            show_results()

# Show results (this is an example placeholder function)
def show_results():
    # Split the right section into two: Output and Test cases
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Accuracy")
        st.write("75%")  # Example accuracy

    with col2:
        st.subheader("Test Cases")
        st.write("""
        Test case 1: Passed
        Test case 2: Failed
        Test case 3: Passed
        """)

# Run the page
show_problem_page(1)

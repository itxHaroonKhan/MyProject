import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Quiz data
quiz = [
    {
        "question": """What is the output of this code: ```javascript
function example() { var x = 1; if (true) { var x = 2; } console.log(x); }
example();
```""",
        "options": ["1", "2", "undefined", "ReferenceError"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "The 'var' keyword is function-scoped, so the inner 'var x = 2' reassigns the same variable, logging 2."
    },
    {
        "question": """What is the output of this code: ```javascript
let x = 10; { let x = 20; } console.log(x);
```""",
        "options": ["10", "20", "undefined", "Error"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "The 'let' keyword is block-scoped, so the inner 'let x = 20' creates a new variable, and the outer x remains 10."
    },
    {
        "question": """Which method validates an email input field in a form: ```javascript
function validateEmail(email) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email); }
```""",
        "options": ["true for 'user@domain.com'", "false for 'user@domain.com'", "true for 'user.domain.com'", "throws an error"],
        "answer": "true for 'user@domain.com'",
        "difficulty": "Hard",
        "explanation": "The regex `/^[^\s@]+@[^\s@]+\.[^\s@]+$/` checks for a valid email format, returning true for 'user@domain.com'."
    },
    {
        "question": """What does this code do: ```javascript
try { throw new Error('Something went wrong'); } catch (e) { console.log(e.message); }
```""",
        "options": ["Logs 'Something went wrong'", "Throws an uncaught error", "Logs 'Error'", "Nothing"],
        "answer": "Logs 'Something went wrong'",
        "difficulty": "Medium",
        "explanation": "The try block throws an Error, which is caught by the catch block, logging the error message 'Something went wrong'."
    },
    {
        "question": """How do you add an event listener to a button: ```javascript
document.getElementById('myButton').addEventListener('click', function() { alert('Clicked!'); });
```""",
        "options": ["Alerts 'Clicked!' on click", "Throws an error", "Does nothing", "Logs 'Clicked!' to console"],
        "answer": "Alerts 'Clicked!' on click",
        "difficulty": "Easy",
        "explanation": "The addEventListener method attaches a click event handler to the button, triggering an alert when clicked."
    },
    {
        "question": """What is the nodeType of a text node in the DOM? ```javascript
let textNode = document.createTextNode('Hello'); console.log(textNode.nodeType);
```""",
        "options": ["1", "3", "8", "9"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "In the DOM, a text node's nodeType is 3, as defined by the DOM specification."
    },
    {
        "question": """How do you get an element by its class name: ```javascript
document.getElementsByClassName('myClass');
```""",
        "options": ["Returns an HTMLCollection", "Returns a single element", "Throws an error", "Returns null"],
        "answer": "Returns an HTMLCollection",
        "difficulty": "Easy",
        "explanation": "getElementsByClassName returns an HTMLCollection of elements with the specified class name."
    },
    {
        "question": """What does this code do: ```javascript
let obj = { name: 'Test', greet: function() { return 'Hello ' + this.name; } }; console.log(obj.greet());
```""",
        "options": ["Logs 'Hello Test'", "Logs 'Hello undefined'", "Throws an error", "Logs 'Test'"],
        "answer": "Logs 'Hello Test'",
        "difficulty": "Medium",
        "explanation": "The greet method uses 'this' to access the object's name property, returning 'Hello Test'."
    },
    {
        "question": """How do you set the URL of the current page: ```javascript
window.location.href = 'https://example.com';
```""",
        "options": ["Navigates to 'https://example.com'", "Opens a new tab", "Logs the URL", "Throws an error"],
        "answer": "Navigates to 'https://example.com'",
        "difficulty": "Easy",
        "explanation": "Setting window.location.href navigates the current page to the specified URL."
    },
    {
        "question": """What does this code do: ```javascript
window.resizeTo(800, 600);
```""",
        "options": ["Resizes the window to 800x600 pixels", "Moves the window", "Closes the window", "Throws an error"],
        "answer": "Resizes the window to 800x600 pixels",
        "difficulty": "Medium",
        "explanation": "The window.resizeTo method resizes the browser window to the specified width and height."
    },
]

# Shuffle quiz without caching to avoid issues
def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.shuffle(q["display_options"])
        q["labeled_answer"] = q["answer"]
    return shuffled

# Initialize session state
if "quiz_data" not in st.session_state:
    if not quiz:
        st.error("Quiz list is empty! Please check the quiz data.")
        st.stop()
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz),
        "score": 0,
        "current_q": 0,
        "start_time": None,
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 3600,  # 60 minutes
        "theme": "dark",
        "streak": 0,
        "max_streak": 0,
        "started": False,
        "paused": False,
        "pause_time": None
    })

# Debug session state
st.write("Debug: Session State Initialized", st.session_state)

# Theme toggle
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
    st.rerun()

# Timer logic
def update_timer():
    if not st.session_state.paused and st.session_state.start_time:
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        st.session_state.time_left = max(3600 - elapsed, 0)
        if st.session_state.time_left <= 0:
            st.session_state.show_results = True
            st.rerun()

# Pause/Resume quiz
def toggle_pause():
    if st.session_state.paused:
        pause_duration = (datetime.now() - st.session_state.pause_time).total_seconds()
        st.session_state.start_time += timedelta(seconds=pause_duration)
        st.session_state.paused = False
    else:
        st.session_state.paused = True
        st.session_state.pause_time = datetime.now()
    st.rerun()

# Reset quiz
def reset_quiz():
    st.session_state.update({
        "quiz_data": shuffle_quiz(quiz),
        "score": 0,
        "current_q": 0,
        "start_time": None,
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 3600,
        "streak": 0,
        "max_streak": 0,
        "started": False,
        "paused": False,
        "pause_time": None
    })
    st.rerun()

# Simplified CSS
st.markdown("""
<style>
body {
    background: var(--bg-gradient);
    color: var(--text-color);
    font-family: 'Arial', sans-serif;
}
:root {
    --bg-gradient: linear-gradient(180deg, #1a1a3b, #2c2c54);
    --bg-container: #2c2c54;
    --text-color: #ffffff;
    --button-bg: #6b21a8;
    --button-hover: #8b5cf6;
    --code-bg: #1e1e1e;
}
[data-theme="light"] {
    --bg-gradient: linear-gradient(180deg, #e0e7ff, #f3e8ff);
    --bg-container: #ffffff;
    --text-color: #1f2937;
    --button-bg: #4f46e5;
    --button-hover: #6366f1;
    --code-bg: #f1f5f9;
}
.main-container {
    background: var(--bg-container);
    padding: 1rem;
    border-radius: 0.5rem;
    max-width: 800px;
    margin: 1rem auto;
}
.stButton>button {
    background: var(--button-bg);
    color: var(--text-color);
    border: none;
    border-radius: 0.5rem;
    padding: 0.5rem;
    width: 100%;
    font-size: 1rem;
    margin: 0.2rem 0;
}
.stButton>button:hover {
    background: var(--button-hover);
}
.stButton>button:disabled {
    background: #6b7280;
}
.selected-correct {
    background: #34c759 !important;
}
.selected-wrong {
    background: #ff3b30 !important;
}
.question-container {
    background: var(--bg-container);
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
}
.feedback-correct {
    color: #34c759;
    font-weight: bold;
    margin: 0.5rem 0;
}
.feedback-wrong {
    color: #ff3b30;
    font-weight: bold;
    margin: 0.5rem 0;
}
.progress-bar {
    background: #4b4b6b;
    border-radius: 0.5rem;
    height: 0.5rem;
    margin: 0.5rem 0;
}
.progress-fill {
    background: var(--button-bg);
    height: 100%;
    border-radius: 0.5rem;
}
.progress-text {
    color: var(--text-color);
    font-size: 0.75rem;
}
.title {
    font-size: 1.5rem;
    text-align: center;
    color: var(--text-color);
}
.timer {
    font-size: 1rem;
    color: #ff6b6b;
    text-align: center;
}
.difficulty {
    font-size: 0.875rem;
    color: #b0b0d0;
}
.stCodeBlock {
    background-color: var(--code-bg) !important;
    border-radius: 0.5rem;
    padding: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# Main UI
try:
    st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">JavaScript Quiz</h1>', unsafe_allow_html=True)

    # Theme toggle
    if st.button("Toggle Theme"):
        toggle_theme()

    # Welcome screen
    if not st.session_state.started:
        st.write("Debug: Showing welcome screen")
        st.markdown("Test your JavaScript skills with 10 questions! 60 minutes, 2 points per correct answer.")
        if st.button("Start Quiz"):
            st.write("Debug: Start Quiz button clicked")
            st.session_state.started = True
            st.session_state.start_time = datetime.now()
            st.rerun()
    else:
        # Timer
        if not st.session_state.show_results and not st.session_state.paused:
            update_timer()
            minutes = int(st.session_state.time_left // 60)
            seconds = int(st.session_state.time_left % 60)
            st.markdown(f'<div class="timer">Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

        # Pause/Resume and Reset buttons
        pause_label = "Pause Quiz" if not st.session_state.paused else "Resume Quiz"
        if st.button(pause_label):
            toggle_pause()
        if st.button("Reset Quiz"):
            reset_quiz()

        if not st.session_state.quiz_data:
            st.error("No quiz questions available.")
            st.stop()

        # Progress bar
        total_questions = len(st.session_state.quiz_data)
        current_q = min(st.session_state.current_q, total_questions - 1)
        progress = (current_q / total_questions) * 100 if total_questions > 0 else 0
        st.markdown(f"""
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress:.1f}%"></div>
            <div class="progress-text">{progress:.1f}%</div>
        </div>
        <div style="text-align: center;">Question {current_q + 1} of {total_questions}</div>
        """, unsafe_allow_html=True)

        if not st.session_state.show_results:
            with st.container():
                st.markdown('<div class="question-container">', unsafe_allow_html=True)
                q = st.session_state.quiz_data[current_q]

                # Display question
                st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]} | Streak: {st.session_state.streak}</div>', unsafe_allow_html=True)
                st.markdown(q["question"], unsafe_allow_html=True)

                # Display options
                for option in q["display_options"]:
                    button_style = ""
                    if st.session_state.selected_option == option:
                        button_style = "selected-correct" if option == q["answer"] else "selected-wrong"
                    if st.button(option, key=f"option_{q['id']}_{option}"):
                        st.write("Debug: Option selected", option)
                        st.session_state.selected_option = option
                        is_correct = option == q["answer"]
                        st.session_state.feedback = (
                            f'<div class="feedback-correct">Correct! {q["explanation"]}</div>'
                            if is_correct
                            else f'<div class="feedback-wrong">Incorrect. {q["explanation"]}</div>'
                        )
                        if is_correct:
                            st.session_state.score += 2
                            st.session_state.streak += 1
                            st.session_state.max_streak = max(st.session_state.streak, st.session_state.max_streak)
                        else:
                            st.session_state.streak = 0
                        st.session_state.answers[current_q] = option
                        st.rerun()

                # Display feedback
                if st.session_state.feedback:
                    st.markdown(st.session_state.feedback, unsafe_allow_html=True)

                # Next/Previous buttons
                col1, col2 = st.columns(2)
                with col1:
                    if current_q > 0 and st.button("Previous"):
                        st.session_state.current_q -= 1
                        st.session_state.selected_option = None
                        st.session_state.feedback = None
                        st.rerun()
                with col2:
                    if st.session_state.selected_option and st.button("Next"):
                        st.session_state.current_q += 1
                        if st.session_state.current_q >= total_questions:
                            st.session_state.show_results = True
                        st.session_state.selected_option = None
                        st.session_state.feedback = None
                        st.rerun()

                st.markdown('</div>', unsafe_allow_html=True)
        else:
            # Results screen
            st.markdown(f"""
            <div style="text-align: center;">
                <h2>Quiz Completed!</h2>
                <p>Score: {st.session_state.score} / {total_questions * 2}</p>
                <p>Max Streak: {st.session_state.max_streak}</p>
            </div>
            """, unsafe_allow_html=True)
            for i, (q, ans) in enumerate(zip(st.session_state.quiz_data, st.session_state.answers)):
                st.markdown(f"""
                <div class="question-container">
                    <div>Question {i + 1} ({q["difficulty"]})</div>
                    {q["question"]}
                    <p><strong>Your Answer:</strong> {ans or "Not answered"}</p>
                    <p><strong>Correct Answer:</strong> {q["answer"]}</p>
                    <p>{q["explanation"]}</p>
                </div>
                """, unsafe_allow_html=True)
            if st.button("Restart Quiz"):
                reset_quiz()

    st.markdown('</div>', unsafe_allow_html=True)

except Exception as e:
    st.error(f"Error: {str(e)}")

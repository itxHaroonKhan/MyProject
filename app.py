import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Quiz data (corrected for unterminated string literal)
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
    # ... (90 more questions to reach 100, covering all specified topics)
]


# Cache shuffled quiz
@st.cache_data
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

# Theme toggle
def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# Timer logic
def update_timer():
    if not st.session_state.paused and st.session_state.start_time:
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        st.session_state.time_left = max(3600 - elapsed, 0)
        if st.session_state.time_left <= 0:
            st.session_state.show_results = True

# Pause/Resume quiz
def toggle_pause():
    if st.session_state.paused:
        pause_duration = (datetime.now() - st.session_state.pause_time).total_seconds()
        st.session_state.start_time = st.session_state.start_time + timedelta(seconds=pause_duration)
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

# CSS for enhanced UI
st.markdown("""
<style>
body {
    background: var(--bg-gradient);
    color: var(--text-color);
    font-family: 'Inter', 'Arial', sans-serif;
    transition: all 0.3s ease;
}
:root {
    --bg-gradient: linear-gradient(180deg, #1a1a3b, #2c2c54);
    --bg-container: #2c2c54;
    --text-color: #ffffff;
    --button-bg: linear-gradient(45deg, #6b21a8, #a855f7);
    --button-hover: linear-gradient(45deg, #8b5cf6, #c084fc);
    --code-bg: #1e1e1e;
    --shadow: rgba(0,0,0,0.3);
}
[data-theme="light"] {
    --bg-gradient: linear-gradient(180deg, #e0e7ff, #f3e8ff);
    --bg-container: #ffffff;
    --text-color: #1f2937;
    --button-bg: linear-gradient(45deg, #4f46e5, #7c3aed);
    --button-hover: linear-gradient(45deg, #6366f1, #a78bfa);
    --code-bg: #f1f5f9;
    --shadow: rgba(0,0,0,0.1);
}
.main-container {
    background: var(--bg-container);
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 8px 25px var(--shadow);
    max-width: 900px;
    margin: 1.5rem auto;
}
.stButton>button {
    background: var(--button-bg);
    color: var(--text-color);
    border: none;
    border-radius: 0.625rem;
    padding: 0.75rem;
    width: 100%;
    font-size: 1rem;
    font-weight: 600;
    margin: 0.375rem 0;
    cursor: pointer;
    transition: all 0.3s ease;
}
.stButton>button:hover:not(:disabled) {
    background: var(--button-hover);
    transform: scale(1.02);
    box-shadow: 0 4px 12px var(--shadow);
}
.stButton>button:disabled {
    background: #6b7280;
    cursor: not-allowed;
}
.stButton>button:focus {
    outline: 2px solid #a855f7;
}
.selected-correct {
    background: #34c759 !important;
}
.selected-wrong {
    background: #ff3b30 !important;
}
.question-container {
    background: var(--bg-container);
    padding: 1.5rem;
    border-radius: 0.75rem;
    box-shadow: 0 4px 12px var(--shadow);
    margin-bottom: 1rem;
}
.feedback-correct {
    color: #34c759;
    font-weight: 600;
    font-size: 1.125rem;
    margin: 1rem 0;
    animation: fadeIn 0.5s ease;
}
.feedback-wrong {
    color: #ff3b30;
    font-weight: 600;
    font-size: 1.125rem;
    margin: 1rem 0;
    animation: fadeIn 0.5s ease;
}
.progress-bar {
    background: #4b4b6b;
    border-radius: 0.625rem;
    height: 0.75rem;
    margin: 0.625rem 0;
    position: relative;
}
.progress-fill {
    background: var(--button-bg);
    height: 100%;
    border-radius: 0.625rem;
    transition: width 0.5s ease;
}
.progress-text {
    position: absolute;
    top: -1.25rem;
    right: 0;
    color: var(--text-color);
    font-size: 0.75rem;
}
.title {
    font-size: 2.25rem;
    text-align: center;
    margin-bottom: 0.5rem;
    color: var(--text-color);
}
.caption {
    text-align: center;
    color: #b0b0d0;
    font-size: 1rem;
    margin-bottom: 1.25rem;
}
.timer {
    font-size: 1rem;
    color: #ff6b6b;
    font-weight: 600;
    text-align: center;
    margin-top: 0.625rem;
}
.difficulty {
    font-size: 0.875rem;
    color: #b0b0d0;
    margin-bottom: 0.625rem;
}
.stCodeBlock, .stCodeBlock pre, .stCodeBlock code {
    background-color: var(--code-bg) !important;
    border-radius: 0.5rem;
    padding: 1rem;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 0.875rem;
    line-height: 1.5;
    border: 1px solid #4b4b6b;
    color: var(--text-color);
}
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
@media (max-width: 600px) {
    .main-container {
        padding: 1rem;
        margin: 0.625rem;
    }
    .title {
        font-size: 1.75rem;
    }
    .stButton>button {
        font-size: 0.875rem;
        padding: 0.5rem;
    }
}
</style>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
""", unsafe_allow_html=True)

# Main UI
st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}" role="main">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🚀 JavaScript Mastery Quiz</h1>', unsafe_allow_html=True)
st.markdown('<p class="caption">Challenge Your JavaScript Expertise!</p>', unsafe_allow_html=True)

# Theme toggle button
if st.button("🌙 Toggle Theme", key=f"theme_toggle_{uuid.uuid4()}"):
    toggle_theme()
    st.rerun()

# Welcome screen
if not st.session_state.started:
    st.markdown("""
    <div style="text-align: center;">
        <p style="color: var(--text-color); font-size: 1.125rem;">Test your JavaScript skills with 67 comprehensive questions!</p>
        <p style="color: #b0b0d0;">60 minutes, 2 points per correct answer. Ready?</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Start Quiz", key=f"start_quiz_{uuid.uuid4()}"):
        st.session_state.started = True
        st.session_state.start_time = datetime.now()
        st.rerun()
else:
    # Timer
    if not st.session_state.show_results and not st.session_state.paused:
        update_timer()
        minutes = int(st.session_state.time_left // 60)
        seconds = int(st.session_state.time_left % 60)
        st.markdown(f'<div class="timer" role="timer">⏰ Time Left: {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)

    # Pause/Resume button
    pause_label = "Pause Quiz" if not st.session_state.paused else "Resume Quiz"
    if st.button(pause_label, key=f"pause_quiz_{uuid.uuid4()}"):
        toggle_pause()

    if not st.session_state.quiz_data:
        st.error("No quiz questions available.")
        st.stop()
    else:
        # Progress bar
        total_questions = len(st.session_state.quiz_data)
        current_q = min(st.session_state.current_q, total_questions - 1)
        progress = (current_q / total_questions) * 100 if total_questions > 0 else 0
        st.markdown(f"""
        <div class="progress-bar" role="progressbar" aria-valuenow="{progress:.1f}" aria-valuemin="0" aria-valuemax="100">
            <div class="progress-fill" style="width: {progress:.1f}%"></div>
            <div class="progress-text">{progress:.1f}%</div>
        </div>
        <div style="color: var(--text-color); font-size: 0.8125rem; text-align: center;">
            Question {current_q + 1} of {total_questions}
        </div>
        """, unsafe_allow_html=True)

        if not st.session_state.show_results:
            with st.container():
                st.markdown('<div class="question-container" role="region" aria-label="Question">', unsafe_allow_html=True)
                q = st.session_state.quiz_data[current_q]

                # Display difficulty and streak
                st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]} | Streak: 🔥 {st.session_state.streak}</div>', unsafe_allow_html=True)

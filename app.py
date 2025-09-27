import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Quiz data (unchanged)
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

# Shuffle quiz
def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.shuffle(q["display_options"])
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

# CSS for improved styling
st.markdown("""
<style>
:root {
    --bg-gradient: linear-gradient(180deg, #1e1e3f, #2a2a5e);
    --bg-container: #2c2c54;
    --text-color: #e0e0ff;
    --button-bg: #7c3aed;
    --button-hover: #9f67fa;
    --code-bg: #1e1e2e;
    --accent: #22d3ee;
}
[data-theme="light"] {
    --bg-gradient: linear-gradient(180deg, #dbeafe, #f3e8ff);
    --bg-container: #ffffff;
    --text-color: #1e293b;
    --button-bg: #4f46e5;
    --button-hover: #7c3aed;
    --code-bg: #f1f5f9;
    --accent: #2563eb;
}
body {
    background: var(--bg-gradient);
    color: var(--text-color);
    font-family: 'Inter', sans-serif;
}
.main-container {
    background: var(--bg-container);
    padding: 1.5rem;
    border-radius: 0.75rem;
    max-width: 900px;
    margin: 1rem auto;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}
.stButton>button {
    background: var(--button-bg);
    color: var(--text-color);
    border: none;
    border-radius: 0.5rem;
    padding: 0.75rem;
    width: 100%;
    font-size: 1rem;
    margin: 0.25rem 0;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background: var(--button-hover);
    transform: translateY(-2px);
}
.stButton>button:disabled {
    background: #6b7280;
    cursor: not-allowed;
}
.selected-correct {
    background: #22c55e !important;
    transform: scale(1.02);
}
.selected-wrong {
    background: #ef4444 !important;
    transform: scale(1.02);
}
.question-container {
    background: var(--code-bg);
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1.5rem;
}
.feedback-correct {
    color: #22c55e;
    font-weight: 600;
    margin: 0.75rem 0;
    padding: 0.5rem;
    background: rgba(34, 197, 94, 0.1);
    border-radius: 0.5rem;
}
.feedback-wrong {
    color: #ef4444;
    font-weight: 600;
    margin: 0.75rem 0;
    padding: 0.5rem;
    background: rgba(239, 68, 68, 0.1);
    border-radius: 0.5rem;
}
.progress-bar {
    background: #3b3b5b;
    border-radius: 1rem;
    height: 0.75rem;
    margin: 1rem 0;
}
.progress-fill {
    background: var(--accent);
    height: 100%;
    border-radius: 1rem;
    transition: width 0.5s ease;
}
.progress-text {
    color: var(--text-color);
    font-size: 0.9rem;
    text-align: center;
    margin-top: 0.5rem;
}
.title {
    font-size: 2rem;
    font-weight: 700;
    text-align: center;
    color: var(--accent);
    margin-bottom: 1rem;
}
.timer {
    font-size: 1.2rem;
    font-weight: 600;
    color: #f87171;
    text-align: center;
    margin-bottom: 1rem;
}
.difficulty {
    font-size: 0.9rem;
    color: #a1a1aa;
    margin-bottom: 0.5rem;
}
.stCodeBlock {
    background-color: var(--code-bg) !important;
    border-radius: 0.5rem;
    padding: 1rem;
    margin: 0.5rem 0;
}
.stats-container {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1rem;
}
.stat-box {
    background: var(--code-bg);
    padding: 1rem;
    border-radius: 0.5rem;
    flex: 1;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Main UI
try:
    st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">JavaScript Quiz Challenge</h1>', unsafe_allow_html=True)

    # Theme toggle
    col_theme, col_reset = st.columns([1, 1])
    with col_theme:
        if st.button("🌙 Toggle Theme"):
            toggle_theme()
    with col_reset:
        if st.button("🔄 Reset Quiz"):
            reset_quiz()

    # Welcome screen
    if not st.session_state.started:
        st.markdown("""
        <div style="text-align: center;">
            <p style="font-size: 1.2rem;">Test your JavaScript skills with 10 exciting questions!</p>
            <p style="font-size: 1rem; color: #a1a1aa;">60 minutes | 2 points per correct answer | Track your streak!</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Start Quiz", key="start_quiz"):
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

        # Pause/Resume button
        pause_label = "⏸️ Pause Quiz" if not st.session_state.paused else "▶️ Resume Quiz"
        st.button(pause_label, on_click=toggle_pause)

        if not st.session_state.quiz_data:
            st.error("No quiz questions available.")
            st.stop()

        # Stats
        total_questions = len(st.session_state.quiz_data)
        current_q = min(st.session_state.current_q, total_questions - 1)
        progress = (current_q / total_questions) * 100 if total_questions > 0 else 0
        st.markdown(f"""
        <div class="stats-container">
            <div class="stat-box">
                <div>Score</div>
                <div style="font-size: 1.2rem; font-weight: 600;">{st.session_state.score}/{total_questions * 2}</div>
            </div>
            <div class="stat-box">
                <div>Streak</div>
                <div style="font-size: 1.2rem; font-weight: 600;">{st.session_state.streak}</div>
            </div>
            <div class="stat-box">
                <div>Max Streak</div>
                <div style="font-size: 1.2rem; font-weight: 600;">{st.session_state.max_streak}</div>
            </div>
        </div>
        <div class="progress-bar">
            <div class="progress-fill" style="width: {progress:.1f}%"></div>
        </div>
        <div class="progress-text">Question {current_q + 1} of {total_questions} ({progress:.1f}%)</div>
        """, unsafe_allow_html=True)

        if not st.session_state.show_results:
            with st.container():
                st.markdown('<div class="question-container">', unsafe_allow_html=True)
                q = st.session_state.quiz_data[current_q]

                # Display question
                st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]}</div>', unsafe_allow_html=True)
                st.markdown(q["question"], unsafe_allow_html=True)

                # Display options
                for option in q["display_options"]:
                    button_style = ""
                    if st.session_state.selected_option == option:
                        button_style = "selected-correct" if option == q["answer"] else "selected-wrong"
                    if st.button(option, key=f"option_{q['id']}_{option}", disabled=st.session_state.selected_option is not None):
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

                # Navigation buttons
                col_prev, col_next = st.columns(2)
                with col_prev:
                    if current_q > 0 and st.button("⬅️ Previous", disabled=st.session_state.paused):
                        st.session_state.current_q -= 1
                        st.session_state.selected_option = None
                        st.session_state.feedback = None
                        st.rerun()
                with col_next:
                    if st.session_state.selected_option and st.button("➡️ Next", disabled=st.session_state.paused):
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
                <h2>Quiz Completed! 🎉</h2>
                <p style="font-size: 1.5rem;">Score: {st.session_state.score} / {total_questions * 2}</p>
                <p style="font-size: 1.2rem;">Max Streak: {st.session_state.max_streak}</p>
            </div>
            """, unsafe_allow_html=True)
            for i, (q, ans) in enumerate(zip(st.session_state.quiz_data, st.session_state.answers)):
                status = "Correct" if ans == q["answer"] else "Incorrect" if ans else "Not answered"
                st.markdown(f"""
                <div class="question-container">
                    <div style="font-weight: 600;">Question {i + 1} ({q["difficulty"]}) - {status}</div>
                    {q["question"]}
                    <p><strong>Your Answer:</strong> {ans or "Not answered"}</p>
                    <p><strong>Correct Answer:</strong> {q["answer"]}</p>
                    <p>{q["explanation"]}</p>
                </div>
                """, unsafe_allow_html=True)
            if st.button("🔄 Restart Quiz"):
                reset_quiz()

    st.markdown('</div>', unsafe_allow_html=True)

except Exception as e:
    st.error(f"Error: {str(e)}")

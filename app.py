import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Quiz data - Enhanced with more questions
quiz = [
    {
        "question": """What is the output of this code: ```javascript
function example() { var x = 1; if (true) { var x = 2; } console.log(x); }
example();
```""",
        "options": ["1", "2", "undefined", "ReferenceError"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "The 'var' keyword is function-scoped, so the inner 'var x = 2' reassigns the same variable, logging 2.",
        "category": "Variables"
    },
    {
        "question": """What is the output of this code: ```javascript
let x = 10; { let x = 20; } console.log(x);
```""",
        "options": ["10", "20", "undefined", "Error"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "The 'let' keyword is block-scoped, so the inner 'let x = 20' creates a new variable, and the outer x remains 10.",
        "category": "Variables"
    },
    {
        "question": """Which method validates an email input field in a form: ```javascript
function validateEmail(email) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email); }
```""",
        "options": ["true for 'user@domain.com'", "false for 'user@domain.com'", "true for 'user.domain.com'", "throws an error"],
        "answer": "true for 'user@domain.com'",
        "difficulty": "Hard",
        "explanation": "The regex `/^[^\s@]+@[^\s@]+\.[^\s@]+$/` checks for a valid email format, returning true for 'user@domain.com'.",
        "category": "Regex"
    },
    {
        "question": """What does this code do: ```javascript
try { throw new Error('Something went wrong'); } catch (e) { console.log(e.message); }
```""",
        "options": ["Logs 'Something went wrong'", "Throws an uncaught error", "Logs 'Error'", "Nothing"],
        "answer": "Logs 'Something went wrong'",
        "difficulty": "Medium",
        "explanation": "The try block throws an Error, which is caught by the catch block, logging the error message 'Something went wrong'.",
        "category": "Error Handling"
    },
    {
        "question": """How do you add an event listener to a button: ```javascript
document.getElementById('myButton').addEventListener('click', function() { alert('Clicked!'); });
```""",
        "options": ["Alerts 'Clicked!' on click", "Throws an error", "Does nothing", "Logs 'Clicked!' to console"],
        "answer": "Alerts 'Clicked!' on click",
        "difficulty": "Easy",
        "explanation": "The addEventListener method attaches a click event handler to the button, triggering an alert when clicked.",
        "category": "DOM"
    },
    {
        "question": """What is the nodeType of a text node in the DOM? ```javascript
let textNode = document.createTextNode('Hello'); console.log(textNode.nodeType);
```""",
        "options": ["1", "3", "8", "9"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "In the DOM, a text node's nodeType is 3, as defined by the DOM specification.",
        "category": "DOM"
    },
    {
        "question": """How do you get an element by its class name: ```javascript
document.getElementsByClassName('myClass');
```""",
        "options": ["Returns an HTMLCollection", "Returns a single element", "Throws an error", "Returns null"],
        "answer": "Returns an HTMLCollection",
        "difficulty": "Easy",
        "explanation": "getElementsByClassName returns an HTMLCollection of elements with the specified class name.",
        "category": "DOM"
    },
    {
        "question": """What does this code do: ```javascript
let obj = { name: 'Test', greet: function() { return 'Hello ' + this.name; } }; console.log(obj.greet());
```""",
        "options": ["Logs 'Hello Test'", "Logs 'Hello undefined'", "Throws an error", "Logs 'Test'"],
        "answer": "Logs 'Hello Test'",
        "difficulty": "Medium",
        "explanation": "The greet method uses 'this' to access the object's name property, returning 'Hello Test'.",
        "category": "Objects"
    },
    {
        "question": """How do you set the URL of the current page: ```javascript
window.location.href = 'https://example.com';
```""",
        "options": ["Navigates to 'https://example.com'", "Opens a new tab", "Logs the URL", "Throws an error"],
        "answer": "Navigates to 'https://example.com'",
        "difficulty": "Easy",
        "explanation": "Setting window.location.href navigates the current page to the specified URL.",
        "category": "Browser API"
    },
    {
        "question": """What does this code do: ```javascript
window.resizeTo(800, 600);
```""",
        "options": ["Resizes the window to 800x600 pixels", "Moves the window", "Closes the window", "Throws an error"],
        "answer": "Resizes the window to 800x600 pixels",
        "difficulty": "Medium",
        "explanation": "The window.resizeTo method resizes the browser window to the specified width and height.",
        "category": "Browser API"
    },
]

# Enhanced CSS with better styling
st.markdown("""
<style>
:root {
    --primary: #6b21a8;
    --primary-hover: #8b5cf6;
    --success: #34c759;
    --danger: #ff3b30;
    --warning: #ff9500;
    --info: #007aff;
    --dark: #1a1a3b;
    --light: #f3e8ff;
}

body {
    background: linear-gradient(135deg, var(--dark) 0%, #2c2c54 100%);
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

[data-theme="light"] {
    --bg-gradient: linear-gradient(135deg, #e0e7ff 0%, #f3e8ff 100%);
    --text-color: #1f2937;
    --card-bg: #ffffff;
}

[data-theme="dark"] {
    --bg-gradient: linear-gradient(135deg, #1a1a3b 0%, #2c2c54 100%);
    --text-color: #ffffff;
    --card-bg: #2c2c54;
}

.main-container {
    background: var(--card-bg);
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    margin: 1rem auto;
    max-width: 900px;
    color: var(--text-color);
}

.title {
    text-align: center;
    font-size: 2.5rem;
    background: linear-gradient(90deg, var(--primary), var(--info));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: var(--text-color);
    opacity: 0.8;
    margin-bottom: 2rem;
}

.stButton>button {
    background: var(--primary);
    color: white;
    border: none;
    border-radius: 0.75rem;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease;
    margin: 0.5rem 0;
    width: 100%;
}

.stButton>button:hover {
    background: var(--primary-hover);
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.option-button {
    background: rgba(107, 33, 168, 0.1) !important;
    border: 2px solid var(--primary) !important;
    color: var(--text-color) !important;
}

.option-button:hover {
    background: var(--primary) !important;
    color: white !important;
}

.selected-correct {
    background: var(--success) !important;
    color: white !important;
    border: 2px solid var(--success) !important;
}

.selected-wrong {
    background: var(--danger) !important;
    color: white !important;
    border: 2px solid var(--danger) !important;
}

.difficulty-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.8rem;
    font-weight: bold;
    margin: 0.5rem 0;
}

.easy { background: var(--success); color: white; }
.medium { background: var(--warning); color: white; }
.hard { background: var(--danger); color: white; }

.category-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    font-size: 0.8rem;
    background: var(--info);
    color: white;
    margin-left: 0.5rem;
}

.progress-container {
    background: rgba(255,255,255,0.1);
    border-radius: 1rem;
    padding: 1rem;
    margin: 1rem 0;
}

.progress-bar {
    background: rgba(255,255,255,0.2);
    border-radius: 0.5rem;
    height: 0.75rem;
    margin: 0.5rem 0;
    overflow: hidden;
}

.progress-fill {
    background: linear-gradient(90deg, var(--primary), var(--info));
    height: 100%;
    border-radius: 0.5rem;
    transition: width 0.3s ease;
}

.streak-counter {
    background: linear-gradient(135deg, #ff6b6b, #ffa726);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    font-weight: bold;
    text-align: center;
    margin: 0.5rem 0;
}

.timer-display {
    font-size: 1.5rem;
    font-weight: bold;
    text-align: center;
    background: rgba(255,255,255,0.1);
    padding: 0.5rem;
    border-radius: 0.5rem;
    margin: 0.5rem 0;
}

.feedback-box {
    padding: 1rem;
    border-radius: 0.5rem;
    margin: 1rem 0;
    font-weight: bold;
}

.correct-feedback {
    background: rgba(52, 199, 89, 0.2);
    border: 2px solid var(--success);
    color: var(--success);
}

.wrong-feedback {
    background: rgba(255, 59, 48, 0.2);
    border: 2px solid var(--danger);
    color: var(--danger);
}

.results-container {
    text-align: center;
    padding: 2rem;
}

.score-display {
    font-size: 3rem;
    font-weight: bold;
    background: linear-gradient(90deg, var(--primary), var(--info));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 1rem 0;
}

.achievement-badge {
    background: linear-gradient(135deg, #ffd700, #ffa726);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    font-weight: bold;
    margin: 0.5rem;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
def initialize_session_state():
    if "quiz_data" not in st.session_state:
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
            "theme": "dark",
            "streak": 0,
            "max_streak": 0,
            "started": False,
            "paused": False,
            "pause_time": None,
            "quiz_duration": 3600
        })

def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.shuffle(q["display_options"])
        q["labeled_answer"] = q["answer"]
    return shuffled

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

def update_timer():
    if not st.session_state.paused and st.session_state.start_time:
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        st.session_state.time_left = max(st.session_state.quiz_duration - elapsed, 0)
        if st.session_state.time_left <= 0:
            st.session_state.show_results = True

def toggle_pause():
    if st.session_state.paused:
        pause_duration = (datetime.now() - st.session_state.pause_time).total_seconds()
        st.session_state.start_time += timedelta(seconds=pause_duration)
        st.session_state.paused = False
    else:
        st.session_state.paused = True
        st.session_state.pause_time = datetime.now()

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
        "time_left": st.session_state.quiz_duration,
        "streak": 0,
        "max_streak": 0,
        "started": False,
        "paused": False,
        "pause_time": None
    })

def get_achievement(score, max_streak, total_questions):
    percentage = (score / (total_questions * 2)) * 100
    if percentage >= 90 and max_streak >= total_questions:
        return "JavaScript Master 🏆"
    elif percentage >= 80:
        return "Expert Developer 💻"
    elif percentage >= 70:
        return "Skilled Programmer ⚡"
    elif percentage >= 60:
        return "Good Learner 📚"
    else:
        return "Keep Practicing 🌱"

# Main application
def main():
    initialize_session_state()
    
    st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}">', unsafe_allow_html=True)
    
    # Header
    st.markdown('<h1 class="title">🚀 JavaScript Mastery Quiz</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Test your JavaScript skills with interactive coding challenges!</p>', unsafe_allow_html=True)
    
    # Theme toggle
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🌓 Toggle Theme"):
            toggle_theme()
            st.rerun()
    
    # Welcome screen
    if not st.session_state.started:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h2>📋 Quiz Overview</h2>
            <p><strong>10 Questions</strong> • <strong>60 Minutes</strong> • <strong>2 Points per Question</strong></p>
            <p>Categories: Variables, DOM, Error Handling, Browser API, and more!</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎯 Start Quiz", use_container_width=True):
            st.session_state.started = True
            st.session_state.start_time = datetime.now()
            st.rerun()
    else:
        # Timer and controls
        if not st.session_state.show_results:
            update_timer()
            
            # Timer display
            minutes = int(st.session_state.time_left // 60)
            seconds = int(st.session_state.time_left % 60)
            timer_color = "🔴" if st.session_state.time_left < 300 else "🟡" if st.session_state.time_left < 900 else "🟢"
            st.markdown(f'<div class="timer-display">{timer_color} {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)
            
            # Control buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                pause_label = "⏸️ Pause" if not st.session_state.paused else "▶️ Resume"
                if st.button(pause_label, use_container_width=True):
                    toggle_pause()
                    st.rerun()
            with col2:
                if st.button("🔄 Restart", use_container_width=True):
                    reset_quiz()
                    st.rerun()
            with col3:
                if st.button("🏁 Submit", use_container_width=True):
                    st.session_state.show_results = True
                    st.rerun()
        
        # Progress section
        total_questions = len(st.session_state.quiz_data)
        current_q = min(st.session_state.current_q, total_questions - 1)
        progress = ((current_q + 1) / total_questions) * 100
        
        st.markdown(f"""
        <div class="progress-container">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span>Question {current_q + 1} of {total_questions}</span>
                <span>Score: {st.session_state.score}/{total_questions * 2}</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress}%"></div>
            </div>
            <div style="display: flex; justify-content: space-between; margin-top: 0.5rem;">
                <span>Progress: {progress:.1f}%</span>
                <div class="streak-counter">🔥 Streak: {st.session_state.streak}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.show_results:
            # Question display
            q = st.session_state.quiz_data[current_q]
            
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 0.75rem; margin: 1rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="difficulty-badge {q['difficulty'].lower()}">{q['difficulty']}</span>
                    <span class="category-badge">{q['category']}</span>
                </div>
                {q['question']}
            </div>
            """, unsafe_allow_html=True)
            
            # Options
            for option in q["display_options"]:
                button_class = "option-button"
                if st.session_state.selected_option == option:
                    button_class = "selected-correct" if option == q["answer"] else "selected-wrong"
                
                if st.button(option, key=f"option_{q['id']}_{option}", use_container_width=True):
                    st.session_state.selected_option = option
                    is_correct = option == q["answer"]
                    st.session_state.feedback = {
                        "message": f"{'✅ Correct!' if is_correct else '❌ Incorrect'} {q['explanation']}",
                        "type": "correct" if is_correct else "wrong"
                    }
                    
                    if is_correct:
                        st.session_state.score += 2
                        st.session_state.streak += 1
                        st.session_state.max_streak = max(st.session_state.streak, st.session_state.max_streak)
                    else:
                        st.session_state.streak = 0
                    
                    st.session_state.answers[current_q] = option
                    st.rerun()
            
            # Feedback
            if st.session_state.feedback:
                feedback_class = "correct-feedback" if st.session_state.feedback["type"] == "correct" else "wrong-feedback"
                st.markdown(f'<div class="feedback-box {feedback_class}">{st.session_state.feedback["message"]}</div>', unsafe_allow_html=True)
            
            # Navigation buttons
            col1, col2 = st.columns(2)
            with col1:
                if current_q > 0 and st.button("⬅️ Previous", use_container_width=True):
                    st.session_state.current_q -= 1
                    st.session_state.selected_option = st.session_state.answers[st.session_state.current_q]
                    st.session_state.feedback = None
                    st.rerun()
            with col2:
                if st.session_state.selected_option and st.button("Next ➡️", use_container_width=True):
                    st.session_state.current_q += 1
                    if st.session_state.current_q >= total_questions:
                        st.session_state.show_results = True
                    else:
                        st.session_state.selected_option = st.session_state.answers[st.session_state.current_q]
                        st.session_state.feedback = None
                    st.rerun()
        else:
            # Results screen
            achievement = get_achievement(st.session_state.score, st.session_state.max_streak, total_questions)
            
            st.markdown(f"""
            <div class="results-container">
                <h2>🎉 Quiz Completed!</h2>
                <div class="score-display">{st.session_state.score}/{total_questions * 2}</div>
                <div class="achievement-badge">{achievement}</div>
                <p>Maximum Streak: 🔥 {st.session_state.max_streak}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Detailed results
            st.markdown("### 📊 Detailed Results")
            for i, (q, ans) in enumerate(zip(st.session_state.quiz_data, st.session_state.answers)):
                is_correct = ans == q["answer"]
                result_icon = "✅" if is_correct else "❌"
                
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 0.5rem; margin: 0.5rem 0;">
                    <div style="display: flex; justify-content: space-between;">
                        <strong>Question {i + 1} {result_icon}</strong>
                        <span class="difficulty-badge {q['difficulty'].lower()}">{q['difficulty']}</span>
                    </div>
                    {q['question']}
                    <p><strong>Your Answer:</strong> <span style="color: {'var(--success)' if is_correct else 'var(--danger)'}">{ans or "Not answered"}</span></p>
                    <p><strong>Correct Answer:</strong> {q['answer']}</p>
                    <p><em>{q['explanation']}</em></p>
                </div>
                """, unsafe_allow_html=True)
            
            if st.button("🔄 Take Quiz Again", use_container_width=True):
                reset_quiz()
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

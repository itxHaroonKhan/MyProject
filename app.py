import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Quiz data (100 questions, sample subset provided)
quiz = [
    # Variable Scoping
    {
        "question": """What is the output of: ```javascript
var x = 10;
function test() {
    console.log(x);
    var x = 20;
}
test();
```""",
        "options": ["10", "20", "undefined", "ReferenceError"],
        "answer": "undefined",
        "difficulty": "Medium",
        "explanation": "Due to hoisting, 'var x' is declared at the top of the function, but its assignment happens later, so 'x' is undefined when logged."
    },
    {
        "question": """What is the output of: ```javascript
let x = 5;
{ let x = 10; }
console.log(x);
```""",
        "options": ["5", "10", "undefined", "ReferenceError"],
        "answer": "5",
        "difficulty": "Easy",
        "explanation": "'let' is block-scoped, so the inner 'x' is a separate variable and does not affect the outer 'x'."
    },
    # Form Validation: Drop-downs
    {
        "question": """How do you validate a drop-down (select) element in JavaScript to ensure a value is selected? ```javascript
function validateSelect(element) {
    return element.value !== '';
}
```""",
        "options": ["Check if element.value is not empty", "Check if element.selectedIndex is -1", "Check if element.value is null", "Check if element.options is empty"],
        "answer": "Check if element.value is not empty",
        "difficulty": "Easy",
        "explanation": "For a select element, checking if 'element.value' is not an empty string ensures a valid option is selected."
    },
    # Form Validation: Radio Buttons
    {
        "question": """How do you validate that a radio button group has a selection? ```javascript
function validateRadio(groupName) {
    return document.querySelector(`input[name="${groupName}"]:checked`) !== null;
}
```""",
        "options": ["Check if any radio is checked", "Check if groupName.value exists", "Check if groupName.length > 0", "Check if radio.value is not null"],
        "answer": "Check if any radio is checked",
        "difficulty": "Medium",
        "explanation": "Using querySelector with ':checked' ensures at least one radio button in the group is selected."
    },
    # Form Validation: ZIP Codes
    {
        "question": "What is a common regex for validating a 5-digit US ZIP code?",
        "options": ["/^\\d{5}$/", "/^[0-9]{5}-[0-9]{4}$/", "/^\\w{5}$/", "/^[0-9]{5,9}$/"],
        "answer": "/^\\d{5}$/",
        "difficulty": "Medium",
        "explanation": "The regex /^\\d{5}$/ matches exactly five digits, suitable for a standard US ZIP code."
    },
    # Form Validation: Email
    {
        "question": """What does this email validation regex do? ```javascript
/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/
```""",
        "options": ["Matches emails with letters, numbers, and specific symbols", "Matches any string with an @ symbol", "Matches emails with exactly 2 characters after the dot", "Matches emails without a domain"],
        "answer": "Matches emails with letters, numbers, and specific symbols",
        "difficulty": "Hard",
        "explanation": "The regex ensures a valid email format with allowed characters before and after the @, a domain, and a TLD of 2+ characters."
    },
    # Exceptions: Try and Catch
    {
        "question": """What is the output of: ```javascript
try {
    throw new Error('Something went wrong');
} catch (e) {
    console.log(e.message);
}
```""",
        "options": ["Something went wrong", "Error", "undefined", "ReferenceError"],
        "answer": "Something went wrong",
        "difficulty": "Medium",
        "explanation": "The catch block captures the thrown Error object, and 'e.message' logs the error message."
    },
    # Exceptions: Throw
    {
        "question": "What does the 'throw' statement do in JavaScript?",
        "options": ["Throws a custom error", "Catches an error", "Logs an error to the console", "Stops the function execution without an error"],
        "answer": "Throws a custom error",
        "difficulty": "Easy",
        "explanation": "The 'throw' statement creates and throws a custom error, which can be caught by a try-catch block."
    },
    # Handling Events within JavaScript
    {
        "question": """How do you add a click event listener to a button? ```javascript
document.getElementById('myButton').addEventListener('click', function() {
    alert('Button clicked!');
});
```""",
        "options": ["Using addEventListener", "Using onclick attribute", "Using attachEvent", "Using bind"],
        "answer": "Using addEventListener",
        "difficulty": "Easy",
        "explanation": "addEventListener is the modern way to attach event handlers in JavaScript."
    },
    # The DOM: Junk Artifacts and nodeType
    {
        "question": "What is the nodeType of a text node in the DOM?",
        "options": ["1", "3", "8", "9"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "In the DOM, a text node has a nodeType of 3, while elements are 1, comments are 8, and documents are 9."
    },
    # The DOM: More Ways to Target Elements
    {
        "question": "Which method targets elements by class name?",
        "options": ["getElementsByClassName", "getElementById", "querySelector", "getElementsByTagName"],
        "answer": "getElementsByClassName",
        "difficulty": "Easy",
        "explanation": "getElementsByClassName returns a live HTMLCollection of elements with the specified class name."
    },
    # The DOM: Getting a Target's Name
    {
        "question": "How do you get the tag name of a DOM element?",
        "options": ["element.tagName", "element.nodeName", "element.name", "Both element.tagName and element.nodeName"],
        "answer": "Both element.tagName and element.nodeName",
        "difficulty": "Medium",
        "explanation": "Both tagName and nodeName return the tag name of an element in uppercase."
    },
    # The DOM: Counting Elements
    {
        "question": """How do you count all <p> elements in the DOM? ```javascript
document.getElementsByTagName('p').length
```""",
        "options": ["getElementsByTagName('p').length", "querySelectorAll('p').length", "getElementsByClassName('p').length", "Both getElementsByTagName and querySelectorAll"],
        "answer": "Both getElementsByTagName and querySelectorAll",
        "difficulty": "Medium",
        "explanation": "Both methods return collections that can be counted using the length property."
    },
    # The DOM: Attributes
    {
        "question": "How do you get an element's attribute value?",
        "options": ["element.getAttribute('name')", "element.attribute('name')", "element.name", "element.attributes['name']"],
        "answer": "element.getAttribute('name')",
        "difficulty": "Easy",
        "explanation": "getAttribute('name') retrieves the value of the specified attribute."
    },
    # The DOM: Attribute Names and Values
    {
        "question": "How do you get all attributes of an element?",
        "options": ["element.attributes", "element.getAttributes()", "element.attributeList", "element.getAttributeNames()"],
        "answer": "element.attributes",
        "difficulty": "Medium",
        "explanation": "The attributes property returns a NamedNodeMap of an element's attributes."
    },
    # The DOM: Adding Nodes
    {
        "question": """How do you create a new element in the DOM? ```javascript
document.createElement('div')
```""",
        "options": ["createElement", "createNode", "newElement", "appendElement"],
        "answer": "createElement",
        "difficulty": "Easy",
        "explanation": "document.createElement creates a new DOM element with the specified tag name."
    },
    # The DOM: Inserting Nodes
    {
        "question": """How do you insert a node before another node? ```javascript
parentNode.insertBefore(newNode, referenceNode);
```""",
        "options": ["insertBefore", "appendChild", "insertAfter", "prepend"],
        "answer": "insertBefore",
        "difficulty": "Medium",
        "explanation": "insertBefore inserts a new node before a specified reference node."
    },
    # Objects
    {
        "question": "How do you create an object in JavaScript?",
        "options": ["let obj = {}", "let obj = new Object()", "let obj = Object.create()", "All of the above"],
        "answer": "All of the above",
        "difficulty": "Easy",
        "explanation": "Objects can be created using object literals, new Object(), or Object.create()."
    },
    # Objects: Properties
    {
        "question": """How do you add a property to an object? ```javascript
obj.name = 'John';
```""",
        "options": ["obj.name = 'John'", "obj.setProperty('name', 'John')", "obj.add('name', 'John')", "obj['name'] = 'John'"],
        "answer": "obj.name = 'John'",
        "difficulty": "Easy",
        "explanation": "Properties can be added using dot notation or bracket notation."
    },
    # Browser Control: Getting and Setting the URL
    {
        "question": "How do you get the current URL in JavaScript?",
        "options": ["window.location.href", "document.URL", "window.href", "Both window.location.href and document.URL"],
        "answer": "Both window.location.href and document.URL",
        "difficulty": "Medium",
        "explanation": "Both window.location.href and document.URL return the current page's URL."
    },
    # ... (add more questions to reach 100, following the same format)
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
        <p style="color: var(--text-color); font-size: 1.125rem;">Test your JavaScript skills with 100 questions on Variable Scoping, DOM, Objects, and more!</p>
        <p style="color: #b0b0d0;">60 minutes, 2 points per correct answer, 0.5 bonus for streaks ≥3. Ready?</p>
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

                # Split question into text and code
                if "```javascript" in q["question"]:
                    question_parts = q["question"].split("```javascript
                    question_text = question_parts[0].strip() if question_parts else q["question"]
                    code_snippet = ""
                    if len(question_parts) > 1:
                        code_parts = question_parts[1].split("```")
                        code_snippet = code_parts[0].strip() if code_parts else ""
                    st.markdown(f"### Question {current_q + 1}")
                    st.markdown(f"**{question_text}**")
                    if code_snippet:
                        st.code(code_snippet, language="javascript")
                else:
                    st.markdown(f"### Question {current_q + 1}")
                    st.markdown(f"**{q['question']}**")

                # Option buttons
                for i, option in enumerate(q["display_options"]):
                    button_class = ""
                    if st.session_state.selected_option == option:
                        button_class = "selected-correct" if option == q["labeled_answer"] else "selected-wrong"
                    button_key = f"q_{q['id']}_{i}"
                    if st.button(
                        option,
                        key=button_key,
                        disabled=st.session_state.selected_option is not None or st.session_state.paused,
                        help=f"Select option {i + 1}"
                    ):
                        is_correct = option == q["labeled_answer"]
                        st.session_state.selected_option = option
                        st.session_state.feedback = {
                            "is_correct": is_correct,
                            "correct_answer": q["labeled_answer"],
                            "explanation": q["explanation"]
                        }
                        st.session_state.answers[current_q] = {
                            "question": q["question"],
                            "user_answer": option,
                            "correct_answer": q["labeled_answer"],
                            "is_correct": is_correct,
                            "difficulty": q["difficulty"]
                        }
                        if is_correct:
                            st.session_state.score += 2
                            st.session_state.streak += 1
                            if st.session_state.streak > st.session_state.max_streak:
                                st.session_state.max_streak = st.session_state.streak
                            if st.session_state.streak >= 3:
                                st.session_state.score += 0.5
                        else:
                            st.session_state.streak = 0
                        if current_q < total_questions - 1:
                            st.session_state.current_q += 1
                            st.session_state.selected_option = None
                            st.session_state.feedback = None
                        else:
                            st.session_state.show_results = True
                        st.rerun()

                # Feedback
                if st.session_state.feedback:
                    if st.session_state.feedback["is_correct"]:
                        st.markdown('<div class="feedback-correct">✅ Correct!</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="feedback-wrong">❌ Wrong: {st.session_state.feedback["correct_answer"]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<div style="color: var(--text-color); font-size: 0.875rem;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

        else:
            # Results
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 3600) if st.session_state.start_time else 3600
            total_possible_score = len(quiz) * 2
            accuracy = (st.session_state.score / total_possible_score) * 100 if total_possible_score > 0 else 0
            st.markdown('<div class="question-container" role="region" aria-label="Results">', unsafe_allow_html=True)
            st.markdown(f'<h2 style="color: #34c759; text-align: center;">🏆 Score: {st.session_state.score}/{total_possible_score}</h2>', unsafe_allow_html=True)
            st.markdown(f"""
            <h3>📊 Results</h3>
            <div style="color: var(--text-color); font-size: 0.9375rem;">
                - ⏱️ Time: {int(time_taken) // 60}m {int(time_taken) % 60}s<br>
                - 🎯 Accuracy: {accuracy:.1f}%<br>
                - ✅ Correct: {sum(1 for ans in st.session_state.answers if ans and ans["is_correct"])}<br>
                - ❌ Incorrect: {sum(1 for ans in st.session_state.answers if ans and not ans["is_correct"])}<br>
                - 🔥 Max Streak: {st.session_state.max_streak}
            </div>
            """, unsafe_allow_html=True)

            # Confetti for high score
            if accuracy > 80:
                st.markdown("""
                <script>
                    if (typeof confetti === 'function') {
                        confetti({
                            particleCount: 100,
                            spread: 70,
                            origin: { y: 0.6 }
                        });
                    }
                </script>
                """, unsafe_allow_html=True)

            # Review Answers
            st.markdown('<h3>📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})"
                    st.markdown(f"""
                    <div style="color: var(--text-color); margin-bottom: 0.625rem;">
                        Question {i+1}: {ans["question"]}<br>
                        Your Answer: {ans["user_answer"]}<br>
                        {status}<br>
                        Explanation: {quiz[i]["explanation"]}
                    </div>
                    """, unsafe_allow_html=True)

            # Play Again button
            if st.button("🔄 Play Again", key=f"play_again_{uuid.uuid4()}"):
                reset_quiz()
                st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

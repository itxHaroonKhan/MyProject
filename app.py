import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Quiz data (unchanged, assuming it's correct)
quiz = [
    {
        "question": "What is the output of: ```javascript\nfunction test() { var x = 1; if (true) { var x = 2; } return x; }\nconsole.log(test());```",
        "options": ["2", "1", "undefined", "ReferenceError"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "The 'var' keyword is function-scoped, so the inner 'var x = 2' reassigns the same variable, returning 2."
    },
    # ... (other quiz questions unchanged for brevity; ensure all questions are included)
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
        # Resume: adjust start_time to account for pause duration
        pause_duration = (datetime.now() - st.session_state.pause_time).total_seconds()
        st.session_state.start_time = st.session_state.start_time + timedelta(seconds=pause_duration)
        st.session_state.paused = False
    else:
        # Pause
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
        current_q = min(st.session_state.current_q, total_questions - 1)  # Prevent index out of range
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
                    question_text = question_parts[0].strip()
                    code_snippet = question_parts[1].split("```")[0].strip() if len(question_parts) > 1 else ""
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
                        help=f"Select option {i + 1}",
                        args=(button_class,)
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
                        # Move to next question or show results
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


import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Quiz data - Reduced for stability
quiz = [
    {
        "question": "What is the output of: ```typescript\nlet x: number = 10; console.log(x * 2);```",
        "options": ["20", "10", "Error", "undefined"],
        "answer": "20",
        "difficulty": "Easy",
        "explanation": "The variable 'x' is typed as a number, so 'x * 2' computes 20.",
        "category": "TypeScript"
    },
    {
        "question": "What does TypeScript provide over JavaScript?",
        "options": ["Static typing", "Runtime execution", "Module bundling", "Code minification"],
        "answer": "Static typing",
        "difficulty": "Easy",
        "explanation": "TypeScript adds static typing to JavaScript, enabling type checking at compile time.",
        "category": "TypeScript"
    },
    # Add more questions as needed, but start with fewer for testing
]

# Simplified CSS
st.markdown("""
<style>
.main-container {
    padding: 2rem;
    border-radius: 1rem;
    margin: 1rem auto;
    max-width: 900px;
}

.title {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 1rem;
    font-weight: bold;
}

.stButton>button {
    background: #6b21a8;
    color: white;
    border: none;
    border-radius: 0.75rem;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 600;
    margin: 0.5rem 0;
    width: 100%;
}

.stButton>button:hover {
    background: #8b5cf6;
}

.progress-bar {
    background: rgba(0,0,0,0.1);
    border-radius: 0.5rem;
    height: 0.75rem;
    margin: 0.5rem 0;
    overflow: hidden;
}

.progress-fill {
    background: linear-gradient(90deg, #6b21a8, #007aff);
    height: 100%;
    border-radius: 0.5rem;
    transition: width 0.3s ease;
}

.feedback-correct {
    background: rgba(52, 199, 89, 0.2);
    border: 2px solid #34c759;
    color: #34c759;
    padding: 1rem;
    border-radius: 0.5rem;
    margin: 1rem 0;
}

.feedback-wrong {
    background: rgba(255, 59, 48, 0.2);
    border: 2px solid #ff3b30;
    color: #ff3b30;
    padding: 1rem;
    border-radius: 0.5rem;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
def initialize_session_state():
    default_state = {
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
        "pause_time": None,
        "quiz_duration": 3600
    }
    
    for key, value in default_state.items():
        if key not in st.session_state:
            st.session_state[key] = value

def shuffle_quiz(_quiz):
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.shuffle(q["display_options"])
        q["labeled_answer"] = q["answer"]
    return shuffled

def update_timer():
    if (not st.session_state.paused and st.session_state.start_time and 
        st.session_state.started and not st.session_state.show_results):
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        st.session_state.time_left = max(st.session_state.quiz_duration - elapsed, 0)
        if st.session_state.time_left <= 0:
            st.session_state.show_results = True

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

# Main application
def main():
    initialize_session_state()
    
    st.markdown('<h1 class="title">🚀 TypeScript Quiz</h1>', unsafe_allow_html=True)
    
    # Welcome screen
    if not st.session_state.started:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h2>📋 Quiz Overview</h2>
            <p><strong>TypeScript Knowledge Test</strong></p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🎯 Start Quiz", use_container_width=True):
            st.session_state.started = True
            st.session_state.start_time = datetime.now()
            st.rerun()
    else:
        # Timer and progress
        if not st.session_state.show_results:
            update_timer()
            
            # Timer display
            minutes = int(st.session_state.time_left // 60)
            seconds = int(st.session_state.time_left % 60)
            st.markdown(f'<div style="text-align: center; font-size: 1.5rem; font-weight: bold; margin: 1rem 0;">⏱️ {minutes:02d}:{seconds:02d}</div>', unsafe_allow_html=True)
        
        # Progress section
        total_questions = len(st.session_state.quiz_data)
        current_q = min(st.session_state.current_q, total_questions - 1)
        progress = ((current_q + 1) / total_questions) * 100
        
        st.markdown(f"""
        <div style="margin: 1rem 0;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span>Question {current_q + 1} of {total_questions}</span>
                <span>Score: {st.session_state.score}</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress}%"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.show_results:
            # Question display
            q = st.session_state.quiz_data[current_q]
            
            st.markdown(f"""
            <div style="background: rgba(0,0,0,0.05); padding: 1.5rem; border-radius: 0.75rem; margin: 1rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                    <span style="background: #6b21a8; color: white; padding: 0.25rem 0.75rem; border-radius: 1rem; font-size: 0.8rem;">{q['difficulty']}</span>
                    <span style="background: #007aff; color: white; padding: 0.25rem 0.75rem; border-radius: 1rem; font-size: 0.8rem;">{q['category']}</span>
                </div>
                {q['question']}
            </div>
            """, unsafe_allow_html=True)
            
            # Options
            for option in q["display_options"]:
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
                feedback_class = "feedback-correct" if st.session_state.feedback["type"] == "correct" else "feedback-wrong"
                st.markdown(f'<div class="{feedback_class}">{st.session_state.feedback["message"]}</div>', unsafe_allow_html=True)
            
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
                
            # Add restart button
            if st.button("🔄 Restart Quiz", use_container_width=True):
                reset_quiz()
                st.rerun()
        else:
            # Results screen
            st.markdown(f"""
            <div style="text-align: center; padding: 2rem;">
                <h2>🎉 Quiz Completed!</h2>
                <div style="font-size: 3rem; font-weight: bold; color: #6b21a8; margin: 1rem 0;">
                    {st.session_state.score}/{(total_questions * 2)}
                </div>
                <p>Maximum Streak: 🔥 {st.session_state.max_streak}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🔄 Take Quiz Again", use_container_width=True):
                reset_quiz()
                st.rerun()

if __name__ == "__main__":
    main()

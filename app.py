import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Set page config
st.set_page_config(page_title="TypeScript Quiz - 100 Questions", page_icon="🟦", layout="centered")

# Quiz data (your full 100 questions)
quiz = [
    # ... (paste your full quiz list here - I'll show the structure, you already have it)
    # For brevity, I'm showing only the first and last, but YOU MUST INCLUDE ALL 100
    {
        "question": "What is TypeScript?",
        "options": [
            "A superset of JavaScript that adds static typing",
            "A new programming language unrelated to JavaScript",
            "A JavaScript framework for building UIs",
            "A database query language"
        ],
        "answer": "A superset of JavaScript that adds static typing",
        "difficulty": "Easy",
        "explanation": "TypeScript is a superset of JavaScript that compiles to plain JavaScript and adds optional static typing.",
        "category": "TypeScript Basics"
    },
    # ... ALL OTHER 99 QUESTIONS GO HERE ...
    {
        "question": "What does the 'target' option specify?",
        "options": [
            "The JavaScript version the TypeScript code is compiled to",
            "The target directory for compiled files",
            "The target browser",
            "The target platform"
        ],
        "answer": "The JavaScript version the TypeScript code is compiled to",
        "difficulty": "Easy",
        "explanation": "The 'target' in tsconfig.json specifies the ECMAScript version to compile to (e.g., ES5, ES6, ES2020).",
        "category": "Configuration"
    }
]

# Ensure exactly 100 questions
assert len(quiz) == 100, f"Expected 100 questions, got {len(quiz)}"

# Initialize session state
if 'quiz_state' not in st.session_state:
    st.session_state.quiz_state = {
        'quiz_id': str(uuid.uuid4()),
        'start_time': None,
        'current_question': 0,
        'score': 0,
        'answers': [],
        'shuffled_questions': random.sample(quiz, len(quiz)),
        'show_results': False,
        'selected_option': None,
        'submitted': False,
        'time_limit': 60 * 60  # 60 minutes total
    }

state = st.session_state.quiz_state

# CSS Styling
st.markdown("""
<style>
    .big-font { font-size: 24px !important; font-weight: bold; }
    .question-box { 
        padding: 20px; 
        border-radius: 15px; 
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .option-btn {
        width: 100%;
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        font-size: 16px;
        text-align: left;
        border: 2px solid #ddd;
        transition: all 0.3s;
    }
    .option-btn:hover { border-color: #667eea; background: #f0f2ff; }
    .correct { background-color: #d4edda; border-color: #c3e6cb; color: #155724; }
    .incorrect { background-color: #f8d7da; border-color: #f5c6cb; color: #721c24; }
    .progress-bar { height: 30px; border-radius: 15px; }
    .stProgress > div > div > div > div { background-color: #667eea; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #2E86AB;'>🟦 TypeScript Mastery Quiz</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>100 Questions • 60 Minutes • All Topics</p>", unsafe_allow_html=True)

# Start Quiz
if not state['start_time']:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Start Quiz", use_container_width=True, type="primary"):
            state['start_time'] = datetime.now()
            st.rerun()

    st.markdown("### Topics Covered:")
    topics = list(set(q["category"] for q in quiz))
    cols = st.columns(3)
    for i, topic in enumerate(topics):
        cols[i % 3].markdown(f"• **{topic}**")

    st.info("💡 You can skip questions and return later. Timer runs continuously.")
    st.stop()

# Timer Logic
if state['start_time']:
    elapsed = (datetime.now() - state['start_time']).total_seconds()
    remaining = max(0, state['time_limit'] - elapsed)
    minutes = int(remaining // 60)
    seconds = int(remaining % 60)

    if remaining <= 0:
        state['show_results'] = True
        st.rerun()

    # Progress bar
    progress = (state['current_question'] + 1) / len(quiz)
    st.progress(progress, text=f"Question {state['current_question'] + 1}/100")

    # Timer display
    st.markdown(f"""
    <div style='text-align: center; padding: 10px; background: #ff6b6b; color: white; border-radius: 10px; font-size: 20px; font-weight: bold;'>
        ⏱️ Time Remaining: {minutes:02d}:{seconds:02d}
    </div>
    """, unsafe_allow_html=True)

# Current Question
if not state['show_results']:
    q = state['shuffled_questions'][state['current_question']]
    
    st.markdown(f"""
    <div class='question-box'>
        <div class='big-font'>Question {state['current_question'] + 1}</div>
        <div style='margin: 15px 0; font-size: 18px;'>
            <strong>Category:</strong> {q['category']} | <strong>Difficulty:</strong> {q['difficulty']}
        </div>
        <hr style='border: 1px solid rgba(255,255,255,0.3);'>
        <p style='font-size: 22px; margin: 20px 0;'>{q['question']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Store selected option
    if f"q_{state['current_question']}" not in st.session_state:
        st.session_state[f"q_{state['current_question']}"] = None

    selected = st.session_state[f"q_{state['current_question']}"]

    for i, option in enumerate(q['options']):
        key = f"option_{state['current_question']}_{i}"
        cols = st.columns([4, 1])
        
        with cols[0]:
            if st.button(
                option,
                key=key,
                use_container_width=True,
                disabled=state.get('submitted', False)
            ):
                st.session_state[f"q_{state['current_question']}"] = option
                selected = option
                st.rerun()

        with cols[1]:
            if selected == option:
                st.markdown("✅")

    # Show feedback if submitted
    if state.get('submitted', False):
        user_answer = state['answers'][-1]['user_answer']
        correct = user_answer == q['answer']
        
        if correct:
            st.success(f"🎉 Correct! +1 point")
        else:
            st.error(f"❌ Incorrect. The answer is: **{q['answer']}**")

        with st.expander("📖 Explanation"):
            st.write(q['explanation'])

    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        if st.button("⬅️ Previous", disabled=state['current_question'] == 0):
            if state.get('submitted', False):
                state['answers'].pop()
            state['current_question'] -= 1
            state['submitted'] = False
            st.rerun()

    with col2:
        if not state.get('submitted', False):
            if selected:
                if st.button("✅ Submit Answer", use_container_width=True, type="primary"):
                    state['answers'].append({
                        'question_index': state['current_question'],
                        'user_answer': selected,
                        'correct': selected == q['answer']
                    })
                    if selected == q['answer']:
                        state['score'] += 1
                    state['submitted'] = True
                    st.rerun()
            else:
                st.warning("Please select an answer before submitting.")
        else:
            if st.button("➡️ Next Question", use_container_width=True):
                state['current_question'] += 1
                state['submitted'] = False
                st.rerun()

    with col3:
        if st.button("🏁 Finish Quiz", type="secondary"):
            if len(state['answers']) < len(quiz):
                if st.warning("You haven't answered all questions. Finish anyway?"):
                    state['show_results'] = True
                    st.rerun()
            else:
                state['show_results'] = True
                st.rerun()

# Results Page
if state['show_results']:
    st.balloons()
    st.markdown("<h2 style='text-align: center;'>🎊 Quiz Complete! 🎊</h2>", unsafe_allow_html=True)
    
    score = state['score']
    percentage = (score / len(quiz)) * 100
    
    st.markdown(f"""
    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 20px; margin: 20px 0;'>
        <h1>{score}/100</h1>
        <h3>{percentage:.1f}% Correct</h3>
        <p>Time taken: {timedelta(seconds=int((datetime.now() - state['start_time']).total_seconds()))}</p>
    </div>
    """, unsafe_allow_html=True)

    # Performance by category
    category_stats = {}
    for ans in state['answers']:
        q_idx = ans['question_index']
        q = state['shuffled_questions'][q_idx]
        cat = q['category']
        if cat not in category_stats:
            category_stats[cat] = {'correct': 0, 'total': 0}
        category_stats[cat]['total'] += 1
        if ans['correct']:
            category_stats[cat]['correct'] += 1

    st.markdown("### 📊 Performance by Category")
    for cat, stats in category_stats.items():
        pct = (stats['correct'] / stats['total']) * 100
        st.markdown(f"**{cat}**: {stats['correct']}/{stats['total']} ({pct:.0f}%)")

    # Show incorrect answers
    incorrect = [a for a in state['answers'] if not a['correct']]
    if incorrect:
        st.markdown("### ❌ Review Incorrect Answers")
        for ans in incorrect:
            q = state['shuffled_questions'][ans['question_index']]
            with st.expander(f"Q{ans['question_index'] + 1}: {q['question'][:60]}..."):
                st.write(f"**Your answer:** {ans['user_answer']}")
                st.write(f"**Correct answer:** {q['answer']}")
                st.info(q['explanation'])

    # Restart
    if st.button("🔄 Take Quiz Again", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>Made with ❤️ using Streamlit | TypeScript Quiz v1.0</p>", unsafe_allow_html=True)

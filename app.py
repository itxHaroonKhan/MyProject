import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Set page config
st.set_page_config(page_title="TypeScript Quiz - 100 Questions", page_icon="🟦", layout="centered")

# Quiz data (your full 100 questions)
quiz = [
    # Type Annotations (10)
    {"question": "Which is a valid type annotation for a function returning void?", "options": ["(): void", "function(): void", "() => void", "function => void"], "answer": "() => void", "explanation": "Arrow functions use `=> void` for return type.", "category": "Type Annotations"},
    {"question": "How do you annotate a parameter that can be null or undefined?", "options": ["x: any", "x?: string", "x: string | null", "x: string!"], "answer": "x: string | null", "explanation": "Use union with `null` or `undefined`.", "category": "Type Annotations"},
    {"question": "What does `!` mean in `user!.name`?", "options": ["Optional chaining", "Non-null assertion", "Definite assignment", "Type guard"], "answer": "Non-null assertion", "explanation": "Tells compiler: 'I know this is not null'.", "category": "Type Annotations"},
    {"question": "Which is NOT a primitive type?", "options": ["string", "number", "object", "boolean"], "answer": "object", "explanation": "`object` is not primitive; primitives are string, number, boolean, etc.", "category": "Type Annotations"},
    {"question": "How to annotate a function that never returns?", "options": ["(): void", "(): never", "(): undefined", "(): null"], "answer": "(): never", "explanation": "`never` means function throws or loops forever.", "category": "Type Annotations"},
    {"question": "What is `unknown` type?", "options": ["Like any but safer", "Only for objects", "Top type", "Bottom type"], "answer": "Like any but safer", "explanation": "Must narrow `unknown` before use.", "category": "Type Annotations"},
    {"question": "Can you annotate array as `string[]`?", "options": ["Yes", "No", "Only in ES6", "Only with generics"], "answer": "Yes", "explanation": "`string[]` and `Array<string>` both work.", "category": "Type Annotations"},
    {"question": "What is `readonly` modifier?", "options": ["Prevents reassignment", "Prevents reading", "Runtime check", "Compiler error only"], "answer": "Prevents reassignment", "explanation": "Compiler blocks mutation of readonly properties.", "category": "Type Annotations"},
    {"question": "How to annotate a tuple?", "options": ["[string, number]", "{0: string, 1: number}", "Tuple<string, number>", "string | number[]"], "answer": "[string, number]", "explanation": "Fixed-length arrays use tuple syntax.", "category": "Type Annotations"},
    {"question": "What is `as const`?", "options": ["Makes object readonly & literal", "Casts to any", "Enables strict mode", "Runtime assertion"], "answer": "Makes object readonly & literal", "explanation": "Preserves literal types.", "category": "Type Annotations"},

    # Interfaces (10)
    {"question": "Can interfaces be merged?", "options": ["Yes", "No", "Only in same file", "Only with classes"], "answer": "Yes", "explanation": "Declaration merging combines same-name interfaces.", "category": "Interfaces"},
    {"question": "What is an index signature?", "options": ["[key: string]: string", "[index: number]: any", "Both", "Neither"], "answer": "Both", "explanation": "Allows dynamic keys.", "category": "Interfaces"},
    {"question": "Can interface extend a class?", "options": ["Yes", "No", "Only abstract", "Only with implements"], "answer": "Yes", "explanation": "Extracts public/protected members.", "category": "Interfaces"},
    {"question": "What does `implements` do?", "options": ["Checks class conforms to interface", "Inherits methods", "Creates instance", "Copies properties"], "answer": "Checks class conforms to interface", "explanation": "Enforces structure.", "category": "Interfaces"},
    {"question": "Can interface have private members?", "options": ["No", "Yes", "Only readonly", "Only static"], "answer": "No", "explanation": "Interfaces describe public shape.", "category": "Interfaces"},
    {"question": "How to make property optional?", "options": ["name?: string", "name: string?", "optional name: string", "?name: string"], "answer": "name?: string", "explanation": "Question mark after name.", "category": "Interfaces"},
    {"question": "Can interface describe a function?", "options": ["Yes", "No", "Only arrow", "Only class"], "answer": "Yes", "explanation": "Call signatures allowed.", "category": "Interfaces"},
    {"question": "What is a hybrid type?", "options": ["Function + object", "Class + interface", "Union + intersection", "Generic + conditional"], "answer": "Function + object", "explanation": "Like jQuery: callable and has properties.", "category": "Interfaces"},
    {"question": "Can interface extend multiple interfaces?", "options": ["Yes", "No", "Only two", "Only with &"], "answer": "Yes", "explanation": "`extends A, B` is valid.", "category": "Interfaces"},
    {"question": "What is `interface A extends B, C {}`?", "options": ["Intersection", "Union", "Merge", "Error"], "answer": "Intersection", "explanation": "Must satisfy both B and C.", "category": "Interfaces"},

    # Classes (10)
    {"question": "What does `private` mean?", "options": ["Accessible only in class", "In subclasses too", "Public", "Static"], "answer": "Accessible only in class", "explanation": "Not even in subclasses.", "category": "Classes"},
    {"question": "What is `protected`?", "options": ["Class + subclasses", "Only class", "Public", "Static"], "answer": "Class + subclasses", "explanation": "Inheritance access.", "category": "Classes"},
    {"question": "Can constructor be async?", "options": ["No", "Yes", "Only in ESNext", "Only with decorators"], "answer": "No", "explanation": "Constructors cannot be async.", "category": "Classes"},
    {"question": "What are parameter properties?", "options": ["public name: string in constructor", "name: string in body", "this.name = name", "All of the above"], "answer": "public name: string in constructor", "explanation": "Shorthand for field + assignment.", "category": "Classes"},
    {"question": "Can class have multiple constructors?", "options": ["No", "Yes, via overloading", "Yes, directly", "Only static"], "answer": "Yes, via overloading", "explanation": "Signature overloads, one body.", "category": "Classes"},
    {"question": "What is `abstract` class?", "options": ["Cannot be instantiated", "Can be instantiated", "No methods", "No properties"], "answer": "Cannot be instantiated", "explanation": "Base class only.", "category": "Classes"},
    {"question": "What is `static`?", "options": ["Belongs to class", "Belongs to instance", "Readonly", "Private"], "answer": "Belongs to class", "explanation": "ClassName.prop", "category": "Classes"},
    {"question": "Can `readonly` be used on methods?", "options": ["No", "Yes", "Only static", "Only private"], "answer": "No", "explanation": "Only on properties.", "category": "Classes"},
    {"question": "What is `super()`?", "options": ["Calls parent constructor", "Calls parent method", "Both", "Neither"], "answer": "Both", "explanation": "Depends on context.", "category": "Classes"},
    {"question": "Can class implement multiple interfaces?", "options": ["Yes", "No", "Only two", "Only with extends"], "answer": "Yes", "explanation": "`implements A, B`", "category": "Classes"},

    # Generics (10)
    {"question": "What is `<T>`?", "options": ["Type parameter", "HTML tag", "Template", "Tuple"], "answer": "Type parameter", "explanation": "Placeholder for type.", "category": "Generics"},
    {"question": "What does `extends` do in `<T extends string>`?", "options": ["Constraints T to string or subtype", "T must be string", "T can be any", "Error"], "answer": "Constraints T to string or subtype", "explanation": "Bounds the generic.", "category": "Generics"},
    {"question": "What is `keyof T`?", "options": ["Union of keys", "Values", "Length", "Type"], "answer": "Union of keys", "explanation": "String literal union of property names.", "category": "Generics"},
    {"question": "What is `typeof` in generics?", "options": ["Gets type of value", "Runtime type", "Compiler only", "Both"], "answer": "Gets type of value", "explanation": "Type query operator.", "category": "Generics"},
    {"question": "Can generics have default types?", "options": ["Yes", "No", "Only in functions", "Only in classes"], "answer": "Yes", "explanation": "`<T = string>`", "category": "Generics"},
    {"question": "What is conditional type?", "options": ["T extends U ? X : Y", "if/else", "Runtime", "Both"], "answer": "T extends U ? X : Y", "explanation": "Type-level ternary.", "category": "Generics"},
    {"question": "What is `infer`?", "options": ["Extracts type", "Creates type", "Loops", "Maps"], "answer": "Extracts type", "explanation": "Infers part of a type.", "category": "Generics"},
    {"question": "What is mapped type?", "options": ["{ [K in keyof T]: U }", "Array map", "Runtime", "Both"], "answer": "{ [K in keyof T]: U }", "explanation": "Transforms properties.", "category": "Generics"},
    {"question": "What is `Partial<T>`?", "options": ["Makes all props optional", "Removes props", "Adds props", "Clones"], "answer": "Makes all props optional", "explanation": "Utility type.", "category": "Generics"},
    {"question": "What is `ReturnType<T>`?", "options": ["Extracts function return type", "Parameter types", "Both", "Neither"], "answer": "Extracts function return type", "explanation": "Built-in utility.", "category": "Generics"},

    # Enums (10)
    {"question": "What is default enum start?", "options": ["0", "1", "undefined", "null"], "answer": "0", "explanation": "Numeric enums start at 0.", "category": "Enums"},
    {"question": "Can enum have string values?", "options": ["Yes", "No", "Only numeric", "Only const"], "answer": "Yes", "explanation": "String enums exist.", "category": "Enums"},
    {"question": "What is `const enum`?", "options": ["Inlined at compile time", "Preserved", "Runtime object", "Mutable"], "answer": "Inlined at compile time", "explanation": "No runtime code.", "category": "Enums"},
    {"question": "Can enum be reverse-mapped?", "options": ["Yes, for numeric", "Yes, for string", "Never", "Always"], "answer": "Yes, for numeric", "explanation": "Enum.Name and Enum[0] both work.", "category": "Enums"},
    {"question": "Are enums types or values?", "options": ["Both", "Only types", "Only values", "Neither"], "answer": "Both", "explanation": "Dual nature.", "category": "Enums"},
    {"question": "Can enum have computed members?", "options": ["Yes", "No", "Only strings", "Only numbers"], "answer": "Yes", "explanation": "But not in const enum.", "category": "Enums"},
    {"question": "What is `enum E { A = 1 << 0 }`?", "options": ["Bit flag", "String enum", "Const enum", "Error"], "answer": "Bit flag", "explanation": "Common for flags.", "category": "Enums"},
    {"question": "Can you loop over enum?", "options": ["Yes", "No", "Only numeric", "Only string"], "answer": "Yes", "explanation": "for...in or Object.keys.", "category": "Enums"},
    {"question": "Are string enums runtime objects?", "options": ["Yes", "No", "Only in dev", "Only in prod"], "answer": "Yes", "explanation": "Exist in JS output.", "category": "Enums"},
    {"question": "Can enum extend another?", "options": ["No", "Yes", "Only numeric", "Only string"], "answer": "No", "explanation": "No inheritance.", "category": "Enums"},

    # Type Inference (10)
    {"question": "What is inferred for `let x = 10`?", "options": ["number", "any", "10", "unknown"], "answer": "number", "explanation": "Literal narrows to type.", "category": "Type Inference"},
    {"question": "What is `const x = 10` inferred as?", "options": ["10", "number", "any", "literal"], "answer": "10", "explanation": "Const preserves literal.", "category": "Type Inference"},
    {"question": "Does `let x: number = 'hello'` compile?", "options": ["No", "Yes", "Only in JS", "With any"], "answer": "No", "explanation": "Type mismatch.", "category": "Type Inference"},
    {"question": "What is contextual typing?", "options": ["Type from usage context", "Manual annotation", "Runtime", "Both"], "answer": "Type from usage context", "explanation": "e.g., event handlers.", "category": "Type Inference"},
    {"question": "What is `best common type`?", "options": ["Widest compatible type", "Narrowest", "any", "unknown"], "answer": "Widest compatible type", "explanation": "For arrays of mixed types.", "category": "Type Inference"},
    {"question": "Can inference fail?", "options": ["Yes", "No", "Only in functions", "Only in classes"], "answer": "Yes", "explanation": "May fall back to any.", "category": "Type Inference"},
    {"question": "What is `as const` for?", "options": ["Preserve literals", "Widen types", "Narrow", "Cast"], "answer": "Preserve literals", "explanation": "Deep readonly literals.", "category": "Type Inference"},
    {"question": "What is inferred for `[]`?", "options": ["never[]", "any[]", "unknown[]", "object[]"], "answer": "never[]", "explanation": "Empty array has no type info.", "category": "Type Inference"},
    {"question": "Can return type be inferred?", "options": ["Yes", "No", "Only void", "Only any"], "answer": "Yes", "explanation": "From return statements.", "category": "Type Inference"},
    {"question": "What is `noImplicitAny`?", "options": ["Errors on inferred any", "Allows any", "Ignores any", "Runtime"], "answer": "Errors on inferred any", "explanation": "Strict mode flag.", "category": "Type Inference"},

    # Union & Intersection (10)
    {"question": "What is `string | number`?", "options": ["Union", "Intersection", "Tuple", "Enum"], "answer": "Union", "explanation": "Value is one or the other.", "category": "Union Types"},
    {"question": "What is `A & B`?", "options": ["Intersection", "Union", "Merge", "Both"], "answer": "Intersection", "explanation": "Must satisfy both.", "category": "Intersection Types"},
    {"question": "Can you access property on union?", "options": ["Only common props", "Any prop", "No props", "With casting"], "answer": "Only common props", "explanation": "Type narrowing required.", "category": "Union Types"},
    {"question": "What is discriminated union?", "options": ["Union with tag property", "Any union", "Intersection", "Enum"], "answer": "Union with tag property", "explanation": "e.g., { kind: 'square' }", "category": "Union Types"},
    {"question": "What is `never` in unions?", "options": ["Eliminates impossible branches", "Always included", "Error", "Any"], "answer": "Eliminates impossible branches", "explanation": "Exhaustive checks.", "category": "Union Types"},
    {"question": "Can intersection have conflicting types?", "options": ["Becomes never", "Allowed", "Merged", "Error"], "answer": "Becomes never", "explanation": "e.g., string & number", "category": "Intersection Types"},
    {"question": "What is `A extends B ? C : D`?", "options": ["Conditional type", "Union", "Intersection", "Guard"], "answer": "Conditional type", "explanation": "Type-level if.", "category": "Union Types"},
    {"question": "Can union be used in generics?", "options": ["Yes", "No", "Only string", "Only number"], "answer": "Yes", "explanation": "Distributive.", "category": "Union Types"},
    {"question": "What is distributive conditional?", "options": ["Applies to each union member", "Once to whole", "Error", "Runtime"], "answer": "Applies to each union member", "explanation": "Default behavior.", "category": "Union Types"},
    {"question": "What is `Extract<T, U>`?", "options": ["Subset of T assignable to U", "All of T", "None", "Union"], "answer": "Subset of T assignable to U", "explanation": "Utility type.", "category": "Union Types"},

    # Type Guards (10)
    {"question": "What is `typeof x === 'string'`?", "options": ["Type guard", "Runtime check", "Both", "Neither"], "answer": "Both", "explanation": "Narrows type.", "category": "Type Guards"},
    {"question": "What is `x is string`?", "options": ["User-defined type guard", "Built-in", "Runtime", "Error"], "answer": "User-defined type guard", "explanation": "Return type predicate.", "category": "Type Guards"},
    {"question": "What is `in` operator guard?", "options": ["'name' in obj", "'name' in string", "Both", "Neither"], "answer": "'name' in obj", "explanation": "Checks property existence.", "category": "Type Guards"},
    {"question": "What is `instanceof`?", "options": ["Class check", "Type check", "Both", "Neither"], "answer": "Class check", "explanation": "Runtime constructor.", "category": "Type Guards"},
    {"question": "Can type guard narrow union?", "options": ["Yes", "No", "Only string", "Only number"], "answer": "Yes", "explanation": "Core feature.", "category": "Type Guards"},
    {"question": "What is exhaustive check?", "options": ["default: never", "if/else", "switch", "All"], "answer": "default: never", "explanation": "Catches missing cases.", "category": "Type Guards"},
    {"question": "Can type guard be async?", "options": ["No", "Yes", "Only in TS 4", "Only with await"], "answer": "No", "explanation": "Must be sync.", "category": "Type Guards"},
    {"question": "What is assertion function?", "options": ["asserts condition", "throws", "Both", "Neither"], "answer": "asserts condition", "explanation": "Narrows after call.", "category": "Type Guards"},
    {"question": "What is `x!`?", "options": ["Non-null assertion", "Type guard", "Both", "Neither"], "answer": "Non-null assertion", "explanation": "Not a guard.", "category": "Type Guards"},
    {"question": "Can type guard narrow generics?", "options": ["Yes", "No", "Only in functions", "Only in classes"], "answer": "Yes", "explanation": "With constraints.", "category": "Type Guards"},

    # Decorators (10)
    {"question": "Are decorators stable?", "options": ["Stage 3", "Stable", "Experimental", "Removed"], "answer": "Stage 3", "explanation": "Need `--experimentalDecorators`.", "category": "Decorators"},
    {"question": "What is `@log`?", "options": ["Method decorator", "Class", "Property", "Parameter"], "answer": "Method decorator", "explanation": "Wraps method.", "category": "Decorators"},
    {"question": "Can decorator be on parameter?", "options": ["Yes", "No", "Only class", "Only method"], "answer": "Yes", "explanation": "Rarely used.", "category": "Decorators"},
    {"question": "What is decorator factory?", "options": ["Function returning decorator", "Decorator itself", "Class", "Interface"], "answer": "Function returning decorator", "explanation": "e.g., `@debounce(100)`", "category": "Decorators"},
    {"question": "What is first arg to method decorator?", "options": ["target", "propertyKey", "descriptor", "All"], "answer": "All", "explanation": "Standard signature.", "category": "Decorators"},
    {"question": "Can decorator modify property?", "options": ["Yes", "No", "Only methods", "Only classes"], "answer": "Yes", "explanation": "Via descriptor.", "category": "Decorators"},
    {"question": "What is `@Component` in Angular?", "options": ["Class decorator", "Method", "Property", "Parameter"], "answer": "Class decorator", "explanation": "Defines component.", "category": "Decorators"},
    {"question": "Are decorators runtime or compile?", "options": ["Runtime", "Compile only", "Both", "Neither"], "answer": "Runtime", "explanation": "Exist in JS.", "category": "Decorators"},
    {"question": "Can decorator throw?", "options": ["Yes", "No", "Only in dev", "Only in prod"], "answer": "Yes", "explanation": "Affects runtime.", "category": "Decorators"},
    {"question": "What is metadata?", "options": ["reflect-metadata", "Built-in", "TypeScript", "Both"], "answer": "reflect-metadata", "explanation": "Separate package.", "category": "Decorators"},
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

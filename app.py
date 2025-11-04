import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Set page config
st.set_page_config(page_title="TypeScript Quiz - 100 Questions", page_icon="🟦", layout="centered")

# Quiz data (your full 100 questions)
quiz =[
  {
    "question": "What does the 'target' option specify in tsconfig.json?",
    "options": [
      "The JavaScript version the TypeScript code is compiled to",
      "The target directory for compiled files",
      "The target browser",
      "The target platform"
    ],
    "answer": "The JavaScript version the TypeScript code is compiled to",
    "difficulty": "Easy",
    "explanation": "The 'target' in tsconfig.json specifies the ECMAScript version to compile to (e.g., ES5, ES6, ES2020).",
    "category": "TS Compiler"
  },
  {
    "question": "Which flag enables strict type-checking?",
    "options": ["strict", "noImplicitAny", "strictNullChecks", "alwaysStrict"],
    "answer": "strict",
    "difficulty": "Easy",
    "explanation": "'strict: true' turns on all strict family options.",
    "category": "TS Compiler"
  },
  {
    "question": "What does 'outDir' control?",
    "options": [
      "Directory where .js files are emitted",
      "Directory for source .ts files",
      "Directory for declaration files",
      "Directory for map files"
    ],
    "answer": "Directory where .js files are emitted",
    "difficulty": "Easy",
    "explanation": "'outDir' specifies the output folder for compiled JavaScript files.",
    "category": "TS Compiler"
  },
  {
    "question": "Which option generates .d.ts files?",
    "options": ["declaration", "emitDeclarationOnly", "declarationMap", "sourceMap"],
    "answer": "declaration",
    "difficulty": "Easy",
    "explanation": "Set 'declaration: true' to emit type declaration files.",
    "category": "TS Compiler"
  },
  {
    "question": "What is the default value of 'module' for modern projects?",
    "options": ["CommonJS", "ESNext", "AMD", "System"],
    "answer": "ESNext",
    "difficulty": "Easy",
    "explanation": "When 'target' is ES2015+, default module is 'ESNext'.",
    "category": "TS Compiler"
  },
  {
    "question": "Which flag skips type checking of declaration files?",
    "options": ["skipLibCheck", "skipDefaultLibCheck", "noLib", "fastCheck"],
    "answer": "skipLibCheck",
    "difficulty": "Easy",
    "explanation": "'skipLibCheck: true' speeds up compilation.",
    "category": "TS Compiler"
  },
  {
    "question": "What does 'noEmitOnError' do?",
    "options": [
      "Prevents .js output if there are type errors",
      "Deletes previous output on error",
      "Emits only on zero errors",
      "Emits only declaration files on error"
    ],
    "answer": "Prevents .js output if there are type errors",
    "difficulty": "Easy",
    "explanation": "No JavaScript emitted on type errors.",
    "category": "TS Compiler"
  },
  {
    "question": "Which option enables source maps?",
    "options": ["sourceMap", "inlineSourceMap", "mapRoot", "sourceRoot"],
    "answer": "sourceMap",
    "difficulty": "Easy",
    "explanation": "'sourceMap: true' generates .map files.",
    "category": "TS Compiler"
  },
  {
    "question": "What is the purpose of 'rootDir'?",
    "options": [
      "Defines the root folder for input files",
      "Defines the root folder for output",
      "Sets the project root for tsconfig",
      "Sets the root for node_modules"
    ],
    "answer": "Defines the root folder for input files",
    "difficulty": "Easy",
    "explanation": "Mirrors input structure in outDir.",
    "category": "TS Compiler"
  },
  {
    "question": "Which flag allows JavaScript files in the project?",
    "options": ["allowJs", "checkJs", "emitJs", "includeJs"],
    "answer": "allowJs",
    "difficulty": "Easy",
    "explanation": "'allowJs: true' enables .js imports.",
    "category": "TS Compiler"
  },

  // Type Annotations (10)
  {
    "question": "How do you annotate a variable as string?",
    "options": ["let name: String", "let name: string", "let name = String", "let name: 'string'"],
    "answer": "let name: string",
    "difficulty": "Easy",
    "explanation": "Use lowercase primitive types.",
    "category": "Type Annotations"
  },
  {
    "question": "Correct array type annotation?",
    "options": ["number[]", "Array<number>", "Both", "Neither"],
    "answer": "Both",
    "difficulty": "Easy",
    "explanation": "Both syntaxes are equivalent.",
    "category": "Type Annotations"
  },
  {
    "question": "How to type a function parameter?",
    "options": ["(x: number) => {}", "(x) => number {}", "function(x: number)", "function x(number)"],
    "answer": "(x: number) => {}",
    "difficulty": "Easy",
    "explanation": "Arrow syntax annotates directly.",
    "category": "Type Annotations"
  },
  {
    "question": "Type for 'null' and 'undefined'?",
    "options": ["null | undefined", "void", "any", "unknown"],
    "answer": "null | undefined",
    "difficulty": "Easy",
    "explanation": "Literal types for optional values.",
    "category": "Type Annotations"
  },
  {
    "question": "Tuple annotation syntax?",
    "options": ["[string, number]", "{0: string, 1: number}", "Array<string | number>", "Tuple<string, number>"],
    "answer": "[string, number]",
    "difficulty": "Easy",
    "explanation": "Square brackets define tuples.",
    "category": "Type Annotations"
  },
  {
    "question": "Correct 'any' usage?",
    "options": ["let x: any", "let x = any", "let x: Any", "let x as any"],
    "answer": "let x: any",
    "difficulty": "Easy",
    "explanation": "'any' disables type checking.",
    "category": "Type Annotations"
  },
  {
    "question": "'never' represents what?",
    "options": ["Value that never occurs", "Function that never returns", "Both", "Empty type"],
    "answer": "Both",
    "difficulty": "Medium",
    "explanation": "Impossible paths or infinite loops.",
    "category": "Type Annotations"
  },
  {
    "question": "Dynamic keys object type?",
    "options": ["{[key: string]: number}", "Record<string, number>", "Both", "Map<string, number>"],
    "answer": "Both",
    "difficulty": "Medium",
    "explanation": "Record is a utility type.",
    "category": "Type Annotations"
  },
  {
    "question": "Correct 'void' return?",
    "options": ["() => void", "() => undefined", "Both", "() => null"],
    "answer": "Both",
    "difficulty": "Easy",
    "explanation": "void allows undefined return.",
    "category": "Type Annotations"
  },
  {
    "question": "Promise return type?",
    "options": ["Promise<T>", "async T", "Future<T>", "Thenable<T>"],
    "answer": "Promise<T>",
    "difficulty": "Easy",
    "explanation": "Standard async return type.",
    "category": "Type Annotations"
  },

  // Interfaces (10)
  {
    "question": "Keyword to declare interface?",
    "options": ["interface", "type", "class", "declare"],
    "answer": "interface",
    "difficulty": "Easy",
    "explanation": "Defines object shape contract.",
    "category": "Interfaces"
  },
  {
    "question": "Can interfaces extend others?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "Use 'extends' keyword.",
    "category": "Interfaces"
  },
  {
    "question": "Optional property syntax?",
    "options": ["?", "!", "*", "~"],
    "answer": "?",
    "difficulty": "Easy",
    "explanation": "name?: string",
    "category": "Interfaces"
  },
  {
    "question": "Readonly properties in interfaces?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "readonly id: number",
    "category": "Interfaces"
  },
  {
    "question": "Function interface syntax?",
    "options": ["interface Fn { (x: number): string }", "interface Fn = (x: number) => string", "Both", "Neither"],
    "answer": "interface Fn { (x: number): string }",
    "difficulty": "Medium",
    "explanation": "Call signature inside interface.",
    "category": "Interfaces"
  },
  {
    "question": "Index signatures in interfaces?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "[key: string]: number",
    "category": "Interfaces"
  },
  {
    "question": "Interface declaration merging?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "Same name merges members.",
    "category": "Interfaces"
  },
  {
    "question": "Hybrid interface example?",
    "options": ["Call + properties", "Extends class", "With generics", "All"],
    "answer": "Call + properties",
    "difficulty": "Hard",
    "explanation": "Can be called and have props.",
    "category": "Interfaces"
  },
  {
    "question": "Can interfaces extend classes?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "Inherits instance members.",
    "category": "Interfaces"
  },
  {
    "question": "Interface vs type merging?",
    "options": ["Interfaces merge", "Types merge", "Both", "Neither"],
    "answer": "Interfaces merge",
    "difficulty": "Medium",
    "explanation": "Only interfaces support merging.",
    "category": "Interfaces"
  },

  // Classes (10)
  {
    "question": "Public property in class?",
    "options": ["public name: string", "name: string", "Both", "private name: string"],
    "answer": "Both",
    "difficulty": "Easy",
    "explanation": "Public is default.",
    "category": "Classes"
  },
  {
    "question": "'protected' means?",
    "options": ["Subclass access", "Same class only", "Anywhere", "Same module"],
    "answer": "Subclass access",
    "difficulty": "Easy",
    "explanation": "Visible in derived classes.",
    "category": "Classes"
  },
  {
    "question": "Readonly class fields?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "readonly name = 'TS'",
    "category": "Classes"
  },
  {
    "question": "Parameter property shorthand?",
    "options": ["public constructor(public name: string) {}", "Manual this.name", "Both", "None"],
    "answer": "Both",
    "difficulty": "Medium",
    "explanation": "Auto-declares field.",
    "category": "Classes"
  },
  {
    "question": "Implement interface in class?",
    "options": ["implements", "extends", "uses", "inherits"],
    "answer": "implements",
    "difficulty": "Easy",
    "explanation": "class User implements Person",
    "category": "Classes"
  },
  {
    "question": "Abstract class features?",
    "options": ["Can't instantiate", "Abstract methods", "Both", "None"],
    "answer": "Both",
    "difficulty": "Medium",
    "explanation": "Base with required overrides.",
    "category": "Classes"
  },
  {
    "question": "Static members typed?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "static version: string",
    "category": "Classes"
  },
  {
    "question": "super() calls?",
    "options": ["Parent constructor", "Current constructor", "Interface", "Global"],
    "answer": "Parent constructor",
    "difficulty": "Easy",
    "explanation": "Required in derived ctor.",
    "category": "Classes"
  },
  {
    "question": "Index signatures in classes?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Hard",
    "explanation": "class Dict { [k: string]: number }",
    "category": "Classes"
  },
  {
    "question": "Class-level decorator?",
    "options": ["@Component", "@Input", "@Output", "@HostListener"],
    "answer": "@Component",
    "difficulty": "Medium",
    "explanation": "Applies to constructor.",
    "category": "Classes"
  },

  // Generics (10)
  {
    "question": "Generic function syntax?",
    "options": ["function id<T>(arg: T): T", "function id(arg: T): T", "<T>function id", "function id<T>: T"],
    "answer": "function id<T>(arg: T): T",
    "difficulty": "Easy",
    "explanation": "<T> before parameters.",
    "category": "Generics"
  },
  {
    "question": "Constrain generic?",
    "options": ["<T extends string>", "<T = string>", "<T: string>", "<T super string>"],
    "answer": "<T extends string>",
    "difficulty": "Easy",
    "explanation": "Limits possible types.",
    "category": "Generics"
  },
  {
    "question": "Generic interface?",
    "options": ["interface Box<T> { value: T }", "interface Box = <T>{}", "Both", "None"],
    "answer": "interface Box<T> { value: T }",
    "difficulty": "Easy",
    "explanation": "Box<number>, Box<string>",
    "category": "Generics"
  },
  {
    "question": "Default generic type?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "class Cache<T = string>",
    "category": "Generics"
  },
  {
    "question": "keyof T returns?",
    "options": ["Union of keys", "Array of keys", "Object", "String"],
    "answer": "Union of keys",
    "difficulty": "Medium",
    "explanation": "keyof User → 'id' | 'name'",
    "category": "Generics"
  },
  {
    "question": "Mapped type syntax?",
    "options": ["{ [P in keyof T]: U }", "{ P in keyof T: U }", "Both", "None"],
    "answer": "{ [P in keyof T]: U }",
    "difficulty": "Hard",
    "explanation": "Transforms properties.",
    "category": "Generics"
  },
  {
    "question": "Conditional type?",
    "options": ["T extends U ? X : Y", "T extends U => X", "T ? U : X", "then/else"],
    "answer": "T extends U ? X : Y",
    "difficulty": "Hard",
    "explanation": "Type-level if/else.",
    "category": "Generics"
  },
  {
    "question": "Utility: extract return type?",
    "options": ["ReturnType<T>", "Parameters<T>", "InstanceType<T>", "ThisType<T>"],
    "answer": "ReturnType<T>",
    "difficulty": "Medium",
    "explanation": "ReturnType<typeof fn>",
    "category": "Generics"
  },
  {
    "question": "Generics in type aliases?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "type Pair<T> = [T, T]",
    "category": "Generics"
  },
  {
    "question": "What does 'infer' do?",
    "options": ["Captures type in conditional", "Creates type", "Extends", "Merges"],
    "answer": "Captures type in conditional",
    "difficulty": "Hard",
    "explanation": "Used in ReturnType implementation.",
    "category": "Generics"
  },

  // Enums (10)
  {
    "question": "Numeric enum declaration?",
    "options": ["enum Direction { Up, Down }", "enum = { Up }", "const enum", "type Direction"],
    "answer": "enum Direction { Up, Down }",
    "difficulty": "Easy",
    "explanation": "Auto-increment from 0.",
    "category": "Enums"
  },
  {
    "question": "Explicit enum values?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "Red = 1, Green = 2",
    "category": "Enums"
  },
  {
    "question": "String enum?",
    "options": ["String values", "Number values", "Both", "Const enum"],
    "answer": "String values",
    "difficulty": "Easy",
    "explanation": "Info = 'INFO'",
    "category": "Enums"
  },
  {
    "question": "const enum effect?",
    "options": ["Inlined at compile", "Runtime object", "No export", "Readonly"],
    "answer": "Inlined at compile",
    "difficulty": "Medium",
    "explanation": "No runtime enum.",
    "category": "Enums"
  },
  {
    "question": "Reverse mapping?",
    "options": ["Numeric only", "String only", "Both", "No"],
    "answer": "Numeric only",
    "difficulty": "Medium",
    "explanation": "Direction[0] === 'Up'",
    "category": "Enums"
  },
  {
    "question": "Heterogeneous enum?",
    "options": ["Mixed string/number", "With functions", "With objects", "Computed"],
    "answer": "Mixed string/number",
    "difficulty": "Hard",
    "explanation": "Discouraged pattern.",
    "category": "Enums"
  },
  {
    "question": "Computed enum members?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "Name = 'file'.length",
    "category": "Enums"
  },
  {
    "question": "Enums are?",
    "options": ["Types + values", "Only types", "Only values", "Neither"],
    "answer": "Types + values",
    "difficulty": "Medium",
    "explanation": "Dual nature.",
    "category": "Enums"
  },
  {
    "question": "Type variable with enum?",
    "options": ["let d: Direction", "let d = Direction", "Both", "as Direction"],
    "answer": "let d: Direction",
    "difficulty": "Easy",
    "explanation": "Restricts to members.",
    "category": "Enums"
  },
  {
    "question": "preserveConstEnums does?",
    "options": ["Keeps in .d.ts", "Deletes", "Converts to let", "Merges"],
    "answer": "Keeps in .d.ts",
    "difficulty": "Hard",
    "explanation": "For declaration files.",
    "category": "Enums"
  },

  // Type Inference (5)
  {
    "question": "Inferred type: let x = 10",
    "options": ["number", "10", "any", "unknown"],
    "answer": "number",
    "difficulty": "Easy",
    "explanation": "Widens literal.",
    "category": "Type Inference"
  },
  {
    "question": "const x = 10 infers?",
    "options": ["10", "number", "any", "literal"],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "Const preserves literal.",
    "category": "Type Inference"
  },
  {
    "question": "Function return inferred?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "Based on return expression.",
    "category": "Type Inference"
  },
  {
    "question": "Contextual typing?",
    "options": ["From assignment context", "File context", "Module", "Compiler"],
    "answer": "From assignment context",
    "difficulty": "Medium",
    "explanation": "Event handlers auto-typed.",
    "category": "Type Inference"
  },
  {
    "question": "Force wider inference?",
    "options": ["Yes, assertion", "No"],
    "answer": "Yes, assertion",
    "difficulty": "Medium",
    "explanation": "10 as number",
    "category": "Type Inference"
  },

  // Union & Intersection Types (10) — BUG FIXED HERE
  {
    "question": "Union type syntax?",
    "options": ["string | number", "string & number", "string + number", "string || number"],
    "answer": "string | number",
    "difficulty": "Easy",
    "explanation": "Value can be either.",
    "category": "Union and Intersection Types"
  },
  {
    "question": "Intersection type?",
    "options": ["A & B", "A | B", "A + B", "A, B"],
    "answer": "A & B",
    "difficulty": "Easy",
    "explanation": "Combines members.",
    "category": "Union and Intersection Types"
  },
  {
    "question": "Safe on union?",
    "options": ["Common properties", "All", "None", "Optional only"],
    "answer": "Common properties",
    "difficulty": "Easy",
    "explanation": "Only shared members.",
    "category": "Union and Intersection Types"
  },
  {
    "question": "Narrow union?",
    "options": ["Yes, type guards", "No"],
    "answer": "Yes, type guards",
    "difficulty": "Easy",
    "explanation": "typeof checks.",
    "category": "Union and Intersection Types"
  },
  {
    "question": "Discriminated union?",
    "options": ["Common literal tag", "Union of interfaces", "Union of classes", "All"],
    "answer": "Common literal tag",
    "difficulty": "Medium",
    "explanation": "kind: 'circle' | 'square'",
    "category": "Union and Intersection Types"
  },
  {
    "question": "never & string = ?",
    "options": ["never", "string", "any", "unknown"],
    "answer": "never",
    "difficulty": "Hard",
    "explanation": "Absorbs in intersection.",
    "category": "Union and Intersection Types"
  },
  {
    "question": "Intersections with primitives?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "string & 'hello' → 'hello'",
    "category": "Union and Intersection Types"
  },
  {
    "question": "Extract union members?",
    "options": ["Extract<T, U>", "T extends U ? T : never", "Both", "None"],
    "answer": "Both",
    "difficulty": "Hard",
    "explanation": "Built-in + manual.",
    "category": "Union and Intersection Types"
  },
  {
    "question": "Exhaustive checking?",
    "options": ["All cases handled", "Property check", "Runtime", "Loop"],
    "answer": "All cases handled",
    "difficulty": "Medium",
    "explanation": "never in default.",
    "category": "Union and Intersection Types"
  },
  {
    "question": "Distributive conditionals?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Hard",
    "explanation": "Applies per union member.",
    "category": "Union and Intersection Types"
  },

  // Type Guards (10)
  {
    "question": "typeof guard?",
    "options": ["typeof x === 'string'", "x instanceof String", "x is string", "'length' in x"],
    "answer": "typeof x === 'string'",
    "difficulty": "Easy",
    "explanation": "Primitives narrowing.",
    "category": "Type Guards"
  },
  {
    "question": "instanceof guard?",
    "options": ["x instanceof Date", "typeof x === Date", "x is Date", "Date in x"],
    "answer": "x instanceof Date",
    "difficulty": "Easy",
    "explanation": "Class instances.",
    "category": "Type Guards"
  },
  {
    "question": "'in' operator guard?",
    "options": ["'name' in x", "x.has('name')", "x.name exists", "nameof x"],
    "answer": "'name' in x",
    "difficulty": "Easy",
    "explanation": "Property existence.",
    "category": "Type Guards"
  },
  {
    "question": "User-defined guard?",
    "options": ["function isString(x): x is string", "returns boolean", "Both", "Generic"],
    "answer": "function isString(x): x is string",
    "difficulty": "Medium",
    "explanation": "Predicate return type.",
    "category": "Type Guards"
  },
  {
    "question": "Generic type guards?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "Preserve type param.",
    "category": "Type Guards"
  },
  {
    "question": "Literal type guard?",
    "options": ["x === 'admin'", "typeof x", "x is 'admin'", "A and C"],
    "answer": "A and C",
    "difficulty": "Medium",
    "explanation": "Equality narrows.",
    "category": "Type Guards"
  },
  {
    "question": "Switch narrowing?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "Per case.",
    "category": "Type Guards"
  },
  {
    "question": "Null/undefined guard?",
    "options": ["x != null", "x !== null && x !== undefined", "Both", "x is defined"],
    "answer": "Both",
    "difficulty": "Easy",
    "explanation": "Non-null assertion !",
    "category": "Type Guards"
  },
  {
    "question": "Assertion function?",
    "options": ["asserts x is string", "assert(x: string)", "Both", "None"],
    "answer": "asserts x is string",
    "difficulty": "Hard",
    "explanation": "Throws if false.",
    "category": "Type Guards"
  },
  {
    "question": "Guard arrays?",
    "options": ["Yes, .filter(isString)", "No"],
    "answer": "Yes, .filter(isString)",
    "difficulty": "Medium",
    "explanation": "Narrows array type.",
    "category": "Type Guards"
  },

  // Decorators (10)
  {
    "question": "Enable decorators flag?",
    "options": ["experimentalDecorators", "enableDecorators", "decorators", "useDecorators"],
    "answer": "experimentalDecorators",
    "difficulty": "Easy",
    "explanation": "Required in tsconfig.",
    "category": "Decorators"
  },
  {
    "question": "Class decorator args?",
    "options": ["1 (constructor)", "0", "2", "3"],
    "answer": "1 (constructor)",
    "difficulty": "Easy",
    "explanation": "Function constructor.",
    "category": "Decorators"
  },
  {
    "question": "Method decorator args?",
    "options": ["(target, key, descriptor)", "(target, descriptor)", "(key, descriptor)", "(target, key)"],
    "answer": "(target, key, descriptor)",
    "difficulty": "Medium",
    "explanation": "PropertyDescriptor.",
    "category": "Decorators"
  },
  {
    "question": "Parameter decorators?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "@Inject() service",
    "category": "Decorators"
  },
  {
    "question": "Decorator composition?",
    "options": ["@A @B", "Multiple on one", "Both", "Factory"],
    "answer": "Both",
    "difficulty": "Medium",
    "explanation": "Applied bottom-up.",
    "category": "Decorators"
  },
  {
    "question": "Decorator factory?",
    "options": ["Returns decorator", "Creates classes", "Built-in", "None"],
    "answer": "Returns decorator",
    "difficulty": "Medium",
    "explanation": "function log(prefix)",
    "category": "Decorators"
  },
  {
    "question": "Modify property initializer?",
    "options": ["Yes, descriptor", "No"],
    "answer": "Yes, descriptor",
    "difficulty": "Hard",
    "explanation": "Return new descriptor.",
    "category": "Decorators"
  },
  {
    "question": "Metadata package?",
    "options": ["reflect-metadata", "ts-metadata", "decorator-metadata", "meta-ts"],
    "answer": "reflect-metadata",
    "difficulty": "Medium",
    "explanation": "With emitDecoratorMetadata.",
    "category": "Decorators"
  },
  {
    "question": "Decorator execution order?",
    "options": ["Bottom to top", "Top to bottom"],
    "answer": "Bottom to top",
    "difficulty": "Hard",
    "explanation": "@A @B → B first.",
    "category": "Decorators"
  },
  {
    "question": "Decorators in plain TS?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "Angular, NestJS, etc.",
    "category": "Decorators"
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

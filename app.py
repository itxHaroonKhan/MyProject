import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Set page config
st.set_page_config(page_title="TypeScript Quiz - 100 Questions", page_icon="🟦", layout="centered")

# Quiz data (your full 100 questions)
quiz = [
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
    "explanation": "'strict: true' turns on all strict family options including noImplicitAny, strictNullChecks, etc.",
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
    "explanation": "Set 'declaration: true' to emit type declaration (.d.ts) files.",
    "category": "TS Compiler"
  },
  {
    "question": "What is the default value of 'module' for modern projects?",
    "options": ["CommonJS", "ESNext", "AMD", "System"],
    "answer": "ESNext",
    "difficulty": "Easy",
    "explanation": "When 'target' is ES2015+, the default module is 'ESNext'.",
    "category": "TS Compiler"
  },
  {
    "question": "Which flag skips type checking of declaration files?",
    "options": ["skipLibCheck", "skipDefaultLibCheck", "noLib", "fastCheck"],
    "answer": "skipLibCheck",
    "difficulty": "Easy",
    "explanation": "'skipLibCheck: true' speeds up compilation by skipping .d.ts files.",
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
    "explanation": "When true, no JavaScript is emitted if compilation fails type-checking.",
    "category": "TS Compiler"
  },
  {
    "question": "Which option enables source maps?",
    "options": ["sourceMap", "inlineSourceMap", "mapRoot", "sourceRoot"],
    "answer": "sourceMap",
    "difficulty": "Easy",
    "explanation": "'sourceMap: true' generates .map files for debugging.",
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
    "explanation": "Helps the compiler resolve relative paths and mirrors folder structure in outDir.",
    "category": "TS Compiler"
  },
  {
    "question": "Which flag allows JavaScript files in the project?",
    "options": ["allowJs", "checkJs", "emitJs", "includeJs"],
    "answer": "allowJs",
    "difficulty": "Easy",
    "explanation": "'allowJs: true' lets .js files be imported and compiled.",
    "category": "TS Compiler"
  },

  // Type Annotations (10)
  {
    "question": "How do you annotate a variable as string?",
    "options": ["let name: String", "let name: string", "let name = String", "let name: 'string'"],
    "answer": "let name: string",
    "difficulty": "Easy",
    "explanation": "Lowercase 'string' is the primitive type; 'String' is the wrapper object.",
    "category": "Type Annotations"
  },
  {
    "question": "Which is the correct array type annotation?",
    "options": ["number[]", "Array<number>", "Both", "Neither"],
    "answer": "Both",
    "difficulty": "Easy",
    "explanation": "Both syntaxes are valid and equivalent.",
    "category": "Type Annotations"
  },
  {
    "question": "How do you type a function parameter?",
    "options": ["(x: number) => {}", "(x) => number {}", "function(x: number)", "function x(number)"],
    "answer": "(x: number) => {}",
    "difficulty": "Easy",
    "explanation": "Arrow functions annotate parameters directly after the name.",
    "category": "Type Annotations"
  },
  {
    "question": "What is the type for 'null' and 'undefined'?",
    "options": ["null | undefined", "void", "any", "unknown"],
    "answer": "null | undefined",
    "difficulty": "Easy",
    "explanation": "They are literal types; use union for optional values.",
    "category": "Type Annotations"
  },
  {
    "question": "How do you annotate a tuple?",
    "options": ["[string, number]", "{0: string, 1: number}", "Array<string | number>", "Tuple<string, number>"],
    "answer": "[string, number]",
    "difficulty": "Easy",
    "explanation": "Square brackets define fixed-length tuples.",
    "category": "Type Annotations"
  },
  {
    "question": "Which is a correct 'any' usage?",
    "options": ["let x: any", "let x = any", "let x: Any", "let x as any"],
    "answer": "let x: any",
    "difficulty": "Easy",
    "explanation": "'any' disables type checking for that value.",
    "category": "Type Annotations"
  },
  {
    "question": "What does 'never' represent?",
    "options": ["A value that never occurs", "A function that never returns", "Both", "An empty type"],
    "answer": "Both",
    "difficulty": "Medium",
    "explanation": "Used for impossible code paths or functions that throw/loop forever.",
    "category": "Type Annotations"
  },
  {
    "question": "How do you type an object with dynamic keys?",
    "options": ["{[key: string]: number}", "Record<string, number>", "Both", "Map<string, number>"],
    "answer": "Both",
    "difficulty": "Medium",
    "explanation": "Record<Keys, Type> is a utility type for index signatures.",
    "category": "Type Annotations"
  },
  {
    "question": "Which is the correct 'void' return type?",
    "options": ["() => void", "() => undefined", "Both", "() => null"],
    "answer": "Both",
    "difficulty": "Easy",
    "explanation": "void functions may return undefined but not other values.",
    "category": "Type Annotations"
  },
  {
    "question": "How do you annotate a function that returns a Promise?",
    "options": ["Promise<T>", "async T", "Future<T>", "Thenable<T>"],
    "answer": "Promise<T>",
    "difficulty": "Easy",
    "explanation": "Use Promise<string> for async functions returning string.",
    "category": "Type Annotations"
  },

  // Interfaces (10)
  {
    "question": "What keyword declares an interface?",
    "options": ["interface", "type", "class", "declare"],
    "answer": "interface",
    "difficulty": "Easy",
    "explanation": "'interface' defines a contract for object shape.",
    "category": "Interfaces"
  },
  {
    "question": "Can interfaces be extended?",
    "options": ["Yes", "No", "Only with classes", "Only with types"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "Use 'extends' to inherit from one or more interfaces.",
    "category": "Interfaces"
  },
  {
    "question": "How do you make a property optional?",
    "options": ["?", "!", "*", "~"],
    "answer": "?",
    "difficulty": "Easy",
    "explanation": "name?: string means the property may be missing.",
    "category": "Interfaces"
  },
  {
    "question": "Can interfaces have readonly properties?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "'readonly id: number' prevents reassignment after construction.",
    "category": "Interfaces"
  },
  {
    "question": "What is function interface syntax?",
    "options": ["interface Fn { (x: number): string }", "interface Fn = (x: number) => string", "Both", "Neither"],
    "answer": "interface Fn { (x: number): string }",
    "difficulty": "Medium",
    "explanation": "Call signatures inside interfaces define function types.",
    "category": "Interfaces"
  },
  {
    "question": "Can interfaces describe index signatures?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "[key: string]: number allows any string key with number value.",
    "category": "Interfaces"
  },
  {
    "question": "Can you merge interface declarations?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "Declaring the same interface name multiple times merges members.",
    "category": "Interfaces"
  },
  {
    "question": "What is hybrid interface?",
    "options": ["Interface with both properties and call signature", "Interface that extends class", "Interface with generics", "All of the above"],
    "answer": "Interface with both properties and call signature",
    "difficulty": "Hard",
    "explanation": "E.g., interface Counter { (x: number): void; count: number }",
    "category": "Interfaces"
  },
  {
    "question": "Can interfaces extend classes?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "Interface can extend a class to inherit its instance members.",
    "category": "Interfaces"
  },
  {
    "question": "Which is true about interface vs type?",
    "options": ["Interfaces can be merged, types cannot", "Types can be merged, interfaces cannot", "Both can be merged", "Neither can be merged"],
    "answer": "Interfaces can be merged, types cannot",
    "difficulty": "Medium",
    "explanation": "Declaration merging is unique to interfaces.",
    "category": "Interfaces"
  },

  // Classes (10)
  {
    "question": "How do you define a public property in a class?",
    "options": ["public name: string", "name: string", "Both", "private name: string"],
    "answer": "Both",
    "difficulty": "Easy",
    "explanation": "Public is default; explicit keyword is optional.",
    "category": "Classes"
  },
  {
    "question": "What does 'protected' access mean?",
    "options": ["Accessible in subclass", "Accessible only in same class", "Accessible anywhere", "Accessible in same module"],
    "answer": "Accessible in subclass",
    "difficulty": "Easy",
    "explanation": "Protected members are visible to derived classes.",
    "category": "Classes"
  },
  {
    "question": "Can you use 'readonly' in class fields?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "readonly name: string = 'TS';",
    "category": "Classes"
  },
  {
    "question": "What is parameter property shorthand?",
    "options": ["public constructor(public name: string) {}", "constructor(name: string) { this.name = name }", "Both", "None"],
    "answer": "Both",
    "difficulty": "Medium",
    "explanation": "The shorthand declares and initializes in one line.",
    "category": "Classes"
  },
  {
    "question": "How do you implement an interface in a class?",
    "options": ["implements", "extends", "uses", "inherits"],
    "answer": "implements",
    "difficulty": "Easy",
    "explanation": "class User implements Person { ... }",
    "category": "Classes"
  },
  {
    "question": "What is an abstract class?",
    "options": ["Cannot be instantiated directly", "Can have abstract methods", "Both", "None"],
    "answer": "Both",
    "difficulty": "Medium",
    "explanation": "Abstract classes provide base implementations with required overrides.",
    "category": "Classes"
  },
  {
    "question": "Can static members be typed?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "static version: string = '1.0';",
    "category": "Classes"
  },
  {
    "question": "What does 'super()' call?",
    "options": ["Parent class constructor", "Current class constructor", "Interface constructor", "Global constructor"],
    "answer": "Parent class constructor",
    "difficulty": "Easy",
    "explanation": "Required in derived class constructors.",
    "category": "Classes"
  },
  {
    "question": "Can classes have index signatures?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Hard",
    "explanation": "class Dict { [key: string]: number }",
    "category": "Classes"
  },
  {
    "question": "Which decorator is class-level?",
    "options": ["@Component", "@Input", "@Output", "@HostListener"],
    "answer": "@Component",
    "difficulty": "Medium",
    "explanation": "Applied to the class constructor.",
    "category": "Classes"
  },

  // Generics (10)
  {
    "question": "What is the syntax for a generic function?",
    "options": ["function id<T>(arg: T): T", "function id(arg: T): T", "function<T> id(arg: T): T", "function id<T>: T"],
    "answer": "function id<T>(arg: T): T",
    "difficulty": "Easy",
    "explanation": "Angle brackets before parameter list.",
    "category": "Generics"
  },
  {
    "question": "How do you constrain a generic?",
    "options": ["<T extends string>", "<T = string>", "<T: string>", "<T super string>"],
    "answer": "<T extends string>",
    "difficulty": "Easy",
    "explanation": "Ensures T has at least the members of string.",
    "category": "Generics"
  },
  {
    "question": "What is a generic interface?",
    "options": ["interface Box<T> { value: T }", "interface Box = <T> { value: T }", "Both", "None"],
    "answer": "interface Box<T> { value: T }",
    "difficulty": "Easy",
    "explanation": "Can be instantiated with any type: Box<number>.",
    "category": "Generics"
  },
  {
    "question": "Can generic classes have default types?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "class Cache<T = string> {}",
    "category": "Generics"
  },
  {
    "question": "What does keyof T return?",
    "options": ["Union of property names", "Array of keys", "Object with keys", "String literal"],
    "answer": "Union of property names",
    "difficulty": "Medium",
    "explanation": "keyof User → 'id' | 'name'.",
    "category": "Generics"
  },
  {
    "question": "How do you create a mapped type?",
    "options": ["{ [P in keyof T]: U }", "{ P in keyof T: U }", "Both", "None"],
    "answer": "{ [P in keyof T]: U }",
    "difficulty": "Hard",
    "explanation": "Transforms each property type.",
    "category": "Generics"
  },
  {
    "question": "What is conditional type syntax?",
    "options": ["T extends U ? X : Y", "T extends U => X | Y", "T ? U : X : Y", "T extends U then X else Y"],
    "answer": "T extends U ? X : Y",
    "difficulty": "Hard",
    "explanation": "Resolves to X or Y based on type relationship.",
    "category": "Generics"
  },
  {
    "question": "Which utility type extracts return type?",
    "options": ["ReturnType<T>", "Parameters<T>", "InstanceType<T>", "ThisType<T>"],
    "answer": "ReturnType<T>",
    "difficulty": "Medium",
    "explanation": "ReturnType<typeof fn> gives return type.",
    "category": "Generics"
  },
  {
    "question": "Can generics be used in type aliases?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "type Pair<T, U> = [T, U];",
    "category": "Generics"
  },
  {
    "question": "What does infer do?",
    "options": ["Infers a type variable in conditional types", "Creates a new type", "Extends a type", "Merges types"],
    "answer": "Infers a type variable in conditional types",
    "difficulty": "Hard",
    "explanation": "Used in ReturnType: type ReturnType<T> = T extends (...a: any) => infer R ? R : any;",
    "category": "Generics"
  },

  // Enums (10)
  {
    "question": "How do you declare a numeric enum?",
    "options": ["enum Direction { Up, Down }", "enum Direction = { Up, Down }", "const enum Direction { Up }", "type Direction = 'Up' | 'Down'"],
    "answer": "enum Direction { Up, Down }",
    "difficulty": "Easy",
    "explanation": "Members are auto-incremented from 0.",
    "category": "Enums"
  },
  {
    "question": "Can enum members have explicit values?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "enum Color { Red = 1, Green = 2 }",
    "category": "Enums"
  },
  {
    "question": "What is a string enum?",
    "options": ["enum with string values", "enum with number values", "enum with both", "const enum"],
    "answer": "enum with string values",
    "difficulty": "Easy",
    "explanation": "enum Log { Info = 'INFO', Error = 'ERROR' }",
    "category": "Enums"
  },
  {
    "question": "What does 'const enum' do?",
    "options": ["Inlines values at compile time", "Generates runtime object", "Prevents export", "Makes enum readonly"],
    "answer": "Inlines values at compile time",
    "difficulty": "Medium",
    "explanation": "No runtime enum object; values are replaced directly.",
    "category": "Enums"
  },
  {
    "question": "Can enums be reverse-mapped?",
    "options": ["Yes, for numeric", "Yes, for string", "Both", "No"],
    "answer": "Yes, for numeric",
    "difficulty": "Medium",
    "explanation": "Direction[0] === 'Up' only works for numeric enums.",
    "category": "Enums"
  },
  {
    "question": "What is heterogeneous enum?",
    "options": ["Mix of string and number members", "Enum with functions", "Enum with objects", "Computed enum"],
    "answer": "Mix of string and number members",
    "difficulty": "Hard",
    "explanation": "enum Mixed { A = 1, B = 'two' } – discouraged.",
    "category": "Enums"
  },
  {
    "question": "Can enums have computed members?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "enum File { Name = 'file'.length }",
    "category": "Enums"
  },
  {
    "question": "Are enums types or values?",
    "options": ["Both", "Only types", "Only values", "Neither"],
    "answer": "Both",
    "difficulty": "Medium",
    "explanation": "Enum name is a type; members are values.",
    "category": "Enums"
  },
  {
    "question": "How do you type a variable with enum?",
    "options": ["let d: Direction", "let d = Direction", "Both", "let d as Direction"],
    "answer": "let d: Direction",
    "difficulty": "Easy",
    "explanation": "Restricts to enum member values.",
    "category": "Enums"
  },
  {
    "question": "What is 'preserveConstEnums'?",
    "options": ["Keeps const enum in emitted code", "Deletes const enum", "Converts to let", "Merges enums"],
    "answer": "Keeps const enum in emitted code",
    "difficulty": "Hard",
    "explanation": "For declaration files; no runtime impact.",
    "category": "Enums"
  },

  // Type Inference (5)
  {
    "question": "What type is inferred for 'let x = 10'?",
    "options": ["number", "10", "any", "unknown"],
    "answer": "number",
    "difficulty": "Easy",
    "explanation": "Literal widens to primitive type.",
    "category": "Type Inference"
  },
  {
    "question": "What is inferred for 'const x = 10'?",
    "options": ["10", "number", "any", "literal"],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "const preserves literal type.",
    "category": "Type Inference"
  },
  {
    "question": "Does TS infer return type of functions?",
    "options": ["Yes", "No", "Only with --noImplicitAny", "Only in .ts files"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "function add(a, b) { return a + b } → (a: number, b: number) => number",
    "category": "Type Inference"
  },
  {
    "question": "What is contextual typing?",
    "options": ["Infer type from assignment context", "Infer from file context", "Infer from module", "Infer from compiler"],
    "answer": "Infer type from assignment context",
    "difficulty": "Medium",
    "explanation": "window.onmousedown = (e) => { e.button; } → e is MouseEvent",
    "category": "Type Inference"
  },
  {
    "question": "Can you force wider inference?",
    "options": ["Yes, with type assertion", "No"],
    "answer": "Yes, with type assertion",
    "difficulty": "Medium",
    "explanation": "let x = 10 as number; widens from 10.",
    "category": "Type Inference"
  },

  // Union & Intersection (10)
  {
    "question": "How do you declare a union type?",
    "options": ["string | number", "string & number", "string + number", "string || number"],
    "answer": "string | number",
    "difficulty": "Easy",
    "explanation": "Value can be either type.",
    "category": "Union and Intersection Types"
  },
  {
    "question": "What is an intersection type?",
    "options": ["A & B", "A | B", "A + B", "A, B"],
    "answer": "A & B",
    "difficulty": "Easy",
    "explanation": "Combines members of both types.",
    "category": ": "Union and Intersection Types"
  },
  {
    "question": "Which properties are safe on a union?",
    "options": ["Only common properties", "All properties", "None", "Only optional"],
    "answer": "Only common properties",
    "difficulty": "Easy",
    "explanation": "string | number → only .toString(), .valueOf()",
    "category": "Union and Intersection Types"
  },
  {
    "question": "Can you narrow a union?",
    "options": ["Yes, with type guards", "No"],
    "answer": "Yes, with type guards",
    "difficulty": "Easy",
    "explanation": "if (typeof x === 'string') { x.length }",
    "category": "Union and Intersection Types"
  },
  {
    "question": "What is a discriminated union?",
    "options": ["Union with a common literal property", "Union of interfaces", "Union of classes", "All of the above"],
    "answer": "Union with a common literal property",
    "difficulty": "Medium",
    "explanation": "type Shape = Circle | Square; both have 'kind': 'circle' | 'square'",
    "category": "Union and Intersection Types"
  },
  {
    "question": "What does never & string resolve to?",
    "options": ["never", "string", "any", "unknown"],
    "answer": "never",
    "difficulty": "Hard",
    "explanation": "Intersection with never is always never.",
    "category": "Union and Intersection Types"
  },
  {
    "question": "Can intersections be used with primitives?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "string & 'hello' is 'hello'.",
    "category": "Union and Intersection Types"
  },
  {
    "question": "How do you extract union members?",
    "options": ["T extends U ? T : never", "Extract<T, U>", "Both", "None"],
    "answer": "Both",
    "difficulty": "Hard",
    "explanation": "Extract<string | number, string> → string",
    "category": "Union and Intersection Types"
  },
  {
    "question": "What is exhaustive checking?",
    "options": ["Ensuring all union cases are handled", "Checking all properties", "Runtime validation", "Compile-time loop"],
    "answer": "Ensuring all union cases are handled",
    "difficulty": "Medium",
    "explanation": "Use never in default case to catch missing branches.",
    "category": "Union and Intersection Types"
  },
  {
    "question": "Can you distribute over unions?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Hard",
    "explanation": "(A | B) extends C ? X : Y → checks A and B separately.",
    "category": "Union and Intersection Types"
  },

  // Type Guards (10)
  {
    "question": "What is 'typeof' type guard?",
    "options": ["typeof x === 'string'", "x instanceof String", "x is string", "'length' in x"],
    "answer": "typeof x === 'string'",
    "difficulty": "Easy",
    "explanation": "Narrows primitives.",
    "category": "Type Guards"
  },
  {
    "question": "What is 'instanceof' guard?",
    "options": ["x instanceof Date", "typeof x === Date", "x is Date", "Date in x"],
    "answer": "x instanceof Date",
    "difficulty": "Easy",
    "explanation": "Narrows to class instances.",
    "category": "Type Guards"
  },
  {
    "question": "What is 'in' operator guard?",
    "options": ["'name' in x", "x.has('name')", "x.name exists", "nameof x"],
    "answer": "'name' in x",
    "difficulty": "Easy",
    "explanation": "Checks property existence.",
    "category": "Type Guards"
  },
  {
    "question": "How do you write a user-defined type guard?",
    "options": ["function isString(x: any): x is string", "function isString(x: any): boolean", "Both", "function isString<T>(x: T): x is string"],
    "answer": "function isString(x: any): x is string",
    "difficulty": "Medium",
    "explanation": "Return type predicate 'x is string' narrows.",
    "category": "Type Guards"
  },
  {
    "question": "Can type guards be used in generics?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Medium",
    "explanation": "function isArray<T>(x: T[]): x is T[]",
    "category": "Type Guards"
  },
  {
    "question": "What is a literal type guard?",
    "options": ["x === 'admin'", "typeof x === 'string'", "x is 'admin'", "Both A and C"],
    "answer": "Both A and C",
    "difficulty": "Medium",
    "explanation": "Equality narrows to literal type.",
    "category": "Type Guards"
  },
  {
    "question": "Do type guards work in switch?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "Discriminated unions narrow per case.",
    "category": "Type Guards"
  },
  {
    "question": "Can you guard against null/undefined?",
    "options": ["x != null", "x !== null && x !== undefined", "Both", "x is defined"],
    "answer": "Both",
    "difficulty": "Easy",
    "explanation": "Non-null assertion operator ! also removes null.",
    "category": "Type Guards"
  },
  {
    "question": "What is assertion signature?",
    "options": ["function assert(x: any): asserts x is string", "function assert(x: string)", "Both", "None"],
    "answer": "function assert(x: any): asserts x is string",
    "difficulty": "Hard",
    "explanation": "Throws if condition false; narrows afterward.",
    "category": "Type Guards"
  },
  {
    "question": "Can type guards narrow unions in arrays?",
    "options": ["Yes, with .filter()", "No"],
    "answer": "Yes, with .filter()",
    "difficulty": "Medium",
    "explanation": "arr.filter(isString) → string[]",
    "category": "Type Guards"
  },

  // Decorators (10)
  {
    "question": "Which flag enables decorators?",
    "options": ["experimentalDecorators", "enableDecorators", "decorators", "useDecorators"],
    "answer": "experimentalDecorators",
    "difficulty": "Easy",
    "explanation": "Still experimental; required in tsconfig.",
    "category": "Decorators"
  },
  {
    "question": "How many arguments does a class decorator receive?",
    "options": ["1 (constructor)", "0", "2", "3"],
    "answer": "1 (constructor)",
    "difficulty": "Easy",
    "explanation": "@sealed function sealed(ctor: Function) {}",
    "category": "Decorators"
  },
  {
    "question": "What is a method decorator signature?",
    "options": ["(target, key, descriptor)", "(target, descriptor)", "(key, descriptor)", "(target, key)"],
    "answer": "(target, key, descriptor)",
    "difficulty": "Medium",
    "explanation": "key is string | symbol, descriptor is PropertyDescriptor.",
    "category": "Decorators"
  },
  {
    "question": "Can decorators be applied to parameters?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "function method(@Inject() service: Service) {}",
    "category": "Decorators"
  },
  {
    "question": "What is decorator composition?",
    "options": ["@A @B class C {}", "Multiple decorators on one target", "Both", "Decorator returning decorator"],
    "answer": "Both",
    "difficulty": "Medium",
    "explanation": "Applied bottom-up, executed top-down.",
    "category": "Decorators"
  },
  {
    "question": "What is a decorator factory?",
    "options": ["Function that returns a decorator", "Decorator that creates classes", "Built-in decorator", "None"],
    "answer": "Function that returns a decorator",
    "difficulty": "Medium",
    "explanation": "function log(prefix) { return (target) => {...} }",
    "category": "Decorators"
  },
  {
    "question": "Can decorators modify property initializers?",
    "options": ["Yes, via descriptor", "No"],
    "answer": "Yes, via descriptor",
    "difficulty": "Hard",
    "explanation": "Return new descriptor with value or get/set.",
    "category": "Decorators"
  },
  {
    "question": "What is metadata emitted with decorators?",
    "options": ["reflect-metadata", "ts-metadata", "decorator-metadata", "meta-ts"],
    "answer": "reflect-metadata",
    "difficulty": "Medium",
    "explanation": "Requires 'emitDecoratorMetadata' and npm package.",
    "category": "Decorators"
  },
  {
    "question": "Which decorator order is execution order?",
    "options": ["Top to bottom", "Bottom to top"],
    "answer": "Bottom to top",
    "difficulty": "Hard",
    "explanation": "@A @B → B runs first, then A.",
    "category": "Decorators"
  },
  {
    "question": "Can decorators be used in plain TS libraries?",
    "options": ["Yes", "No"],
    "answer": "Yes",
    "difficulty": "Easy",
    "explanation": "Common in Angular, NestJS, TypeORM, etc.",
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

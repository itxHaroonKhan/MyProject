import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Quiz data - Enhanced with more questions
quiz =[
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
    {
        "question": "What is the output of: ```typescript\nconst x: string = 'hello'; console.log(x.toUpperCase());```",
        "options": ["HELLO", "hello", "Error", "undefined"],
        "answer": "HELLO",
        "difficulty": "Easy",
        "explanation": "The 'string' type allows string methods like 'toUpperCase', which returns 'HELLO'.",
        "category": "TypeScript"
    },
    {
        "question": "What happens if you assign: ```typescript\nlet x: boolean = 'true';```",
        "options": ["Type error", "Converts to boolean", "No error", "undefined"],
        "answer": "Type error",
        "difficulty": "Easy",
        "explanation": "Assigning a string to a boolean-typed variable causes a type error in TypeScript.",
        "category": "TypeScript"
    },
    {
        "question": "What is the purpose of the 'tsc' command?",
        "options": ["Compiles TypeScript to JavaScript", "Runs TypeScript code", "Formats code", "Bundles modules"],
        "answer": "Compiles TypeScript to JavaScript",
        "difficulty": "Easy",
        "explanation": "'tsc' transpiles TypeScript files into JavaScript based on tsconfig.json.",
        "category": "TS Compiler"
    },
    {
        "question": "What does 'outDir' specify in tsconfig.json?",
        "options": ["Output directory for compiled files", "Input file directory", "Module type", "Target JavaScript version"],
        "answer": "Output directory for compiled files",
        "difficulty": "Easy",
        "explanation": "'outDir' defines where compiled JavaScript files are saved.",
        "category": "TS Compiler"
    },
    {
        "question": "What happens with: ```typescript\ntsc app.ts --target ES5```?",
        "options": ["Compiles to ES5 JavaScript", "Compiles to ES6", "Causes an error", "Runs the code"],
        "answer": "Compiles to ES5 JavaScript",
        "difficulty": "Medium",
        "explanation": "The '--target ES5' flag compiles TypeScript to ES5-compatible JavaScript.",
        "category": "TS Compiler"
    },
    {
        "question": "What is the effect of 'strictNullChecks' in tsconfig.json?",
        "options": ["Enforces null/undefined checks", "Disables type checking", "Allows any type", "Minifies output"],
        "answer": "Enforces null/undefined checks",
        "difficulty": "Medium",
        "explanation": "'strictNullChecks: true' ensures null and undefined are not assignable to other types.",
        "category": "TS Compiler"
    },
    {
        "question": "What does 'tsc --watch' do?",
        "options": ["Recompiles on file changes", "Runs the code", "Formats the code", "Generates type definitions"],
        "answer": "Recompiles on file changes",
        "difficulty": "Medium",
        "explanation": "'--watch' mode recompiles TypeScript files automatically when they change.",
        "category": "TS Compiler"
    },
    {
        "question": "What is wrong with: ```typescript\ntsc file.js```?",
        "options": ["Cannot compile .js files", "No error", "Missing tsconfig.json", "Invalid flag"],
        "answer": "Cannot compile .js files",
        "difficulty": "Easy",
        "explanation": "'tsc' is designed to compile .ts files, not .js files.",
        "category": "TS Compiler"
    },
    {
        "question": "What is the correct type annotation for an array of strings?",
        "options": ["let arr: string[]", "let arr: Array<string>", "let arr: [string]", "Both A and B"],
        "answer": "Both A and B",
        "difficulty": "Easy",
        "explanation": "TypeScript supports 'string[]' and 'Array<string>' for string arrays.",
        "category": "Type Annotations"
    },
    {
        "question": "What is the output of: ```typescript\nlet x: number | string = 5; x = 'test'; console.log(x);```",
        "options": ["test", "5", "Error", "undefined"],
        "answer": "test",
        "difficulty": "Medium",
        "explanation": "The union type allows 'x' to be reassigned to a string, logging 'test'.",
        "category": "Type Annotations"
    },
    {
        "question": "How do you annotate a function returning a number?",
        "options": ["function fn(): number", "function fn: number", "function fn() => number", "function fn() = number"],
        "answer": "function fn(): number",
        "difficulty": "Easy",
        "explanation": "The ': number' after the parameter list specifies the return type.",
        "category": "Type Annotations"
    },
    {
        "question": "What is wrong with: ```typescript\nlet x: number = true;```",
        "options": ["Type mismatch", "Syntax error", "No error", "Missing declaration"],
        "answer": "Type mismatch",
        "difficulty": "Easy",
        "explanation": "Assigning a boolean to a number-typed variable causes a type error.",
        "category": "Type Annotations"
    },
    {
        "question": "What is the type of 'x' in: ```typescript\nfunction fn(x: { id: number }): void {}```",
        "options": ["Object with id: number", "any", "number", "void"],
        "answer": "Object with id: number",
        "difficulty": "Medium",
        "explanation": "The parameter 'x' is typed as an object with an 'id' property of type number.",
        "category": "Type Annotations"
    },
    {
        "question": "What does this interface define: ```typescript\ninterface User { name: string; age?: number; }```",
        "options": ["Object with name and optional age", "Object with name only", "Object with age only", "Class with name and age"],
        "answer": "Object with name and optional age",
        "difficulty": "Easy",
        "explanation": "The interface defines an object with a required 'name' and optional 'age'.",
        "category": "Interfaces"
    },
    {
        "question": "What is the output of: ```typescript\ninterface Point { x: number; } let p: Point = { x: 10 }; console.log(p.x);```",
        "options": ["10", "undefined", "Error", "null"],
        "answer": "10",
        "difficulty": "Easy",
        "explanation": "The interface ensures 'p' has an 'x' property, logging 10.",
        "category": "Interfaces"
    },
    {
        "question": "What is wrong with: ```typescript\ninterface A { x: number; } let a: A = { x: 1, y: 'test' };```",
        "options": ["Extra property 'y'", "Missing 'x'", "Type mismatch", "No error"],
        "answer": "Extra property 'y'",
        "difficulty": "Medium",
        "explanation": "TypeScript flags extra properties not in the interface as errors in strict mode.",
        "category": "Interfaces"
    },
    {
        "question": "How do you extend an interface?",
        "options": ["interface B extends A {}", "interface B : A {}", "interface B implements A {}", "interface B = A {}"],
        "answer": "interface B extends A {}",
        "difficulty": "Medium",
        "explanation": "'extends' allows an interface to inherit properties from another interface.",
        "category": "Interfaces"
    },
    {
        "question": "What does this log: ```typescript\ninterface A { x: number; } interface B extends A { y: string; } let b: B = { x: 1, y: 'test' }; console.log(b.y);```",
        "options": ["test", "1", "Error", "undefined"],
        "answer": "test",
        "difficulty": "Medium",
        "explanation": "'B' extends 'A', so 'b' has both 'x' and 'y', logging 'test'.",
        "category": "Interfaces"
    },
    {
        "question": "What is the output of: ```typescript\nclass Car { model: string = 'Sedan'; } let car = new Car(); console.log(car.model);```",
        "options": ["Sedan", "undefined", "Error", "null"],
        "answer": "Sedan",
        "difficulty": "Easy",
        "explanation": "The class initializes 'model' to 'Sedan', which is logged.",
        "category": "Classes"
    },
    {
        "question": "How do you define a protected property in a class?",
        "options": ["protected x: number", "private x: number", "#x: number", "public x: number"],
        "answer": "protected x: number",
        "difficulty": "Medium",
        "explanation": "'protected' properties are accessible in the class and its subclasses.",
        "category": "Classes"
    },
    {
        "question": "What does this log: ```typescript\nclass A { x = 1; } class B extends A { x = 2; } let b = new B(); console.log(b.x);```",
        "options": ["2", "1", "Error", "undefined"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "The subclass 'B' overrides 'x', so 'b.x' logs 2.",
        "category": "Classes"
    },
    {
        "question": "What is wrong with: ```typescript\nclass A { private x = 1; } class B extends A { x = 2; }```",
        "options": ["Cannot override private property", "No error", "Syntax error", "Missing constructor"],
        "answer": "Cannot override private property",
        "difficulty": "Medium",
        "explanation": "'private' properties are not accessible in subclasses, causing a type error.",
        "category": "Classes"
    },
    {
        "question": "What does 'implements' ensure in a class?",
        "options": ["Adheres to an interface", "Inherits a class", "Declares a method", "Creates an instance"],
        "answer": "Adheres to an interface",
        "difficulty": "Medium",
        "explanation": "'implements' ensures a class follows the structure of an interface.",
        "category": "Classes"
    },
    {
        "question": "What does this log: ```typescript\nfunction identity<T>(value: T): T { return value; } console.log(identity<string>('hello'));```",
        "options": ["hello", "undefined", "Error", "null"],
        "answer": "hello",
        "difficulty": "Medium",
        "explanation": "The generic function returns the input value, typed as 'string', logging 'hello'.",
        "category": "Generics"
    },
    {
        "question": "How do you constrain a generic type to have a specific property?",
        "options": ["T extends { prop: type }", "T : { prop: type }", "T implements { prop: type }", "T = { prop: type }"],
        "answer": "T extends { prop: type }",
        "difficulty": "Medium",
        "explanation": "'extends' constrains the generic type to objects with the specified property.",
        "category": "Generics"
    },
    {
        "question": "What is wrong with: ```typescript\nfunction fn<T>(x: T): number { return x; }```",
        "options": ["Return type mismatch", "No error", "Syntax error", "Missing generic constraint"],
        "answer": "Return type mismatch",
        "difficulty": "Hard",
        "explanation": "'x' of type 'T' cannot be guaranteed to be a number, causing a type error.",
        "category": "Generics"
    },
    {
        "question": "What does this log: ```typescript\nfunction merge<T, U>(a: T, b: U) { return { ...a, ...b }; } console.log(merge({ x: 1 }, { y: 2 }).y);```",
        "options": ["2", "1", "Error", "undefined"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "The generic function merges objects, and the result has property 'y' with value 2.",
        "category": "Generics"
    },
    {
        "question": "What is the output of: ```typescript\nfunction wrap<T>(x: T[]): T[] { return x; } console.log(wrap<number>([1, 2])[0]);```",
        "options": ["1", "undefined", "Error", "null"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "The generic function returns the input array, and the first element is 1.",
        "category": "Generics"
    },
    {
        "question": "What is the output of: ```typescript\nenum Direction { Up, Down } console.log(Direction.Up);```",
        "options": ["0", "Up", "Error", "undefined"],
        "answer": "0",
        "difficulty": "Medium",
        "explanation": "Numeric enums assign values starting at 0, so 'Up' is 0.",
        "category": "Enums"
    },
    {
        "question": "How do you define a string enum?",
        "options": ["enum E { A = 'a' }", "enum E { A: 'a' }", "enum E { A = string }", "enum E = 'a'"],
        "answer": "enum E { A = 'a' }",
        "difficulty": "Medium",
        "explanation": "String enums assign string values to members, e.g., 'A = 'a''. ",
        "category": "Enums"
    },
    {
        "question": "What does this log: ```typescript\nenum Color { Red = 2, Blue } console.log(Color.Blue);```",
        "options": ["3", "2", "Blue", "Error"],
        "answer": "3",
        "difficulty": "Medium",
        "explanation": "Enums increment numeric values, so 'Blue' is 3 after 'Red = 2'.",
        "category": "Enums"
    },
    {
        "question": "How do you get an enum’s name by value?",
        "options": ["Enum[value]", "Enum.getName(value)", "Enum.valueOf(value)", "Enum.name(value)"],
        "answer": "Enum[value]",
        "difficulty": "Medium",
        "explanation": "Enums are objects at runtime, so 'Enum[value]' retrieves the name for a value.",
        "category": "Enums"
    },
    {
        "question": "What does this log: ```typescript\nenum E { A = 'x' } console.log(E['x']);```",
        "options": ["A", "x", "Error", "undefined"],
        "answer": "A",
        "difficulty": "Medium",
        "explanation": "String enums allow reverse lookup, so 'E['x']' returns the name 'A'.",
        "category": "Enums"
    },
    {
        "question": "What type is inferred for: ```typescript\nlet x = true;```",
        "options": ["boolean", "any", "true", "undefined"],
        "answer": "boolean",
        "difficulty": "Easy",
        "explanation": "TypeScript infers 'boolean' based on the value 'true'.",
        "category": "Type Inference"
    },
    {
        "question": "What is inferred for: ```typescript\nconst arr = [1, 'test'];```",
        "options": ["(number | string)[]", "any[]", "Array<number>", "string[]"],
        "answer": "(number | string)[]",
        "difficulty": "Medium",
        "explanation": "TypeScript infers a union type array based on the mixed elements.",
        "category": "Type Inference"
    },
    {
        "question": "What happens if you assign: ```typescript\nlet x = 10; x = false;```",
        "options": ["Type error", "No error", "Converts to boolean", "undefined"],
        "answer": "Type error",
        "difficulty": "Medium",
        "explanation": "TypeScript infers 'x' as 'number', so assigning a boolean causes a type error.",
        "category": "Type Inference"
    },
    {
        "question": "What is inferred for: ```typescript\nfunction fn(x) { return x.length; }```",
        "options": ["any", "number", "string", "void"],
        "answer": "any",
        "difficulty": "Medium",
        "explanation": "Without type annotations, TypeScript infers 'any' for the parameter and return type.",
        "category": "Type Inference"
    },
    {
        "question": "What is inferred for: ```typescript\nconst x = { id: 1 };```",
        "options": ["{ id: number }", "any", "object", "number"],
        "answer": "{ id: number }",
        "difficulty": "Medium",
        "explanation": "TypeScript infers an object type with an 'id' property of type 'number'.",
        "category": "Type Inference"
    },
    {
        "question": "What does this log: ```typescript\nlet x: number | string = 5; if (typeof x === 'string') { console.log(x.length); } else { console.log(x); }```",
        "options": ["5", "undefined", "Error", "null"],
        "answer": "5",
        "difficulty": "Medium",
        "explanation": "The 'typeof' check ensures 'x' is treated as a number in the 'else' block, logging 5.",
        "category": "Union and Intersection Types"
    },
    {
        "question": "What is an intersection type?",
        "options": ["Combines multiple types", "Selects one type", "Excludes types", "Creates a union"],
        "answer": "Combines multiple types",
        "difficulty": "Medium",
        "explanation": "Intersection types, e.g., 'A & B', require all properties from both types.",
        "category": "Union and Intersection Types"
    },
    {
        "question": "What is wrong with: ```typescript\ntype A = { x: number }; type B = { y: string }; let obj: A & B = { x: 1 };```",
        "options": ["Missing 'y' property", "No error", "Type mismatch", "Invalid syntax"],
        "answer": "Missing 'y' property",
        "difficulty": "Medium",
        "explanation": "An intersection type requires all properties from both 'A' and 'B'.",
        "category": "Union and Intersection Types"
    },
    {
        "question": "What does this log: ```typescript\ntype A = { x: number }; type B = { y: string }; let obj: A | B = { y: 'test' }; console.log('y' in obj ? obj.y : 'no');```",
        "options": ["test", "no", "Error", "undefined"],
        "answer": "test",
        "difficulty": "Medium",
        "explanation": "The 'in' operator checks for 'y', and since 'obj' has 'y', it logs 'test'.",
        "category": "Union and Intersection Types"
    },
    {
        "question": "What is the output of: ```typescript\ntype A = { x: number }; let obj: A | null = { x: 1 }; console.log(obj?.x);```",
        "options": ["1", "null", "Error", "undefined"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "The optional chaining '?.' safely accesses 'x', logging 1 since 'obj' is not null.",
        "category": "Union and Intersection Types"
    },
    {
        "question": "What does this log: ```typescript\nfunction fn(x: string | number) { if (typeof x === 'number') { console.log(x * 2); } } fn(10);```",
        "options": ["20", "undefined", "Error", "null"],
        "answer": "20",
        "difficulty": "Medium",
        "explanation": "The 'typeof' type guard narrows 'x' to 'number', so 'x * 2' logs 20.",
        "category": "Type Guards"
    },
    {
        "question": "What is a type guard using 'instanceof'?",
        "options": ["Checks if an object is an instance of a class", "Checks for a property", "Declares a type", "Casts a type"],
        "answer": "Checks if an object is an instance of a class",
        "difficulty": "Easy",
        "explanation": "'instanceof' narrows a type by checking if an object is an instance of a class.",
        "category": "Type Guards"
    },
    {
        "question": "What does this log: ```typescript\nclass A { x = 1; } function fn(obj: any) { if (obj instanceof A) { console.log(obj.x); } } fn(new A());```",
        "options": ["1", "undefined", "Error", "null"],
        "answer": "1",
        "difficulty": "Medium",
        "explanation": "The 'instanceof' type guard narrows 'obj' to 'A', allowing access to 'x'.",
        "category": "Type Guards"
    },
    {
        "question": "What is wrong with: ```typescript\nfunction isNumber(x: any): x is number { return typeof x === 'string'; }```",
        "options": ["Incorrect type check", "No error", "Syntax error", "Missing return type"],
        "answer": "Incorrect type check",
        "difficulty": "Hard",
        "explanation": "The type guard checks for 'string' but claims 'x is number', which is incorrect.",
        "category": "Type Guards"
    },
    {
        "question": "What does this log: ```typescript\nfunction isString(x: any): x is string { return typeof x === 'string'; } let x: any = 'test'; if (isString(x)) { console.log(x.length); }```",
        "options": ["4", "undefined", "Error", "null"],
        "answer": "4",
        "difficulty": "Medium",
        "explanation": "The user-defined type guard narrows 'x' to 'string', so 'x.length' logs 4.",
        "category": "Type Guards"
    },
    {
        "question": "What does this log: ```typescript\nfunction log(target: any, key: string) { console.log(key); } class C { @log x = 1; } new C();```",
        "options": ["x", "undefined", "Error", "null"],
        "answer": "x",
        "difficulty": "Medium",
        "explanation": "The property decorator logs the property name 'x' during class initialization.",
        "category": "Decorators"
    },
    {
        "question": "What is required to enable decorators?",
        "options": ["'experimentalDecorators' in tsconfig.json", "'useDecorators' in tsconfig.json", "'strict' mode", "No configuration"],
        "answer": "'experimentalDecorators' in tsconfig.json",
        "difficulty": "Medium",
        "explanation": "Decorators require 'experimentalDecorators: true' in tsconfig.json.",
        "category": "Decorators"
    },
    {
        "question": "What does a method decorator receive as arguments?",
        "options": ["target, key, descriptor", "target, value", "key, value", "class, method"],
        "answer": "target, key, descriptor",
        "difficulty": "Medium",
        "explanation": "Method decorators receive the target (class prototype), method name, and property descriptor.",
        "category": "Decorators"
    },
    {
        "question": "What is wrong with: ```typescript\n@decorator class C {}``` without enabling decorators?",
        "options": ["Compilation error", "No error", "Runtime error", "Syntax error"],
        "answer": "Compilation error",
        "difficulty": "Medium",
        "explanation": "Decorators require 'experimentalDecorators: true' or the compiler fails.",
        "category": "Decorators"
    },
    {
        "question": "What does this log: ```typescript\nfunction log(target: any, key: string, descriptor: PropertyDescriptor) { console.log(key); } class C { @log method() {} } new C();```",
        "options": ["method", "undefined", "Error", "null"],
        "answer": "method",
        "difficulty": "Medium",
        "explanation": "The method decorator logs the method name 'method' during class initialization.",
        "category": "Decorators"
    },
    {
        "question": "What is the output of: ```typescript\nlet x: any = 'hello'; console.log(x.toUpperCase());```",
        "options": ["HELLO", "undefined", "Error", "null"],
        "answer": "HELLO",
        "difficulty": "Easy",
        "explanation": "The 'any' type allows calling string methods, so 'toUpperCase' logs 'HELLO'.",
        "category": "TypeScript"
    },
    {
        "question": "What does 'module' specify in tsconfig.json?",
        "options": ["Module system for compiled code", "Output directory", "Target JavaScript version", "Input file format"],
        "answer": "Module system for compiled code",
        "difficulty": "Medium",
        "explanation": "'module' sets the module system (e.g., 'ESNext', 'CommonJS') for compiled output.",
        "category": "TS Compiler"
    },
    {
        "question": "How do you annotate an optional function parameter?",
        "options": ["param?: type", "param: type?", "param: ?type", "param = type"],
        "answer": "param?: type",
        "difficulty": "Medium",
        "explanation": "Optional parameters are marked with '?' in function declarations.",
        "category": "Type Annotations"
    },
    {
        "question": "What does this log: ```typescript\ninterface A { x: number; } let a: A = { x: 5 }; console.log(a.x);```",
        "options": ["5", "undefined", "Error", "null"],
        "answer": "5",
        "difficulty": "Easy",
        "explanation": "The interface ensures 'a' has an 'x' property, logging 5.",
        "category": "Interfaces"
    },
    {
        "question": "What is the output of: ```typescript\nclass A { constructor(public x: number) {} } let a = new A(10); console.log(a.x);```",
        "options": ["10", "undefined", "Error", "null"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "The 'public' parameter property assigns 'x' to the instance, logging 10.",
        "category": "Classes"
    },
    {
        "question": "What does this log: ```typescript\nfunction fn<T extends { id: number }>(x: T) { console.log(x.id); } fn({ id: 42 });```",
        "options": ["42", "undefined", "Error", "null"],
        "answer": "42",
        "difficulty": "Medium",
        "explanation": "The generic constraint ensures 'x' has an 'id' property, logging 42.",
        "category": "Generics"
    },
    {
        "question": "What is the output of: ```typescript\nenum E { X = 'x' } console.log(E.X);```",
        "options": ["x", "0", "Error", "undefined"],
        "answer": "x",
        "difficulty": "Medium",
        "explanation": "String enums assign string values, so 'E.X' is 'x'.",
        "category": "Enums"
    },
    {
        "question": "What is inferred for: ```typescript\nlet x = { name: 'test' };```",
        "options": ["{ name: string }", "any", "object", "string"],
        "answer": "{ name: string }",
        "difficulty": "Easy",
        "explanation": "TypeScript infers an object type with a 'name' property of type 'string'.",
        "category": "Type Inference"
    },
    {
        "question": "What does this log: ```typescript\ntype A = { x: number }; let obj: A | null = null; console.log(obj?.x);```",
        "options": ["undefined", "null", "Error", "0"],
        "answer": "undefined",
        "difficulty": "Medium",
        "explanation": "Optional chaining '?.' returns 'undefined' when 'obj' is null.",
        "category": "Union and Intersection Types"
    },
    {
        "question": "What does this log: ```typescript\nfunction fn(x: any): x is number { return typeof x === 'number'; } let x: any = 10; if (fn(x)) { console.log(x * 2); }```",
        "options": ["20", "undefined", "Error", "null"],
        "answer": "20",
        "difficulty": "Medium",
        "explanation": "The user-defined type guard narrows 'x' to 'number', so 'x * 2' logs 20.",
        "category": "Type Guards"
    }
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

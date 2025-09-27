import streamlit as st
import random
from datetime import datetime, timedelta
import uuid

# Quiz data - Enhanced with more questions
quiz =[
    {
        "question": "What is the output of this code: ```javascript\nfunction example() { var x = 1; if (true) { var x = 2; } console.log(x); }\nexample();```",
        "options": ["1", "2", "undefined", "ReferenceError"],
        "answer": "2",
        "difficulty": "Medium",
        "explanation": "The 'var' keyword is function-scoped, so the inner 'var x = 2' reassigns the same variable, logging 2.",
        "category": "Variable Scoping"
    },
    {
        "question": "What is the output of this code: ```javascript\nlet x = 10; { let x = 20; } console.log(x);```",
        "options": ["10", "20", "undefined", "Error"],
        "answer": "10",
        "difficulty": "Medium",
        "explanation": "The 'let' keyword is block-scoped, so the inner 'let x = 20' creates a new variable, and the outer x remains 10.",
        "category": "Variable Scoping"
    },
    {
        "question": "What happens when you declare a variable with 'const' inside a block scope?",
        "options": ["It’s accessible globally", "It’s accessible only within the block", "It’s hoisted to the function scope", "It causes a SyntaxError"],
        "answer": "It’s accessible only within the block",
        "difficulty": "Easy",
        "explanation": "'const' is block-scoped, so the variable is only accessible within the block it’s declared in.",
        "category": "Variable Scoping"
    },
    {
        "question": "What is the output of: ```javascript\nfunction test() { console.log(x); var x = 5; }\ntest();```",
        "options": ["5", "undefined", "ReferenceError", "null"],
        "answer": "undefined",
        "difficulty": "Medium",
        "explanation": "Due to hoisting, 'var x' is declared but not initialized when console.log is called, so it outputs 'undefined'.",
        "category": "Variable Scoping"
    },
    {
        "question": "What is the scope of a variable declared without any keyword inside a function?",
        "options": ["Block scope", "Function scope", "Global scope", "Module scope"],
        "answer": "Global scope",
        "difficulty": "Medium",
        "explanation": "Without a keyword (var, let, const), a variable is implicitly declared in the global scope.",
        "category": "Variable Scoping"
    },
    {
        "question": "How do you validate that a drop-down menu (<select>) has a selected option?",
        "options": ["Check if select.value is empty", "Check if select.selectedIndex is -1", "Check if select.options is null", "Check if select.text is undefined"],
        "answer": "Check if select.selectedIndex is -1",
        "difficulty": "Easy",
        "explanation": "A drop-down’s selectedIndex is -1 when no option is selected, making it a reliable way to validate.",
        "category": "Form validation: drop-downs"
    },
    {
        "question": "What does select.options[select.selectedIndex].value return for a drop-down?",
        "options": ["The text of the selected option", "The value of the selected option", "The index of the selected option", "The entire select element"],
        "answer": "The value of the selected option",
        "difficulty": "Medium",
        "explanation": "select.options[select.selectedIndex].value retrieves the 'value' attribute of the currently selected option.",
        "category": "Form validation: drop-downs"
    },
    {
        "question": "How can you ensure at least one radio button in a group is selected?",
        "options": ["Use input.checked for each radio", "Use radioGroup.value", "Use radioGroup.selected", "Use input.value"],
        "answer": "Use input.checked for each radio",
        "difficulty": "Easy",
        "explanation": "Loop through radio buttons with the same 'name' attribute and check if any has 'input.checked' as true.",
        "category": "Form validation: radio buttons"
    },
    {
        "question": "What is the correct way to get the value of a selected radio button?",
        "options": ["document.querySelector('input[type=radio]:checked').value", "document.getElementById('radio').value", "document.querySelector('input[type=radio]').value", "document.getElementsByName('radio').value"],
        "answer": "document.querySelector('input[type=radio]:checked').value",
        "difficulty": "Medium",
        "explanation": "The ':checked' pseudo-class selects the radio button that is currently checked, and '.value' retrieves its value.",
        "category": "Form validation: radio buttons"
    },
    {
        "question": "Which regex pattern validates a US ZIP code (5 digits or 5+4)?",
        "options": ["/^\\d{5}(-\\d{4})?$/", "/^\\d{5}$/", "/^\\d{5}-\\d{4}$/", "/^[0-9]{5,9}$/"],
        "answer": "/^\\d{5}(-\\d{4})?$/",
        "difficulty": "Medium",
        "explanation": "The pattern allows 5 digits optionally followed by a hyphen and 4 digits, covering both ZIP formats.",
        "category": "Form validation: ZIP codes"
    },
    {
        "question": "What does the regex /^\\d{5}$/ validate for a ZIP code?",
        "options": ["5-digit ZIP code", "5 or 9-digit ZIP code", "Any numeric string", "ZIP code with letters"],
        "answer": "5-digit ZIP code",
        "difficulty": "Easy",
        "explanation": "The pattern /^\\d{5}$/ matches exactly 5 digits, suitable for basic US ZIP codes.",
        "category": "Form validation: ZIP codes"
    },
    {
        "question": "Which regex is best for validating an email address?",
        "options": ["/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/", "/^\\w+@\\w+\\.\\w+$/", "/^[a-zA-Z0-9]+@[a-zA-Z0-9]+\\.[a-zA-Z]{2}$/", "/^.*@.*\\..*$/"],
        "answer": "/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/",
        "difficulty": "Hard",
        "explanation": "This regex allows common email characters before and after the '@', a domain, and a TLD of 2+ characters.",
        "category": "Form validation: email"
    },
    {
        "question": "What happens if an email input fails regex validation?",
        "options": ["Form submission stops", "Browser shows a default error", "Nothing, unless handled in JS", "The input is cleared"],
        "answer": "Nothing, unless handled in JS",
        "difficulty": "Medium",
        "explanation": "HTML5 email validation triggers browser errors, but custom regex validation in JS requires manual handling.",
        "category": "Form validation: email"
    },
    {
        "question": "What does a 'try...catch' block do in JavaScript?",
        "options": ["Declares variables", "Handles errors", "Loops through arrays", "Defines functions"],
        "answer": "Handles errors",
        "difficulty": "Easy",
        "explanation": "The 'try...catch' block catches exceptions thrown in the 'try' block and handles them in the 'catch' block.",
        "category": "Exceptions: try and catch"
    },
    {
        "question": "What is logged in: ```javascript\ntry { throw new Error('Oops'); } catch (e) { console.log(e.message); }```",
        "options": ["Oops", "Error", "undefined", "null"],
        "answer": "Oops",
        "difficulty": "Medium",
        "explanation": "The 'throw new Error('Oops')' creates an error with the message 'Oops', which is caught and logged.",
        "category": "Exceptions: try and catch"
    },
    {
        "question": "What does the 'throw' statement do?",
        "options": ["Exits a function", "Throws an exception", "Logs a message", "Declares a variable"],
        "answer": "Throws an exception",
        "difficulty": "Easy",
        "explanation": "The 'throw' statement creates and throws a custom exception, often used with 'try...catch'.",
        "category": "Exceptions: throw"
    },
    {
        "question": "What happens in: ```javascript\nthrow 'CustomError';```?",
        "options": ["Logs 'CustomError'", "Throws a string as an exception", "Creates a variable", "Causes a SyntaxError"],
        "answer": "Throws a string as an exception",
        "difficulty": "Medium",
        "explanation": "The 'throw' statement can throw any value, like a string, which can be caught in a 'catch' block.",
        "category": "Exceptions: throw"
    },
    {
        "question": "How do you add an event listener to a button in JavaScript?",
        "options": ["button.addEventListener('click', handler)", "button.onClick(handler)", "button.attachEvent('click', handler)", "button.event('click', handler)"],
        "answer": "button.addEventListener('click', handler)",
        "difficulty": "Easy",
        "explanation": "'addEventListener' is the standard way to attach an event handler to an element for events like 'click'.",
        "category": "Handling events within JavaScript"
    },
    {
        "question": "What does 'event.preventDefault()' do in an event handler?",
        "options": ["Stops event propagation", "Prevents the default action", "Removes the event listener", "Logs the event"],
        "answer": "Prevents the default action",
        "difficulty": "Medium",
        "explanation": "'preventDefault()' stops the browser’s default action, like form submission or link navigation.",
        "category": "Handling events within JavaScript"
    },
    {
        "question": "What is a 'junk artifact' in the DOM?",
        "options": ["A text node", "A comment node", "An element node", "A script node"],
        "answer": "A comment node",
        "difficulty": "Medium",
        "explanation": "Junk artifacts, like comment nodes, are non-element nodes (nodeType 8) that don’t affect rendering.",
        "category": "The DOM: Junk artifacts and nodeType"
    },
    {
        "question": "What is the nodeType of an HTML element?",
        "options": ["1", "3", "8", "9"],
        "answer": "1",
        "difficulty": "Easy",
        "explanation": "The nodeType of an HTML element is 1, while text nodes are 3, and comment nodes are 8.",
        "category": "The DOM: Junk artifacts and nodeType"
    },
    {
        "question": "Which method targets an element by its ID?",
        "options": ["document.querySelector()", "document.getElementById()", "document.getElementsByClassName()", "document.getElementsByTagName()"],
        "answer": "document.getElementById()",
        "difficulty": "Easy",
        "explanation": "'getElementById()' is the most direct way to target an element by its unique ID.",
        "category": "The DOM: More ways to target elements"
    },
    {
        "question": "How do you select all elements with a specific class?",
        "options": ["document.querySelectorAll('.class')", "document.getElementByClass('.class')", "document.getElementsByClassName('class')", "Both A and C"],
        "answer": "Both A and C",
        "difficulty": "Medium",
        "explanation": "Both 'querySelectorAll' and 'getElementsByClassName' can select elements by class, returning a NodeList or HTMLCollection.",
        "category": "The DOM: More ways to target elements"
    },
    {
        "question": "How do you get the tag name of a DOM element?",
        "options": ["element.tagName", "element.nodeName", "element.name", "Both A and B"],
        "answer": "Both A and B",
        "difficulty": "Medium",
        "explanation": "Both 'tagName' and 'nodeName' return the tag name of an element, like 'DIV' or 'P'.",
        "category": "The DOM: Getting a target's name"
    },
    {
        "question": "What does element.tagName return for a <div> element?",
        "options": ["div", "DIV", "<div>", "null"],
        "answer": "DIV",
        "difficulty": "Easy",
        "explanation": "'tagName' returns the tag name in uppercase, so a <div> element returns 'DIV'.",
        "category": "The DOM: Getting a target's name"
    },
    {
        "question": "How do you count the number of <p> elements in a document?",
        "options": ["document.getElementsByTagName('p').length", "document.querySelector('p').count", "document.getElementsByClassName('p').length", "document.querySelectorAll('p').count"],
        "answer": "document.getElementsByTagName('p').length",
        "difficulty": "Easy",
        "explanation": "'getElementsByTagName' returns an HTMLCollection, and '.length' gives the count of matching elements.",
        "category": "The DOM: Counting elements"
    },
    {
        "question": "What does document.querySelectorAll('div').length return?",
        "options": ["Number of divs", "Number of all elements", "Number of classes", "Number of attributes"],
        "answer": "Number of divs",
        "difficulty": "Easy",
        "explanation": "'querySelectorAll('div')' returns a NodeList of all <div> elements, and '.length' counts them.",
        "category": "The DOM: Counting elements"
    },
    {
        "question": "How do you check if an element has a specific attribute?",
        "options": ["element.hasAttribute('name')", "element.getAttribute('name')", "element.attribute('name')", "element.checkAttribute('name')"],
        "answer": "element.hasAttribute('name')",
        "difficulty": "Easy",
        "explanation": "'hasAttribute' checks if an element has a specified attribute, returning true or false.",
        "category": "The DOM: Attributes"
    },
    {
        "question": "How do you set an attribute on a DOM element?",
        "options": ["element.setAttribute('name', 'value')", "element.attribute('name', 'value')", "element.name = 'value'", "element.addAttribute('name', 'value')"],
        "answer": "element.setAttribute('name', 'value')",
        "difficulty": "Easy",
        "explanation": "'setAttribute' sets or updates an attribute’s value on a DOM element.",
        "category": "The DOM: Attributes"
    },
    {
        "question": "How do you get all attribute names of an element?",
        "options": ["Array.from(element.attributes).map(attr => attr.name)", "element.getAttributeNames()", "element.attributes.map(attr => attr.name)", "Both A and B"],
        "answer": "Both A and B",
        "difficulty": "Medium",
        "explanation": "'getAttributeNames()' directly returns an array of attribute names, or you can map 'element.attributes'.",
        "category": "The DOM: Attribute names and values"
    },
    {
        "question": "What does element.getAttribute('id') return?",
        "options": ["The element’s ID", "The element’s class", "The element’s tag", "null if no ID"],
        "answer": "null if no ID",
        "difficulty": "Medium",
        "explanation": "'getAttribute('id')' returns the ID’s value or null if the attribute doesn’t exist.",
        "category": "The DOM: Attribute names and values"
    },
    {
        "question": "How do you create a new DOM element?",
        "options": ["document.createElement('tag')", "document.newElement('tag')", "document.createNode('tag')", "document.addElement('tag')"],
        "answer": "document.createElement('tag')",
        "difficulty": "Easy",
        "explanation": "'createElement' creates a new DOM element with the specified tag name.",
        "category": "The DOM: Adding nodes"
    },
    {
        "question": "What does document.createElement('div') return?",
        "options": ["A new div element", "A text node", "A comment node", "An attribute"],
        "answer": "A new div element",
        "difficulty": "Easy",
        "explanation": "'createElement('div')' returns a new <div> element, not yet added to the DOM.",
        "category": "The DOM: Adding nodes"
    },
    {
        "question": "How do you append a node to an element’s children?",
        "options": ["element.appendChild(node)", "element.addChild(node)", "element.insertChild(node)", "element.append(node)"],
        "answer": "element.appendChild(node)",
        "difficulty": "Easy",
        "explanation": "'appendChild' adds a node as the last child of the specified element.",
        "category": "The DOM: Inserting nodes"
    },
    {
        "question": "How do you insert a node before an existing child?",
        "options": ["parent.insertBefore(newNode, existingNode)", "parent.insertChild(newNode, existingNode)", "parent.addBefore(newNode, existingNode)", "parent.prepend(newNode)"],
        "answer": "parent.insertBefore(newNode, existingNode)",
        "difficulty": "Medium",
        "explanation": "'insertBefore' inserts a new node before the specified existing child in the parent.",
        "category": "The DOM: Inserting nodes"
    },
    {
        "question": "What is a JavaScript object?",
        "options": ["A collection of properties", "A function", "A variable", "A DOM element"],
        "answer": "A collection of properties",
        "difficulty": "Easy",
        "explanation": "A JavaScript object is a collection of key-value pairs, where values can be data or functions.",
        "category": "Objects"
    },
    {
        "question": "How do you access a property of an object?",
        "options": ["object.property or object['property']", "object.getProperty()", "object(property)", "object->property"],
        "answer": "object.property or object['property']",
        "difficulty": "Easy",
        "explanation": "Properties can be accessed using dot notation or bracket notation.",
        "category": "Objects: Properties"
    },
    {
        "question": "How do you add a method to an object?",
        "options": ["object.method = function() {}", "object.addMethod(function)", "object.method(function)", "object.setMethod()"],
        "answer": "object.method = function() {}",
        "difficulty": "Easy",
        "explanation": "A method is added by assigning a function to a property of the object.",
        "category": "Objects: Methods"
    },
    {
        "question": "What is a constructor in JavaScript?",
        "options": ["A function to create objects", "A loop", "An event handler", "A variable"],
        "answer": "A function to create objects",
        "difficulty": "Medium",
        "explanation": "A constructor is a function used with 'new' to create and initialize objects.",
        "category": "Objects: Constructors"
    },
    {
        "question": "What is the output of: ```javascript\nfunction Person(name) { this.name = name; }\nlet p = new Person('Alice');\nconsole.log(p.name);```",
        "options": ["Alice", "Person", "undefined", "null"],
        "answer": "Alice",
        "difficulty": "Medium",
        "explanation": "The constructor 'Person' sets the 'name' property, and 'new' creates an object with that property.",
        "category": "Objects: Constructors"
    },
    {
        "question": "How do you add a method to a constructor’s prototype?",
        "options": ["Constructor.prototype.method = function() {}", "Constructor.method = function() {}", "Constructor.addMethod()", "Constructor.setMethod()"],
        "answer": "Constructor.prototype.method = function() {}",
        "difficulty": "Medium",
        "explanation": "Methods added to the prototype are shared by all instances of the constructor.",
        "category": "Objects: Constructors for methods"
    },
    {
        "question": "What is a prototype in JavaScript?",
        "options": ["An object for inheritance", "A function", "A variable", "A DOM node"],
        "answer": "An object for inheritance",
        "difficulty": "Medium",
        "explanation": "Prototypes are objects from which other objects inherit properties and methods.",
        "category": "Objects: Prototypes"
    },
    {
        "question": "How do you check if an object has a property?",
        "options": ["'property' in object", "object.hasProperty('property')", "object.propertyExists('property')", "object.getProperty('property')"],
        "answer": "'property' in object",
        "difficulty": "Medium",
        "explanation": "The 'in' operator checks if a property exists in an object or its prototype chain.",
        "category": "Objects: Checking for properties and methods"
    },
    {
        "question": "How do you check if a property is directly on an object (not inherited)?",
        "options": ["object.hasOwnProperty('property')", "object.owns('property')", "object.property('property')", "'property' in object"],
        "answer": "object.hasOwnProperty('property')",
        "difficulty": "Medium",
        "explanation": "'hasOwnProperty' checks if a property exists directly on the object, not its prototype.",
        "category": "Objects: Checking for properties and methods"
    },
    {
        "question": "How do you get the current URL of a page?",
        "options": ["window.location.href", "document.url", "window.url", "document.location"],
        "answer": "window.location.href",
        "difficulty": "Easy",
        "explanation": "'window.location.href' returns the full URL of the current page.",
        "category": "Browser control: Getting and setting the URL"
    },
    {
        "question": "How do you set a new URL for the page?",
        "options": ["window.location.href = 'new-url'", "window.url = 'new-url'", "document.location('new-url')", "window.setUrl('new-url')"],
        "answer": "window.location.href = 'new-url'",
        "difficulty": "Easy",
        "explanation": "Assigning a new value to 'window.location.href' navigates to the new URL.",
        "category": "Browser control: Getting and setting the URL"
    },
    {
        "question": "What does window.location.assign('new-url') do?",
        "options": ["Navigates to a new URL", "Reloads the page", "Clears the URL", "Opens a popup"],
        "answer": "Navigates to a new URL",
        "difficulty": "Medium",
        "explanation": "'window.location.assign' navigates to a new URL, similar to setting 'window.location.href'.",
        "category": "Browser control: Getting and setting the URL another way"
    },
    {
        "question": "How do you go back to the previous page?",
        "options": ["window.history.back()", "window.back()", "window.history.prev()", "window.location.back()"],
        "answer": "window.history.back()",
        "difficulty": "Easy",
        "explanation": "'window.history.back()' navigates to the previous page in the browser’s history.",
        "category": "Browser control: Forward and reverse"
    },
    {
        "question": "How do you go forward in browser history?",
        "options": ["window.history.forward()", "window.forward()", "window.history.next()", "window.location.forward()"],
        "answer": "window.history.forward()",
        "difficulty": "Easy",
        "explanation": "'window.history.forward()' navigates to the next page in the browser’s history.",
        "category": "Browser control: Forward and reverse"
    },
    {
        "question": "How do you set the content of the entire page?",
        "options": ["document.body.innerHTML = 'content'", "window.content = 'content'", "document.write('content')", "Both A and C"],
        "answer": "Both A and C",
        "difficulty": "Medium",
        "explanation": "'document.body.innerHTML' and 'document.write' can both set the page’s content, though 'write' is less common.",
        "category": "Browser control: Filling the window with content"
    },
    {
        "question": "How do you resize a browser window?",
        "options": ["window.resizeTo(width, height)", "window.setSize(width, height)", "window.size(width, height)", "document.resize(width, height)"],
        "answer": "window.resizeTo(width, height)",
        "difficulty": "Medium",
        "explanation": "'window.resizeTo' resizes the browser window to the specified dimensions.",
        "category": "Browser control: Controlling the window's size and location"
    },
    {
        "question": "How do you move a window to a specific position?",
        "options": ["window.moveTo(x, y)", "window.setPosition(x, y)", "window.location(x, y)", "window.move(x, y)"],
        "answer": "window.moveTo(x, y)",
        "difficulty": "Medium",
        "explanation": "'window.moveTo' moves the browser window to the specified coordinates.",
        "category": "Browser control: Controlling the window's size and location"
    },
    {
        "question": "How can you detect if popups are blocked?",
        "options": ["Check if window.open() returns null", "Check window.popupBlocked", "Check document.popup", "Check window.isBlocked"],
        "answer": "Check if window.open() returns null",
        "difficulty": "Medium",
        "explanation": "If 'window.open()' returns null, it indicates the popup was blocked by the browser.",
        "category": "Browser control: Testing for popup blockers"
    },
    {
        "question": "How do you validate a text field is not empty?",
        "options": ["input.value.trim() !== ''", "input.text !== ''", "input.value.length > 0", "Both A and C"],
        "answer": "Both A and C",
        "difficulty": "Easy",
        "explanation": "Both checking 'value.length > 0' and 'value.trim() !== ''' validate a non-empty text field, with 'trim()' handling whitespace.",
        "category": "Form validation: text fields"
    },
    {
        "question": "What does input.value.trim() do in form validation?",
        "options": ["Removes whitespace from both ends", "Converts to lowercase", "Removes special characters", "Checks for numbers"],
        "answer": "Removes whitespace from both ends",
        "difficulty": "Easy",
        "explanation": "'trim()' removes leading and trailing whitespace from a string, useful for validating text fields.",
        "category": "Form validation: text fields"
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

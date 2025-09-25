import streamlit as st
import random
from datetime import datetime
import uuid
quiz = [
  {
    "question": "What is the scope of a variable declared with 'var' inside a function?",
    "options": [
      "Function-scoped",
      "Block-scoped",
      "Global-scoped",
      "Module-scoped"
    ],
    "answer": "Function-scoped",
    "difficulty": "Medium",
    "explanation": "'var' declarations are function-scoped, meaning they are accessible throughout the function they are defined in."
  },
  {
    "question": "What happens to a 'let' variable declared inside a block?",
    "options": [
      "It’s only accessible within that block",
      "It’s accessible globally",
      "It’s accessible throughout the function",
      "It’s undefined outside the function"
    ],
    "answer": "It’s only accessible within that block",
    "difficulty": "Medium",
    "explanation": "'let' is block-scoped, so it’s only accessible within the block (e.g., inside curly braces) where it’s declared."
  },
  {
    "question": "What is the output of: function test() { var x = 1; if (true) { var x = 2; } return x; }?",
    "options": [
      "2",
      "1",
      "undefined",
      "Error"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "Since 'var' is function-scoped, the second 'var x = 2' reassigns the same variable, so test() returns 2."
  },
  {
    "question": "What does: let x = 10; { let x = 20; } console.log(x); output?",
    "options": [
      "10",
      "20",
      "undefined",
      "Error"
    ],
    "answer": "10",
    "difficulty": "Medium",
    "explanation": "The 'let x = 20' is block-scoped and doesn’t affect the outer x, so 10 is logged."
  },
  {
    "question": "What is the scope of a variable declared without 'var', 'let', or 'const' in a function?",
    "options": [
      "Global scope",
      "Function scope",
      "Block scope",
      "Module scope"
    ],
    "answer": "Global scope",
    "difficulty": "Medium",
    "explanation": "Variables declared without a keyword in non-strict mode become global, accessible everywhere."
  },
  {
    "question": "How do you validate a text field to ensure it’s not empty?",
    "options": [
      "if (input.value.trim() !== '')",
      "if (input.value === null)",
      "if (input.text !== '')",
      "if (input.length > 0)"
    ],
    "answer": "if (input.value.trim() !== '')",
    "difficulty": "Medium",
    "explanation": "'trim()' removes whitespace, and checking '!== ''' ensures the field isn’t empty."
  },
  {
    "question": "How do you check if a dropdown has a selected option?",
    "options": [
      "if (select.selectedIndex > -1)",
      "if (select.value === null)",
      "if (select.option !== '')",
      "if (select.selected === true)"
    ],
    "answer": "if (select.selectedIndex > -1)",
    "difficulty": "Medium",
    "explanation": "'selectedIndex > -1' confirms an option is selected in a dropdown."
  },
  {
    "question": "How do you validate that a radio button group has a selection?",
    "options": [
      "document.querySelector('input[name=group]:checked')",
      "document.getElementByName('group').checked",
      "document.querySelector('input.group:checked')",
      "document.getRadio('group').selected"
    ],
    "answer": "document.querySelector('input[name=group]:checked')",
    "difficulty": "Medium",
    "explanation": "The selector returns the checked radio button, or null if none is selected."
  },
  {
    "question": "What regex validates a 5-digit ZIP code?",
    "options": [
      "/^\\d{5}$/",
      "/^\\d{5}-\\d{4}$/",
      "/^\\d{9}$/",
      "/^\\d{5}(-\\d{4})?$/"
    ],
    "answer": "/^\\d{5}$/",
    "difficulty": "Medium",
    "explanation": "'/^\\d{5}$/' ensures exactly 5 digits, suitable for a basic ZIP code."
  },
  {
    "question": "What regex validates an email address format?",
    "options": [
      "/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/",
      "/^\\w+@\\w+\\.com$/",
      "/^[^\\s@]+@[^\\s@]+$/",
      "/^\\w+\\.\\w+@\\w+$/"
    ],
    "answer": "/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/",
    "difficulty": "Medium",
    "explanation": "This regex ensures a valid email format with a username, @, domain, and top-level domain."
  },
  {
    "question": "What does try { let x = y; } catch (e) { console.log(e.name); } log?",
    "options": [
      "ReferenceError",
      "TypeError",
      "SyntaxError",
      "undefined"
    ],
    "answer": "ReferenceError",
    "difficulty": "Medium",
    "explanation": "Accessing an undefined variable 'y' throws a ReferenceError, caught and logged."
  },
  {
    "question": "What does throw new Error('Invalid') do?",
    "options": [
      "Throws a custom error",
      "Logs 'Invalid'",
      "Stops the function",
      "Returns 'Invalid'"
    ],
    "answer": "Throws a custom error",
    "difficulty": "Medium",
    "explanation": "'throw new Error()' creates and throws a custom error with the specified message."
  },
  {
    "question": "How do you handle a click event on a button?",
    "options": [
      "button.addEventListener('click', handler)",
      "button.onClick(handler)",
      "button.event('click', handler)",
      "button.click(handler)"
    ],
    "answer": "button.addEventListener('click', handler)",
    "difficulty": "Medium",
    "explanation": "'addEventListener()' attaches a handler function to the button’s click event."
  },
  {
    "question": "What does node.nodeType === 1 indicate?",
    "options": [
      "Element node",
      "Text node",
      "Comment node",
      "Document node"
    ],
    "answer": "Element node",
    "difficulty": "Medium",
    "explanation": "A 'nodeType' of 1 indicates an HTML element node in the DOM."
  },
  {
    "question": "How do you select elements with class 'test' using querySelectorAll?",
    "options": [
      "document.querySelectorAll('.test')",
      "document.getElementsByClassName('test')",
      "document.querySelector('.test')",
      "Both querySelectorAll and getElementsByClassName"
    ],
    "answer": "Both querySelectorAll and getElementsByClassName",
    "difficulty": "Medium",
    "explanation": "Both methods select elements with the class 'test'; querySelectorAll uses CSS selectors."
  },
  {
    "question": "What does element.tagName return for a <p> element?",
    "options": [
      "P",
      "p",
      "Paragraph",
      "undefined"
    ],
    "answer": "P",
    "difficulty": "Medium",
    "explanation": "'tagName' returns the tag name in uppercase, so 'P' for a <p> element."
  },
  {
    "question": "How do you count the number of child elements in a node?",
    "options": [
      "element.children.length",
      "element.childNodes.length",
      "element.countChildren()",
      "element.getNodes()"
    ],
    "answer": "element.children.length",
    "difficulty": "Medium",
    "explanation": "'children.length' counts only HTML element children, excluding text or comments."
  },
  {
    "question": "How do you get an element’s attribute value?",
    "options": [
      "element.getAttribute('name')",
      "element.attribute('name')",
      "element.name",
      "element.getAttr('name')"
    ],
    "answer": "element.getAttribute('name')",
    "difficulty": "Medium",
    "explanation": "'getAttribute()' retrieves the value of the specified attribute."
  },
  {
    "question": "How do you set an attribute on an element?",
    "options": [
      "element.setAttribute('name', 'value')",
      "element.attribute = 'value'",
      "element.name = 'value'",
      "element.setAttr('name', 'value')"
    ],
    "answer": "element.setAttribute('name', 'value')",
    "difficulty": "Medium",
    "explanation": "'setAttribute()' sets the value of a specified attribute on an element."
  },
  {
    "question": "How do you create a new <span> element?",
    "options": [
      "document.createElement('span')",
      "document.newElement('span')",
      "document.create('span')",
      "document.addElement('span')"
    ],
    "answer": "document.createElement('span')",
    "difficulty": "Medium",
    "explanation": "'createElement('span')' creates a new <span> element node."
  },
  {
    "question": "How do you insert a node before an existing node?",
    "options": [
      "parent.insertBefore(newNode, referenceNode)",
      "parent.appendChild(newNode)",
      "parent.insertAfter(newNode)",
      "parent.addNode(newNode)"
    ],
    "answer": "parent.insertBefore(newNode, referenceNode)",
    "difficulty": "Medium",
    "explanation": "'insertBefore()' inserts a new node before the specified reference node."
  },
  {
    "question": "What is a JavaScript object?",
    "options": [
      "A collection of key-value pairs",
      "A type of array",
      "A function declaration",
      "A loop structure"
    ],
    "answer": "A collection of key-value pairs",
    "difficulty": "Medium",
    "explanation": "An object in JavaScript stores data as key-value pairs, also called properties."
  },
  {
    "question": "How do you access an object’s property?",
    "options": [
      "object.property or object['property']",
      "object.getProperty('property')",
      "object(property)",
      "object::property"
    ],
    "answer": "object.property or object['property']",
    "difficulty": "Medium",
    "explanation": "Properties are accessed using dot notation or bracket notation."
  },
  {
    "question": "What is an object method in JavaScript?",
    "options": [
      "A function stored as a property",
      "A variable inside an object",
      "A loop inside an object",
      "A class definition"
    ],
    "answer": "A function stored as a property",
    "difficulty": "Medium",
    "explanation": "A method is a function assigned to an object’s property, enabling behavior."
  },
  {
    "question": "What does this constructor do: function Car(model) { this.model = model; }?",
    "options": [
      "Creates objects with a model property",
      "Creates an array of models",
      "Defines a loop",
      "Throws an error"
    ],
    "answer": "Creates objects with a model property",
    "difficulty": "Medium",
    "explanation": "The constructor creates objects with a 'model' property when called with 'new'."
  },
  {
    "question": "How do you add a method to a constructor’s prototype?",
    "options": [
      "Constructor.prototype.method = function() {}",
      "Constructor.method = function() {}",
      "Constructor.addMethod(function() {})",
      "Constructor.setMethod(function() {})"
    ],
    "answer": "Constructor.prototype.method = function() {}",
    "difficulty": "Medium",
    "explanation": "Adding a method to the prototype makes it available to all instances."
  },
  {
    "question": "What is the purpose of an object’s prototype?",
    "options": [
      "To share properties and methods across instances",
      "To store private data",
      "To create loops",
      "To validate forms"
    ],
    "answer": "To share properties and methods across instances",
    "difficulty": "Medium",
    "explanation": "Prototypes allow instances of a constructor to share properties and methods."
  },
  {
    "question": "How do you check if an object has a specific property?",
    "options": [
      "object.hasOwnProperty('prop')",
      "object.exists('prop')",
      "object.checkProperty('prop')",
      "object.get('prop')"
    ],
    "answer": "object.hasOwnProperty('prop')",
    "difficulty": "Medium",
    "explanation": "'hasOwnProperty()' checks if a property exists directly on the object."
  },
  {
    "question": "What does window.location.href return?",
    "options": [
      "The full URL of the current page",
      "The page title",
      "The domain name only",
      "The query string"
    ],
    "answer": "The full URL of the current page",
    "difficulty": "Medium",
    "explanation": "'window.location.href' returns the complete URL of the current webpage."
  },
  {
    "question": "What does window.location.assign('new-url') do?",
    "options": [
      "Navigates to a new URL",
      "Reloads the current page",
      "Opens a new tab",
      "Changes the page title"
    ],
    "answer": "Navigates to a new URL",
    "difficulty": "Medium",
    "explanation": "'location.assign()' loads a new URL in the current window."
  },
  {
    "question": "What does window.history.back() do?",
    "options": [
      "Navigates to the previous page",
      "Navigates to the next page",
      "Reloads the current page",
      "Opens a new window"
    ],
    "answer": "Navigates to the previous page",
    "difficulty": "Medium",
    "explanation": "'history.back()' moves to the previous page in the browser’s history."
  },
  {
    "question": "How do you make an element fill the entire viewport?",
    "options": [
      "element.style.width = '100vw'; element.style.height = '100vh'",
      "element.style.width = '100%'; element.style.height = '100%'",
      "element.setSize('full')",
      "element.style.fullscreen = true"
    ],
    "answer": "element.style.width = '100vw'; element.style.height = '100vh'",
    "difficulty": "Medium",
    "explanation": "'100vw' and '100vh' set the element to the full viewport width and height."
  },
  {
    "question": "What does window.resizeTo(800, 600) do?",
    "options": [
      "Resizes the window to 800x600 pixels",
      "Moves the window to (800, 600)",
      "Scrolls the window",
      "Sets the viewport size"
    ],
    "answer": "Resizes the window to 800x600 pixels",
    "difficulty": "Medium",
    "explanation": "'window.resizeTo()' sets the browser window’s dimensions to the specified width and height."
  },
  {
    "question": "How do you test for a popup blocker?",
    "options": [
      "if (!window.open('url'))",
      "if (window.isBlocked())",
      "if (window.popup === null)",
      "if (document.popupBlocked)"
    ],
    "answer": "if (!window.open('url'))",
    "difficulty": "Medium",
    "explanation": "'window.open()' returns null if a popup blocker prevents the window from opening."
  },
  {
    "question": "How do you validate a text field for a minimum length of 5 characters?",
    "options": [
      "if (input.value.length >= 5)",
      "if (input.text.length >= 5)",
      "if (input.value >= 5)",
      "if (input.length >= 5)"
    ],
    "answer": "if (input.value.length >= 5)",
    "difficulty": "Medium",
    "explanation": "Checking 'input.value.length >= 5' ensures the text field has at least 5 characters."
  },
  {
    "question": "What happens if you access a variable declared later with 'let'?",
    "options": [
      "ReferenceError due to temporal dead zone",
      "undefined",
      "null",
      "The variable’s value"
    ],
    "answer": "ReferenceError due to temporal dead zone",
    "difficulty": "Medium",
    "explanation": "'let' variables are in a temporal dead zone until their declaration, causing a ReferenceError."
  },
  {
    "question": "What is the output of: function test() { let x = 1; { let x = 2; } return x; }?",
    "options": [
      "1",
      "2",
      "undefined",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "The inner 'let x = 2' is block-scoped, so the outer x remains 1."
  },
  {
    "question": "What does 'use strict' do to undeclared variables?",
    "options": [
      "Prevents them, throwing ReferenceError",
      "Makes them global",
      "Assigns them null",
      "Ignores them"
    ],
    "answer": "Prevents them, throwing ReferenceError",
    "difficulty": "Medium",
    "explanation": "In strict mode, assigning to an undeclared variable throws a ReferenceError."
  },
  {
    "question": "How do you validate a dropdown’s selected value isn’t the default placeholder?",
    "options": [
      "if (select.value !== '')",
      "if (select.value === null)",
      "if (select.selectedIndex === 0)",
      "if (select.option === '')"
    ],
    "answer": "if (select.value !== '')",
    "difficulty": "Medium",
    "explanation": "Checking 'value !== ''' ensures a non-empty, non-placeholder option is selected."
  },
  {
    "question": "How do you get the value of a selected radio button?",
    "options": [
      "document.querySelector('input[name=group]:checked').value",
      "document.getElementByName('group').value",
      "document.querySelector('input.group').value",
      "document.getRadio('group').value"
    ],
    "answer": "document.querySelector('input[name=group]:checked').value",
    "difficulty": "Medium",
    "explanation": "The selector retrieves the checked radio button’s value."
  },
  {
    "question": "What regex allows a ZIP code like 12345 or 12345-6789?",
    "options": [
      "/^\\d{5}(-\\d{4})?$/",
      "/^\\d{5}$/",
      "/^\\d{5}-\\d{4}$/",
      "/^\\d{9}$/"
    ],
    "answer": "/^\\d{5}(-\\d{4})?$/",
    "difficulty": "Medium",
    "explanation": "The regex matches 5 digits with an optional hyphen and 4 digits."
  },
  {
    "question": "What does try { JSON.parse('invalid') } catch (e) { console.log(e.name); } log?",
    "options": [
      "SyntaxError",
      "ReferenceError",
      "TypeError",
      "undefined"
    ],
    "answer": "SyntaxError",
    "difficulty": "Medium",
    "explanation": "Invalid JSON in 'JSON.parse()' throws a SyntaxError, caught and logged."
  },
  {
    "question": "What does throw 'Custom error' do?",
    "options": [
      "Throws a string as an error",
      "Logs the string",
      "Returns the string",
      "Stops execution without error"
    ],
    "answer": "Throws a string as an error",
    "difficulty": "Medium",
    "explanation": "'throw' can throw any value, like a string, but 'new Error' is preferred for errors."
  },
  {
    "question": "How do you handle a mouseover event on an element?",
    "options": [
      "element.addEventListener('mouseover', handler)",
      "element.onMouseover(handler)",
      "element.event('mouseover', handler)",
      "element.mouseover(handler)"
    ],
    "answer": "element.addEventListener('mouseover', handler)",
    "difficulty": "Medium",
    "explanation": "'addEventListener()' attaches a handler to the 'mouseover' event."
  },
  {
    "question": "What does node.nodeType === 8 indicate?",
    "options": [
      "Comment node",
      "Element node",
      "Text node",
      "Document node"
    ],
    "answer": "Comment node",
    "difficulty": "Medium",
    "explanation": "A 'nodeType' of 8 indicates a comment node (e.g., <!-- comment -->) in the DOM."
  },
  {
    "question": "How do you select elements with data-test attribute?",
    "options": [
      "document.querySelectorAll('[data-test]')",
      "document.getElementsByAttribute('data-test')",
      "document.querySelector('data-test')",
      "document.getDataTest()"
    ],
    "answer": "document.querySelectorAll('[data-test]')",
    "difficulty": "Medium",
    "explanation": "'querySelectorAll()' uses CSS selector syntax to select elements with the data-test attribute."
  },
  {
    "question": "What does element.tagName return for a <div> element?",
    "options": [
      "DIV",
      "div",
      "Div",
      "undefined"
    ],
    "answer": "DIV",
    "difficulty": "Medium",
    "explanation": "'tagName' returns the tag name in uppercase, so 'DIV' for a <div> element."
  },
  {
    "question": "How do you count all child nodes, including text and comments?",
    "options": [
      "element.childNodes.length",
      "element.children.length",
      "element.countNodes()",
      "element.getChildren()"
    ],
    "answer": "element.childNodes.length",
    "difficulty": "Medium",
    "explanation": "'childNodes.length' counts all nodes, including text and comment nodes."
  },
  {
    "question": "How do you check if an element has a specific attribute?",
    "options": [
      "element.hasAttribute('name')",
      "element.getAttribute('name')",
      "element.attribute('name')",
      "element.checkAttribute('name')"
    ],
    "answer": "element.hasAttribute('name')",
    "difficulty": "Medium",
    "explanation": "'hasAttribute()' returns true if the element has the specified attribute."
  },
  {
    "question": "How do you remove an attribute from an element?",
    "options": [
      "element.removeAttribute('name')",
      "element.deleteAttribute('name')",
      "element.setAttribute('name', null)",
      "element.attribute = null"
    ],
    "answer": "element.removeAttribute('name')",
    "difficulty": "Medium",
    "explanation": "'removeAttribute()' removes the specified attribute from an element."
  },
  {
    "question": "How do you append a new node to an element?",
    "options": [
      "parent.appendChild(newNode)",
      "parent.insertChild(newNode)",
      "parent.addNode(newNode)",
      "parent.append(newNode)"
    ],
    "answer": "parent.appendChild(newNode)",
    "difficulty": "Medium",
    "explanation": "'appendChild()' adds a new node as the last child of the parent element."
  },
  {
    "question": "How do you insert a node after an existing node?",
    "options": [
      "parent.insertBefore(newNode, referenceNode.nextSibling)",
      "parent.appendChild(newNode)",
      "parent.insertAfter(newNode)",
      "parent.addNode(newNode)"
    ],
    "answer": "parent.insertBefore(newNode, referenceNode.nextSibling)",
    "difficulty": "Medium",
    "explanation": "'insertBefore()' with 'nextSibling' inserts a node after the reference node."
  },
  {
    "question": "What does let obj = { a: 1, b: 2 }; console.log(obj.a); output?",
    "options": [
      "1",
      "undefined",
      "a",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "The property 'a' is accessed using dot notation, logging its value, 1."
  },
  {
    "question": "How do you add a new property to an object?",
    "options": [
      "obj.newProp = 'value'",
      "obj.addProp('value')",
      "obj.set('newProp', 'value')",
      "obj.createProp('value')"
    ],
    "answer": "obj.newProp = 'value'",
    "difficulty": "Medium",
    "explanation": "Properties are added using dot notation or bracket notation, e.g., obj['newProp'] = 'value'."
  },
  {
    "question": "What does this do: let obj = { say() { return 'Hi'; } }; console.log(obj.say());?",
    "options": [
      "Logs 'Hi'",
      "Logs undefined",
      "Logs say",
      "Throws an error"
    ],
    "answer": "Logs 'Hi'",
    "difficulty": "Medium",
    "explanation": "'say' is a method that returns 'Hi' when called."
  },
  {
    "question": "What is the output of: function User(name) { this.name = name; } let u = new User('Bob'); console.log(u.name);?",
    "options": [
      "Bob",
      "User",
      "undefined",
      "Error"
    ],
    "answer": "Bob",
    "difficulty": "Medium",
    "explanation": "The constructor sets the 'name' property, accessed as u.name."
  },
  {
    "question": "How do you define a method in a constructor?",
    "options": [
      "this.method = function() {}",
      "method: function() {}",
      "function method() {}",
      "method = function() {}"
    ],
    "answer": "this.method = function() {}",
    "difficulty": "Medium",
    "explanation": "Methods are defined in a constructor using 'this' to attach them to instances."
  },
  {
    "question": "What does Object.prototype.hasOwnProperty.call(obj, 'prop') do?",
    "options": [
      "Checks if 'prop' exists on obj",
      "Adds 'prop' to obj",
      "Calls the 'prop' method",
      "Removes 'prop' from obj"
    ],
    "answer": "Checks if 'prop' exists on obj",
    "difficulty": "Medium",
    "explanation": "This safely checks if 'prop' is a direct property, avoiding issues with overridden methods."
  },
  {
    "question": "What does window.location.search return?",
    "options": [
      "The query string of the URL",
      "The full URL",
      "The domain name",
      "The path of the URL"
    ],
    "answer": "The query string of the URL",
    "difficulty": "Medium",
    "explanation": "'window.location.search' returns the query string, starting with '?'."
  },
  {
    "question": "What does window.history.forward() do?",
    "options": [
      "Navigates to the next page in history",
      "Goes back one page",
      "Reloads the page",
      "Opens a new tab"
    ],
    "answer": "Navigates to the next page in history",
    "difficulty": "Medium",
    "explanation": "'history.forward()' moves to the next page in the browser’s history."
  },
  {
    "question": "How do you set an element to full viewport width?",
    "options": [
      "element.style.width = '100vw'",
      "element.style.width = '100%'",
      "element.setWidth('full')",
      "element.style.width = '100vh'"
    ],
    "answer": "element.style.width = '100vw'",
    "difficulty": "Medium",
    "explanation": "'100vw' sets the element’s width to the full viewport width."
  },
  {
    "question": "What does window.moveTo(200, 200) do?",
    "options": [
      "Moves the window to coordinates (200, 200)",
      "Resizes the window",
      "Scrolls the window",
      "Opens a new window"
    ],
    "answer": "Moves the window to coordinates (200, 200)",
    "difficulty": "Medium",
    "explanation": "'window.moveTo()' repositions the browser window to the specified coordinates."
  },
  {
    "question": "How do you validate a text field for only alphabetic characters?",
    "options": [
      "/^[a-zA-Z]+$/.test(input.value)",
      "/^\\d+$/.test(input.value)",
      "/^[a-zA-Z0-9]+$/.test(input.value)",
      "/^\\w+$/.test(input.value)"
    ],
    "answer": "/^[a-zA-Z]+$/.test(input.value)",
    "difficulty": "Medium",
    "explanation": "The regex '/^[a-zA-Z]+$/' ensures the input contains only letters."
  },
  {
    "question": "What is the output of: let x = 5; function test() { let x = 10; return x; } console.log(test(), x);?",
    "options": [
      "10, 5",
      "5, 10",
      "10, 10",
      "5, 5"
    ],
    "answer": "10, 5",
    "difficulty": "Medium",
    "explanation": "The inner 'let x = 10' is function-scoped, so test() returns 10; the outer x remains 5."
  },
  {
    "question": "How do you validate a dropdown to ensure a specific value is selected?",
    "options": [
      "if (select.value === 'specific')",
      "if (select.selectedIndex === 'specific')",
      "if (select.option === 'specific')",
      "if (select.value === null)"
    ],
    "answer": "if (select.value === 'specific')",
    "difficulty": "Medium",
    "explanation": "Checking 'select.value' ensures the dropdown’s selected option matches 'specific'."
  },
  {
    "question": "How do you get all radio buttons in a group?",
    "options": [
      "document.querySelectorAll('input[name=group]')",
      "document.getElementsByName('group').checked",
      "document.querySelector('input.group')",
      "document.getRadios('group')"
    ],
    "answer": "document.querySelectorAll('input[name=group]')",
    "difficulty": "Medium",
    "explanation": "'querySelectorAll()' selects all radio buttons with the same 'name' attribute."
  },
  {
    "question": "What regex validates a 9-digit ZIP code?",
    "options": [
      "/^\\d{9}$/",
      "/^\\d{5}$/",
      "/^\\d{5}-\\d{4}$/",
      "/^\\d{5}(-\\d{4})?$/"
    ],
    "answer": "/^\\d{9}$/",
    "difficulty": "Medium",
    "explanation": "'/^\\d{9}$/' matches exactly 9 digits for a ZIP+4 code without a hyphen."
  },
  {
    "question": "What does try { null.a; } catch (e) { console.log(e.name); } log?",
    "options": [
      "TypeError",
      "ReferenceError",
      "SyntaxError",
      "undefined"
    ],
    "answer": "TypeError",
    "difficulty": "Medium",
    "explanation": "Accessing a property on null throws a TypeError, caught and logged."
  },
  {
    "question": "How do you throw a custom error with additional data?",
    "options": [
      "throw new Error('Message', { data: value })",
      "throw 'Message' + data",
      "throw new Error('Message')",
      "throw { message: 'Message', data: value }"
    ],
    "answer": "throw { message: 'Message', data: value }",
    "difficulty": "Medium",
    "explanation": "Throwing an object allows attaching custom data, caught as the error object."
  },
  {
    "question": "How do you handle a double-click event?",
    "options": [
      "element.addEventListener('dblclick', handler)",
      "element.onDoubleClick(handler)",
      "element.event('dblclick', handler)",
      "element.doubleClick(handler)"
    ],
    "answer": "element.addEventListener('dblclick', handler)",
    "difficulty": "Medium",
    "explanation": "'addEventListener()' attaches a handler to the 'dblclick' event."
  },
  {
    "question": "What does node.nodeType === 3 indicate?",
    "options": [
      "Text node",
      "Element node",
      "Comment node",
      "Document node"
    ],
    "answer": "Text node",
    "difficulty": "Medium",
    "explanation": "A 'nodeType' of 3 indicates a text node in the DOM."
  },
  {
    "question": "How do you select the first element with a specific class?",
    "options": [
      "document.querySelector('.class')",
      "document.querySelectorAll('.class')[0]",
      "document.getElementsByClassName('class')[0]",
      "Both querySelector and getElementsByClassName"
    ],
    "answer": "Both querySelector and getElementsByClassName",
    "difficulty": "Medium",
    "explanation": "Both methods can select the first element with a class; querySelector uses CSS syntax."
  },
  {
    "question": "How do you get the attribute names of an element?",
    "options": [
      "Array.from(element.attributes).map(attr => attr.name)",
      "element.getAttributes()",
      "element.attributeNames()",
      "element.listAttributes()"
    ],
    "answer": "Array.from(element.attributes).map(attr => attr.name)",
    "difficulty": "Medium",
    "explanation": "'element.attributes' is a NamedNodeMap; convert to array and map to names."
  },
  {
    "question": "How do you replace a node in the DOM?",
    "options": [
      "parent.replaceChild(newNode, oldNode)",
      "parent.swapNode(newNode, oldNode)",
      "parent.replace(newNode, oldNode)",
      "parent.changeNode(newNode)"
    ],
    "answer": "parent.replaceChild(newNode, oldNode)",
    "difficulty": "Medium",
    "explanation": "'replaceChild()' replaces an existing child node with a new one."
  },
  {
    "question": "What does delete obj.prop do?",
    "options": [
      "Removes the 'prop' property from obj",
      "Sets 'prop' to null",
      "Sets 'prop' to undefined",
      "Throws an error"
    ],
    "answer": "Removes the 'prop' property from obj",
    "difficulty": "Medium",
    "explanation": "The 'delete' operator removes a property from an object."
  },
  {
    "question": "What is the output of: let obj = { x: 10 }; obj.x = 20; console.log(obj.x);?",
    "options": [
      "20",
      "10",
      "undefined",
      "Error"
    ],
    "answer": "20",
    "difficulty": "Medium",
    "explanation": "Assigning to obj.x updates the property value to 20."
  },
  {
    "question": "What does window.location.pathname return?",
    "options": [
      "The path of the URL",
      "The full URL",
      "The query string",
      "The domain name"
    ],
    "answer": "The path of the URL",
    "difficulty": "Medium",
    "explanation": "'window.location.pathname' returns the path portion of the URL, e.g., '/page'."
  },
  {
    "question": "How do you validate a text field for a maximum length of 10 characters?",
    "options": [
      "if (input.value.length <= 10)",
      "if (input.text.length <= 10)",
      "if (input.value <= 10)",
      "if (input.length <= 10)"
    ],
    "answer": "if (input.value.length <= 10)",
    "difficulty": "Medium",
    "explanation": "Checking 'input.value.length <= 10' ensures the text field has 10 or fewer characters."
  },
  {
    "question": "What is the output of: function test() { var x = 1; { var x = 2; } return x; }?",
    "options": [
      "2",
      "1",
      "undefined",
      "Error"
    ],
    "answer": "2",
    "difficulty": "Medium",
    "explanation": "'var' is function-scoped, so the inner 'var x = 2' reassigns the same variable."
  },
  {
    "question": "How do you validate a dropdown’s selected option has a specific attribute?",
    "options": [
      "if (select.options[select.selectedIndex].hasAttribute('data-valid'))",
      "if (select.value.hasAttribute('data-valid'))",
      "if (select.option.getAttribute('data-valid'))",
      "if (select.selected.hasAttribute('data-valid'))"
    ],
    "answer": "if (select.options[select.selectedIndex].hasAttribute('data-valid'))",
    "difficulty": "Medium",
    "explanation": "'options[selectedIndex]' accesses the selected option to check for attributes."
  },
  {
    "question": "How do you check if no radio button is selected in a group?",
    "options": [
      "if (!document.querySelector('input[name=group]:checked'))",
      "if (document.querySelector('input[name=group]').checked === false)",
      "if (document.getElementByName('group').value === null)",
      "if (document.querySelector('input.group') === null)"
    ],
    "answer": "if (!document.querySelector('input[name=group]:checked'))",
    "difficulty": "Medium",
    "explanation": "If no radio button is checked, the selector returns null, so '!selector' is true."
  },
  {
    "question": "What does try { undefined.b; } catch (e) { console.log(e.name); } log?",
    "options": [
      "TypeError",
      "ReferenceError",
      "SyntaxError",
      "undefined"
    ],
    "answer": "TypeError",
    "difficulty": "Medium",
    "explanation": "Accessing a property on undefined throws a TypeError, caught and logged."
  },
  {
    "question": "How do you handle a keypress event on an input?",
    "options": [
      "input.addEventListener('keypress', handler)",
      "input.onKeypress(handler)",
      "input.event('keypress', handler)",
      "input.keypress(handler)"
    ],
    "answer": "input.addEventListener('keypress', handler)",
    "difficulty": "Medium",
    "explanation": "'addEventListener()' attaches a handler to the 'keypress' event."
  },
  {
    "question": "How do you get the value of a custom attribute?",
    "options": [
      "element.getAttribute('data-custom')",
      "element.data.custom",
      "element.getData('custom')",
      "element.customAttribute"
    ],
    "answer": "element.getAttribute('data-custom')",
    "difficulty": "Medium",
    "explanation": "'getAttribute()' retrieves the value of a custom attribute like 'data-custom'."
  },
  {
    "question": "What does document.createElement('div').appendChild(document.createTextNode('text')) do?",
    "options": [
      "Creates a div with a text node 'text'",
      "Creates a div with a child div",
      "Creates a text node only",
      "Throws an error"
    ],
    "answer": "Creates a div with a text node 'text'",
    "difficulty": "Medium",
    "explanation": "'createElement()' and 'createTextNode()' create a div containing the text 'text'."
  },
  {
    "question": "What does 'in' operator do with objects?",
    "options": [
      "Checks if a property exists in an object or its prototype",
      "Checks if a property is undefined",
      "Adds a property to an object",
      "Removes a property from an object"
    ],
    "answer": "Checks if a property exists in an object or its prototype",
    "difficulty": "Medium",
    "explanation": "The 'in' operator returns true if the property exists on the object or its prototype chain."
  },
  {
    "question": "What does window.location.reload() do?",
    "options": [
      "Reloads the current page",
      "Navigates to a new URL",
      "Opens a new window",
      "Goes back one page"
    ],
    "answer": "Reloads the current page",
    "difficulty": "Medium",
    "explanation": "'location.reload()' refreshes the current page."
  },
  {
    "question": "How do you validate a text field for only numbers?",
    "options": [
      "/^\\d+$/.test(input.value)",
      "/^[a-zA-Z]+$/.test(input.value)",
      "/^\\w+$/.test(input.value)",
      "/^[0-9a-zA-Z]+$/.test(input.value)"
    ],
    "answer": "/^\\d+$/.test(input.value)",
    "difficulty": "Medium",
    "explanation": "The regex '/^\\d+$/' ensures the input contains only digits."
  },
  {
    "question": "What is the output of: let x = 1; { let x = 2; { let x = 3; } } console.log(x);?",
    "options": [
      "1",
      "2",
      "3",
      "Error"
    ],
    "answer": "1",
    "difficulty": "Medium",
    "explanation": "Each 'let x' is block-scoped; the outermost x remains 1 and is logged."
  },
  {
    "question": "How do you validate a dropdown for multiple selections?",
    "options": [
      "if (select.selectedOptions.length > 0)",
      "if (select.value.length > 0)",
      "if (select.options.length > 0)",
      "if (select.multiple === true)"
    ],
    "answer": "if (select.selectedOptions.length > 0)",
    "difficulty": "Medium",
    "explanation": "'selectedOptions.length' checks the number of selected options in a multiple select."
  },
  {
    "question": "How do you set a radio button as checked?",
    "options": [
      "radio.checked = true",
      "radio.value = true",
      "radio.setChecked(true)",
      "radio.select = true"
    ],
    "answer": "radio.checked = true",
    "difficulty": "Medium",
    "explanation": "Setting 'checked = true' selects the radio button programmatically."
  },
  {
    "question": "What does try { throw new Error('Test'); } catch (e) { console.log(e.message); } log?",
    "options": [
      "Test",
      "Error",
      "undefined",
      "TypeError"
    ],
    "answer": "Test",
    "difficulty": "Medium",
    "explanation": "The thrown error’s message, 'Test', is caught and logged."
  },
  {
    "question": "How do you handle a form’s submit event?",
    "options": [
      "form.addEventListener('submit', handler)",
      "form.onSubmit(handler)",
      "form.event('submit', handler)",
      "form.submit(handler)"
    ],
    "answer": "form.addEventListener('submit', handler)",
    "difficulty": "Medium",
    "explanation": "'addEventListener()' attaches a handler to the form’s 'submit' event."
  },
  {
    "question": "How do you remove a node from the DOM?",
    "options": [
      "parent.removeChild(node)",
      "node.delete()",
      "node.removeNode()",
      "parent.deleteChild(node)"
    ],
    "answer": "parent.removeChild(node)",
    "difficulty": "Medium",
    "explanation": "'removeChild()' removes a specified child node from its parent."
  },
  {
    "question": "What does Object.keys(obj).length return?",
    "options": [
      "The number of own properties in obj",
      "The number of prototype properties",
      "The number of methods in obj",
      "The total number of keys in obj"
    ],
    "answer": "The number of own properties in obj",
    "difficulty": "Medium",
    "explanation": "'Object.keys()' returns an array of an object’s own property names, and 'length' counts them."
  },
  {
    "question": "What does window.location.replace('new-url') do?",
    "options": [
      "Navigates to a new URL without adding to history",
      "Adds the URL to history",
      "Reloads the current page",
      "Opens a new tab"
    ],
    "answer": "Navigates to a new URL without adding to history",
    "difficulty": "Medium",
    "explanation": "'location.replace()' navigates to a new URL without creating a new history entry."
  }
]
# Quiz data
quiz = 

# Cache shuffled quiz with a fixed key
@st.cache_data
def shuffle_quiz(_quiz, seed=42):
    random.seed(seed)  # Ensure consistent shuffling for caching
    shuffled = random.sample(_quiz, len(_quiz))
    for q in shuffled:
        q["id"] = str(uuid.uuid4())
        q["display_options"] = q["options"].copy()
        random.seed(seed + int(q["id"].replace("-", ""), 16))  # Unique seed per question
        random.shuffle(q["display_options"])
        q["labeled_answer"] = q["answer"]
    return shuffled

# Initialize session state with minimal data
if "initialized" not in st.session_state:
    if not quiz:
        st.error("Quiz list is empty! Please check the quiz data.")
        st.stop()
    st.session_state.update({
        "initialized": True,
        "quiz_data": shuffle_quiz(quiz),
        "score": 0,
        "current_q": 0,
        "start_time": None,
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 30 * len(quiz),  # 30 seconds per question
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
    st.rerun()

# Timer logic
def update_timer():
    if not st.session_state.paused and st.session_state.start_time:
        elapsed = (datetime.now() - st.session_state.start_time).total_seconds()
        st.session_state.time_left = max(30 * len(quiz) - elapsed, 0)
        if st.session_state.time_left <= 0:
            st.session_state.show_results = True
            st.rerun()

# Pause/Resume quiz
def toggle_pause():
    if st.session_state.paused:
        pause_duration = (datetime.now() - st.session_state.pause_time).total_seconds()
        st.session_state.start_time += pause_duration
        st.session_state.paused = False
    else:
        st.session_state.paused = True
        st.session_state.pause_time = datetime.now()
    st.rerun()

# Reset quiz
def reset_quiz():
    st.session_state.update({
        "initialized": True,
        "quiz_data": shuffle_quiz(quiz),
        "score": 0,
        "current_q": 0,
        "start_time": None,
        "answers": [None] * len(quiz),
        "show_results": False,
        "selected_option": None,
        "feedback": None,
        "time_left": 30 * len(quiz),
        "streak": 0,
        "max_streak": 0,
        "started": False,
        "paused": False,
        "pause_time": None
    })
    st.rerun()

# CSS for UI (minimized for performance)
st.markdown("""
<style>
:root {
    --bg-container: #2c2c54;
    --text-color: #ffffff;
    --button-bg: #6b21a8;
    --button-hover: #8b5cf6;
    --code-bg: #1e1e1e;
    --shadow: rgba(0,0,0,0.3);
}
[data-theme="light"] {
    --bg-container: #ffffff;
    --text-color: #1f2937;
    --button-bg: #4f46e5;
    --button-hover: #6366f1;
    --code-bg: #f1f5f9;
    --shadow: rgba(0,0,0,0.1);
}
.main-container {
    background: var(--bg-container);
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 2px 10px var(--shadow);
    max-width: 700px;
    margin: 10px auto;
}
.stButton>button {
    background: var(--button-bg);
    color: var(--text-color);
    border: none;
    border-radius: 6px;
    padding: 8px;
    width: 100%;
    font-size: 13px;
    margin: 4px 0;
    cursor: pointer;
    transition: all 0.2s ease;
}
.stButton>button:hover:not(:disabled) {
    background: var(--button-hover);
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
    padding: 10px;
    border-radius: 6px;
}
.feedback-correct {
    color: #34c759;
    font-weight: 600;
    font-size: 14px;
    margin: 8px 0;
}
.feedback-wrong {
    color: #ff3b30;
    font-weight: 600;
    font-size: 14px;
    margin: 8px 0;
}
.progress-bar {
    background: #4b4b6b;
    border-radius: 6px;
    height: 8px;
    margin: 6px 0;
    position: relative;
}
.progress-fill {
    background: var(--button-bg);
    height: 100%;
    border-radius: 6px;
}
.progress-text {
    position: absolute;
    top: -16px;
    right: 0;
    color: var(--text-color);
    font-size: 10px;
}
.title {
    font-size: 24px;
    text-align: center;
    margin-bottom: 5px;
    color: var(--text-color);
}
.caption {
    text-align: center;
    color: #b0b0d0;
    font-size: 12px;
    margin-bottom: 10px;
}
.timer {
    font-size: 12px;
    color: #ff6b6b;
    font-weight: 600;
    text-align: center;
    margin-top: 6px;
}
.difficulty {
    font-size: 11px;
    color: #b0b0d0;
    margin-bottom: 6px;
}
.stCodeBlock, .stCodeBlock pre, .stCodeBlock code {
    background-color: var(--code-bg) !important;
    border-radius: 5px;
    padding: 8px;
    font-family: 'Consolas', monospace;
    font-size: 12px;
    border: 1px solid #4b4b6b;
    color: var(--text-color);
}
@media (max-width: 600px) {
    .main-container {
        padding: 10px;
        margin: 5px;
    }
    .title {
        font-size: 20px;
    }
    .stButton>button {
        font-size: 12px;
        padding: 6px;
    }
}
</style>
""", unsafe_allow_html=True)

# Main UI
try:
    st.markdown(f'<div class="main-container" data-theme="{st.session_state.theme}" role="main">', unsafe_allow_html=True)
    st.markdown('<h1 class="title">🚀 JavaScript Quiz</h1>', unsafe_allow_html=True)
    st.markdown('<p class="caption">Test Your JavaScript Skills!</p>', unsafe_allow_html=True)

    # Theme toggle
    if st.button("🌙 Toggle Theme", key="theme_toggle"):
        toggle_theme()

    # Welcome screen
    if not st.session_state.started:
        st.markdown(f"""
        <div style="text-align: center;">
            <p style="color: var(--text-color); font-size: 14px;">Challenge yourself with {len(quiz)} JavaScript questions!</p>
            <p style="color: #b0b0d0;">{int(30 * len(quiz) / 60)} minutes, 2 points per correct answer.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Start Quiz", key="start_quiz"):
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

        # Pause/Resume
        pause_label = "Pause Quiz" if not st.session_state.paused else "Resume Quiz"
        if st.button(pause_label, key="pause_quiz"):
            toggle_pause()

        if not st.session_state.quiz_data:
            st.error("No quiz questions available.")
            st.stop()

        # Progress bar
        progress = st.session_state.current_q / len(st.session_state.quiz_data)
        progress_percentage = progress * 100
        st.markdown(f"""
        <div class="progress-bar" role="progressbar" aria-valuenow="{progress_percentage:.1f}" aria-valuemin="0" aria-valuemax="100">
            <div class="progress-fill" style="width: {progress_percentage}%"></div>
            <div class="progress-text">{progress_percentage:.1f}%</div>
        </div>
        <div style="color: var(--text-color); font-size: 11px; text-align: center;">
            Question {st.session_state.current_q + 1} of {len(st.session_state.quiz_data)}
        </div>
        """, unsafe_allow_html=True)

        if not st.session_state.show_results:
            with st.container():
                st.markdown('<div class="question-container" role="region" aria-label="Question">', unsafe_allow_html=True)
                q = st.session_state.quiz_data[st.session_state.current_q]

                # Display difficulty and streak
                st.markdown(f'<div class="difficulty">Difficulty: {q["difficulty"]} | Streak: 🔥 {st.session_state.streak}</div>', unsafe_allow_html=True)

                # Split question into text and code
                if "`" in q["question"]:
                    question_parts = q["question"].split("`")
                    question_text = question_parts[0].strip()
                    code_snippet = question_parts[1].strip() if len(question_parts) > 1 else ""
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
                    st.markdown(f"**{question_text}**")
                    if code_snippet:
                        st.code(code_snippet, language="javascript")
                else:
                    st.markdown(f"### Question {st.session_state.current_q + 1}")
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
                        st.session_state.answers[st.session_state.current_q] = {
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
                        else:
                            st.session_state.streak = 0
                        if st.session_state.current_q < len(st.session_state.quiz_data) - 1:
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
                        st.markdown(f'<div style="color: var(--text-color); font-size: 12px;">Explanation: {st.session_state.feedback["explanation"]}</div>', unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

        else:
            # Results
            time_taken = min((datetime.now() - st.session_state.start_time).total_seconds(), 30 * len(quiz)) if st.session_state.start_time else 30 * len(quiz)
            total_possible_score = len(quiz) * 2
            accuracy = (st.session_state.score / total_possible_score) * 100 if total_possible_score > 0 else 0
            st.markdown('<div class="question-container" role="region" aria-label="Results">', unsafe_allow_html=True)
            st.markdown(f'<h2 style="color: #34c759; text-align: center;">🏆 Score: {st.session_state.score}/{total_possible_score}</h2>', unsafe_allow_html=True)
            st.markdown(f"""
            <h3>📊 Results</h3>
            <div style="color: var(--text-color); font-size: 13px;">
                - ⏱️ Time: {int(time_taken) // 60}m {int(time_taken) % 60}s<br>
                - 🎯 Accuracy: {accuracy:.1f}%<br>
                - ✅ Correct: {sum(1 for ans in st.session_state.answers if ans and ans["is_correct"])}<br>
                - ❌ Incorrect: {sum(1 for ans in st.session_state.answers if ans and not ans["is_correct"])}<br>
                - 🔥 Max Streak: {st.session_state.max_streak}
            </div>
            """, unsafe_allow_html=True)

            # Review Answers
            st.markdown('<h3>📝 Review Your Answers</h3>', unsafe_allow_html=True)
            for i, ans in enumerate(st.session_state.answers):
                if ans:
                    status = "✅ Correct" if ans["is_correct"] else f"❌ Wrong (Correct: {ans['correct_answer']})"
                    st.markdown(f"""
                    <div style="color: var(--text-color); margin-bottom: 6px;">
                        Question {i+1}: {ans["question"]}<br>
                        Your Answer: {ans["user_answer"]}<br>
                        {status}<br>
                        Explanation: {quiz[i]["explanation"]}
                    </div>
                    """, unsafe_allow_html=True)

            # Play Again
            if st.button("🔄 Play Again", key="play_again"):
                reset_quiz()

            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

except Exception as e:
    st.error(f"An error occurred: {str(e)}. Please try refreshing or running locally.")
    st.markdown("To run locally, save this code as `quiz_app.py` and run `streamlit run quiz_app.py`.")



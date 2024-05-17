corpus_of_documents = [

    "Python is Interpreted: Python is an interpreted language, meaning that the code is executed line by line by an interpreter, rather than compiled into machine code.",
    "Python is High-level: Python is a high-level programming language, which means it abstracts away the complexities of the machine language, making it easier to write and understand code.",
    "Python is Dynamically Typed: Python is dynamically typed, which means that you don't need to declare the type of a variable when you create one. The interpreter automatically assigns the appropriate type to the variable based on its value.",
    "Python is Object-Oriented: Python supports object-oriented programming (OOP) principles, allowing you to create classes and objects, encapsulate data, and implement inheritance and polymorphism.",
    "Python has a Large Standard Library: Python comes with a large standard library that provides support for many common programming tasks, such as file I/O, networking, and web development, right out of the box.",
    "Python is used for Web Development: Python is widely used for web development, with popular frameworks like Django and Flask that make it easy to build web applications.",
    "Python is used for Data Analysis and Machine Learning: Python has become the de facto language for data analysis and machine learning, with libraries like NumPy, pandas, and scikit-learn that make it easy to work with large datasets and build machine learning models.",
    "Python is used for Automation: Python is often used for automation tasks, such as scripting repetitive tasks, building bots, or controlling hardware devices.",
    "Python is Cross-platform: Python is a cross-platform language, meaning that it runs on all major operating systems, including Windows, macOS, and Linux.",
    "Python is Open Source: Python is open source and has a large and active community of developers who contribute to its development and maintenance."
    "Start with the Basics: Begin by learning the basics: variables, data types, and control structures like loops and conditionals.",
    "Practice Regularly: Practice coding regularly to reinforce your skills and build confidence.",
    "Use Python Documentation: Refer to the official Python documentation and online resources for help and examples.",
    "Leverage Libraries: Take advantage of Python's extensive library ecosystem to simplify your coding tasks.",
    "Readability Matters: Write clean and readable code by following Python's style guide (PEP 8) and using meaningful variable names.",
    "Debugging Tools: Learn to use debugging tools like print() statements and Python's built-in debugger (pdb) to identify and fix errors in your code.",
    "Version Control: Use version control systems like Git to manage your code and collaborate with others effectively.",
    "Stay Organized: Organize your code into functions and modules to improve reusability and maintainability.",
    "Test Your Code: Write unit tests to verify that your code behaves as expected and catches bugs early.",
    "Keep Learning: Python is vast and constantly evolving, so keep learning new concepts, libraries, and best practices."
    
    ]

def jaccard_similarity(query, document):
    query = query.lower().split(" ")
    document = document.lower().split(" ")
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)

def return_response(query, corpus):
    similarities = []
    for doc in corpus:
        similarity = jaccard_similarity(user_input, doc)
        similarities.append(similarity)
    return corpus_of_documents[similarities.index(max(similarities))]

user_prompt = "What would you like to ask about Python?"

user_input = "How should Python be written?"

return_response(user_input, corpus_of_documents)
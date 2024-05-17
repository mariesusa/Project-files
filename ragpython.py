from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('http://127.0.0.1:8080/Simple%20RAG%20on%20website.html')

@app.route('/process', methods=['POST'])
def process():
    # Get value from HTML form
    user_input = request.form['user_input']
    
    # Process the input (you can put your code here)
    processed_output = user_input.upper()
    
    # Pass the processed output to the HTML template
    return render_template('http://127.0.0.1:8080/Simple%20RAG%20on%20website.html', processed_output=processed_output)

if __name__ == '__main__':
    app.run(debug=True)

'''corpus_of_documents = [
    "Take a leisurely walk in the park and enjoy the fresh air.",
    "Visit a local museum and discover something new.",
    "Attend a live music concert and feel the rhythm.",
    "Go for a hike and admire the natural scenery.",
    "Have a picnic with friends and share some laughs.",
    "Explore a new cuisine by dining at an ethnic restaurant.",
    "Take a yoga class and stretch your body and mind.",
    "Join a local sports league and enjoy some friendly competition.",
    "Attend a workshop or lecture on a topic you're interested in.",
    "Visit an amusement park and ride the roller coasters."
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

user_input(user_prompt)

return_response(user_input, corpus_of_documents)

print(return_response)'''
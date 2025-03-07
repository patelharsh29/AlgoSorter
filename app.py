from flask import Flask, render_template, jsonify, request
from sorting_algorithms import bubble_sort, merge_sort, quick_sort, selection_sort, insertion_sort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    data = request.json
    array = data['array']
    algorithm = data['algorithm']
    steps = []

    def update_callback(arr):
        steps.append(arr[:])

    if algorithm == 'bubble':
        bubble_sort(array, update_callback)
    elif algorithm == 'merge':
        merge_sort(array, update_callback)
    elif algorithm == 'quick':
        quick_sort(array, 0, len(array) - 1, update_callback)
    elif algorithm == 'selection':
        selection_sort(array, update_callback)
    elif algorithm == 'insertion':
        insertion_sort(array, update_callback)

    return jsonify(steps)

if __name__ == '__main__':
    app.run(debug=True)

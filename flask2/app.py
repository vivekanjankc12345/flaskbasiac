from flask import Flask, request

app = Flask(__name__)

data = {}  

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        data[key] = value
        return f"Entry '{key}': '{value}' created successfully!"
    return """
        <form method="post" action="/create">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key"><br>
            <label for="value">Value:</label>
            <input type="text" id="value" name="value"><br>
            <input type="submit" value="Create">
        </form>
    """

@app.route('/read')
def read():
    return f"Current state of the dictionary: {data}"

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        key = request.form['key']
        value = request.form['value']
        if key in data:
            data[key] = value
            return f"Entry '{key}' updated successfully!"
        else:
            return f"Entry '{key}' does not exist!"
    return '''
        <form method="post" action="/update">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key"><br>
            <label for="value">Value:</label>
            <input type="text" id="value" name="value"><br>
            <input type="submit" value="Update">
        </form>
    '''

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        key = request.form['key']
        if key in data:
            del data[key]
            return f"Entry '{key}' deleted successfully!"
        else:
            return f"Entry '{key}' does not exist!"
    return '''
        <form method="post" action="/delete">
            <label for="key">Key:</label>
            <input type="text" id="key" name="key"><br>
            <input type="submit" value="Delete">
        </form>
    '''

if __name__ == '__main__':
    app.run()

from flask import Flask, request
import re
app = Flask(__name__)
@app.route('/get_file', methods=['GET'])
def get_file():
      filename = request.args['filename']
      return '''Content of the file {} is...\n\n {}'''.format(filename, cat(filename))


def sanitize_string(filename):
    if re.search('^[\w\-\.]+$', filename):
        pass
    else:
        raise ValueError('Can not use special characters')


def cat(filename):
    sanitize_string(filename)
    with open(filename) as file:
        data = file.read()
        return data

if __name__ == "__main__":
     app.run(host="127.0.0.1", port=int("5000"))


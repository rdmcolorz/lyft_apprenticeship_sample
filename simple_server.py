from flask import Flask, abort, request 
import json

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def parse_json():
    try:
        string_to_cut = request.json['string_to_cut']
    except:
        print('POST request key not recognized')
        abort(400)
    result_string = cut_string(string_to_cut)
    return_json = {
        "return_string": result_string,
    }
    return json.dumps(return_json)

def cut_string(string):
    i = 0
    cut_list = []
    for char in string:
        i += 1
        if i == 3:
            cut_list.append(char)
            i = 0
    return "".join(cut_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
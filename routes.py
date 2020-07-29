from flask import Flask, jsonify, request

def routes(app):

    @app.route("/")
    def index():
        return "Home Page"

    @app.route("/test", methods=['POST'])
    def get_every_third_letter():
        if request.method == 'POST':
            posted_data = request.get_json()
            input_string = posted_data['string_to_cut']
            return_string = ""
            
            if not isinstance(input_string, unicode):
                return jsonify({'error': 'Data Type Error! Please enter string'}), 422 
            if len(input_string) < 3:
                return jsonify({'return_string': ""}), 201
            else:
                for character in input_string[2::3]:
                    return_string += character
                return jsonify({'return_string': return_string}), 201
from flask import Flask, jsonify, request

def routes(app):

    @app.route("/")
    def index():
        return "Home Page"

    @app.route("/test", methods=['POST'])
    def get_every_third_letter():
        print(request.get_json())
        posted_data = ""
        input_string = ""
        return_string = ""

        if request.get_json() != None:
            posted_data = request.get_json()
        else:
            return jsonify({'error': 'Unable to process posted data!'}), 422 

        if 'string_to_cut' in posted_data:
            input_string = posted_data['string_to_cut']
        else:
            return jsonify({'error': 'Unable to process posted data!'}), 422 
        
        if not isinstance(input_string, unicode):
            return jsonify({'error': 'Data Type Error! Please enter string'}), 422 

        if len(input_string) < 3:
            return jsonify({'return_string': ""}), 201
        else:
            for character in input_string[2::3]:
                return_string += character
            return jsonify({'return_string': return_string}), 201
from flask import Blueprint, jsonify, request, render_template, json
from models import UserModel, db

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/sign/<parameter>', methods=["GET"])
def authentication(parameter):
    if parameter == "Test":
        return jsonify({'message': 'Success'}), 200

    else:
        return jsonify({'message': 'Fail'}), 403

@auth.route('/sign', methods=["POST"])
def post():
    # if not request.json:
    #     abort(400)
    # print (request.json)
    return json.dumps(request.json)

@auth.route('/user', methods=["POST", "GET"])
def create_retrieve():
    if request.method == "POST":
        user = UserModel(ID=1, name='Irdi Caushaj', username='IrdiCaushi', email='inc160@aubg.edu', password='not_my_pass')
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'New user successfully created.'}), 200
    else:
        return render_template('user.html', user = UserModel.query.all() )
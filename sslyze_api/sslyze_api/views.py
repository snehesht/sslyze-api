from sslyze_api import app
from sslyze_api.models import User
from sslyze_api.database import db_session
from sslyze_api.utils import auth_required
from sslyze_api import celery_app
import ujson as json
from flask import jsonify, request
from sslyze_api.tasks import scan, scan_cli



@app.route('/api/user/new', methods = ['POST'])
def create_new_user():
    """ Create new user account """

    # Add an app.supersecret token to validate user creation
    # ToDo
    username = request.args.get('username')
    password = request.args.get('password')

    # Check if username and password are valid
    # and if username is unique
    if username is None or password is None:
        return jsonify({'status':'Failed','msg':'Need both username and password'})
    elif User.query.filter_by(username=username).first() is not None:
        return jsonify({'status':'Failed','msg':'Username is already taken'})
    else:
        new_user = User(username=username, password=password)
        new_user.create_token()
        db_session.add(new_user)
        db_session.commit()
        if User.query.filter_by(username=username) is None:
            return jsonify({'status':'Failed','msg':'New user not created, check logs'})
        else:
            return jsonify({'username':new_user.username,
                'created':new_user.created, 'token':new_user.token,'status':'Success'})


@app.route('/api/user/token',methods=['GET'])
@auth_required
def get_user_token():
    """ Get user token after authenticating them with username/password """

    username = request.args.get('username')
    password = request.args.get('password')
    curr_user = User.query.filter_by(username=username).first()
    if curr_user is not None:
        if curr_user.verify_password(password) is True:
            return jsonify({'username':curr_user.username,
                'token':curr_user.token,'status':'Successful'})
        else:
            return jsonify({'status':'Failed', 'msg':'Wrong password'})
    else:
        return jsonify({'status':'Failed', 'msg':'User does not exist'})


# Requires Auth
# Debug Scan from shell
@app.route('/api/debug/scan', methods=['GET'])
@auth_required
def debug_scan_from_shell():
    host = request.args.get('host')
    port = request.args.get('port') or 443 # Default to 443, if port=None
    resp = scan_cli.delay(host,port)
    while resp.ready() == False:
        pass
    return jsonify(resp.result)


@app.route('/api/scan', methods=['GET'])
@auth_required
def scan_host():
    host = request.args.get('host')
    port = request.args.get('port') or 443 # Default to 443, if port=None
    if host != None:
        resp = scan.delay(host,port)
        while resp.ready() == False:
            pass
        return jsonify(resp.result)
    else:
        return jsonify({'status':'Failed','msg':'Valid hostname required'})

# Index API Page
@app.route('/api', methods=['GET'])
def index():
    pass


# Docs
@app.route('/', methods=['GET'])
def home():
    pass






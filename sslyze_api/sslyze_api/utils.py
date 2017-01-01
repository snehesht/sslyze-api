from functools import wraps
from flask import request, jsonify
from sslyze_api.models import User

# Auth by username or token
def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        username = request.args.get('username')
        password = request.args.get('password')
        token = request.headers.get('X-Auth-Token')

        print username, password, token

        if username is None and token is None:
            return jsonify({'msg':'Authentication required, try with username or token','status':'Failed'})

        elif username is not None:
            # Check if auth is valid
            if username is not None and password is not None:
                curr_user = User.query.filter_by(username=username).first()
                if curr_user is not None:
                    if curr_user.verify_password(password) is False:
                        return jsonify({'status':'Failed', 'msg':'Wrong password'})
                    else:
                        return f(*args, **kwargs)
                else:
                    return jsonify({'status':'Failed', 'msg':'User does not exist'})
            else:
                return jsonify({'status':'Failed', 'msg':'Authentication required, both username and password required.'})

        elif token is not None:
            if User.query.filter_by(token=token).first() is not None:
                return f(*args, **kwargs)
            else:
                return jsonify({'status':'Failed', 'msg':'Token does not exist'})

    return decorated



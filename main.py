import hashlib
import hmac


from flask import Flask, request, jsonify

app = Flask(__name__)

_secret_key = "thisissecretkey"


def generate_hmac(secret_key, token):
    hmac_digest = hmac.new(key=secret_key.strip().encode('utf-8'),
                           msg=token.strip().encode('utf-8'),
                           digestmod=hashlib.sha256).hexdigest()
    return hmac_digest


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.post("/webhook/post/verify_success")
def verify_success():
    data = request.json
    _key = data.get('key')
    hmac = generate_hmac(_secret_key, _key)
    print(hmac)
    return jsonify({
        "hmac": hmac
    }), 200


@app.post("/webhook/post/verify_failed")
def verify_failed():
    return jsonify({
        "msg": "me failed"
    }), 400


@app.post("/webhook/post/delivery_success")
def delivery_success():
    data = request.json
    # verify case
    _key = data.get('key')
    if _key:
        hmac = generate_hmac(_secret_key, _key)
        print(hmac)
        return jsonify({
            "hmac": hmac
        }), 200

    # delivery case
    print("received data ", data)
    return jsonify({
        "msg": "ok"
    }), 200


@app.post("/webhook/post/delivery_failed")
def delivery_failed():
    data = request.json
    # verify case
    _key = data.get('key')
    if _key:
        hmac = generate_hmac(_secret_key, _key)
        print(hmac)
        return jsonify({
            "hmac": hmac
        }), 200

    # delivery case
    print("received data ", data)
    return jsonify({
        "msg": "failed"
    }), 400


if __name__ == '__main__':
    app.run(debug=True, port=3000)
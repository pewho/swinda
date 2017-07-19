from jose import jwk, jwt
from jose.utils import base64url_decode

import requests

from swinda.format import format_output


def request_jwk(uri):
    r = requests.get(uri)

    if r.status_code == 200:
        return r.json()["keys"][0]
    else:
        return None


def validate(token, jwk_raw):
    key = jwk.construct(jwk_raw)

    message, encoded_sig = token.rsplit(".", 1)
    decoded_sig = base64url_decode(encoded_sig.encode("utf-8"))

    return key.verify(message.encode("utf-8"), decoded_sig), {}


def format_jwt(jwtoken):
    headers = jwt.get_unverified_header(jwtoken)
    claims = jwt.get_unverified_claims(jwtoken)

    format_output(headers, claims)

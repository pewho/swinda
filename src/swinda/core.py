from jose import  jwt
from swinda.validators import Validator

import requests

from swinda.format import format_output


def request_jwk(uri):
    r = requests.get(uri)

    if r.status_code == 200:
        return r.json()["keys"][0]
    else:
        return None


def validate(token, jwk_raw):
    validator = Validator.build(jwk_raw, token)
    validator.validate()

    return validator


def format_jwt(jwtoken):
    headers = jwt.get_unverified_header(jwtoken)
    claims = jwt.get_unverified_claims(jwtoken)

    format_output(headers, claims)

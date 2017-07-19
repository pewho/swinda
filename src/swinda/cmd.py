#!/usr/bin/env python3

import argparse
from swinda.core import validate, request_jwk, format_jwt
import json


def validate_jwt():
    parser = argparse.ArgumentParser(description="JWT RSA Key validator...")
    parser.add_argument("jwk_uri", help="JWK public key uri")
    parser.add_argument("jwt_token", help="JWT Token to validate")

    args = parser.parse_args()

    print('Request remote JWK... \n')
    jwk_raw = request_jwk(args.jwk_uri)
    print('> JWK infos > ' + json.dumps(jwk_raw) + '\n')

    isValid = validate(args.jwt_token, jwk_raw)

    print('Validate JWT...\n')
    print('>' + format_jwt(args.jwt_token))
    print("\n")

    if isValid:
        print("> OK!")
    else:
        print("> !!!!!!!!!!!!! KO !!!!!!!!!!!!!!!!")


def hello():
    print("Hello, world")


if __name__ == '__main__':
    validate_jwt()

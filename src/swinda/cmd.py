#!/usr/bin/env python3
import argparse
from swinda.core import validate, request_jwk, format_jwt
from swinda.format import show_progress, show_jwk, show_validation_information
from jose.exceptions import JWTError

from blessings import Terminal


def validate_jwt():
    parser = argparse.ArgumentParser(description="JWT RSA Key validator...")
    parser.add_argument("jwk_uri", help="JWK public key uri")
    parser.add_argument("jwt_token", help="JWT Token to validate")

    args = parser.parse_args()

    term = Terminal()
    print(term.enter_fullscreen)
    print(term.clear)

    show_progress("get_jwk")

    jwk_raw = None

    try:
        jwk_raw = request_jwk(args.jwk_uri)
        show_progress("got_jwk")
        show_jwk(jwk_raw)
    except Exception:
        show_progress("jwk_error")
        return

    show_progress("validating_JWT")

    validator = validate(args.jwt_token, jwk_raw)
    try:
        format_jwt(args.jwt_token)
    except JWTError:
        pass

    show_validation_information(validator)

    input()

    print(term.exit_fullscreen)


def hello():
    print("Hello, world")


if __name__ == '__main__':
    validate_jwt()

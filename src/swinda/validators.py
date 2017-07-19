from swinda.format import show_issue
from jose import jwk, jwt
from jose.utils import base64url_decode


class Validator:
    @staticmethod
    def build(jwk_raw, jwt):
        validator = Validator()

        #Signature Validator
        sigValidator = ChildValidator("Signature Validation",
            "JWT is not valid, the signature does not match. \
Do you use the right JWK ?")
        sigValidator.associate_validation_strategy(
            SignatureValidatorStrategy(jwk_raw, jwt)
        )
        validator.append_child(sigValidator)

        return validator

    def __init__(self):
        self.childs = {}
        self.isValid = True

    def append_child(self, child):
        self.childs[child.name] = child

    def remove_child(self, child):
        del self.childs[child.name]

    def remove_child_by_name(self, child_name):
        del self.childs[child_name]

    def validate(self):
        for child in self.childs.values():
            child_is_valid = child.validate()
            if not child_is_valid:
                self.isValid = False

    def show_issues(self):
        for validator in self.childs.values():
            if validator.isValid:
                pass
            elif not validator.isValid and validator.issue is not None:
                show_issue(validator.issue)
            else:
                show_issue("Unknown issue for {name}".format(name=validator.name))


class ChildValidator:
    def __init__(self, name, issue_message):
        self.name = name
        self.validate_strategy = None
        self.issue = issue_message
        self.isValid = None

    def associate_validation_strategy(self, strategy):
        self.validate_strategy = strategy

    def validate(self):
        try:
            self.isValid = self.validate_strategy.validate()
        except Exception as e:
            self.isValid = False

        return self.isValid


class SignatureValidatorStrategy:
    def __init__(self, jwk, jwt):
        self.jwt = jwt
        self.jwk = jwk

    def validate(self):
        try:
            key = jwk.construct(self.jwk)

            message, encoded_sig = self.jwt.rsplit(".", 1)
            decoded_sig = base64url_decode(encoded_sig.encode("utf-8"))

            return key.verify(message.encode("utf-8"), decoded_sig)
        except Exception as e:
            return False

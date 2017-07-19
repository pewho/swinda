"""
Swinda
------
This module handle all the output format on the terminal.
It use [Blessing](http://pythonhosted.org/blessings/)
"""
from blessings import Terminal
from math import floor

term = Terminal()


def format_output(headers, claims):
    print_title("{t.dim_bold}JWT Content{t.normal}".format(t=term))
    print_title("{t.dim}  > JWT header{t.normal}".format(t=term))
    [print_element("{t.cyan} {key}: {t.green_italic}{value}{t.normal}"
        .format(t=term, key=k, value=v)) for k, v in headers.items()]
    print(term.move_down)

    print_title("{t.dim}  > JWT claims{t.normal}".format(t=term))
    [print_element("{t.cyan} {key}: {t.green_italic}{value}{t.normal}"
        .format(t=term, key=k, value=v)) for k, v in claims.items()]
    print(term.move_down)


def show_progress(step):
    available_step = {
        "get_jwk": "{t.dim_yellow}> Retrieving JWK Key{t.normal}"
            .format(t=term),
        "got_jwk": "{t.dim_yellow}> JWK Key retrived successfully{t.normal}"
            .format(t=term),
        "jwk_error":
            "{t.dim_bold_on_red_white}>>> Unknown Issue \
 when retrieving JWK key{t.normal}"
                .format(t=term),
        "validating_JWT": "{t.dim_yellow}> Validating JWT...{t.normal}"
            .format(t=term),
        "validate_JWT_success":
            "{t.on_green_white_bold}\tJWT IS VALID\t{t.normal}"
                .format(t=term),
        "validate_JWT_error":
            "{t.on_red_white_bold}\tJWT IS INVALID\t{t.normal}"
                .format(t=term)
    }

    if step == "validate_JWT_success" or step == "validate_JWT_error":
        term_width = (term.width / 2) - (len(available_step.get(step)) / 2) - 1
        with term.location(int(floor(term_width)), int(term.height - 1)):
            print(available_step.get(step))
    else:
        print_title(available_step.get(step))


def show_jwk(jwk):
    print_title("{t.dim_bold}JWK Content{t.normal}"
        .format(t=term))
    [print_element("{t.cyan} {key}: {t.green_italic}{value}{t.normal}"
        .format(t=term, key=k, value=v)) for k, v in jwk.items()]
    print(term.move_down)


def show_validation_information(validator):
    if validator.isValid:
        show_progress("validate_JWT_success")
    else:
        print_title("{t.red_bold}> JWT Issues{t.normal}".format(t=term))
        validator.show_issues()
        show_progress("validate_JWT_error")


def show_issue(issue):
    print_element("{t.red} - {iss}{t.normal}".format(t=term, iss=issue))


def print_title(title):
    print(term.move_x(2) + title + term.move_down)


def print_element(element):
    print(term.move_x(6) + element)

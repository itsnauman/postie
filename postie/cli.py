import argparse
import os
from postie import Postie

parser = argparse.ArgumentParser(description="Utility to batch send emails")


def is_valid_file(parser, arg):
    arg = os.path.abspath(arg)
    if os.path.exists(arg):
        return arg
    parser.error("The file %s does not exist!" % arg)

parser.add_argument("-t", "--template",
                    required=True,
                    dest="template",
                    type=lambda x: is_valid_file(parser, x),
                    help="Email template file")

parser.add_argument("-csv",
                    required=True,
                    type=lambda x: is_valid_file(parser, x),
                    help="CSV file")

parser.add_argument("-sender",
                    type=str,
                    help="Email to send from")

parser.add_argument("-subject",
                    type=str,
                    help="Subject of the email")

parser.add_argument("-server",
                    help="STMP server address")

parser.add_argument("-port",
                    type=int,
                    help="Port of SMTP server")

parser.add_argument("-user",
                    help="Username of sender")

parser.add_argument("-pwd", "--password",
                    dest="password",
                    help="Password for sender")

if __name__ == "__main__":
    args = parser.parse_args()
    p = Postie(args)
    p.run()

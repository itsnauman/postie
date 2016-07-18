# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import os
from postie import Postie


def is_valid_file(parser, arg):
    arg = os.path.abspath(arg)
    if os.path.exists(arg):
        return arg
    parser.error("The file %s does not exist!" % arg)


def create_parser():
    parser = ArgumentParser(
        description="Utility to batch send emails and text messages")
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
                        help="Sender of email/sms")

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
                        help="Password for account")

    parser.add_argument("-sid",
                        help="Twilio Account SID")

    parser.add_argument("-token",
                        help="Twilio Auth Token")

    return parser

def main():
    p = Postie(create_parser().parse_args())
    p.run()

if __name__ == '__main__':
    main()

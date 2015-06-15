from jinja2 import Template
from mailthon.postman import Postman
from mailthon import email
from mailthon.middleware import TLS, Auth
from collections import OrderedDict
from threading import Thread

import csv


class PostieInvalidFirstHeader(Exception):

    """
    This exception is raised when the csv header is not in correct format.
    """
    pass


class Postie(object):

    def __init__(self, args):
        self.args = args
        self.template = self.args.template
        self.csv = self.args.csv
        self.sender = self.args.sender
        self.subject = self.args.subject
        self.server = self.args.server
        self.port = self.args.port
        self.username = self.args.user
        self.password = self.args.password
        self.init_mailthon()

    def setup_postie(self):
        """
        Initialize .postie file with user settings
        """
        pass

    def init_mailthon(self):
        """
        Setup mailthon instance
        """
        self.postman = Postman(
            host='smtp-mail.outlook.com',
            port=587,
            middlewares=[
                TLS(force=True),
                Auth(username=self.username, password=self.password)
            ],
        )

    @property
    def csv_content(self):
        """
        Read the csv file and return a list of rows.
        """
        with open(self.csv, 'rb') as fp:
            reader = csv.reader(fp)
            content = [item for item in reader]
        return content

    @property
    def dict_template(self):
        """
        Return an ordered dict with all the headers from csv file.
        """
        headers = self.csv_content[0]
        template_var_list = [each.strip() for each in headers][1:]
        return OrderedDict.fromkeys(template_var_list)

    def validate_header(self, content, mode='email'):
        """
        Check is the first column of csv file contains email or phone number.
        """
        headers = content[0]
        email_header = headers[0] if headers[0].lower() == mode else None
        if email_header is None:
            raise PostieInvalidFirstHeader(
                "First column needs to have %s" % mode)

    def render_template(self, **kwargs):
        """
        Render message template with Jinja 2 Engine
        """
        with open(self.template, 'rb') as fp:
            template = Template(fp.read().strip())
        return template.render(**kwargs)

    def send_async_email(self, envelope):
        self.postman.send(envelope)

    def construct_msg(self, arg_list):
        """
        Insert the keyword values from csv file to the template.
        """
        template_kwargs = self.dict_template
        for i, key in enumerate(template_kwargs):
            template_kwargs[key] = arg_list[i + 1].strip()
        return self.render_template(**template_kwargs)

    def send_emails(self):
        content = self.csv_content[1:]
        for row in content:
            envelope = email(
                sender='Nauman Ahmad <tes@mail.com>',
                receivers=[row[0]],
                subject='Hello World!',
                content=self.construct_msg(row))
            # Spawn a thread for each email delivery
            thr = Thread(target=self.send_async_email, args=[envelope])
            thr.start()
        return thr

    def run(self):
        self.send_emails()

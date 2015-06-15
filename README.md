# Postie

<img src="http://41.media.tumblr.com/tumblr_md787xAplD1rnrne9o1_1280.png" width="130" alt="Postman Icon" align="right">
Postie is a command line utility for batch sending email.

#### Features

* Works with any SMTP server
* Fast, templated, bulk emails
* All of the power of Jinja 2 templating engine.
* Uses threads to send emails concurrently.
* Reads attributes from CSV file

### Installation

    $ pip install py-postie

### Usage

    $ usage: postie [-h] -t TEMPLATE -csv CSV [-sender SENDER] [-subject SUBJECT]
              [-server SERVER] [-port PORT] [-user USER] [-pwd PASSWORD]

#### Example

```
$ postie -t template.txt -csv recipients.csv \
    -sender "Bumblebee <bumble@bee.com>" \
    -subject "Hello, World!" -server smtp.bumblebee.com -port 587 \
    -user bumble -password BumbleBee007
```

template.txt:

```
Hey {{ Name }}. You are a {{ Type }}.

{% if Name == "Robot" %}
Yo, we are bros!
{% else %}
We are no more bros!
{% endif %}
```

recipients.csv:

```
Email,Name,Type
mike@ross.com,Mike Ross,Human
mance@rayder,Mance Rayder,Wildling
victor@stone.com,Victor Stone,Robot
```


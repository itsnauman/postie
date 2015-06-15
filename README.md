# Postie

<img src="http://41.media.tumblr.com/tumblr_md787xAplD1rnrne9o1_1280.png" width="280" alt="Postman Icon" align="right">
Postie is a command line utility for batch sending emails and text messages. Inspired by [Postman](https://github.com/zachlatta/postman)

#### Features

* Works with any SMTP server
* Send Text Messages using Twilo
* Fast, templated, bulk emails
* All of the power of Jinja 2 templating engine.
* Uses threads to send emails and text messages concurrently.
* Reads attributes from CSV file

### Installation

    $ pip install py-postie

### Usage

    $ usage: postie [-h] -t TEMPLATE -csv CSV [-sender SENDER] [-subject SUBJECT]
                    [-server SERVER] [-port PORT] [-user USER] [-pwd PASSWORD]
                    [-sid SID] [-token TOKEN]

### Example

##### Sending Emails

```
$ postie -t template.txt -csv recipients.csv \
    -sender "Bumblebee <bumble@bee.com>" \
    -subject "Hello, World!" -server smtp.bumblebee.com -port 587 \
    -user bumble -password BumbleBee007
```

##### Sending Text Messages

```
$ postie -t template.txt -csv recipients.csv \
    -sender "Bumblebee <bumble@bee.com>" \
    -subject "Hello, World!" -sid AC32a3c49700934481addd5ce1659f04d2
    -token {{ auth_token }}
```
##### template.txt:

```
Hey {{ Name }}. You are a {{ Type }}.

{% if Name == "Robot" %}
Yo, we are bros!
{% else %}
We are no more bros!
{% endif %}
```

##### recipients.csv:

```
Email,Name,Type
mike@ross.com,Mike Ross,Human
mance@rayder,Mance Rayder,Wildling
victor@stone.com,Victor Stone,Robot
```


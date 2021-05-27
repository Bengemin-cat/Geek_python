import re


def email_parse(email_address):
    em_ad = re.compile(r'(?P<user_name>[^\s\";]*)@(?P<domain>.*\.\w*)', re.IGNORECASE)
    dict_email_address = re.match(em_ad, email_address)
    if dict_email_address:
        return dict_email_address.groupdict()
    else:
        raise ValueError(f'wrong email: {email_address}')




print(email_parse('someone@geekbrainsru'))

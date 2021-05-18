import requests
from bs4 import BeautifulSoup


def notify(email_to):
    telegram_notify(email_to)
    email_send(email_to)


def email_send(email_to):
    from django.core.mail import send_mail
    send_mail(
        'My Blog',
        'You have subscribed on Author: {}'.format('test name'),
        'nooneons03@gmail.com',
        [email_to],
        fail_silently=False,
    )
    response = requests.get('http://127.0.0.1:8000/')
    print(response.status_code)
    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')


def telegram_notify(email_to):
    pass


def email_send_all(email_to):
    url = 'https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php'
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    from django.core.mail import send_mail
    if res.status_code == 200:
        send_mail(
            'My Blog',
            text,
            'nooneons03@gmail.com',
            [email_to],
            fail_silently=False,
        )
    elif res.status_code == 404:
        pass

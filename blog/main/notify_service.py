# import requests
# from bs4 import BeautifulSoup


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


def telegram_notify(email_to):
    pass

# def email_send_all(email_to):
# url = 'https://tproger.ru/wp-content/plugins/citation-widget/get-quote.php'
# res = requests.get(url)
# from django.core.mail import send_mail
# if res.status_code == 200:
#     html_page = res.content
#     soup = BeautifulSoup(html_page, 'html.parser')
#     text = soup.find_all(text=True)
#     send_mail(
#         'My Blog',
#         text,
#         'nooneons03@gmail.com',
#         [email_to],
#         fail_silently=False,
#     )

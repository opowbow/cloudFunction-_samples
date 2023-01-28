def sendgrid(request):
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail, Email
    from python_http_client.exceptions import HTTPError

    sg = SendGridAPIClient(os.environ['EMAIL_API_KEY'])

    html_content = "<p>Hello World!</p>"

    message = Mail(
        to_emails="send.order.demo@email.com",
        from_email=Email('order_processing@gmail.com', "Order Processing"),
        subject="New Order",
        html_content=html_content
        )
    message.add_bcc("olivepower1@gmail.com@gmail.com")

    try:
        response = sg.send(message)
        return f"email.status_code={response.status_code}"
        #expected 202 Accepted

    except HTTPError as e:
        return e.message

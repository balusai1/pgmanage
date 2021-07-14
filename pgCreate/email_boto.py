class Email(object):
    def __init__(self, subject):
        self.subject = subject
        self._html = None
        self._format = 'html'
        self.connection = boto.ses.connect_to_region(
            'us-east-1',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )

    def html(self, html):
        self._html = html

    def send(self, from_addr, to):
        return self.connection.send_email(
            from_addr,
            self.subject,
            None,
            to,
            format=self._format,
            html_body=self._html
        )
first_name = 'mounika'
last_name = 'thota'
product_name = 'CCA 175'
email = Email(subject='Thanks')
email.html('<html><body>Hello '+ first_name.title()+' '+last_name.title()+',<br>'+ 'Your lab purchase for the product <strong>'+ product_name + '</strong> is success!! You will be given the lab access in <strong>24 hours</strong>, Thank you.</body></html>')  # Optional
email.send(from_addr='support@itversity.com', to='mounika@itversity.in')
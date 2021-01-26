class User:
    def __init__(self, name, mail):
        self.name = name
        if self.validate_mail(mail):
            self.mail = mail
        else:
            raise ValueError("Błąd!")


    def validate_mail(self, mail):
        return '@' in mail
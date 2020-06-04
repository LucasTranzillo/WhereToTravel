from django import forms
from django.core.mail.message import EmailMessage
from setuptools.command.test import test



class ContactForm(forms.form):
    name = forms.CharField(label='name')
    email = forms.EmailField(label='e-mail')
    subject = forms.CharField(label='subject')
    message = forms.CharField(label='message', widget=forms.TextArea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Name: {name} \n E-mai: {email} \n Subject: {subject} \n Message: {message}'

        mail =  EmailMessage(
            subject='E-mail sent by the System',
            body=content,
            from_email='contact@host.com',
            to=['contact@host.com'],
            headers= {'Reply-to:email'}
        )
        mail.send()
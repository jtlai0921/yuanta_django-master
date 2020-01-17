from captcha.fields import CaptchaField
from django.forms import forms


# 驗證碼類別
class CaptchaCheck(forms.Form):
    captcha = CaptchaField()

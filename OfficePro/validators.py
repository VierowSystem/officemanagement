from django.contrib.auth.password_validation import CommonPasswordValidator

class CustomCommonPasswordValidator(CommonPasswordValidator):
    def validate(self, password, user=None):
        return  # Skip common password validation
import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class GenerateActivationToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        )


acc_active_token = GenerateActivationToken()


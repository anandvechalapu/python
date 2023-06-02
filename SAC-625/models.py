# models.py

from django.db import models

class BajajAllianzGroupSampoornaJeevanSuraksha(models.Model):
    MIN_SA = models.IntegerField()
    MAX_SA = models.IntegerField()
    MIN_AGE = models.IntegerField()
    MAX_AGE = models.IntegerField()
    SA_RANGES = models.CharField(max_length=255)
    POLICY_TENURE = models.CharField(max_length=255)
    INCOME_ELIGIBILITY = models.BooleanField()
    OTP_AUTHENTICATION = models.BooleanField()
    SPOUSE_ELIGIBILITY = models.BooleanField()

    def validate_policy(self):
        if self.INCOME_ELIGIBILITY is False:
            return False
        if self.OTP_AUTHENTICATION is False:
            return False
        if self.MIN_SA > self.MAX_SA:
            return False
        if self.MIN_AGE > self.MAX_AGE:
            return False
        return True
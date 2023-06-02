# Generate manage.py
import os
import sys

from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Policy, Income, AgeLimit, SumAssured, Tenure

engine = create_engine('sqlite:///bajajallianz.db')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

def validate_policy():
    """
    This function will validate various criteria before
    issuing the Bajaj Allianz Group Sampoorna Jeevan Suraksha policy
    """

    # get all the users
    users = session.query(User).all()
    for user in users:
        # check minimum and maximum sum assured
        sum_assured = session.query(SumAssured).filter_by(user_id=user.id).first()
        if not sum_assured.min_sum_assured <= user.sum_assured <= sum_assured.max_sum_assured:
            return False

        # check minimum and maximum age limits
        age_limit = session.query(AgeLimit).filter_by(user_id=user.id).first()
        if not age_limit.min_age <= user.age <= age_limit.max_age:
            return False

        # check for annual income
        income = session.query(Income).filter_by(user_id=user.id).first()
        if income.annual_income < 40000:
            return False

        # check for sum assured ranges
        if user.sum_assured not in [50000, 100000, 150000, 200000]:
            return False

        # check for policy tenure ranges
        policy_tenure = session.query(Tenure).filter_by(user_id=user.id).first()
        if policy_tenure.tenure not in [12, 15, 18, 24]:
            return False

        # check for OTP authentication
        if not user.is_otp_authenticated:
            return False

    return True

if __name__ == '__main__':
    validate_policy()
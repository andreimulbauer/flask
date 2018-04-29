from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField #DateField


class ResponsesForm(FlaskForm):
    score = IntegerField('score')
    description = TextField('description')
    campaign_id = IntegerField('campaign_id')

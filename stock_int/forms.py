#
# Data input form
# forms.py
#

# install: pip install Flask-WTF
from wtforms import TextField
from wtforms.fields import SubmitField
from wtforms.validators import DataRequired
from flask_wtf import Form


class SymbolSearch(Form):
    
    symbol = TextField('Symbol (eg AAPL, MSFT)',
                       validators=[DataRequired()])
    trend1 = TextField('Moving Average 1 ',
                       validators=[DataRequired()])
    trend2 = TextField('Moving Average 2 ',
                       validators=[DataRequired()])
    submit = SubmitField()

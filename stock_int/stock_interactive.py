
from pandas_datareader import data as web
import cufflinks
import chart_studio.plotly as py
from flask import Flask, request, render_template, redirect, url_for
from forms import SymbolSearch


py.sign_in('Python-Demo-Account', 'gwt101uhh0')

 
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main():
    form = SymbolSearch(csrf_enabled=False)
    if request.method == 'POST' and form.validate():
        return redirect(url_for('results', symbol=request.form['symbol'],
                                trend1=request.form['trend1'],
                                trend2=request.form['trend2']))
    return render_template('selection.html', form=form)


@app.route("/symbol/<symbol>+<trend1>+<trend2>")
def results(symbol, trend1, trend2):
    data = web.DataReader(symbol, data_source='yahoo')
    data['Moving Average 1'] = data['Adj Close'].rolling(int(trend1)).mean()
    data['Moving Average 2'] = data['Adj Close'].rolling(int(trend2)).mean()
    url = data[['Adj Close', 'Moving Average 1', 'Moving Average 2']].iplot(asUrl=True)
    table = data.tail().to_html()
    return render_template('plotly.html', symbol=symbol,
                           plot=url, table=table)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)

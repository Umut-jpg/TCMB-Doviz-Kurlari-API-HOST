

from flask import Flask, jsonify
from evds import evdsAPI
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)
evds = evdsAPI('APİKEY')

@app.route('/')
def home():
    return "404 Not Found"

def get_last_weekday_data():
    current_dateTime = datetime.now()
    print(current_dateTime.weekday())
   
    if current_dateTime.weekday() == 5:
        current_dateTime -= timedelta(days=1)
         
    
    elif current_dateTime.weekday() == 6:
        current_dateTime -= timedelta(days=2)

 
    data = evds.get_data([
        'TP.DK.USD.A.YTL','TP.DK.USD.S.YTL',
        'TP.DK.EUR.A.YTL','TP.DK.EUR.S.YTL',
        'TP.DK.GBP.A.YTL','TP.DK.GBP.S.YTL',
        'TP.DK.CHF.A.YTL','TP.DK.CHF.S.YTL',
        'TP.DK.AUD.A.YTL','TP.DK.AUD.S.YTL',
        'TP.DK.CAD.A.YTL','TP.DK.CAD.S.YTL',
        'TP.DK.SAR.A.YTL','TP.DK.SAR.S.YTL',
        'TP.DK.AED.A.YTL','TP.DK.AED.S.YTL',
        'TP.DK.QAR.A.YTL','TP.DK.QAR.S.YTL',
        'TP.DK.KWD.A.YTL','TP.DK.KWD.S.YTL',
        'TP.DK.JPY.A.YTL','TP.DK.JPY.S.YTL',
        'TP.DK.NOK.A.YTL','TP.DK.NOK.S.YTL',
        'TP.DK.SEK.A.YTL','TP.DK.SEK.S.YTL',
        'TP.DK.AZN.A.YTL','TP.DK.AZN.S.YTL',
        'TP.DK.KRW.A.YTL','TP.DK.KRW.S.YTL',
        
    ],startdate=f"{current_dateTime.day}-{current_dateTime.month}-{current_dateTime.year}", enddate=f"{current_dateTime.day}-{current_dateTime.month}-{current_dateTime.year}", raw=True)

    return data
 
@app.route('/api/get_data', methods=['GET'])
def get_data():
    data = get_last_weekday_data()

    if not data:
        return "Veri bulunamadı."

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)





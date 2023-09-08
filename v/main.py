# from evds import evdsAPI
# evds = evdsAPI('WRQmTwGYmQ')
# deneme= evds.get_data(['TP.DK.USD.A.YTL','TP.DK.EUR.A.YTL'], startdate="07-09-2023", enddate="07-09-2023")
# print(deneme)


from flask import Flask, jsonify
from evds import evdsAPI
from flask_cors import CORS 
from datetime  import datetime
app = Flask(__name__)
CORS(app) 
@app.route('/')
def home():
    return "404 Not Found"
current_dateTime = datetime.now()
@app.route('/api/get_data', methods=['GET'])
def get_data():
    evds = evdsAPI('WRQmTwGYmQ')
    data = evds.get_data(['TP.DK.USD.A.YTL','TP.DK.EUR.A.YTL'], startdate=f"{current_dateTime.day}-{current_dateTime.month}-{current_dateTime.year}" ,enddate=f"{current_dateTime.day}-{current_dateTime.month}-{current_dateTime.year}")
    json_data = data.to_json(orient='records')   
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
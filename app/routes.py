import requests
import json

from flask import render_template

from app import app


# A decorator
# Modifies the function that follows it
# Registers functions as callbacks for particular events
@app.route('/index')
def index():
    user = {'username': 'Govind'}
    stocks = [{
        'company': {'name': 'Nintendo'},
        'body': "Nintendo's stocks are booming!"
    },
        {
            'company': {'name': 'Sony'},
            'body': "Sony's stocks suck ass!"
        }]
    return render_template('index.html', title='', user=user, stocks=stocks)


@app.route('/')
def marquee():
    auth_data = {
        "grant_type": "client_credentials",
        "client_id": "ffecd6b19bf440a1bb1adba81ab638aa",
        "client_secret": "d97b29447456bf0933ec9221bff0abc7efbd02c8f1f73023edae552a9284ac19",
        "scope": "read_product_data"
    }

    # create session instance
    session = requests.Session()

    auth_request = session.post("https://idfs.gs.com/as/token.oauth2", data=auth_data)
    access_token_dict = json.loads(auth_request.text)
    access_token = access_token_dict["access_token"]

    # update session headers with access token
    session.headers.update({"Authorization": "Bearer " + access_token})

    request_url = "https://api.marquee.gs.com/v1/data/USCANFPP_MINI/query"

    request_query = {
        "where": {
            "gsid": ["75154", "193067", "194688", "902608", "85627"]
        },
        "startDate": "2017-01-15",
        "endDate": "2018-01-15"
    }

    request = session.post(url=request_url, json=request_query)
    results = json.loads(request.text)

    string_results = json.dumps(results)
    return render_template('marquee_test.html', results=string_results)

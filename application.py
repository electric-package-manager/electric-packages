from discord import Webhook, RequestsWebhookAdapter
from flask import Flask
from virus_total_apis import PublicApi as VTApi
import firebase_admin
from firebase_admin import credentials, firestore
import json


# Flask constructor takes the name of
# current module (__name__) as argument.
application = Flask(__name__)


class DatabaseManager:
    def increment(package_name: str):
        cred = credentials.Certificate("serviceAccount.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()

        document_ref = db.collection('Packages').document(package_name)

        # Get the current counter value
        data = document_ref.get().to_dict()
        current_counter = data['installCounter']

        updated_counter = current_counter + 1
        # Increment the current value and update the database
        document_ref.update({'installCounter': updated_counter})


@application.route('/increment/<package_name>')
def increment(package_name: str):
    DatabaseManager.increment(package_name)
    return 'Success'

@application.route('/package-list')
def package_list():
    data = ''
    with open(rf'package-list.json', 'r') as f:
        data = json.load(f)

    return application.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )


@application.route('/submit-package-request/<package_name>')
def submit_package_request(package_name: str):
    wh = Webhook.from_url(
        'https://discord.com/api/webhooks/820726047242453012/WhgDEw-_3zND2YZ5AVdsI9R19fChYk7CND4ZzQQ59AEDqjNfMOZQkWcgFQFhYEM3GRMe', adapter=RequestsWebhookAdapter())
    wh.send(f'Suggestion - Add `{package_name}`', username='Dr Volt')
    return 'Success'


@application.route('/virus-check/<checksum>')
def virus_check(checksum: str):

    API_KEY = 'd3ea5c0f5b034325e3a752c2dcf0fd6754ef6c3aaabc47beeedb2eac738a4524'

    vt = VTApi(API_KEY)

    res = vt.get_file_report(checksum)

    keys = list(res.keys())

    data = res[keys[0]]['scans']

    detected = {}

    for value in data.items():
        if value[1]['detected'] == True:
            detected.update({value[0]: value[1]['result']})

    return detected

@application.route('/install')
def install():
    data = None
    
    with open('install.ps1', 'r') as f:
        data = f.read()

    return application.response_class(
       response=data,
       mimetype='text/plain'
    )

@application.route('/package/<name>')
def package(name: str):
    data = ''
    with open(rf'packages/{name}.json', 'r') as f:
        data = json.load(f)

    return application.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )


@application.route('/package-list')
def list_packages():
    data = ''
    with open(rf'package-list.json', 'r') as f:
        data = json.load(f)

    return application.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )


if __name__ == '__main__':
    application.run(debug=True)

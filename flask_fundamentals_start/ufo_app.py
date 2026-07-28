from flask import Flask, jsonify, request
import csv
app = Flask(__name__)

ufo_sightings = [
    {
        "datetime": "10/10/1949 20:30",
        "city": "san marcos",
        "state": "tx",
        "country": "us",
        "shape": "cylinder",
        "duration (seconds)": "2700",
        "duration (hours/min)": "45 minutes",
        "comments": "This event took place in early fall around 1949-50. It occurred after a Boy Scout meeting in the Baptist Church. The Baptist Church sit",
        "date posted": "4/27/2004",
        "latitude": "29.8830556",
        "longitude": "-97.9411111"
    },
    {
        "datetime": "10/10/1949 21:00",
        "city": "lackland afb",
        "state": "tx",
        "country": "",
        "shape": "light",
        "duration (seconds)": "7200",
        "duration (hours/min)": "1-2 hrs",
        "comments": "1949 Lackland AFB&#44 TX.  Lights racing across the sky &amp; making 90 degree turns on a dime.",
        "date posted": "12/16/2005",
        "latitude": "29.38421",
        "longitude": "-98.581082"
    }
]

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>UFO Sightings</title>
        </head>
        <body>
            <h1>Welcome to the UFO Sightings API</h1>
            <p>Use the /sightings route to get UFO sighting data.</p>
        </body>
    </html>
    """

@app.route('/sightings', methods=['GET'])
def get_sightings():
    country = request.args.get('country', '')
    sightings = load_ufo_data('data/scrubbed.csv')
    # You MUST make a copy of the list you want to modify, because you can't modify a list while looping through it.
    filtered_sightings = sightings.copy()
    # We loop through sightings, and remove from the copy (filtered_sightings)
    # for sighting in sightings:
        # if a country is specified and doesn't match, remove the sighting
        # if country and sighting['country'].lower() != country.lower():
        #     filtered_sightings.remove(sighting)
    # Another filtering option, if only filtering by one element (in this case country)
    # is to use a list comprehension search
    if country:
        filtered_sightings = [s for s in sightings if s.get('country', '').lower() == country.lower()]
    return jsonify(filtered_sightings)

@app.route('/paged_sightings', methods=['GET'])
def paged_sightings():
    country = request.args.get('country', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    sightings = load_ufo_data('data/scrubbed.csv')
    if country:
        filtered_sightings = [s for s in sightings if s.get('country', '').lower() == country.lower()]

    # implement the paging
    start = (page - 1) * per_page
    end = start + per_page
    # Remember end is EXCLUSIVE (does not include the end number)
    # For example when page is 1 and per_page is 25, we return index 0 to 24 (start = 0, end = 25)
    # when page is 2 and per_page is 25, we return index 25 to 49 (start = 25, end = 50)
    paginated_sightings = filtered_sightings[start:end]
    return jsonify(paginated_sightings)
    

def load_ufo_data(filepath):
    sightings = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sightings.append(row)
    return sightings
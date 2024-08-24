from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Map country codes to country names
country_codes_to_names = {
    1: 'India',
    14: 'Australia',
    30: 'Brazil',
    37: 'Canada',
    94: 'Indonesia',
    148: 'New Zealand',
    162: 'Phillipines',
    166: 'Qatar',
    184: 'Singapore',
    189: 'South Africa',
    191: 'Sri Lanka',
    208: 'Turkey',
    214: 'UAE',
    215: 'United Kingdom',
    216: 'United States'
}

@app.route('/')
def restaurant_list():
    page = request.args.get('page', 1, type=int)
    country = request.args.get('country', '')
    avg_spend = request.args.get('avg_spend', type=int)
    cuisines = request.args.get('cuisines', '')
    search = request.args.get('search', '')

    filters = {
        'page': page,
        'country': country,
        'avg_spend': avg_spend,
        'cuisines': cuisines,
        'search': search
    }

    # Call the API with the filters
    response = requests.get('http://localhost:5000/restaurants', params=filters)
    restaurants = response.json()

    # Fetch list of countries and cuisines for filtering options
    countries_response = requests.get('http://localhost:5000/countries')
    country_codes = countries_response.json()

    cuisines_response = requests.get('http://localhost:5000/cuisines')
    cuisines_list = cuisines_response.json()

    # Map country codes to country names for the dropdown
    countries = {code: country_codes_to_names[code] for code in country_codes}

    return render_template(
        'restaurant_list.html',
        restaurants=restaurants,
        page=page,
        countries=countries,
        cuisines_list=cuisines_list,
        country=country,
        avg_spend=avg_spend,
        cuisines=cuisines,
        search=search
    )

@app.route('/restaurant/<int:id>')
def restaurant_detail(id):
    response = requests.get(f'http://localhost:5000/restaurant/{id}')
    if response.status_code == 404:
        return render_template('restaurant_detail.html', restaurant={})

    restaurant = response.json()
    country_name = country_codes_to_names.get(restaurant.get('Country Code'), 'Unknown')
    return render_template('restaurant_detail.html', restaurant=restaurant, country_name=country_name)



if __name__ == '__main__':
    app.run(debug=True, port=5001)

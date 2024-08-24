from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('zomato.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/restaurant/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    conn = get_db_connection()
    restaurant = conn.execute('SELECT * FROM restaurants WHERE "Restaurant ID" = ?', (id,)).fetchone()
    conn.close()
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404
    return jsonify(dict(restaurant))

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    conn = get_db_connection()
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    offset = (page - 1) * per_page

    filters = []
    query = 'SELECT * FROM restaurants WHERE 1=1'
    
    if 'country' in request.args and request.args['country']:
        query += ' AND "Country Code" = ?'
        filters.append(request.args['country'])
        
    if 'avg_spend' in request.args and request.args['avg_spend']:
        query += ' AND "Average Cost for two" <= ?'
        filters.append(request.args['avg_spend'])
        
    if 'cuisines' in request.args and request.args['cuisines']:
        selected_cuisines = request.args['cuisines'].split(',')
        query += ' AND (' + ' OR '.join('"Cuisines" LIKE ?' for _ in selected_cuisines) + ')'
        filters.extend(f"%{cuisine.strip()}%" for cuisine in selected_cuisines)
        
    if 'search' in request.args and request.args['search']:
        search = request.args['search']
        query += ' AND ("Restaurant Name" LIKE ? OR "Address" LIKE ? OR "Locality" LIKE ?)'
        filters.extend([f"%{search}%" for _ in range(3)])
    
    query += ' LIMIT ? OFFSET ?'
    filters.extend([per_page, offset])
    
    restaurants = conn.execute(query, filters).fetchall()
    conn.close()
    return jsonify([dict(restaurant) for restaurant in restaurants])


@app.route('/countries', methods=['GET'])
def get_countries():
    conn = get_db_connection()
    countries = conn.execute('SELECT DISTINCT "Country Code" FROM restaurants').fetchall()
    conn.close()
    return jsonify([country["Country Code"] for country in countries])

@app.route('/cuisines', methods=['GET'])
def get_cuisines():
    conn = get_db_connection()
    cuisines = conn.execute('SELECT "Cuisines" FROM restaurants').fetchall()
    conn.close()
    all_cuisines = set()
    
    for row in cuisines:
        cuisines_field = row["Cuisines"]
        if cuisines_field:
            all_cuisines.update(cuisine.strip() for cuisine in cuisines_field.split(','))
    
    return jsonify(sorted(all_cuisines))

if __name__ == '__main__':
    app.run(debug=True)

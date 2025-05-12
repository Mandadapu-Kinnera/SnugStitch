from itertools import count
from flask import Flask, json, jsonify, render_template, request, redirect, send_from_directory, url_for, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'snugstitch'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        
        if account and check_password_hash(account['password'], password):
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            session['email'] = account['email']
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid credentials!')
    return render_template('login.html', loggedin=session.get('loggedin', False))



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s OR email = %s', (username, email))
        existing_user = cursor.fetchone()
        
        if existing_user:
            return render_template('signup.html', error='Username or email already exists!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return render_template('signup.html', error='Invalid email address!')
        else:
            cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                         (username, email, hashed_password))
            mysql.connection.commit()
            return redirect(url_for('login'))
    
    return render_template('signup.html', loggedin=session.get('loggedin', False))


@app.route('/home')
def home():
    return render_template('home.html', loggedin=session.get('loggedin', False))

@app.route('/profile')
def profile():
    if 'loggedin' in session:
        return render_template('profile.html', 
                             username=session['username'],
                             email=session.get('email', ''),
                             loggedin=True)
    return redirect(url_for('login'))


@app.route('/category/womens')
def womens_collection():
    return render_template('womens.html', loggedin=session.get('loggedin', False))


@app.route('/category/mens')
def mens_collection():
    return render_template('mens.html', loggedin=session.get('loggedin', False))


@app.route('/footwear')
def footwear():
    return render_template('footwear.html')

@app.route('/category/delivery')
def delivery():
    return render_template('delivery.html')


@app.route('/luxury')
def luxury():
    return render_template('luxury.html', loggedin=session.get('loggedin', False))

@app.route('/makeover')
def makeover():
    return render_template('makeover.html', loggedin=session.get('loggedin', False))

@app.route('/hair')
def hair():
    return render_template('hair.html', loggedin=session.get('loggedin', False))

@app.route('/menformaltshirts')
def menformaltshirts():
    return render_template('menformaltshirts.html', loggedin=session.get('loggedin', False))


@app.route('/hoodies')
def hoodies():
    return render_template('hoodies.html', loggedin=session.get('loggedin', False))


@app.route('/menformalpants')
def menformalpants():
    return render_template('menformalpants.html', loggedin=session.get('loggedin', False))

@app.route('/mensjeans')
def mensjeans():
    return render_template('mensjeans.html', loggedin=session.get('loggedin', False))

@app.route('/menshoes')
def menshoes():
    return render_template('menshoes.html', loggedin=session.get('loggedin', False))


@app.route('/menformalshoes')
def menformalshoes():
    return render_template('menformalshoes.html', loggedin=session.get('loggedin', False))


@app.route('/womenshoes')
def womenshoes():
    return render_template('womenshoes.html', loggedin=session.get('loggedin', False))



@app.route('/highrisefootwear')
def highrisefootwear():
    return render_template('highrisefootwear.html')  


@app.route('/clogs')
def clogs():
    return render_template('clogs.html', loggedin=session.get('loggedin', False))

@app.route('/ethnic')  
def ethnic():
    return render_template('ethnic.html', loggedin=session.get('loggedin', False))

@app.route('/flats')
def flats():
    return render_template('flats.html', loggedin=session.get('loggedin', False))

@app.route('/flipflops')
def flipflops():
    return render_template('flipflops.html', loggedin=session.get('loggedin', False))

@app.route('/platform')
def platform():
    return render_template('platform.html', loggedin=session.get('loggedin', False))

@app.route('/wedges')
def wedges():
    return render_template('wedges.html', loggedin=session.get('loggedin', False))


@app.route('/lipproducts')
def lipproducts():
    return render_template('lipproducts.html', loggedin=session.get('loggedin', False))

@app.route('/foundation')
def foundation():
    return render_template('foundation.html', loggedin=session.get('loggedin', False))

@app.route('/blush')
def blush():
    return render_template('blush.html', loggedin=session.get('loggedin', False))

@app.route('/compact')
def compact():
    return render_template('compact.html', loggedin=session.get('loggedin', False))

@app.route('/eyeproducts')
def eyeproducts():
    return render_template('eyeproducts.html', loggedin=session.get('loggedin', False))

@app.route('/concelear')
def concelear():
    return render_template('concelear.html', loggedin=session.get('loggedin', False))

@app.route('/blender')
def blender():
    return render_template('blender.html', loggedin=session.get('loggedin', False))

@app.route('/watch')
def watch():
    return render_template('watch.html', loggedin=session.get('loggedin', False))

@app.route('/chains')
def chains():
    return render_template('chains.html', loggedin=session.get('loggedin', False))

@app.route('/handbags')
def handbags():
    return render_template('handbags.html', loggedin=session.get('loggedin', False))

@app.route('/wallets')
def wallets():
    return render_template('wallets.html', loggedin=session.get('loggedin', False))


@app.route('/frocks')
def frocks():
    return render_template('frocks.html', loggedin=session.get('loggedin', False))

@app.route('/lehenga')
def lehenga():
    return render_template('lehenga.html', loggedin=session.get('loggedin', False))

@app.route('/womenpants')
def womenpants():
    return render_template('womenpants.html', loggedin=session.get('loggedin', False))

@app.route('/hairdye')
def hairdye():
    return render_template('hairdye.html', loggedin=session.get('loggedin', False))

@app.route('/haircare')
def haircare():
    return render_template('haircare.html', loggedin=session.get('loggedin', False))

@app.route('/hairextensions')
def hairextensions():
    return render_template('hairextensions.html', loggedin=session.get('loggedin', False))

@app.route('/hairmachines')
def hairmachines():
    return render_template('hairmachines.html', loggedin=session.get('loggedin', False))



@app.route('/cart')
def cart():
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('''
    SELECT cart.id, products.id as product_id, products.name, 
           products.price, products.image_url, cart.quantity 
    FROM cart 
    JOIN products ON cart.product_id = products.id 
    WHERE cart.user_id = %s
''', (session['id'],))


        cart_items = cursor.fetchall()
        
        total = sum(item['price'] * item['quantity'] for item in cart_items) if cart_items else 0
        
        return render_template('cart.html', 
                             cart_items=cart_items,
                             total=total,
                             loggedin=session.get('loggedin', False))
    
    except Exception as e:
        print(f"Database error: {str(e)}")
        return render_template('cart.html', 
                             cart_items=None,
                             total=0,
                             error="Error loading cart",
                             loggedin=session.get('loggedin', False))



@app.route("/wishlist")
def wishlist():
    if "id" not in session:  
        return redirect(url_for("login"))
    
    user_id = session["id"]
    cursor = mysql.connection.cursor()
    
    cursor.execute("""
    SELECT p.id, p.name, p.price, p.image_url 
    FROM wishlist w
    JOIN products p ON w.product_id = p.id
    WHERE w.user_id = %s
""", (user_id,))

    
    wishlist_items = cursor.fetchall()
    
    return render_template("wishlist.html", wishlist_items=wishlist_items)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'loggedin' not in session:
        return redirect(url_for('login'))
    
    user_id = session['id']
    size = request.form.get('size')
    quantity = 1  # Default quantity

    cursor = mysql.connection.cursor()
    
    # Check if item already exists in cart
    cursor.execute('''
        SELECT * FROM cart 
        WHERE user_id = %s AND product_id = %s
    ''', (user_id, product_id))
    existing_item = cursor.fetchone()
    
    if existing_item:
        # Update quantity if exists
        new_quantity = existing_item['quantity'] + 1
        cursor.execute('''
            UPDATE cart SET quantity = %s 
            WHERE id = %s
        ''', (new_quantity, existing_item['id']))
    else:
        # Insert new item
        cursor.execute('''
            INSERT INTO cart (user_id, product_id, quantity, size)
            VALUES (%s, %s, %s, %s)
        ''', (user_id, product_id, quantity, size))
    
    mysql.connection.commit()
    return redirect(url_for('cart'))


@app.route("/remove_from_wishlist/<int:product_id>")
def remove_from_wishlist(product_id):
    if "id" not in session:
        return redirect(url_for("login"))
    
    user_id = session["id"]
    cursor = mysql.connection.cursor()
    
    cursor.execute("DELETE FROM wishlist WHERE user_id = %s AND product_id = %s", (user_id, product_id))
    mysql.connection.commit()
    
    return redirect(url_for("wishlist"))


@app.route('/womenstshirts')
def womens_tshirts():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM products WHERE category = "womens-tshirts"')
        products = cursor.fetchall()
        print(f"Fetched products: {products}")  # Debug line
        return render_template('womenstshirts.html', 
                            products=products,
                            loggedin=session.get('loggedin', False))
    except Exception as e:
        print(f"Database error: {str(e)}")
        return render_template('womenstshirts.html', 
                            products=[],
                            error="Error loading products",
                            loggedin=session.get('loggedin', False))
    





import os
from datetime import datetime

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/customize')
def customize():
    return render_template('customize.html', loggedin=session.get('loggedin', False))

@app.route('/submit-custom-order', methods=['POST'])
def submit_custom_order():
    if 'designImage' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
        
    file = request.files['designImage']
    if file.filename == '':
        return jsonify({'error': 'No selected image'}), 400
        
    if file and allowed_file(file.filename):
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        try:
            file.save(file_path)
        except Exception as e:
            return jsonify({'error': f'File save failed: {str(e)}'}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400

    try:
        user_id = session.get('id')  # Will be None if not logged in
        clothing_type = request.form.get('clothingType')
        fabric_type = request.form.get('fabricType')
        measurements = request.form.get('measurements')
        street = request.form.get('street')
        city = request.form.get('city')
        state = request.form.get('state')
        zip_code = request.form.get('zip')
        
        delivery_address = f"{street}, {city}, {state} - {zip_code}"
        
        cursor = mysql.connection.cursor()
        cursor.execute('''
            INSERT INTO custom_orders 
            (user_id, image_url, clothing_type, fabric_type, measurements, 
             delivery_address, order_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (user_id, filename, clothing_type, fabric_type, measurements, 
              delivery_address, datetime.now()))
        
        mysql.connection.commit()
        return jsonify({'success': True})
        
    except Exception as e:
        print(f"Error saving order: {str(e)}")
        mysql.connection.rollback()
        return jsonify({'error': 'Failed to save order. Please try again.'}), 500
    
    
@app.route('/get-custom-orders')
def get_custom_orders():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('''
            SELECT * FROM custom_orders 
            ORDER BY order_date DESC 
            LIMIT 10
        ''')
        orders = cursor.fetchall()
        return jsonify([dict(order) for order in orders])
    except Exception as e:
        print(f"Error fetching orders: {str(e)}")
        return jsonify([])


@app.route('/static/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



@app.route('/customize-enhanced')
def customize_enhanced():
    return render_template('customize-enhanced.html', loggedin=session.get('loggedin', False))



@app.route('/submit-enhanced-order', methods=['POST'])
def submit_enhanced_order():
    try:
        required_fields = [
            'clothingCategory', 'clothingType', 'fullName', 
            'email', 'phone', 'street', 'city', 'state', 'zip',
            'deliveryDate'
        ]
        for field in required_fields:
            if not request.form.get(field):
                return jsonify({'success': False, 'error': f'Missing required field: {field}'}), 400

        file = request.files.get('designImage')
        filename = None
        if file and allowed_file(file.filename):
            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{secure_filename(file.filename)}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

        measurements = {}
        if request.form.get('standardSize') == 'custom':
            measurements = {
                'chest': request.form.get('chest'),
                'waist': request.form.get('waist'),
                'hips': request.form.get('hips'),
                'length': request.form.get('length'),
                'sleeveLength': request.form.get('sleeveLength'),
                'additional': request.form.get('additionalMeasurements')
            }
        else:
            measurements = {'standardSize': request.form.get('standardSize')}

        customization = {
            'color': request.form.get('color'),
            'fabric': request.form.get('fabric'),
            'specific_type': request.form.get('specificType'),
            'design_description': request.form.get('designDescription')
        }

        delivery_address = (
            f"{request.form['street']}, {request.form['city']}, "
            f"{request.form['state']} - {request.form['zip']}"
        )

        cursor = mysql.connection.cursor()
        cursor.execute('''
            INSERT INTO custom_orders_enhanced 
            (user_id, image_url, category, clothing_type, specific_type,
             design_description, color, fabric, measurements, customization,
             full_name, email, phone, delivery_address, delivery_date,
             special_instructions, order_date, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 'processing')
        ''', (
            session.get('id'),
            filename,
            request.form['clothingCategory'],
            request.form['clothingType'],
            request.form.get('specificType'),
            request.form.get('designDescription'),
            request.form.get('color'),
            request.form.get('fabric'),
            json.dumps(measurements),
            json.dumps(customization),
            request.form['fullName'],
            request.form['email'],
            f"{request.form.get('countryCode', '')}{request.form['phone']}",
            delivery_address,
            request.form['deliveryDate'],
            request.form.get('specialInstructions'),
            datetime.now()
        ))
        
        mysql.connection.commit()
        return jsonify({
            'success': True,
            'orderId': cursor.lastrowid,
            'deliveryDate': request.form['deliveryDate']
        })

    except Exception as e:
        print(f"Error saving enhanced order: {str(e)}")
        mysql.connection.rollback()
        return jsonify({
            'success': False,
            'error': 'Failed to save order. Please try again.'
        }), 500
    




    

@app.route('/get-enhanced-orders')
def get_enhanced_orders():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('''
            SELECT * FROM custom_orders_enhanced 
            ORDER BY order_date DESC 
            LIMIT 5
        ''')
        orders = cursor.fetchall()
        return jsonify([dict(order) for order in orders])
    except Exception as e:
        print(f"Error fetching enhanced orders: {str(e)}")
        return jsonify([])
    

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)





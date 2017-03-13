from flask import Flask,render_template,url_for,request,redirect
from sqlite_setup import Restaurant, MenuItem, Base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
app = Flask(__name__)


itemName = "Special mix veg spicy Pizza"

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

def Helloworld():
    print ("python 3.5")
#     createRestaurantRecord(itemName)
    return '<h1>Hello world Welcome to Heroku !!!</h1>'
@app.route('/welcome')
def Welcome():
    return '<h1>Welcome to My world !!! </h1>'

@app.route('/restaurant/<int:restaurant_id>/')
def FindRestaurantMenuByID(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menu.html',restaurant = restaurant,items = items)

@app.route('/')
@app.route('/index/')
@app.route('/restaurants/')
def GetRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('index.html',restaurants = restaurants)

#Task 1: Create route for newMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/new/', methods = ['GET','POST'])
def newMenuItem(restaurant_id):
    if(request.method == 'POST'):
        newItem  = MenuItem(name = request.form['name'],restaurant_id = restaurant_id )
        session.add(newItem)
        session.commit()
        return redirect(url_for('FindRestaurantMenuByID',restaurant_id = restaurant_id))
    else:
        return render_template('newmenuitem.html',restaurant_id = restaurant_id)
    

#Task 2: Create route for editMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:MenuID>/edit/', methods = ['GET', 'POST'])
def editMenuItem(restaurant_id, MenuID):
    editedItem = session.query(MenuItem).filter_by(id = MenuID).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('FindRestaurantMenuByID', restaurant_id = restaurant_id))
    else:
        
        #USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
        return render_template('editmenuitem.html', restaurant_id = restaurant_id, MenuID = MenuID, item = editedItem)
    
@app.route('/restaurant/new/',methods = ['GET','POST'])   
def createNewResturant():
    if request.method == 'POST':
        
        name = request.form['name']
        myRestaurant = Restaurant(name = name)
        session.add(myRestaurant)
        session.commit()
        return redirect(url_for('GetRestaurants'))
    else:
        return render_template('newrestaurant.html')
    
#Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:MenuID>/delete/')
def deleteMenuItem(restaurant_id, MenuID):
    return "page to delete a new menu item. Task 3 complete!"
         


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)
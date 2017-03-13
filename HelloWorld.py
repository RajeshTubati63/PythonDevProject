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

@app.route('/')
def Helloworld():
    print ("python 3.5")
    createRestaurantRecord(itemName)

    return '<h1>Hello world Welcome to Heroku !!!</h1>'


@app.route('/welcome')
def Welcome():
    return '<h1>Welcome to My world !!! </h1>'

@app.route('/restaurant/<int:restaurant_id>/')
def FindRestaurantMenuByID(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menu.html',restaurant = restaurant,items = items)



def createRestaurantRecord(itemName):
# Insert 
    myFirstRestaurant = Restaurant(name = "Pizza Palace")
    session.add(myFirstRestaurant)
    session.commit()  

    menuItem = MenuItem(name = itemName, course = 'Pizzas', description = "This is about biriyani's here", restaurant_id = myFirstRestaurant.id)
    session.add(menuItem)
    session.commit()
#Read Menu items based on Restaurant id
    allRows = session.query(MenuItem).all()
    for item in allRows:
        print (item.id)
        print (item.name)
#Update 
#     oneRow.name = "Chicken Burger"
#     session.add(oneRow)
#     session.commit()


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)
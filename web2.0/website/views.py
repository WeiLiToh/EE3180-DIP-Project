from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
import mysql.connector

views = Blueprint('views', __name__)

def get_db_data(search_query=None):
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Password",
            database="dip_db",
            port=3306
        )
        cursor = mydb.cursor()

        query = "SELECT id, username, first_name, last_name, hp, role, department FROM user"

        if search_query:
            query += f" WHERE username LIKE '%{search_query}%' OR first_name LIKE '%{search_query}%' OR last_name LIKE '%{search_query}%'"

        print(f"Executing Query: {query}")  # Debugging Output
        cursor.execute(query)  
        data = cursor.fetchall()

        cursor.close()
        mydb.close()
        return data

    except mysql.connector.Error as err:
        print("❌ Database Error:", err)
        return []

@views.route('/', methods=['GET', 'POST'])  
@login_required
def home():
    search_query = request.form.get('search', '')  
    users = get_db_data(search_query)  

    return render_template("home.html", user=current_user, users=users, search_query=search_query)

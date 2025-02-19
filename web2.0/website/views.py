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
        params = ()

        # Modify query if a search term is provided
        if search_query:
            query += " WHERE username LIKE %s OR first_name LIKE %s OR last_name LIKE %s"
            params = (f"%{search_query}%", f"%{search_query}%", f"%{search_query}%")

        print(query % params)
        cursor.execute(query, params)
        data = cursor.fetchall()

        cursor.close()
        mydb.close()
        return data

    except mysql.connector.Error as err:
        print("❌ Database Error:", err)
        return []

# Main login for users
@views.route('/', methods=['GET', 'POST'])  # Add 'POST' method to handle search
@login_required
def home():
    search_query = request.form.get('search', '')  # Get search input
    users = get_db_data(search_query)  # Fetch data with optional search filter

    return render_template("home.html", user=current_user, users=users, search_query=search_query)

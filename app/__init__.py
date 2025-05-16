from flask import Flask
from flask import render_template
from random import randint
from supabase import create_client
from dotenv import load_dotenv
import os


#get Environment Variables
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

#connect to supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__) 

@app.get("/")
def home():
    response = supabase.table("things").select().execute()
    records = response.data
    return render_template("pages/home.jinja", things = records)



@app.errorhandler
def errorHandler():
    return render_template("pages/404.jinja")


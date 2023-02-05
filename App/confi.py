from flask import Flask, render_template, request, redirect, url_for
#import pymysql
import pymysql.cursors

app = Flask(__name__)

# Connect to the database
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='organdonation',
    cursorclass=pymysql.cursors.DictCursor
)

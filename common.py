from flask import Flask,flash, redirect,url_for, render_template, request,session
import responses
import evemodel 
import expmodel
import umodel
import datetime
from dateutil import parser
import calendar
from collections import defaultdict

app = Flask(__name__)
app.secret_key = 'vanradiamus'
evemodel.create()
expmodel.create()
umodel.create()
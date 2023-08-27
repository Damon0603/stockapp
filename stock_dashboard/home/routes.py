from re import I
from stock_dashboard.home import blueprint
from flask import render_template, request, redirect, url_for, flash
from stocks import * 
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


@blueprint.route('/', methods=['GET', 'POST'])
def home():
 

    return render_template("index.html")


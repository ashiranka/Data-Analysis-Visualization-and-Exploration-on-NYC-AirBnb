from flask import Flask, request, jsonify, render_template, redirect, url_for
import csv
import json
import datetime
import pymongo
from bson import json_util
import numpy as np
import pandas as pd
import pandas_profiling


app = Flask(__name__)


# Connect to MongoDB Database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["new_york_airbnb"]
col = db["Detail"]


# Call route (main page)
@app.route('/', methods=['GET', 'POST'])
def mainmethod():
    return render_template("mainPage.html")


# SEARCH BY CATEGORY
@app.route('/searchByCategory', methods=['GET', 'POST'])
def searchByCategory():
    if request.method == "GET":
        return render_template("searchByCategory.html")

    if request.method == "POST":
        name1 = request.form.get('search')
        name2 = request.form.get('keys')

        # All
        if name2 == "all":
            return redirect(url_for("all", category=name2))

        # name
        if name2 == "name":
            return redirect(url_for("categoryName", category=name2, searchFor=name1))

        # host_id
        if name2 == "host_id":
            return redirect(url_for("categoryhostid", category=name2, searchFor=name1))

        # neighbourhood_group
        if name2 == "neighbourhood_group":
            return redirect(url_for("categoryNeighbourhoodGroup", category=name2, searchFor=name1))

        # neighbourhood
        if name2 == "neighbourhood":
            return redirect(url_for("categoryNeighbourhood", category=name2, searchFor=name1))

        # latitude
        if name2 == "latitude":
            return redirect(url_for("categoryLatitude", category=name2, searchFor=name1))

        # longitude
        if name2 == "longitude":
            return redirect(url_for("categoryLongitude", category=name2, searchFor=name1))

        # room_type
        if name2 == "room_type":
            return redirect(url_for("categoryRoomType", category=name2, searchFor=name1))

        # price
        if name2 == "price":
            return redirect(url_for("categoryPrice", category=name2, searchFor=name1))

        # minimum_nights
        if name2 == "minimum_nights":
            return redirect(url_for("categoryMinimumNights", category=name2, searchFor=name1))

        # number_of_reviews
        if name2 == "number_of_reviews":
            return redirect(url_for("categoryNumberReviews", category=name2, searchFor=name1))

        # reviews_per_month
        if name2 == "reviews_per_month":
            return redirect(url_for("categoryReviewsMonth", category=name2, searchFor=name1))

        # calculated_host_listings_count
        if name2 == "calculated_host_listings_count":
            return redirect(url_for("categoryCalculatedCount", category=name2, searchFor=name1))

        #  availability_365
        if name2 == "availability_365":
            return redirect(url_for("categoryAvailability", category=name2, searchFor=name1))


# all
@app.route('/all/<category>', methods=['GET', 'POST'])
def all(category):
    tempOutput = []
    docs_list = list(col.find())
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# name
@app.route('/categoryName/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryName(category, searchFor):
    tempOutput = []
    # query = {"InnerDetails.name": searchFor}
    query = {"InnerDetails.name": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# host_id
@app.route('/categoryhostid/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryhostid(category, searchFor):
    tempOutput = []
    searchFor = int(searchFor)
    query = {"InnerDetails.host_id": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# neighbourhood_group
@app.route('/categoryNeighbourhoodGroup/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryNeighbourhoodGroup(category, searchFor):
    tempOutput = []
    query = {"InnerDetails.neighbourhood_group": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# neighbourhood
@app.route('/categoryNeighbourhood/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryNeighbourhood(category, searchFor):
    tempOutput = []
    query = {"InnerDetails.neighbourhood": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# latitude
@app.route('/categoryLatitude/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryLatitude(category, searchFor):
    tempOutput = []
    searchFor = float(searchFor)
    query = {"InnerDetails.latitude": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# longitude
@app.route('/categoryLongitude/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryLongitude(category, searchFor):
    tempOutput = []
    searchFor = float(searchFor)
    query = {"InnerDetails.longitude": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# room_type
@app.route('/categoryRoomType/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryRoomType(category, searchFor):
    tempOutput = []
    query = {"InnerDetails.room_type": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# price
@app.route('/categoryPrice/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryPrice(category, searchFor):
    tempOutput = []
    searchFor = int(searchFor)
    query = {"InnerDetails.price": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# minimum_nights
@app.route('/categoryMinimumNights/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryMinimumNights(category, searchFor):
    tempOutput = []
    searchFor = int(searchFor)
    query = {"InnerDetails.minimum_nights": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)\



# number_of_reviews
@app.route('/categoryNumberReviews/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryNumberReviews(category, searchFor):
    tempOutput = []
    searchFor = int(searchFor)
    query = {"InnerDetails.number_of_reviews": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# reviews_per_month
@app.route('/categoryReviewsMonth/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryReviewsMonth(category, searchFor):
    tempOutput = []
    searchFor = float(searchFor)
    query = {"InnerDetails.reviews_per_month": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# calculated_host_listings_count
@app.route('/categoryCalculatedCount/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryCalculatedCount(category, searchFor):
    tempOutput = []
    searchFor = int(searchFor)
    query = {"InnerDetails.calculated_host_listings_count": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# availability_365
@app.route('/categoryAvailability/<category>/<searchFor>', methods=['GET', 'POST'])
def categoryAvailability(category, searchFor):
    tempOutput = []
    searchFor = int(searchFor)
    query = {"InnerDetails.availability_365": searchFor}
    docs_list = list(col.find(query))
    for curr in docs_list:
        tempOutput.append(curr['InnerDetails'])
    result = pd.DataFrame(tempOutput)
    return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# SEARCH BY KEYWORD
# db.Details.createIndex( { "$**": "text" } )
@app.route('/searchByKeyword', methods=['GET', 'POST'])
def searchByKeyword():

    if request.method == "GET":
        return render_template("searchByKeyword.html")

    if request.method == "POST":
        tempOutput = []
        name1 = request.form.get('search')
        query = {"$text": {"$search": name1}}
        docs_list = list(col.find(query))
        for curr in docs_list:
            tempOutput.append(curr['InnerDetails'])
        result = pd.DataFrame(tempOutput)
        return render_template('print.html',  tables=[result.to_html(classes='data')], titles=result.columns.values)


# VISUALIZATION
@app.route('/visualization', methods=['GET', 'POST'])
def visualization():
    if request.method == "GET":
        return render_template("visualization.html")

    if request.method == "POST":
        picture = request.form.get('viz')
        pathOfPicture = "../static/css/images/"+picture+".png"
        return render_template('picture.html', pathOfPicture=pathOfPicture)


# Call Main Route
if __name__ == '__main__':
    app.run(debug=True, port=9098)

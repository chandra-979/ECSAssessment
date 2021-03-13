"""Routes for the course resource.
"""

from run import app
from flask import request
from http import HTTPStatus
import data
import flask
import re
from flask_paginate import Pagination, get_page_args

@app.route("/course/<int:id>", methods=['GET'])
def get_course(id):
    """Get a course by id.

    :param int id: The record id.
    :return: A single course (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------   
    1. Bonus points for not using a linear scan on your data structure.
    """
    # YOUR CODE HERE

    courses=data.load_data()
    for course in courses:
        if course.get('id')==id:
            return flask.jsonify(course),200
#    return flask.jsonify(courses)
    else:
        return flask.jsonify({"message":"Course "+str(id)+" does not exists"}),404
                
    
        


@app.route("/course", methods=['GET'])
def get_courses():
    """Get a page of courses, optionally filtered by title words (a list of
    words separated by commas".

    Query parameters: page-number, page-size, title-words
    If not present, we use defaults of page-number=1, page-size=10

    :return: A page of courses (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    ------------------------------------------------------------------------- 
    1. Bonus points for not using a linear scan, on your data structure, if
       title-words is supplied
    2. Bonus points for returning resulted sorted by the number of words which
       matched, if title-words is supplied.
    3. Bonus points for including performance data on the API, in terms of
       requests/second.
    """
    # YOUR CODE HERE
    title_words=[]
    page_number=int(request.args.get('page-number',1))
    page_size=int(request.args.get('page-size',10))
    if request.args.get('title-words')!=None:
        title_words=request.args.get('title-words').split(',')
    sid=page_size*page_number-page_size
    eid=sid+page_size
    courses=data.load_data()[sid:eid]
    if len(title_words)>0:
        filt_courses=[]
        for course in data.load_data():
            if len(title_words)>0:
                for kw in title_words:
                    if re.search(kw,course['title'])!=None:
                        filt_courses.append(course)
        if len(filt_courses)==0:
            return flask.jsonify({"message":"No courses available"})
        return flask.jsonify(filt_courses)
    if(len(courses[sid:eid]))>0:
        return flask.jsonify(courses[sid:eid])
    else:
        return flask.jsonify({"message":"courses not available"})


@app.route("/course", methods=['POST'])
def create_course():
    """Create a course.
    :return: The course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the POST body fields
    """
    # YOUR CODE HERE
    course={
            "date_created": "2020-07-04 01:02:49", 
            "date_updated": "2021-01-31 15:07:20", 
            "description": "Scala is a multi-paradigm, general-purpose programming language.", 
            "discount_price": 3, 
            "id": 5, 
            "image_path": "", 
            "on_discount": true, 
            "price": 30, 
            "title": "Even A Kid Can Learn Scala!"
            }
    return flask.jsonify(course)


@app.route("/course/<int:id>", methods=['PUT'])
def update_course(id):
    """Update a a course.
    :param int id: The record id.
    :return: The updated course object (see the challenge notes for examples)
    :rtype: object
    """

    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    1. Bonus points for validating the PUT body fields, including checking
       against the id in the URL

    """
    # YOUR CODE HERE
    courses=data.load_data()
    for course in courses:
        if course.get('id')==id:
            course['id']=id
            return flask.jsonify(course)
    return flask.jsonify({"message":"Course "+str(id)+" does not exists"})


@app.route("/course/<int:id>", methods=['DELETE'])
def delete_course(id):
    """Delete a course
    :return: A confirmation message (see the challenge notes for examples)
    """
    """
    -------------------------------------------------------------------------
    Challenge notes:
    -------------------------------------------------------------------------
    None
    """
    # YOUR CODE HERE
    courses=data.load_data()
    for course in courses:
        if course.get('id')==id:
            course['id']=id
            return flask.jsonify({"message":"The specified course was  deleted"})
    return flask.jsonify({"message":"Course "+str(id)+" does not exists"})



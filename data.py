"""Routines associated with the application data.
"""
import json

courses = {}

def load_data():
    """Load the data from the json file.
    """
    f=open(r"C:\Users\chandrakumar\Desktop\challenge\json\course.json")
    data=json.load(f)
    print(data)
    return data



#!/usr/bin/env python3
"""
Function that inserts a new document in a collection based
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs

    Args:
        mongo_collection: pymongo collection object
        **kwargs: keyword arguments representing the fields

    returns:
        The _id of the newly inserted document.
    """
    document = kwargs
    result = mongo_collection.insert_one(document)
    return result.inserted_id

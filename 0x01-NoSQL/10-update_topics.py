#!/usr/bin/env python3
"""
Changes all topics of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name

    Args:
        mongo_collection: pymongo collection object
        name: schoo; name to be update
        topics: list of topics approached in the school

    returns:
        None.
    """
    mongo_collection.update_many({ "name": name}, { "$set": {"topics": topics} })

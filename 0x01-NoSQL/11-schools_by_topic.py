#!/usr/bin/env python3
"""
List os school having a specific topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: PyMongo collection object.
        topic (str): Topic to search.

    Returns:
        A list of schools matching the specified topic.
    """
    schools = mongo_collection.find({"topics": topic})
    return list(schools)

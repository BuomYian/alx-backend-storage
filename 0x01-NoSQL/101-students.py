#!/usr/bin/env python3
"""
Returns all students sorted by their average score
"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students sorted by their average score.

    Args:
        mongo_collection: PyMongo collection object.

    Returns:
        A list of students sorted by their average score.
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]

    students = mongo_collection.aggregate(pipeline)
    return list(students)

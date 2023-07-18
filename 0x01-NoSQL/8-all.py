#!/usr/bin/env python3
"""
Function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    List all non empty document in the collection

    Args:
        mongo_collection: pymongo collection object.

    returns:
        Lis of all documents in the collection
    """
    documents = []
    cursor = mongo_collection.find()

    for document in cursor:
        documents.append(document)

    return documents

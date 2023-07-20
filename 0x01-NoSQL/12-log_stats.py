#!/usr/bin/env python3
"""
Script that provides some stats Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def log_stats():
    """
     script that provides some stats about Nginx logs stored in MongoDB:
    """
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Count of logs by method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"methods": method})
        print(f"\tmethod {method}: {count}")

    # Count of logs with method=GET and path=/status
    count_status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{count_status} status check")

if __name__ == "__main__":
    log_stats()

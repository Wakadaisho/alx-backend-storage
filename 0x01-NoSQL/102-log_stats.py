#!/usr/bin/env python3
"""
Returns the statistical data of HTTP methods in logs
Add top 10 of the most present IPs in the collection
nginx of the database logs
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    requests = client.logs.nginx

    methods = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    for method in methods:
        methods[method] = requests.count_documents({"method": method})

    print("{} logs".format(requests.count_documents({})))
    print("Methods:")
    for method, count in methods.items():
        print("\tmethod {}: {}".format(method, count))

    status_check = requests.count_documents({"method": "GET",
                                             "path": "/status"})
    print("{} status check".format(status_check))
    print("IPs:")
    ips = requests.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in ips:
        print("\t{}: {}".format(ip.get("_id"), ip.get("count")))

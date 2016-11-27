#!/usr/bin/python3
#
# Using this as a rest-ful server so that I can develop the android client
#  
# by Steve Mink
# Copyright 2016 Mink Technologies LLC
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
#
import argparse
from flask import Flask, jsonify, request, make_response
import os
import subprocess
import time

HTTP_STATUS_NOT_FOUND = 404

version = 1.0
app = Flask(__name__)

@app.route('/lanbrowse', methods=['GET'])
def device_list():
    name = request.values.get("name")
    print("Got:", name);
    if name is None:
        return jsonify({"error": "Missing required parameter: name"})
    elif name == "connect":
        return jsonify({"status": "Connecting"})
    elif name == "where":
        return jsonify({"status": "Showing CWD"})
    elif name == "list":
        return jsonify({"status": "Showing list"})
    elif name == "info":
        return jsonify({"status": "Showing info"})
    elif name == "open":
        return jsonify({"status": "Opening file/directory"})
    elif name == "find":
        return jsonify({"status": "finding file/directory"})
    elif name == "download":
        return jsonify({"status": "downloading file to client"})
    elif name == "play":
        return jsonify({"status": "playing file locally"})
    elif name == "stream":
        return jsonify({"status": "streaming file to client"})
    # time.sleep(5) # simulating different test conditions
    return jsonify({"status": "Cannot process unknown command:" + name})

@app.errorhandler(HTTP_STATUS_NOT_FOUND)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}),
                         HTTP_STATUS_NOT_FOUND)

# CLI params
#  - root (-r): root dir (no parent) - optional (default: dot)
#  - bind (-b): bind to address  - optional (default: 0.0.0.0)
#  - port (-p): port - optional (default: 5200)
#  - canplay (-m): whether we can play locally - optional; no parameter (default false)
#  - canstream (-s): whether we can stream - optional; no parameter (default false)
if __name__ == '__main__':
    # setup argument handling first
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bind", default='0.0.0.0', action="store", 
                        dest="bindaddr", help="only listen on specified address")
    parser.add_argument("-p", "--port", type=int, default=5200, action='store',
                        dest='portnum', help="port number server listens on")
    parser.add_argument("-r", "--root", default=os.getcwd(), action="store", 
                        dest="bindaddr", help="only listen on specified address")
    parser.add_argument("-m", "--canplay", help="indicates we can play a file locally")
    parser.add_argument("-s", "--canstream", help="indicates we can stream a file")
    args = parser.parse_args()

    # run it as specified
    try:
        app.run(debug=True, host=args.bindaddr, port=int(args.portnum))
    except OSError:
        print("Unable to start application - is there an instance already running?")
    


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Standard imports
import sys
import logging

# Twistedimports
from twisted.web.server import Site
from twisted.web.static import File
from twisted.web.resource import Resource
from twisted.internet import reactor
import twisted.web.server as server

# Custom imports
import cgi

# Hardset values for the server
__PORT__ = 8086

logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s %(message)s')


class MainPage(File):
    isleaf = False
    allowedMethods = ("POST", "GET")

    def __init__(self):
        File.__init__(self, '/home/jnam/workspace/CubedAnalytics/public/')

    # def render_GET(self, request):
        # return "test"

    # def render_POST(self, request):
    #     return "Test2"

    def getChild(self, name, request):
        if name == "//" or name == " ":
            print "this worked"
        else:
            logging.info(('jMagic', name, request))
            return "this worked here?"


def main():
    # Set up the main page
    root = MainPage()
    # root.putChild("", )
    factory = Site(root)

    # Open TCP/Port and listen for incoming connections
    reactor.listenTCP(__PORT__, factory)

    # Run the server
    reactor.run()


# Handle Authentication

# Error handling

if __name__ == "__main__":
    main()
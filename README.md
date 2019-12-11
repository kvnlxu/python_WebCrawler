# python_WebCrawler

Simple web crawler written in python 3 with a basic link filter. Run by calling StartCrawler.py. Modifiable settings are at the top of the StartCrawler.py file. The crawler_save file must be removed to start a fresh run. The clean.bat shows an example of how to remove files from previous runs when running with default settings.

## Setting Variables
WEBPAGES_DIR - directory where crawled web pages are saved
SAVEFILE_NAME - file to store crawler progress
SEED - initial web page to start from
LIMIT - hard limit on number of webpages to store

## Usage/Purpose
This is meant to be a basic skeleton code for a web crawler. Filtering options can be added to the crawler class to better suit the user needs (i.e. save only files with certain keywords).

## Features not yet implemented
Separate file for default settings
CLI interface for user inputted settings
Modifiable politeness delay

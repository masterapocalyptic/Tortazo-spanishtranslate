from os.path import expanduser
import os
import sys

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

tortazo_currentdir=os.getcwd()
tortazo_minorversion=2
tortazo_majorversion=1
home = expanduser("~")
####
####          REPORTING SETTINGS
####
ShodanOutputFile=home+"/shodanReport.html"
NmapOutputFile=home+"/nmapReport.html"
deepWebCrawlerOutdir=os.getcwd()+"/onionSites/"
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
####
####          DATABASE SETTINGS
####
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
databaseName="db/tortazo.db"
dbPostgres=True
dbMySQL=False
dbName="tortazo"
dbServer="127.0.0.1"
dbPort=5432
dbUser="postgres"
dbPass="postgres"
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
####
####          NESSUS SETTINGS
####
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
nessusHost="127.0.0.1"
nessusPort=8834
nessusUser="adastra"
nessusPass="adastra"
nessusInitialSeq=200
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
####
####          SOCKS SETTINGS AND ONION REPOSITORY PROPERTIES
####
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
socksHost="127.0.0.1"
#Default Socks Port if TOR has been started with tor-browser.
# If you start manually TOR using the command "tor -f torrc" the default Socks Port will be 9050. Beware with that!!
socksPort=9150
#Number of seconds before give up and timeout for every http connection against the generated onion addresses generated in the onion repository mode.
timeOutRequests=5
#Tries to load in database the records in the file "db/knownOnionSites.txt"
loadKnownOnionSites=True
#Path for the Tor Executable.
torExecutablePath="/home/adastra/Escritorio/TOR/tor-browser_363/Tor/tor"
onionupUrl="https://onionup.com/?q="
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
####
####          GEOLOCATION DATABASE SETTINGS
####
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
geoLiteDB="db/GeoLiteCity.dat"
# Probe selector :

This thing will take a json file from the ripe NCC FTP server to take all the id's out and discriminate on what it wants.

First, it will take all country id's and create a dictionnary with it. Then for every country, it will randomly select 10 probes (if available) that are IPv4 and IPv6. It will output the final list on the terminal on a single line separated by coma's (format required by the RIPE Atlas interface for bulk id import)


# Needed : 
You need to download the latest archive from [ftp.ripe.net](https://ftp.ripe.net/ripe/atlas/probes/archive/)
the .bz2 needs to be decompressed and file needs to be renamed atlas.json

# PHT Demonstrator

This repository provides the building blocks for a PHT station. The following components have been included:

* A central message broker
* Station A
* Station B

Both stations contain the following components:

* A computation engine for PHT purposes
* An RDF store for the available data
* The [Triplifier](https://gitlab.com/UM-CDS/fair/tools/triplifier) to convert the uploaded CSV files into RDF
* A Filebrowser to upload CSV files

## How to run this repository?

There is a [startup.bat](startup.bat) file available for Windows users, or [startup.sh](startup.sh) for macOS/Linux users. This file can be executed to setup the complete infrastructure on one machine.
The file [teardown.bat](teardown.bat) can be used to stop and remove all services accordingly ([teardown.sh](teardown.sh) for macOS/Linux users).
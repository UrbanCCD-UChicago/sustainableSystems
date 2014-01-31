EcoDistricts/Sustainable Systems Framework
======================

The initial programming framework for the San Francisco Sustainable Systems project

##San Francisco Sustainable Systems Project 
We are helping San Francisco use data collected by the city to help inform community-driven sustainable development. This project 

###Setup
First, you'll need to set up your machine to work with the data in a shared environment. We've made this easy for you by using [vagrant](link to vagrant).

To get started take the following steps
- **Clone this repo** by opening up terminal, changing directories, and typing `git clone git@github.com:hunterowens/ecodistricts_framework.git`
- **Change drives** into your newly cloned project folder by typing `cd ecodistricts_framework`
- **Start Vagrant** by typing `vagrant up`

After a few moments, you will have a a vagrant instance up and running and you will be working with the common development environment used by all team members.


###Tasks



###Process

####Managing Data
All raw data will be store on S3 buckets. To load a dataset, use the requests library to grab the dataset on load. I recommend using an ipython notebook as your dev environment in order to only download the dataset once.  ‘S3 Endpoint’ + filename. 

####Common Tasks Across Datasets
The Utils module will contain a variety of custom utilities that 
For example, convert XLSX files to CSV files, or extract tabular data from a shapefile. 

####Dataset-specific cleaning and analysis 
All scripts making custom modifications  and cleaning will be saved in the scripts directory. Please only add 1 script per dataset. Reminder, you can use version control (git) to get access to old versions of the same file. Commit Early and Commit Often. 

####Merging and Linking (TODO)
---

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

You should also set up a virtual env called 'venv' by running `virtualenv venv` in the root. 

#### Syncing Data

First, you're going to need to install the [AWS command line tools](http://aws.amazon.com/cli/), which can be done by running `pip install awscli`. Then, create a folder in the root directory of the project called `data`. This folder will not be added to git (even when you run `git add .`) because it is in the `.gitignore`. 

Then, in your venv's activate script (should be at 'venv/bin/activate', simply open with a text editor) add 
`
export AWS_ACCESS_KEY_ID=AKIAJIBF5J7ASUINF5NA
export AWS_SECRET_ACCESS_KEY=ke9ITTJWFX0R/XWCHyf2+sucIyy07ziHCYzO5J1l
export  AWS_DEFAULT_REGION=us-west-2
`
to the bottom of the script and reactivate the virtualenv. 

Then, you should be able to run `aws s3 sync  s3://ecodistricts /path/to/data/directory` and you'll have a copy of the data stored on your local machine. 

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

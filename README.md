# Open Data Search
This project is a part of the [Data Science Working Group](http://datascience.codeforsanfrancisco.org) at [Code for San Francisco](http://www.codeforsanfrancisco.org).  Other DSWG projects can be found at the [main GitHub repo](https://github.com/sfbrigade/data-science-wg).

#### -- Project Status: Active

## Project Intro/Objective
The purpose of this project is to use analytics and topic modelling of search text to improve the user experience at https://data.sfgov.org/

### Partner
* SF Open Data
* https://datasf.org/opendata/
* Partner contact: Jason Lally, @jasonlally


### Methods Used
* Data Analysis
* Descriptive Statistics/Data Visualization
* Natural Language Processing
* Word2Vec Modelling

### Technologies
* R
* Python
  - Pandas, Spacy

## Project Description

Th major goals of the project are as follows:
* Clean and process search terms and categorize search terms by quality
* Utilize Natural Language Processing and Topic Modelling on valid search terms and cluster terms to determine potential demand for data sources
* Provide actionable insights to improve search functionality on the site


## Needs of this project

- NLP/Topic Modelling Expertise

## Getting Started

1. Clone this repo, for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)
2. Data is being kept [here](Repo folder containing raw data)   
   
3. Data processing/transformation script is [Data Combiner](https://github.com/sfbrigade/open-data-search/blob/master/data_combiner.R) 
    - Script that combines raw data from .tsv files into a single .csv file
    * [Search Data Processing Jupyter Notebook](https://github.com/sfbrigade/open-data-search/blob/master/search_data_processing.ipynb) - Notebook that cleans, processes and categorizes search terms

*If your project is well underway and setup is fairly complicated (ie. requires installation of many packages) create another "setup.md" file and link to it here*  


5. Follow setup [instructions](Link to file)

## Featured Notebooks/Analysis
* [Exploration of Search Google Analytics](https://github.com/sfbrigade/open-data-search/blob/master/open_search_exploration.md)

* [Search Data Modelling Juptyer Notebook](https://github.com/sfbrigade/open-data-search/blob/master/word2vec_modelling.ipynb) 
    - Notebook with vectorization of search terms using pre-trained word2vec model
    
* 

## Contributing DSWG Members

**Team Leads (Contacts) : [Rocio S Ng](https://github.com/RocioSNg) (@Rocio)**

#### Other Members:

|Name     |  Slack Handle   | Github 
|---------|-----------------|
|[Bao Lin Liu](https://github.com/baolinliu) | @johnDoe        |
|[Scott Brenstuhl](https://github.com/808sAndBR)|     @janeDoe    |



## Contact
* If you haven't joined the SF Brigade Slack, [you can do that here](http://c4sf.me/slack).  
* Our slack channel is `#datasci-open-data_src`
* Feel free to contact team leads with any questions or if you are interested in contributing!

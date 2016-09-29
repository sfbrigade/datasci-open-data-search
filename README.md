# Open Data Search
This project aims to use analytics and topic modelling of search text to improve the user experience at https://data.sfgov.org/

## General Goals
* Clean and process search terms and categorize search terms by quality
* Utilize Natural Language Processing and Topic Modelling on valid search terms and cluster terms to determine potential demand for data sources
* Provide actionable insights to improve search functionality on the site

## Contributors
* [Rocio S Ng](https://github.com/RocioSNg) - Project Lead and Contact
* [Bao Lin Liu](https://github.com/baolinliu)
* [Scott Brenstuhl](https://github.com/808sAndBR)

## Data Processing 
* [Data Combiner](https://github.com/sfbrigade/open-data-search/blob/master/data_combiner.R) - Script that combines raw data from .tsv files into a single .csv file
* [Search Data Processing Jupyter Notebook](https://github.com/sfbrigade/open-data-search/blob/master/search_data_processing.ipynb) - Notebook that cleans, processes and categorizes search terms

## Topic Modelling
* [Search Ddata Modelling Juptyer Notebook](https://github.com/sfbrigade/open-data-search/blob/master/word2vec_modelling.ipynb) - Notebook with vectorization of search terms using pre-trained word2vec model

## Data Exploration 
* [Exploration of Search Google Analytics](https://github.com/sfbrigade/open-data-search/blob/master/open_search_exploration.md)

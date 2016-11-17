    ## Warning: package 'tidyr' was built under R version 3.2.5

Understanding the Data
----------------------

This data is coming from Google analytics "Site Search" functionality, which is hooked up to the SF Open Data portal's search page.

A lot of the useful information about this can be found at: <https://developers.google.com/analytics/devguides/reporting/core/dimsmets>

#### ga.searchKeyword(Search Terms)

These are the words and keywords that have been entered into the search form at <https://data.sfgov.org/>

This is what the bulk of our analysis will be covering so I will spare you the summaries.

#### ga.searchStartPage(Search Page)

The page where users initiated an internal search.

aka Page on site where the user enters terms for a web search?

Pretty early on in the most common start page we get really specific pages:

| ga.searchStartPage                                                                                       |  count|
|:---------------------------------------------------------------------------------------------------------|------:|
| '/                                                                                                       |  23550|
| (entrance)                                                                                               |   8562|
| '/browse/embed?category=&limit=20&limitTo=&q=&view\_type=rich                                            |   2924|
| '/browse/embed?Department-Metrics\_Publishing-Department=&category=&limit=20&limitTo=&q=&view\_type=rich |   1686|
| '/browse/embed?category=Transportation&limit=20&limitTo=&q=&view\_type=rich                              |    650|
| '/browse/embed?category=Geographic+Locations+and+Boundaries&limit=20&limitTo=&q=&view\_type=rich         |    602|

So it's interesting to look at the root of the search page (dropping everything after the second slash)

| startSearchRoot                     |  count|
|:------------------------------------|------:|
| browse                              |  34077|
|                                     |  23550|
| (entrance)                          |   8562|
| Geographic-Locations-and-Boundaries |    869|
| City-Management-and-Ethics          |    410|
| Transportation                      |    409|
| data                                |    383|
| Economy-and-Community               |    381|
| Housing-and-Buildings               |    329|
| Public-Safety                       |    323|
| City-Infrastructure                 |    277|
| Culture-and-Recreation              |    149|
| Health-and-Social-Services          |    123|
| showcase                            |     99|
| Energy-and-Environment              |     96|
| w                                   |     59|
| profile                             |     46|
| widgets                             |     34|
| dataset                             |     29|
| about                               |     23|

I'm very confused about how sometimes this is a specific data set? Basically it seems like a lot of the start pages are specific data sets where there is not a search widget such as in the ones below.

``` r
mostly_datasets <- !grepl('\\?', queries$ga.searchStartPage) & 
                    queries$ga.searchStartPage != "(entrance)"  &
                    queries$ga.searchStartPage != "'/" &
                    str_count(queries$ga.searchStartPage, '/') > 1

head(queries[mostly_datasets,], 20)
```

| ga.searchKeyword              | ga.searchStartPage                                                                                | ga.searchAfterDestinationPage                                                                                                    |  ga.searchUniques|  ga.avgSearchResultViews|  ga.avgSearchDepth|  ga.percentSearchRefinements|  ga.searchDuration|  ga.searchExitRate| startSearchRoot                     |
|:------------------------------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|-----------------:|------------------------:|------------------:|----------------------------:|------------------:|------------------:|:------------------------------------|
| open business                 | '/Transportation/Parking-meters/28my-4796                                                         | '/data?search=open+business&dept=&category=&type=                                                                                |                27|                 1.000000|           0.000000|                     0.000000|                  0|                  0| Transportation                      |
| 311                           | '/City-Management-and-Ethics/Case-Data-from-San-Francisco-311-SF311-/vw6y-z8j6                    | '/data?search=311                                                                                                                |                 6|                 2.166667|           0.000000|                     0.000000|                  0|                  0| City-Management-and-Ethics          |
| crime                         | '/Public-Safety/Map-Crime-Incidents-from-1-Jan-2003/gxxq-x39z                                     | '/browse/embed?category=&limit=20&limitTo=&q=crime&view\_type=rich                                                               |                 6|                10.500000|          41.833333|                     4.761905|              14138|                  0| Public-Safety                       |
| total housing units           | '/Economy-and-Community/Registered-Business-Map/vt9c-aeiw                                         | '/browse/embed?category=&limit=20&limitTo=&q=total+housing+units&view\_type=rich                                                 |                 6|                 1.000000|           2.166667|                     0.000000|                957|                  0| Economy-and-Community               |
| business                      | '/Transportation/Parking-meters/28my-4796                                                         | '/data?search=business&dept=&category=&type=                                                                                     |                 5|                 1.000000|           0.000000|                     0.000000|                  0|                  0| Transportation                      |
| crime                         | '/Public-Safety/Map-Crime-Incidents-from-1-Jan-2003/gxxq-x39z                                     | '/browse/embed?Department-Metrics\_Publishing-Department=&category=&limit=20&limitTo=&q=crime&view\_type=rich                    |                 5|                 6.200000|          17.000000|                    19.354839|               2497|                  0| Public-Safety                       |
| meter                         | '/Economy-and-Community/Open-Business-Locations-San-Francisco/g8m3-pdis                           | '/data?search=meter&dept=&category=&type=                                                                                        |                 5|                 1.200000|           0.000000|                     0.000000|                  0|                  0| Economy-and-Community               |
| no parking                    | '/Transportation/SFMTA-Enforced-Temporary-Tow-Zones/cqn5-muyy                                     | '/data?search=no+parking&dept=&category=Transportation&type=                                                                     |                 5|                 1.000000|           0.000000|                     0.000000|                  0|                  0| Transportation                      |
| police                        | '/City-Infrastructure/Street-Tree-List/tkzw-k3nq                                                  | '/data?category=&dept=&search=police&type=datasets                                                                               |                 5|                 1.200000|           0.000000|                     0.000000|                  0|                  0| City-Infrastructure                 |
| Housing                       | '/Housing-and-Buildings/Residential-Housing-Density-San-Francisco-CA/q35t-jeti                    | '/data?search=Housing&dept=&category=&type=                                                                                      |                 4|                 1.000000|           0.000000|                     0.000000|                  0|                  0| Housing-and-Buildings               |
| pipeline                      | '/Housing-and-Buildings/San-Francisco-Development-Pipeline-2015-Quarter-3/apz9-dh7k               | '/browse/embed?Department-Metrics\_Publishing-Department=Planning&category=&limit=20&limitTo=datasets&q=pipeline&view\_type=rich |                 4|                 1.000000|           2.750000|                     0.000000|                715|                  0| Housing-and-Buildings               |
| pipeline                      | '/Housing-and-Buildings/San-Francisco-Development-Pipeline-2015-Quarter-4/ra2x-jzmk               | '/browse/embed?Department-Metrics\_Publishing-Department=Planning&category=&limit=20&limitTo=datasets&q=pipeline&view\_type=rich |                 4|                 1.250000|           7.500000|                     0.000000|               2859|                  0| Housing-and-Buildings               |
| pipeline                      | '/Housing-and-Buildings/San-Francisco-Development-Pipeline-2015-Quarter-4/ra2x-jzmk               | '/browse/embed?category=&limit=20&limitTo=datasets&q=pipeline&view\_type=rich                                                    |                 4|                 1.000000|           2.500000|                    25.000000|                230|                  0| Housing-and-Buildings               |
| total housing units           | '/Economy-and-Community/Registered-Business-Map/vt9c-aeiw                                         | '/browse/embed?Department-Metrics\_Publishing-Department=&category=&limit=20&limitTo=&q=total+housing+units&view\_type=rich      |                 4|                 1.250000|           2.500000|                     0.000000|                 61|                  0| Economy-and-Community               |
| 311                           | '/City-Infrastructure/Case-Data-from-San-Francisco-311-SF311-/vw6y-z8j6                           | '/browse/embed?category=&limit=20&limitTo=&q=311&view\_type=rich                                                                 |                 3|                 4.666667|          34.333333|                    21.428571|              10367|                  0| City-Infrastructure                 |
| Murder                        | '/widgets/tmnf-yvry                                                                               | '/browse/embed?category=Public+Safety&limit=20&limitTo=&q=Murder&view\_type=rich                                                 |                 3|                 1.000000|           3.000000|                     0.000000|                158|                  0| widgets                             |
| Water Bodies in San Francisco | '/Geographic-Locations-and-Boundaries/Bay-Area-General-Zipped-Shapefile-Format-/ye46-7n65         | '/data?search=Water+Bodies+in+San+Francisco&dept=&category=&type=                                                                |                 3|                 1.000000|           0.000000|                     0.000000|                  1|                  0| Geographic-Locations-and-Boundaries |
| business                      | '/Economy-and-Community/Open-Business-Locations-San-Francisco/g8m3-pdis                           | '/data?search=business                                                                                                           |                 3|                 4.333333|           0.000000|                     0.000000|                  0|                  0| Economy-and-Community               |
| business                      | '/Economy-and-Community/Registered-Business-Locations-San-Francisco/g8m3-pdis                     | '/data?search=business                                                                                                           |                 3|                 3.666667|           0.000000|                     0.000000|                 65|                  0| Economy-and-Community               |
| census 2010                   | '/Geographic-Locations-and-Boundaries/Streets-of-San-Francisco-Zipped-Shapefile-Format-/wbm8-ratb | '/data?search=census+2010&dept=&category=Geographic+Locations+and+Boundaries&type=                                               |                 3|                 1.000000|           0.000000|                     0.000000|                  0|                  0| Geographic-Locations-and-Boundaries |

``` r
# Uncomment and run to see all
# View(queries[mostly_datasets,])
```

The highest count of searchUnique for these is 27 (then 6 and trails off fast), while there is roughly 1900 rows total.

#### ga.searchAfterDestinationPage(Search Destination Page)

The page that users visited after performing an internal search on the site.

    ## 
    ##                                                                                                      (exit) 
    ##                                                                                                         967 
    ##                                                                                                          '/ 
    ##                                                                                                         875 
    ##                                                                                                    '/browse 
    ##                                                                                                         165 
    ##                                                                   '/data?search=crime&dept=&category=&type= 
    ##                                                                                                         130 
    ##                                                               '/data?search=shapefile&dept=&category=&type= 
    ##                                                                                                         123 
    ##                                           '/browse/embed?category=&limit=20&limitTo=&q=crime&view_type=rich 
    ##                                                                                                         100 
    ##                                                                '/data?search=business&dept=&category=&type= 
    ##                                                                                                          99 
    ##                                                                 '/data?search=streets&dept=&category=&type= 
    ##                                                                                                          95 
    ## '/browse/embed?Department-Metrics_Publishing-Department=&category=&limit=20&limitTo=&q=crime&view_type=rich 
    ##                                                                                                          87 
    ##                                                                                                      '/data 
    ##                                                                                                          87 
    ##                                                                  '/data?search=street&dept=&category=&type= 
    ##                                                                                                          84 
    ##                               '/Economy-and-Community/Registered-Business-Locations-San-Francisco/g8m3-pdis 
    ##                                                                                                          79 
    ##                                                                    '/data?search=bike&dept=&category=&type= 
    ##                                                                                                          72 
    ##                                          '/browse/embed?category=&limit=20&limitTo=&q=census&view_type=rich 
    ##                                                                                                          70 
    ##                                                                  '/data?search=census&dept=&category=&type= 
    ##                                                                                                          70 
    ##                                                                 '/data?search=parking&dept=&category=&type= 
    ##                                                                                                          70 
    ##                                                                 '/data?search=bicycle&dept=&category=&type= 
    ##                                                                                                          67 
    ##                                                                  '/data?search=income&dept=&category=&type= 
    ##                                                                                                          66 
    ##                                                                  '/data?search=parcel&dept=&category=&type= 
    ##                                                                                                          64 
    ##                                                                   '/data?search=water&dept=&category=&type= 
    ##                                                                                                          63

#### ga.searchUniques(Total Unique Searches)

The total number of times your site search was used. This excludes multiple searches on the same keyword during the same session.

Oddly the most common number of searches is 0 (if it's been 0 times how is it here??) After talking to Jason we have a theory that this is caused by when people search for the same term multiple times in one session but do so from different ga.searchStartPage or go to a different ga.searchAfterDestinationPage.

Support for this theory: - If Jason pulls the same report without searchStartPage and searchAfterDestinationPage then it is about 60K rows shorter (was working off his memory)

-   All terms with 0 searchUniques show up somewhere else with a searchUniques \> 0

``` r
filter(queries,ga.searchUniques == 0)$ga.searchKeyword %in% 
    filter(queries, !ga.searchUniques == 0)$ga.searchKeyword %>%
    table()
```

TRUE
----

65688

Additional theory: Clicking back to a search page reruns the page and might count it as a new search in the same session.

If our assumptions hold, we should be able to use these queries to look into what terms people search and either don't find what they are looking for or to narrow their explorations. (I think this is currently "what gets searched the most", should likely figure out how to scale these based on the values with \> 0 searchUniques?)

``` r
reran_searches <- filter(queries, ga.searchUniques == 0) %>% 
                    group_by(search = ga.searchKeyword) %>%
                    summarise(count = n()) %>%
                    arrange(desc(count)) 

ggplot(head(reran_searches, 20), aes(x = reorder(search, -count), y = count)) +
    geom_bar(stat="identity") +
    theme(axis.text.x = element_text(angle = -45, hjust = 0)) +
    labs(x = 'search terms')
```

![](open_search_exploration_files/figure-markdown_github/unnamed-chunk-7-1.png)<!-- -->

#### ga.avgSearchResultViews(Results Pageviews / Search)

The average number of times people viewed a page as a result of a search.

#### ga.avgSearchDepth(Average Search Depth)

The average number of pages people viewed after performing a search.

#### ga.percentSearchRefinements(Search Refinements)

The percentage of the number of times a refinement (i.e., transition) occurs between internal keywords search within a session.

#### ga.searchDuration(Time after Search)

The session duration when the site's internal search feature is used.

#### ga.searchExitRate(Search Exits)

The percentage of searches that resulted in an immediate exit from the property.

-   What is the difference between searchAfterDestinationPage == (exit) and searchExitRate == 100?

``` r
#filter(queries,ga.searchAfterDestinationPage == '(exit)')
```

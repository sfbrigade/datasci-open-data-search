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

Pretty early on in the most common start page we get pretty specific pages:

    ## Source: local data frame [6 x 2]
    ## 
    ##                                                            ga.searchStartPage
    ##                                                                         (chr)
    ## 1                                                                          '/
    ## 2                                                                  (entrance)
    ## 3                '/browse/embed?category=&limit=20&limitTo=&q=&view_type=rich
    ## 4 '/browse/embed?Department-Metrics_Publishing-Department=&category=&limit=20
    ## 5  '/browse/embed?category=Transportation&limit=20&limitTo=&q=&view_type=rich
    ## 6 '/browse/embed?category=Geographic+Locations+and+Boundaries&limit=20&limitT
    ## Variables not shown: count (int)

So it's interesting to look at the root of the seach page (dropping everything after the second slash)

    ## Source: local data frame [20 x 2]
    ## 
    ##                        startSearchRoot count
    ##                                  (chr) (int)
    ## 1                               browse 34077
    ## 2                                      23550
    ## 3                           (entrance)  8562
    ## 4  Geographic-Locations-and-Boundaries   869
    ## 5           City-Management-and-Ethics   410
    ## 6                       Transportation   409
    ## 7                                 data   383
    ## 8                Economy-and-Community   381
    ## 9                Housing-and-Buildings   329
    ## 10                       Public-Safety   323
    ## 11                 City-Infrastructure   277
    ## 12              Culture-and-Recreation   149
    ## 13          Health-and-Social-Services   123
    ## 14                            showcase    99
    ## 15              Energy-and-Environment    96
    ## 16                                   w    59
    ## 17                             profile    46
    ## 18                             widgets    34
    ## 19                             dataset    29
    ## 20                               about    23

Very confused about how sometimes this is a specific data set? Basicaly it seems like a lot of the start pages are specific data sets where there is not a search widget as in the ones below.

``` r
mostly_datasets <- !grepl('\\?', queries$ga.searchStartPage) & 
                    queries$ga.searchStartPage != "(entrance)"  &
                    queries$ga.searchStartPage != "'/" &
                    str_count(queries$ga.searchStartPage, '/') > 1

head(queries[mostly_datasets,], 20)
```

    ## Source: local data frame [20 x 10]
    ## 
    ##                 ga.searchKeyword
    ##                            (chr)
    ## 1                  open business
    ## 2                            311
    ## 3                          crime
    ## 4            total housing units
    ## 5                       business
    ## 6                          crime
    ## 7                          meter
    ## 8                     no parking
    ## 9                         police
    ## 10                       Housing
    ## 11                      pipeline
    ## 12                      pipeline
    ## 13                      pipeline
    ## 14           total housing units
    ## 15                           311
    ## 16                        Murder
    ## 17 Water Bodies in San Francisco
    ## 18                      business
    ## 19                      business
    ## 20                   census 2010
    ## Variables not shown: ga.searchStartPage (chr),
    ##   ga.searchAfterDestinationPage (chr), ga.searchUniques (int),
    ##   ga.avgSearchResultViews (dbl), ga.avgSearchDepth (dbl),
    ##   ga.percentSearchRefinements (dbl), ga.searchDuration (int),
    ##   ga.searchExitRate (int), startSearchRoot (chr)

``` r
# Uncomment and run to see all
# View(queries[mostly_datasets,])
```

The highest count of searchUnique for these is 27 (then 6 and trails off fast), while there is roughly 18

#### ga.searchAfterDestinationPage(Search Destination Page)

The page that users visited after performing an internal search on the site.

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

    ## .
    ##  TRUE 
    ## 65688

Additional theory: Clicking back to a search page reruns the page and might count it as a new search in the same session.

If our assumptions hold, we should be able to use these queries to look into what terms people search and either dont find what they are looking for or to narrow their explorations. (I think this is currently "what gets searched the most", should likely figure out how to scale these based on the values with \> 0 searchUniques?)

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

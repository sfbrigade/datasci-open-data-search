``` r
queries <- read_csv("data/all_queries.csv")
```

    ## Warning: 12 parsing failures.
    ##   row               col               expected          actual
    ## 10004 ga.searchExitRate no trailing characters .47905852236365
    ## 20008 ga.searchExitRate no trailing characters .47905852236365
    ## 30012 ga.searchExitRate no trailing characters .47905852236365
    ## 36307 ga.searchExitRate no trailing characters .47905852236365
    ## 46311 ga.searchExitRate no trailing characters .47905852236365
    ## ..... ................. ...................... ...............
    ## .See problems(...) for more details.

``` r
# Check what these errors are from
problems(queries)
```

    ## Source: local data frame [12 x 4]
    ## 
    ##       row               col               expected          actual
    ##     (int)             (chr)                  (chr)           (chr)
    ## 1   10004 ga.searchExitRate no trailing characters .47905852236365
    ## 2   20008 ga.searchExitRate no trailing characters .47905852236365
    ## 3   30012 ga.searchExitRate no trailing characters .47905852236365
    ## 4   36307 ga.searchExitRate no trailing characters .47905852236365
    ## 5   46311 ga.searchExitRate no trailing characters .47905852236365
    ## 6   56315 ga.searchExitRate no trailing characters .47905852236365
    ## 7   66319 ga.searchExitRate no trailing characters .47905852236365
    ## 8   76323 ga.searchExitRate no trailing characters .47905852236365
    ## 9   86327 ga.searchExitRate no trailing characters .47905852236365
    ## 10  96331 ga.searchExitRate no trailing characters .47905852236365
    ## 11 106335 ga.searchExitRate no trailing characters .47905852236365
    ## 12 116339 ga.searchExitRate no trailing characters .47905852236365

``` r
# We should remove these weird rows
# Did every sheet that got combined create one?
View(tail(queries))
```

Understanding the Data
----------------------

This data is coming from Google analytics "Site Search" funtionality, which is hooked up to the SF Open Data portal's search page.

A lot of the useful information about this can be found at: <https://developers.google.com/analytics/devguides/reporting/core/dimsmets>

#### ga.searchKeyword(Search Terms)

These are the words and keywords that have been entered into the search form at <https://data.sfgov.org/>

#### ga.searchStartPage(Search Page)

Page on site where the user enters terms for a web search

``` r
tail(sort(table(queries$ga.searchStartPage)))
```

    ## 
    ##        '/browse/embed?category=Geographic+Locations+and+Boundaries&limit=20&limitTo=&q=&view_type=rich 
    ##                                                                                                    431 
    ##                          '/Economy-and-Community/Registered-Business-Locations-San-Francisco/g8m3-pdis 
    ##                                                                                                    629 
    ## '/browse/embed?Department-Metrics_Publishing-Department=&category=&limit=20&limitTo=&q=&view_type=rich 
    ##                                                                                                   1468 
    ##                                           '/browse/embed?category=&limit=20&limitTo=&q=&view_type=rich 
    ##                                                                                                   2329 
    ##                                                                                             (entrance) 
    ##                                                                                                   4819 
    ##                                                                                                     '/ 
    ##                                                                                                  11566

#### ga.searchAfterDestinationPage(Search Destination Page)

The page that users visited after performing an internal search on the site.

#### ga.searchUniques(Total Unique Searches)

The total number of times your site search was used. This excludes multiple searches on the same keyword during the same session.

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

-   What is the difference between searchAfterDestinationPage and searchExitRate == 100?

``` r
filter(queries,ga.searchAfterDestinationPage == '(exit)')
```

    ## Source: local data frame [967 x 9]
    ## 
    ##     ga.searchKeyword ga.searchStartPage ga.searchAfterDestinationPage
    ##                (chr)              (chr)                         (chr)
    ## 1        restaurants         (entrance)                        (exit)
    ## 2              crime         (entrance)                        (exit)
    ## 3         sfopenbook         (entrance)                        (exit)
    ## 4            parking         (entrance)                        (exit)
    ## 5      road polygons         (entrance)                        (exit)
    ## 6         facilities         (entrance)                        (exit)
    ## 7                sfo         (entrance)                        (exit)
    ## 8              crime                 '/                        (exit)
    ## 9            traffic         (entrance)                        (exit)
    ## 10 business licenses         (entrance)                        (exit)
    ## ..               ...                ...                           ...
    ## Variables not shown: ga.searchUniques (int), ga.avgSearchResultViews
    ##   (dbl), ga.avgSearchDepth (dbl), ga.percentSearchRefinements (dbl),
    ##   ga.searchDuration (int), ga.searchExitRate (int)

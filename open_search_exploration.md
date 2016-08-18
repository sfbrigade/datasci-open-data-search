    ## Warning: 12 parsing failures.
    ##   row               col               expected          actual
    ## 10004 ga.searchExitRate no trailing characters .47905852236365
    ## 20008 ga.searchExitRate no trailing characters .47905852236365
    ## 30012 ga.searchExitRate no trailing characters .47905852236365
    ## 36307 ga.searchExitRate no trailing characters .47905852236365
    ## 46311 ga.searchExitRate no trailing characters .47905852236365
    ## ..... ................. ...................... ...............
    ## .See problems(...) for more details.

Understanding the Data
----------------------

This data is coming from Google analytics "Site Search" functionality, which is hooked up to the SF Open Data portal's search page.

A lot of the useful information about this can be found at: <https://developers.google.com/analytics/devguides/reporting/core/dimsmets>

#### ga.searchKeyword(Search Terms)

These are the words and keywords that have been entered into the search form at <https://data.sfgov.org/>

#### ga.searchStartPage(Search Page)

Page on site where the user enters terms for a web search

-   Worth also exploring based on page category (dropping everything after the slash)

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

-   What is the difference between searchAfterDestinationPage == (exit) and searchExitRate == 100?

<!-- -->

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

*below wording could be improved*
One of the imediately interesting things about the data is how often people are searching the same term multiple times in one session. We can sum all of the unique search counts and take the timese that ga.searchUniques equals 0 and see that a search is at least 93% as likely to be a reran search as to be new for the user durring the session. In reality this is likely even more common because ga.searchUniques does not increase if multiple people have made multiple searches for a term with all the other variables also being the same.

Searches originate from 46.2 thousand differnt urls, mostly due to previous search results and other metadata being appended to the url. Focusing on just the root domains brings us down to 46, with the vast majority of searches comeing from the browse and entrance pages.

![](Figs/search_origination_plot-1.png)

Looking at just when users search for the same term multiple times in a session, the data root domain jumps to the lead and all of the more specific catagories rise.

![](Figs/re_search_origination_plot-1.png)

By seperating previous searches out of ga.searchStartPage we can look at what was searched in succession. Shockingly to me, in 98% of these cases people searched the same term again. For the other 2%, it's pretty interesting to see how people change their queries, which can be viewed in the changed\_searches.csv.

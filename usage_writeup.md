*below wording could be improved*
One of the immediately interesting things about the data is how often people are searching the same term multiple times in one session. We can sum all of the unique search counts and take the times that ga.searchUniques equals 0 and see that a search is at least 93% as likely to be a reran search as to be new for the user during the session. In reality this is likely even more common because ga.searchUniques does not increase if multiple people have made multiple searches for a term with all the other variables also being the same.

Searches originate from 46.2 thousand different urls, mostly due to previous search results and other metadata being appended to the url. Focusing on just the root domains brings us down to 46, with the vast majority of searches coming from the browse and entrance pages.

![](Figs/search_origination_plot-1.png)

Looking at just when users search for the same term multiple times in a session, the data root domain jumps to the lead and all of the more specific categories rise.

![](Figs/re_search_origination_plot-1.png)

By separating previous searches out of ga.searchStartPage we can look at what was searched in succession. Shockingly to me, in 98% of these cases people searched the same term again. For the other 2%, it's pretty interesting to see how people change their queries, which can be viewed in the changed\_searches.csv.

![](Figs/unnamed-chunk-3-1.png)

Since 98% of searches have 0 character changes it doesn't make a very interesting plot at all. Ignoring that, the most common change for people to make is one character (normally a typo fix).

More interesting are the searches with a Levenshtein distance over 3. This is when users start really refining their searches or abandon them completely, so it's an excellent place for Jason and us to take over for the machines. Plus it brings us down to a manageable ~340 searches to focus on.

From here we can look into:

-   If the data is available is it poorly tagged, labeled, or named?
-   If the data isn't available, can we make it so?
-   Can we use this as proof to show departments people want your data available?

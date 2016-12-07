*below wording could be improved*
One of the immediately interesting things about the data is how often people are searching the same term multiple times in one session. We can sum all of the unique search counts and take the times that ga.searchUniques equals 0 and see that a search is at least 93% as likely to be a reran search as to be new for the user during the session. In reality this is likely even more common because ga.searchUniques does not increase if multiple people have made multiple searches for a term with all the other variables also being the same.

Searches originate from 46.2 thousand different urls, mostly due to previous search results and other metadata being appended to the url. Focusing on just the root domains brings us down to 46, with the vast majority of searches coming from the browse and entrance pages.

![](Figs/search_origination_plot-1.png)

Looking at just when users search for the same term multiple times in a session, the data root domain jumps to the lead and all of the more specific categories rise.

![](Figs/re_search_origination_plot-1.png)

By separating previous searches out of ga.searchStartPage we can look at what was searched in succession. Shockingly to me, in 98% of these cases people searched the same term again. For the other 2%, it's pretty interesting to see how people change their queries, which can be viewed in the changed\_searches.csv.

![](Figs/unnamed-chunk-3-1.png)

Since 98% of searches have 0 character changes it doesn't make a very interesting plot at all. Ignoring that, the most common change for people to make is one character (normally a typo fix).

More interesting are the searches with a Levenshtein distance over 3. This is when users start really refining their searches or abandon them completely, so it's an exilent place for Jason and us to take over for the machines. Plus it brings us down to a managable ~340 searches to focuse on.

From here we can look into:

-   If the data is available is it poorly tagged, labled, or named?
-   If the data isn't available, can we make it so?
-   Can we use this as proof to show departments people want your data available?

<!-- -->

    ## [1] "\n      9 Results\n      filtered by  "

    ## [1] "Community Resiliency Indicator System, Building Permits, San Francisco Development Pipeline 2015 Quarter 1, Boiler Permits, Plumbing Permits, Electrical Permits, Call Center Metrics for the Health Service System, San Francisco Flood Health Vulnerability, San Francisco City Survey Data 1996-2015"

    ##     ga.searchKeyword Count appears_in in_published in_unpublished
    ## 1                311   676          6            6              0
    ## 2                460    88         13           13              0
    ## 3                911    71          1            0              1
    ## 4           accident    52          0            0              0
    ## 5            address   118         42           20             22
    ## 6          addresses    75         14            9              5
    ## 7             aerial    60          1            1              0
    ## 8            airport    53         23           13             10
    ## 9            alcohol    64          0            0              0
    ## 10               art    62        234          171             62
    ## 11          assessor   111          5            4              1
    ## 12              bart   141          1            0              1
    ## 13           basemap    54          7            7              0
    ## 14           bicycle   243          9            9              0
    ## 15              bike   325          8            6              2
    ## 16             block    71         18           13              5
    ## 17            blocks    77          9            6              3
    ## 18          boundary    96          3            3              0
    ## 19            budget   153         11            3              8
    ## 20          building   243         28           17             11
    ## 21         buildings   148         10            5              5
    ## 22               bus   143         32           16             16
    ## 23          business   794         30           14             16
    ## 24        businesses    97         13            6              7
    ## 25            census   356         16           15              1
    ## 26      construction    65         14           11              3
    ## 27           contour   101          1            1              0
    ## 28          contours    97          1            1              0
    ## 29             crime  1871          4            2              2
    ## 30             Crime   144          4            2              2
    ## 31            crimes    69          0            0              0
    ## 32              curb    72          5            3              2
    ## 33             curbs    55          1            1              0
    ## 34       demographic    64         35            8             27
    ## 35      demographics    82         11            0             11
    ## 36           density    56          1            1              0
    ## 37          district    96         75           67              7
    ## 38         districts    75         67           63              3
    ## 39        earthquake    65          2            2              0
    ## 40         education   135          8            6              2
    ## 41         elevation   247          1            1              0
    ## 42        employment    67          8            2              6
    ## 43            energy   143          3            2              1
    ## 44          eviction   135          2            2              0
    ## 45         evictions   126          2            2              0
    ## 46        facilities    55         19           13              6
    ## 47              film    67          3            1              2
    ## 48              fire   231         14           10              4
    ## 49             flood    63          1            1              0
    ## 50              food   206          5            4              1
    ## 51         footprint    72          3            2              1
    ## 52        footprints    54          2            1              1
    ## 53               gis   118         84           68             15
    ## 54               GIS    65         84           68             15
    ## 55          graffiti    99          0            0              0
    ## 56            health   107         20           12              8
    ## 57            height    50         11           11              0
    ## 58          homeless   277          3            0              3
    ## 59          hospital    71          3            1              2
    ## 60         hospitals    51          1            1              0
    ## 61             hotel    68          6            3              3
    ## 62           housing   242         36           22             14
    ## 63           imagery    51          4            3              1
    ## 64      inclusionary    98          4            2              2
    ## 65            income   337          2            1              1
    ## 66         inventory   109         19           15              4
    ## 67              json    64          1            1              0
    ## 68           landuse    57          1            1              0
    ## 69           library    74         10            6              4
    ## 70          lobbyist    68         12           12              0
    ## 71              lots    50          7            6              1
    ## 72               map    86         51           43              7
    ## 73             meter   258         16           13              3
    ## 74             movie    50          1            1              0
    ## 75              muni   259         57           36             20
    ## 76      neighborhood   319         13           10              2
    ## 77     neighborhoods   293          9            8              1
    ## 78             noise   107          5            4              1
    ## 79            parcel   438         17           13              4
    ## 80           parcels   242          9            7              2
    ## 81              park   198         48           34             14
    ## 82           parking   789         25           16              9
    ## 83           Parking    70         25           16              9
    ## 84             parks   369         20           16              4
    ## 85        pedestrian   105          2            2              0
    ## 86            permit   101         40           27             13
    ## 87           permits    89         26           19              7
    ## 88          pipeline   249          9            3              6
    ## 89          planning    57         88           79              7
    ## 90            police   181         11            8              3
    ## 91              poop    67          0            0              0
    ## 92        population   412         11            8              3
    ## 93           poverty    62          0            0              0
    ## 94          property   125         31           12             18
    ## 95              race    52          7            6              1
    ## 96              rent   232         83           63             20
    ## 97        restaurant   312          3            2              1
    ## 98       restaurants   413          0            0              0
    ## 99              road   101          6            5              1
    ## 100            roads   162          2            2              0
    ## 101           salary   129          7            6              1
    ## 102           school   231         15            7              8
    ## 103          schools   189          6            4              2
    ## 104            sewer    92          3            3              0
    ## 105            sfmta    93         29           20              9
    ## 106              sfo    52         38           15             23
    ## 107             sfpd    94          9            6              3
    ## 108        shapefile   436         52           50              1
    ## 109       shapefiles   144          4            3              0
    ## 110        shoreline   120          2            2              0
    ## 111         sidewalk    63          8            8              0
    ## 112           street   421         54           45              9
    ## 113          streets   716         26           23              3
    ## 114              tax    72         17            7             10
    ## 115             taxi   156          1            1              0
    ## 116          tickets    53          1            1              0
    ## 117             topo    67          2            2              0
    ## 118       topography   126          0            0              0
    ## 119          traffic   375         14           10              4
    ## 120          transit   163          9            5              4
    ## 121   transportation   109         12            9              3
    ## 122             tree   157         59           47             12
    ## 123             Tree    52         59           47             12
    ## 124            trees   210          4            2              2
    ## 125            waste    61          2            2              0
    ## 126            water   398         19           16              3
    ## 127          weather   151          3            3              0
    ## 128             wind    62          3            3              0
    ## 129              zip    52         56           54              1
    ## 130           zoning   266         30           28              2
    ##     result_count all_result_count
    ## 1              9               48
    ## 2             13              193
    ## 3              2                4
    ## 4              0                1
    ## 5             56              147
    ## 6             56              147
    ## 7              0                1
    ## 8             19               23
    ## 9              0                0
    ## 10             3                5
    ## 11             2               19
    ## 12             0                2
    ## 13             4               10
    ## 14             5               14
    ## 15             5               12
    ## 16            39              110
    ## 17            39              110
    ## 18            24              132
    ## 19             5                7
    ## 20            54               95
    ## 21            54               95
    ## 22             1                4
    ## 23            18               36
    ## 24            18               36
    ## 25             9               28
    ## 26            31               46
    ## 27             0                1
    ## 28             0                1
    ## 29             2               15
    ## 30             2               15
    ## 31             2               15
    ## 32             2                7
    ## 33             2                7
    ## 34             9               24
    ## 35             9               24
    ## 36             0                2
    ## 37            61              288
    ## 38            61              288
    ## 39             0                2
    ## 40            21               57
    ## 41             1                2
    ## 42             7               17
    ## 43             4               16
    ## 44             4                5
    ## 45             4                5
    ## 46            19               34
    ## 47             1                1
    ## 48            14               25
    ## 49             1                1
    ## 50             4                7
    ## 51             1                3
    ## 52             1                3
    ## 53             5               67
    ## 54             5               67
    ## 55             3                7
    ## 56            10               31
    ## 57             8               21
    ## 58             3                4
    ## 59             1                4
    ## 60             1                4
    ## 61             2                3
    ## 62            52              100
    ## 63             0               14
    ## 64             2                3
    ## 65             3                5
    ## 66            12               20
    ## 67             0                1
    ## 68            16               31
    ## 69             0                4
    ## 70            10               25
    ## 71            30               95
    ## 72            19              123
    ## 73             5                9
    ## 74             1                1
    ## 75             1                3
    ## 76            44              102
    ## 77            44              102
    ## 78             4                5
    ## 79            18               75
    ## 80            18               75
    ## 81            32               69
    ## 82            32               69
    ## 83            32               69
    ## 84            32               69
    ## 85             2                6
    ## 86            41               75
    ## 87            41               75
    ## 88            20               28
    ## 89            44              143
    ## 90            11               37
    ## 91             0                0
    ## 92             1                8
    ## 93             1                1
    ## 94             8               28
    ## 95             5               13
    ## 96             6                7
    ## 97             1                2
    ## 98             1                2
    ## 99             0                3
    ## 100            0                3
    ## 101           13               17
    ## 102            4                8
    ## 103            4                8
    ## 104            1                2
    ## 105           13               35
    ## 106           19               19
    ## 107            2               18
    ## 108            3               76
    ## 109            3               76
    ## 110            0                2
    ## 111            6               10
    ## 112           66              158
    ## 113           66              158
    ## 114            7               20
    ## 115            0                5
    ## 116            2                4
    ## 117            0                0
    ## 118            0                0
    ## 119            9               17
    ## 120            2               13
    ## 121           47              109
    ## 122            4               18
    ## 123            4               18
    ## 124            4               18
    ## 125            1                2
    ## 126            2               17
    ## 127            2                5
    ## 128            0                2
    ## 129           26              109
    ## 130           25               81

Call each search term and see how many results there is: <https://data.sfgov.org/browse?q=street%20cleaning> Maybe limit to dataset and external

Can look at what the value as assigned by department is and see if true.

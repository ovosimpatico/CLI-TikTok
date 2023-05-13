# A Note about Web Scraping

## Why is it bad

Web scraping is generally considered forbidden or unethical because it involves accessing and extracting data from websites without the website owner's permission. This can be seen as a violation of the website's terms of service and can potentially cause harm to the website's performance or functionality, which can negatively impact other users who are legitimately trying to access the website.


## Bibliogram (Discontinued)

Bibliogram was a private-frontend for Instagram - It was discontinued in 2022 due to many factors, one of them being botting.

From [Discontinuing Bibliogram](https://cadence.moe/blog/2022-09-01-discontinuing-bibliogram) ([Alternative link](https://web.archive.org/web/20230513150354/https://cadence.moe/blog/2022-09-01-discontinuing-bibliogram)):
> From as soon as mid-2020 I began to deal with a serious problem of poorly coded bots accessing Bibliogram and using up its rate limit. 
>
> These bots were created without regard for whether their requests succeed and they don't acknowledge my requests to slow down. They were designed specifically to scrape data from Bibliogram, and the owners were apparently too lazy to run their own instance of Bibliogram, or to contact me asking for help setting one up. 
>
> The bots are a problem because they appear to be unmonitored, and they're using up the rate limit that would be better if it were helping real people.

## Proxitok

The most used instance of Proxitok, PussTheCat explicitely states that scraping is not allowed. [Source](https://pussthecat.org/tos/) ([Alternative link](https://web.archive.org/web/20230513151425/https://pussthecat.org/tos/))

> You are not allowed to:
> - Scrape any content of anything.

On Proxitok's Github, the creator stated:
[Source](https://github.com/pablouser1/ProxiTok/issues/84) ([Alternative link](https://web.archive.org/web/20230513151833/https://github.com/pablouser1/ProxiTok/issues/84))

> Bots/automated requests are a growing problem in ProxiTok. I guess it's OK if you don't spam requests, but I would still highly appreciate anyone trying to scrape ProxiTok not to. There are already libraries such as TikTok-Api for Python or tiktok-scraper for JS/TS, to name a few, that do the job for you.
>
> RSS isn't much of a problem (at least for now). All requests made to TikTok are cached for some time so they don't impact that much rate limits.

## Relation to CLI TikTok

CLI TikTok used to download RSS feeds from Proxitok until May 13, 2023. In this date, we switched to web scraping due to limited functionality that RSS feeds brought. There is no reliable and working alternative for obtaining the data.

CLI TikTok uses the official Proxitok instance for the scraping, https://proxitok.pabloferreiro.es

I heavily recommend users to run their own instance of Proxitok if they plan to do moderate or heavy usage of this software. The instance can be changed at any time on `src/contants.py` file.
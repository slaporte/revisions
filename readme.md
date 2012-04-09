Revision stats
===

This tool is intended to run on the [Wikimedia Toolserver](http://toolserver.org/). It computes statistics from the revision history of a page on Wikipedia:
* Total revisions
* Total minor revisions
* First edit date
* Most recent edit date
* Average time between edits
* Age (time since the first revision)
* Recent edit age
* Count of editors with 5 or more edits on this article
* Percent of edits from the top 20% editors on this page
* Percent of edits from the top 5% of editors on this page
* Total unique editors
* Average revision length
* Estimate of revert revisions (from the edit summery)
* Some of the above, limited to the last 30 days
* Some of the above, limited to the last 500 edits

Instructions
---

Run `revision.py`. Bottle will listen on port `8088`.

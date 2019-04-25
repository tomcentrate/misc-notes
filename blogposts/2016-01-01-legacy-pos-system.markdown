---
layout: article
title:  "Data Driven Restaurant Business Production"
date:   2016-01-01 00:01:00
categories: project
tags: restaurant
---


As part of revitalizing a family owned chinese restaurant, we are looking at ways to grow and expand our abilities and output. One of the major bottlenecks we see is the difficulty in the kitchen. Certain dishes can back up and hold the entire kitchen production hostage. And the [bus factor][busfactor] is essentially 1.


# Optimize the menu

The head chef fears in removing items from their menu. This lead to a giant setup of 5 different menus, 300+ items, with many slightly varied or having arbitrary rules and pricing. This leads to difficulties in the amount offered.

We needed metrics on which items worked well, and which needs to get chopped.
- Appetizer items should not take more than 5 minutes to make
- Items need to be ordered more than n times within a month
- Items need to have base ingredients in more than 2 dishes
- Dishes need to be simple enough to take less than 10 minutes to get out the door

And Overall, the menu should shrink down to 60 items overall, including take out menu.

# Game Plan:

1. Get all the information from the database.
2. Run queries on the receipts by date.
3. Group Orders by Types of Customers, and see if it's available.

# Getting the Data

We're using an outdated Point-of-Sales System Software, Champion POS, which I think is now defunct.
Champion POS used an old MySQL database. There was some encoding problems involved with the SQL dump.
```

```
[busfactor]: https://en.wikipedia.org/wiki/Bus_factor

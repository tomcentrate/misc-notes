---
layout: article
title: "One Man Development Team"
date: 2015-09-07 22:05:53 -0400
comments: true
categories: projects
---

I recently picked up a small project over the weekend. With the promise to myself to launch an MVP by week's end, I needed to have a solid system down that worked well enough.

It is a customer rewards tracking system, so that a business can keep track of customer purchases, and offer discounts at time of purchase. This is meant to replace their current Access database.

## Organizing Thoughts
Tickets and feature management is a must. I've tried other ticketing systems, and I wanted a little more integration with Github or Bitbucket. From a recommendation from my coworker [Brandon][tbash], [waffle.io][waffleio] has been a very good choice. Tickets integrated well with Github issues, features, and pull requests. Progress of the ticket was tracked as I pushed changes to feature branches.

Some required features to emulate the current system:

- Cashier Login
- Cashier can add a new customer into system
- Cashier can add a visit and add a new reward
- A report to determine when customers at the month are

Some new features requested:

- Rewards to show up at intervals of dollars spent
- Rewards for frequency of visits
- Alerting the cashier at time of entry about the available deal.

## Make sure it works
Since this is a part time project, I need to make sure that it's functional enough for people to use. While I'm doing some things from a TDD perspective, I didn't want to spend too much time debugging launches.

After enough listens to the [Ruby on Rails Podcasts][rorpodcast], I checked out [Codeship's continous deployment service][codeship] to keep my application recent and working. It's a change in pace to how I've been doing my projects.

There were some growing pains setting up Capistrano to deploy on my own servers.  I wrote up some steps and left it in my project's readmes. Overall I'm pretty satisfied on how it works.

## Keeping it small and tight.

I don't want to mess around with small details, like User Authentication and Authorization. Using gems like CanCanCan and Devise speed up my creation process.

For the front-end sections, I'm looking to find a better way to build interfaces. Right now I'm just grabbing Javascript plugins for search boxes and autocompletes, and its working out okay for an MVP.

[tbash]: http://teebash.co
[waffleio]: http://waffle.io
[codeship]: http://codeship.com
[rorpodcast]: http://5by5.tv/rubyonrails

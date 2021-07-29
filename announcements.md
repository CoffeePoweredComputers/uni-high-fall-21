---
layout: page
title: Announcements
nav_exclude: true
description: A feed containing all of the class announcements.
---
# NOTE: This course website is still under development
# Announcements

{% assign announcements = site.announcements | reverse %}
{% for announcement in announcements %}
{{ announcement }}
{% endfor %}

---
layout: page
title: Staff
description: A listing of all the course staff members.
---


## Instructor

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

## Teaching Assistant

{% assign  tas = site.staffers | where: 'role', 'Teaching Assistant' %}
{% for ta in tas %}
{{ ta }}
{% endfor %}


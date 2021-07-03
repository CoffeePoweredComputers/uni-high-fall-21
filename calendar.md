---
layout: page
title: Calendar
description: Listing of course modules and topics.
---

# Calendar

{% assign sortedModules = site.modules | sort:n %}
{% for sortedModule in modules %}
<details markdown="block">
<summary> {{module.navtitle}} </summary>
{{ module }}
{{ module.n }}
</details>
{% endfor %}

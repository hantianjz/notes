---
publish: false
reviewed: 2023-04-29
review-frequency: ignore
link:
  - "[[reading]]"
tags:
  - MOC
---
## Health
```dataview
list from #notes WHERE icontains(link, [[health]]) sort file.ctime desc
```
## History
```dataview
list from #notes where icontains(link, [[history]]) sort file.ctime desc
```
## Career
```dataview
list from #notes where icontains(link, [[career]]) sort file.ctime desc
```
## Self-improvement
```dataview
list from  #notes where icontains(link, [[self help]]) OR icontains(link, [[self improvement]]) sort file.ctime desc
```
## Fiction
```dataview
list from  #notes where icontains(link, [[fiction]]) sort file.ctime desc
```
## Programming
```dataview
list from  #notes where icontains(link, [[programming]]) AND icontains(link, [[reading]]) sort file.ctime desc
```
## Everything else
```dataview
list from #notes 
WHERE 
icontains(link, [[reading]]) 
and !icontains(link, [[programming]]) 
and !icontains(link, [[fiction]]) 
and !icontains(link, [[self improvement]]) 
and !icontains(link, [[self help]]) 
and !icontains(link, [[career]]) 
and !icontains(link, [[history]]) 
and !icontains(link, [[health]]) 
sort file.ctime desc
```

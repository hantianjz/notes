---
link:
  - "[[habit]]"
tags:
  - personal
---

``` tracker
searchType: dvField
searchTarget: Deadlift, Squat, Shoulder press, Bench press
datasetName: DeadLift, Squat, ShoulderPress, BenchPress
separator: 'comma'
month:
    mode: annotation
    color: lightgreen
    headerMonthColor: lightgreen
    annotation: dl, sq, sp, bp 
    showAnnotationOfAllTargets: true
```

``` tracker
searchType: task.notdone
searchTarget: PMO
month:
    color: tomato
    headerMonthColor: orange
    todayRingColor: orange
    selectedRingColor: steelblue
    showSelectedValue: false
datasetName: F
summary:
    template: "Break: {{currentBreaks()}} day\nLast streak: {{currentStreak()}} day"
```

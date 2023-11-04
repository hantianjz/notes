---
publish: false
review-frequency: normal
link:
- '[[demo]]'
- '[[python]]'
- '[[orbital mechanic]]'
- '[[learning]]'
- '[[blogging]]'
- '[[Notes todo]]'
tags:
- documentation
---

# Building an orbital mechanic demo

Reading [Bartosz Ciechanowski](https://ciechanow.ski/)'s GPS article on [GPS](https://ciechanow.ski/gps/) made me want to learn orbital mechanic more properly, especially some of the math and be able to visualize the orbits. I also see this as a great opportunity to learn how to do some GUI programming which I am an absolute novice at.

First I had to learn the absolute basics of orbital mechanics. Using the example provided by Bartosz's GPS article. Using a Keplerian system seemed like a good starting point.
A Keplerian elements are a commonly used method to specify a position in space.
- Semi-major axis
- Eccentricity
- inclination
- longitude of the ascending node
- argument of perigee
- true anomaly

## Road map
A initial development road map I have envisioned is as follow:
1. 2D canvas drawing an eclipse orbit around a center given semi-major axis and eccentricity.
2. Allow multiple eclipse to be displayed
3. Support eclipse draw on different angle
4. Support drag and rotate via mouse
PS: Display logic should be kept GUI framework independent.
5. Project the 3D orbit into 2D, start with a fixed inclination from earth's plane of rotation.

[[2022-10-25]]
Starting the project in python with pysimplegui for now.
First day goal, draw a circle, and rotate with a given radius.
Okay first thing, I figured out how to draw a circle/oval using the example app, and got a way to move the shape. There are two way to move it, relative move, or absolute move.

For the purpose of orbiting a circle I might want to use absolute move to keep thing simple, this way I don't have to figure out where the shape is right now. And also figure out the delta for each position.

So I need to do some simple trig. Okay now I can get a dot.
So this is really interesting, I may need to do aliasing eventually because due to the pixel size my circle is not very smooth. For now I have a round circle being drawn now.

[[2022-10-26]]
Do I want to try playing with openGL, to get better quality display? Can I use opengl in ios/swift?
Okay took a side bender and playing with swift, it's an interesting language with a lot of nice syntactic sugar.

---
# References
- [Keplerian Elements](https://ciechanow.ski/gps/#keplerian-elements)
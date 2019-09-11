# BoardCAM
> *design it. build it. enjoy it*

[![Build Status](https://travis-ci.org/boardcam/BoardCAM.svg?branch=master)](https://travis-ci.org/boardcam/BoardCAM)
[![CircleCI](https://circleci.com/gh/BoardCAM/BoardCAM.svg?style=svg)](https://circleci.com/gh/boardcam/BoardCAM)

BoardCAM is a [CAD](https://en.wikipedia.org/wiki/Computer-aided_design)/[CAM](https://en.wikipedia.org/wiki/Computer-aided_manufacturing) software.
It is designed to provide engineering drawings and gcode support for handcrafted snowboard. It's written by [Python](https://www.python.org/).

![Head Image](./docs/background.jpg)

## Quick Start
generate snowboard manufacturing files for your specified parameters, first edit it. Then run it:
``` {.sourceCode .python}
>>> pip install -r requirements.txt
>>> python boardcam.py
```
Then, see the [output](./output) folder.

## Prerequisites
* mathematics: including but not limited to Pythagorean theorem, Cartesian coordinate system, various curves (parabolic hyperbolic Bezier curve), trigonometric function formula (sin cos tan), circular and elliptical standard equations, etc.
* Experience in machining, experience in tool clamping CAD/CAM software, CNC programming
* Gcode、PDF、SVG、DXF principle or grammar
* Snowboard manufacturing experience
* Python3 programming

The [docs](./docs) directory contains some of the references I have compiled.

## TODO-LIST
### Export format
- [x] SVG
- [x] PDF
- [x] G-code
- [ ] DXF
### Control board
- [ ] LinuxCNC
- [x] Grbl
- [ ] mach3
### Components
- [ ] Nose&Tail tip
- [x] Core
- [ ] Base
- [x] Mold
### Type
- [x] snowboard
- [ ] ski

## Links
* Ski Builder: http://www.skibuilders.com/phpBB2/
* Facebook group: https://www.facebook.com/groups/snowboardbuilders
* 【滑雪板制造】QQ群: [632878898](https://jq.qq.com/?_wv=1027&k=56qxmgw)

## How to Contribute
Please read [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for details on our code of conduct, 
and the process for submitting pull requests to us.

## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for more details.

## Sponsors
* [JetBrains](https://www.jetbrains.com/) - Offer free JetBrains Open Source license.

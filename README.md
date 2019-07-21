# BoardCAM

[![Build Status](https://travis-ci.org/boardcam/BoardCAM.svg?branch=master)](https://travis-ci.org/boardcam/BoardCAM)
[![CircleCI](https://circleci.com/gh/boardcam/BoardCAM.svg?style=svg)](https://circleci.com/gh/boardcam/BoardCAM)

BoardCAM is a snowboard [CAD](https://zh.wikipedia.org/zh-hans/%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%BE%85%E5%8A%A9%E8%AE%BE%E8%AE%A1)/[CAM](https://zh.wikipedia.org/wiki/%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%BE%85%E5%8A%A9%E5%88%B6%E9%80%A0) software.
It's written by [Python](https://www.python.org/).

![](https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwi-nKzxgMbjAhXHr1QKHXnqAiEQjRx6BAgBEAU&url=https%3A%2F%2Folympic.ca%2Fteam-canada%2Fsebastien-toutant%2Fsebastien-toutant-5%2F&psig=AOvVaw0rXdNoC1v_On_VggFzNfVc&ust=1563798325500563)

### Prerequisites

* 高中数学知识: 勾股定理、笛卡尔坐标系、各种曲线(抛物线 双曲线 贝塞尔曲线)、三角函数公式(sin cos tan)、圆和椭圆标准方程等;
* 机械加工的经验、对刀 夹持CAD/CAM软件使用经验 数控编程;
* gcode、PDF、SVG、DXF文件格式语法;
* 滑雪板制造经验;
* python3编程能力;

在[docs](./docs)目录包含一些我整理的参考资料。

## Contributing

Please read [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## TODO-LIST
- [x] SVG
- [x] PDF
- [x] Gcode
- [ ] DXF

- [ ] LinuxCNC
- [x] Grbl
- [ ] mach3

- [ ] 板头板尾垫片
- [x] 板芯
- [ ] 底板
- [x] 模具

- [x] snowboard
- [ ] ski

- 将pdf_export svg_export gcode_export 移至export模块

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for more details.
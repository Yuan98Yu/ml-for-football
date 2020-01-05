# football 环境

## 1 google-research/football

[google-research/football](https://github.com/google-research/football) 是一个用于强化学习的环境，其基于另一个使用 pygame 编写的足球游戏。而我们使用该环境的目的仅是获得数据。

在按照其 README 指导安装了 gfootball 的 python 模块后，便可以调用其 API 编写自己的程序以进行自定义的足球比赛并获得数据。

gfootball 模块的架构可如下理解：

- env

    - player

        玩家如何参与游戏，方式有：键盘, 手柄, 默认的 AI, 自定义的策略

    - football_env

        游戏场景，有：1v1,  11v11

- observation

    在特定时刻的 env 的所有数据：

    - 球的详细信息，包含位置信息
    - 左侧球队的详细信息，包含每个球员的位置，每个球员当前的移动方向
    - 右侧球队的详细信息，同上
    - ...

## 2 利用 google/football 编写一个自定义的足球比赛并获得数据

google-research/football 已经给出了一个默认的脚本（ play_game.py ）用于进行足球比赛。我只在其基础上改写，目的如下：

1. 两支队伍均使用默认 AI 进行 11 v 11 的比赛
2. 自定义比赛场数
3. 自定义 Observations 的输出格式和输出地址
4. 加快比赛速度：关闭 realtime 选项，关闭比赛的可视化界面

改写过程中，除 play_game.py 外，参考的资料是官方的 API 文档 [Environment API](https://github.com/google-research/football/blob/master/gfootball/doc/api.md) , [Observations](https://github.com/google-research/football/blob/master/gfootball/doc/observation.md)

## 3 运行 auto_game.py

我将命令写在 /ex/makefile 中，输入以下命令运行 2 中所述自定义比赛

```bash
make autogame
```

## 4 输出数据



## 5 我个人的运行环境

我在 win10 系统下，使用 WSL: Ubuntu18.04 作为运行环境。

在进行一场足球比赛的时候，如果需要开启可视化界面，则需另外安装桌面环境。我参考的博客 [Windows10访问Ubuntu子系统（WSL）的桌面环境](https://blog.csdn.net/xmh19936688/article/details/90212960)
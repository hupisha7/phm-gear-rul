# 学习进度（唯一进度来源）

> **规则**：做完一项就把 `[ ]` 改成 `[x]`，然后 `git commit`。
> 双机同步方式见 [WORKFLOW.md](WORKFLOW.md)。
> **详细计划**（每周读什么、写什么代码、怎么算学会了）见 [plans/](plans/00-索引.md)。

---

## 阶段 0 · 环境（第 0 周）

- [x] 建 conda 环境 `phm`（Python 3.10 + torch 2.5.0+cu124）
- [x] 关闭 conda 自动激活 base
- [x] `python check_env.py` 全部通过
- [x] 装 Git（2.56.0）+ 配置 `user.name` / `user.email`
- [x] 配置代理 `http://127.0.0.1:7897`（Clash Verge）→ GitHub 从 23.8s 超时变 1.7s
- [x] **在 GitHub 建仓库** `hupisha7/phm-gear-rul`（Public，未初始化 README）
- [x] `git push -u origin main` 成功 → `git branch -vv` 显示 `[origin/main]`
- [x] 本地 `git init` + 第一次 commit
- [x] 邮箱改为 noreply：`268777793+hupisha7@users.noreply.github.com`
- [ ] 家里电脑装好 Python + numpy/scipy/matplotlib
- [ ] 家里电脑 `git clone` 成功并能跑通练习题
- [ ] 把 `phm-gear-rul` 在 GitHub 主页 **Pin** 置顶

> **GitHub**：https://github.com/hupisha7/phm-gear-rul
> 详细：[plans/00-索引.md](plans/00-索引.md)

---

## 阶段 1 · Python / NumPy 基础（第 1–4 周）

> 详细计划：[notes/python_补漏计划.md](notes/python_补漏计划.md)

### W1 · Python 语法补漏

- [ ] 跑 `src/python_selftest.py`，记录通过数：____ / 16
- [ ] 列表 / 字典 / 元组 / 集合
- [ ] **列表推导式** + f-string
- [ ] `if` / `for` / `while` / `break` / `continue`
- [ ] 函数：参数、默认值、返回值
- [ ] `enumerate` / `zip` / `sorted(key=)` / `range`
- [ ] `try / except` + `with open()`
- [ ] A 组 + B 组诊断题重做，全部通过
- [ ] `notes/weekly.md` 写第一篇复盘
- [ ] **Git commit ≥ 2 次**

### W2 · 类 + NumPy 入门

- [ ] `class` / `__init__` / `self` / 方法（写 2 个小类）
- [ ] NumPy：数组创建、`shape`、`dtype`、`reshape`
- [ ] 索引切片 + **布尔索引**
- [ ] **广播机制**（官方文档 Broadcasting 一节）
- [ ] **`axis` 语义**（反复练 `sum` / `mean`）
- [ ] 逐元素运算 vs `@`；`concatenate` / `stack`
- [ ] C 组诊断题重做，全部通过
- [ ] `src/handwritten_matmul.py` 三重循环版通过
- [ ] **Git commit ≥ 2 次**

### W3 · NumPy 100 题

- [ ] `rougier/numpy-100` 前 20 题
- [ ] 前 40 题
- [ ] 前 60 题
- [ ] `src/handwritten_matmul.py` **向量化版**通过
- [ ] 大矩阵性能对比跑通，记录两种写法的耗时
- [ ] **Git commit ≥ 2 次**

### W4 · 回到项目

- [ ] `src/spectrum_peek.py`：画出频谱图
- [ ] 在图上标出 GMF=304 / 2GMF=608 / 3GMF=912 Hz
- [ ] 回答：主峰 911.36 Hz 是几倍频？反推真实转速？
- [ ] `notes/blindspots.md` 里 6 个问题全部作答
- [ ] **Git commit ≥ 2 次**

> **阶段 1 检查点**：关掉 AI，能独立写出一个读 `.mat`、算 RMS、画频谱的脚本。

---

## 阶段 2 · 信号处理（第 5–9 周）

> 详细计划：**[plans/阶段2-信号处理.md](plans/阶段2-信号处理.md)**
> 产出：《UNSW 齿轮振动特征手册》

### W5 · 傅里叶变换
- [ ] 采样定理、奈奎斯特、**频率分辨率 Δf = Fs/N**、频谱泄漏
- [ ] 窗函数（Hanning）的作用与代价
- [ ] **手写 DFT**（双重循环，1024 点）并与 `np.fft.fft` 对比
- [ ] 对 vib1 做 FFT 画频谱；改变数据长度观察分辨率变化
- [ ] 产出 `src/w5_fft.py` + 2 张图

### W6 · 齿轮运动学
- [ ] 从 `tacIN` 脉冲间隔反推**真实输入轴转频**
- [ ] 计算 GMF = 19 × f_in（干 190 Hz / 润 304 Hz）
- [ ] 谐波与**边频带**（间隔 = 转频）
- [ ] 在频谱图上标注 GMF 及其边频带，判断是大齿轮还是小齿轮损伤
- [ ] 产出 `src/w6_gear_kinematics.py` + 2 张图

### W7 · 时域指标
- [ ] 自己实现 RMS、峰值、峰峰值、**峭度**、峰值因子、裕度因子
- [ ] 对 20 个文件各算 6 个指标，画趋势图
- [ ] 用 **Spearman** 量化单调性，排出 Top 3
- [ ] 产出 `src/w7_time_features.py` + 趋势图 + CSV

### W8 · 包络解调
- [ ] Hilbert 变换原理、解析信号
- [ ] 带通滤波 → 包络 → **包络谱**
- [ ] 对比健康（00h00m）vs 退化（67h14m）
- [ ] 产出 `src/w8_envelope.py` + 2 张图

### W9 · 时频分析与特征手册
- [ ] STFT 时频图 + 窗长实验
- [ ] 小波变换（了解）
- [ ] 循环平稳初步（谱相关）
- [ ] **交付：《UNSW 齿轮振动特征手册》**

> **阶段 2 检查点**：能口头回答"为什么齿轮局部磨损会产生间隔等于转频的边频带"。

---

## 阶段 3 · 真实健康指标（第 10–14 周）⭐ 成败点

> 详细计划：**[plans/阶段3-健康指标.md](plans/阶段3-健康指标.md)**

### W10 · 绝对传动误差
- [ ] 先画 `tacIN` / `encOUT` 波形，判断 `encOUT` 是什么信号
- [ ] 解码 `tacIN`（转速计，1 脉冲/转）→ 输入轴转角
- [ ] 解码 `encOUT`（编码器，干 1000 / 润 512 脉冲每转）→ 输出轴转角
- [ ] 计算**绝对传动误差** ATE（读 Chin et al. 2021, MSSP 146:107070）
- [ ] 画出 20 个文件的 ATE 趋势曲线

### W11 · 特征筛选（三准则）
- [ ] **单调性** / **趋势性** / **鲁棒性** 三个指标
- [ ] 汇总 12–18 个候选特征并打分
- [ ] 产出 Top 5 特征评分表

### W12 · 无监督健康指标
- [ ] 先用简单方法（马氏距离 / PCA），**几行代码拿到曲线**
- [ ] （不够好再上）自编码器：只用 `00h00m` 训练，重构误差作 HI
- [ ] **得到一条单调上升的 HI 曲线**（|Spearman| > 0.9）
- [ ] 自查：代码里有没有用到 `current_hour`？（不能有）

### W13 · 阈值与退化建模
- [ ] 定义失效阈值（推荐取最后一个文件的 HI）
- [ ] 指数退化模型拟合 HI(t)
- [ ] **只用 t_i 之前的数据**外推 → RUL 预测曲线

### W14 · 严格评估
- [ ] 按文件顺序划分：前 6 训练 / 中 2 验证 / 后 2 测试
- [ ] 报告**真实的** MSE / MAE / R²（会很难看）
- [ ] **泄漏对照实验**：随机+时间标签 / 顺序+时间标签 / 顺序+HI标签
- [ ] 交付 `notes/leakage_case_study.md`（⭐ 招牌文章底稿）

> **阶段 3 检查点（第 13 周）**：能不能做出单调的 HI？
> **做不出来就停下来复盘，不要往下走。**
> 同时：**从这一周开始投简历**，一边做一边投。

---

## 阶段 4 · 建模与对比（第 15–20 周）

> 详细计划：**[plans/阶段4-建模与对比.md](plans/阶段4-建模与对比.md)**

- [ ] W15 · 换到 **NASA C-MAPSS**，跑通标准 RUL 流程（有标签的教科书版）
- [ ] W16 · 传统 ML 基线：特征 + RandomForest / XGBoost / SVR
- [ ] W17 · 深度学习：复用毕设框架，**标签换成 HI**
- [ ] W18 · **不确定性量化**：MC-Dropout → RUL 置信区间（PICP / MPIW）
- [ ] W19 · **跨工况迁移**：润滑 ↔ 干摩擦（基线 / 微调 / 域适应）
- [ ] W20 · 消融实验 + 结果整理 + 项目总结

> **阶段 4 检查点**：能不能用 15 分钟讲清整个项目（背景 → 方法 → 结果 → 局限）？

---

## 阶段 5 · 工程化与作品集（第 21–26 周）

> 详细计划：**[plans/阶段5-工程化与作品集.md](plans/阶段5-工程化与作品集.md)**

- [ ] W21 · Git 分支 / Linux / **Docker** 基础
- [ ] W22 · 仓库规范化（配置、测试、README 重写）
- [ ] W23 · **FastAPI** 推理接口 + InfluxDB/TDengine 时序存储
- [ ] W24 · 监测看板（Streamlit）
- [ ] W25 · 技术博客 2–3 篇（含泄漏复盘招牌文）
- [ ] W26 · **重写简历 + 模拟面试 3 次 + 投出 30 份**

> **阶段 5 检查点**：远程仓库完整、简历已投出。

---

## 长期检查点

| 时间 | 检查点 | 状态 |
|---|---|---|
| 2027.01 | 计划是否过半？能否独立写 PyTorch 代码？ | ☐ |
| 2027.07 | 是否参与过至少 1 个数字化/工业相关项目？ | ☐ |
| 2027.12 | 技能是否够面初级工业 AI 岗？内部转岗有进展？ | ☐ |

---

## 日常打卡（倒序，最新的写最上面）

| 日期 | 时长 | 做了什么 | 卡在哪 |
|---|---|---|---|
| 2026-10-09 | 1h | 建 phm 环境、跑通 check_env.py | PyCharm 选了 base 环境 |
| 2026-10-09 | 0.5h | 装 Git、`git init`、第一次 commit | **GitHub 推不上去（流量被限速）** |
| 2026-10-16 | 2h | 装 Git、配代理、建仓库、首次 push 成功 | GitHub 账号认错（3jw vs hupisha7） |

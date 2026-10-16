# PHM Rebuild

工业设备预测性维护（PHM）学习项目。

**目标**：从原始振动信号 → 特征提取 → 健康指标 → 剩余寿命预测，全流程代码自己写，每一步能讲清为什么。

**数据**：UNSW Sydney 单级直齿轮运行至失效试验（齿轮 19/52 齿，100 kHz 采样）
- 路径：`C:\bishe2\datasets\`（干摩擦 10 个文件 + 润滑 10 个文件）

**环境**：conda 环境 `phm`（Python 3.10.20 + torch 2.5.0+cu124 + RTX 3060）

---

## 快速开始

```powershell
conda activate phm
python check_env.py
```

看到「全部通过」就说明环境没问题。

---

## W1 任务清单（本周）

### ☐ 任务 1：环境自检

```powershell
conda activate phm
python check_env.py
```

把输出里的 `频谱主峰频率` 和 `理论啮合频率 GMF` 记下来。

### ☐ 任务 2：手写矩阵乘法（不看任何现成代码）

在 `src/handwritten_matmul.py` 里写三个版本，**都不许用 `np.dot` / `@`**：

1. **纯 Python 版**：三重 for 循环，列表套列表
2. **NumPy 向量化版**：用广播 + `np.sum`（提示：`A[:, :, None] * B[None, :, :]`）
3. **对比**：和 `A @ B` 的结果比对，验证误差 < 1e-10

然后测三种写法在 200×200 矩阵上的耗时，打印出来。

**验收标准**：能口头解释
- 为什么向量化版本快这么多
- `axis` 参数在 `np.sum` 里到底在做什么
- 形状 `(200, 200)` 和 `(200, 1)` 相加时发生了什么

### ☐ 任务 3：在频谱图上标出啮合频率

在 `src/spectrum_peek.py` 里：

1. 读 `Lubricated-16Hz-20Nm-00h00m.mat` 的 `vib1`
2. 做 FFT，画出频谱（**x 轴限制在 0–3000 Hz**，否则看不清）
3. 在图上用竖线标出：`GMF = 304 Hz`、`2×GMF = 608 Hz`、`3×GMF = 912 Hz`
4. 找出主峰，打印出它的频率和幅值

**验收标准**：能回答
- 主峰落在哪个频率上？它是 GMF 的几倍频？
- 如果你算出的主峰不是正好 912 Hz，说明什么？（提示：反推真实转速）
- 为什么齿轮振动的主峰常常不在 GMF 本身，而在高次谐波上？

### ☐ 任务 4：建立「盲区清单」

在 `notes/blindspots.md` 里记录：读自己毕设代码时，**每一处读不懂的地方**。

格式：
```
- 文件:行号 | 读不懂的东西 | 我的猜测
- gear_mat_dataset_v2.py:128 | np.linspace 第三个参数是点数还是步长？ | 点数
```

**不求读懂，只求知道盲区在哪。** 这张清单就是你后面 12 周的靶子。

### ☐ 任务 5：周日复盘

在 `notes/weekly.md` 写下 200 字：做了什么 / 卡在哪 / 下周补什么。

---

## 三条铁律

1. **不许 AI 生成代码。** 可以查概念、可以贴报错问「为什么」，代码自己敲。
2. 卡住先查官方文档，**30 分钟解决不了再问 AI**；问完必须自己重写一遍。
3. 每周至少 2 次 Git commit。

---

## 目录说明

```
phm/
├── PROGRESS.md           ⭐ 学习进度（唯一来源，28 周任务清单）
├── WORKFLOW.md           ⭐ 双机工作流（办公室 + 家里怎么同步）
├── check_env.py          环境自检
├── README.md             本文件
├── src/                  自己写的代码
├── results/              图表输出
└── notes/
    ├── python_补漏计划.md Python 4 周补漏计划
    ├── blindspots.md     盲区清单（读不懂的都记这里）
    └── weekly.md         每周复盘
```

## 双机同步（办公室 + 家里）

用 Git + GitHub 做主干。**每天的固定动作只有两条：**

```powershell
git pull                                          # 开工前
git add -A; git commit -m "W1: xxx"; git push     # 收工前
```

详见 [WORKFLOW.md](WORKFLOW.md)。

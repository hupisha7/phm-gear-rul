# 双机工作流（办公室 + 家里）

> **结论先说：用 Git + GitHub 做主干。** 代码、笔记、进度全走这条路，两台机器自动一致。

---

## 0. 为什么是 Git，不是网盘

| 方案 | 代码同步 | 冲突处理 | 历史记录 | 对求职有用 |
|---|---|---|---|---|
| **Git + GitHub** | ✅ | ✅ 能合 | ✅ 每次提交都有记录 | ✅ **HR 会点进来看** |
| 网盘同步文件夹 | ✅ | ❌ 会覆盖、会冲突 | ❌ | ❌ |
| 微信/QQ 传文件 | 🔶 手动 | ❌ | ❌ | ❌ |
| U 盘 | 🔶 手动 | ❌ | ❌ | ❌ |

**Git 不只是同步工具，它同时是：**
- 你的**进度条**（GitHub 主页的绿色格子）
- 你的**作品集**（招聘方真的会看 commit 记录）
- 你今天要学的一项**核心工程技能**（阶段 5 正式要考）

**一举三得，所以现在就用起来。**

---

## 1. 一次性设置（在办公室电脑做，约 15 分钟）

### 1.1 装 Git

下载：https://git-scm.com/download/win
安装时一路默认即可。

验证：
```powershell
git --version
```

### 1.2 配置身份

```powershell
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

### 1.3 注册账号 + 建仓库

**两个选择：**

| | GitHub | Gitee（码云） |
|---|---|---|
| 国际认可度 | ⭐⭐⭐ | ⭐ |
| 国内访问速度 | 慢（有时要代理） | 快 |
| 推荐 | ✅ **优先**（招聘方看这个） | 备份/备用 |

**建议先试 GitHub**，打不开或太慢就用 Gitee。网站是 gitee.com，操作一模一样。

**建仓库步骤（GitHub）：**
1. 右上角 `+` → `New repository`
2. 名字填：**`phm-gear-rul`**
3. 描述填：`Industrial gear RUL prediction — PHM learning & portfolio`
4. 选 **Public**（作品集要公开；初始阶段写得糙没关系，**commit 记录本身就是价值**）
5. **不要**勾选 "Add a README file"（本地已经有了）
6. 点 `Create repository`

### 1.4 本地推到远程

在 `C:\phm` 目录下：

```powershell
cd C:\phm

git init
git add -A
git commit -m "init: 项目骨架 + 环境自检脚本 + 28周学习计划"

git branch -M main
git remote add origin https://github.com/你的用户名/phm-gear-rul.git
git push -u origin main
```

**第一次 push 会弹出登录窗口**，按提示授权即可（GitHub 现在用浏览器授权，不用输密码）。

成功后刷新网页，你应该能看到自己的文件。

---

## 2. 日常习惯（只有两条）

### 开工前：拉取

```powershell
cd C:\phm
git pull
```

### 收工前：提交并推送

```powershell
cd C:\phm
git add -A
git commit -m "W1: 完成矩阵乘法三重循环版"
git push
```

**就这两条。** 养成之后，两台机器永远不会不同步。

### commit message 怎么写

因为 commit 记录是作品集的一部分，写清楚一点：

| ✅ 好 | ❌ 差 |
|---|---|
| `W1: 完成矩阵乘法三重循环版` | `update` |
| `W3: 修复 reshape 维度错误` | `fix` |
| `W5: 加入 FFT 频谱分析与 GMF 标注` | `修改` |

---

## 3. 家里电脑怎么搭（第 0 周做一次）

### 3.1 装 Python

**推荐 Miniconda**（比完整 Anaconda 小很多，约 100 MB）：
https://docs.conda.com/miniconda/

或者更简单：直接装 https://www.python.org/downloads/ 的 Python 3.10。

### 3.2 装必要的包

**关键认知：W1–W4 只需要这些，不需要 PyTorch。**

```powershell
pip install numpy scipy matplotlib
```

就这三个。省掉 2.5 GB 的 torch 下载和 CUDA 折腾。

### 3.3 拉代码

```powershell
git clone https://github.com/你的用户名/phm-gear-rul.git
cd phm-gear-rul
python src/python_selftest.py
```

看到 `通过 X / 16` 就说明家里也能跑了。

### 3.4 什么时候家里才需要 PyTorch

**第 15 周以后**（深度学习阶段）。到那时再装，而且家里没 NVIDIA 显卡的话，装 CPU 版就行：

```powershell
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

你的模型很小（权重才 300 KB），CPU 训练慢一点但完全能跑。

---

## 4. 数据怎么办（第 5 周才开始操心）

**重要：W1–W4 你根本不需要数据。** 纯 Python / NumPy 练习，用不上 `.mat` 文件。

### 到 W5 时，数据总大小约 312 MB

| 通道 | 说明 |
|---|---|
| 20 个 `.mat` 文件 | 干摩擦 10 个 + 润滑 10 个，每个约 15 MB |

### 三种方案

| 方案 | 做法 | 评价 |
|---|---|---|
| **阿里云盘 / OneDrive** | 把 `C:\bishe2\datasets\` 整个上传，家里下载 | ⭐ **推荐**，312 MB 很快 |
| U 盘 / 移动硬盘 | 直接拷 | ✅ 最省事，一次性 |
| 回家重新下载 | 需要原始来源链接 | 🔶 不确定能否公开下载 |

**注意：数据不要提交到 Git！** `.gitignore` 里已经排除了 `*.mat`。Git 不适合存大文件。

### 如果家里不想放数据

也可以反过来安排：
- **办公室**：做需要数据的工作（W5 之后的所有信号处理）
- **家里**：做不需要数据的工作（看论文、写代码框架、做 NumPy 练习）

**但这会让节奏割裂，不推荐。** 还是把数据拷回家最省心。

---

## 5. 进度怎么追踪

### 唯一来源：`PROGRESS.md`

这个文件里有 28 周的全部任务，全是 `[ ]` 复选框。

- 做完一项 → 改成 `[x]`
- 每周日更新一次 → `git commit`
- **在 GitHub 网页上会渲染成漂亮的进度条**

**不需要额外的软件、Excel、Notion。** 越少的地方要维护，越容易坚持。

### 想看得更直观？

GitHub 网页上打开 `PROGRESS.md`，就能看到勾选情况。另外：
- **主页绿色格子**：你哪天提交了代码，一目了然
- **Commits 页面**：你每周做了什么的完整时间线

---

## 6. 常见问题

### GitHub 打不开 / 太慢

1. 换 **Gitee**（gitee.com），操作完全一样
2. 或者用 GitHub 加速工具（如 `Watt Toolkit`，原 Steam++）
3. 或者 `git config --global http.proxy` 配代理

### 忘了 `git pull` 就直接改，冲突了

别慌。冲突通常长这样：
```
<<<<<<< HEAD
你的改动
=======
远程的改动
>>>>>>> origin/main
```
用编辑器打开冲突文件，**删掉 `<<<<<<<`、`=======`、`>>>>>>>` 这些标记，留下你想要的内容**，然后：
```powershell
git add -A
git commit -m "resolve conflict"
git push
```

**预防**：养成"开工先 pull"的习惯，冲突率降到几乎为零。

### 不小心提交了大文件（比如 .mat）

```powershell
git rm --cached 文件名
```
然后把文件名加到 `.gitignore` 里，再 commit。

### 想保留某些图片在仓库里

`.gitignore` 默认忽略了 `results/*.png`。如果某张图是重要的成果图，强制加进去：

```powershell
git add -f results/关键图.png
```

---

## 7. 一张图记住整个流程

```
        办公室电脑                          家里电脑
             │                                  │
             │  ┌─────────── GitHub ───────────┐ │
             │  │   phm-gear-rul (仓库)         │ │
             └──┤   ├── src/       代码         ├─┘
                │   ├── notes/     笔记         │
                │   ├── PROGRESS.md 进度        │
                │   └── README.md  说明         │
                └──────────────────────────────┘

  每天：开工 git pull ──► 写代码/做题 ──► 收工 git push
  每周：更新 PROGRESS.md 复选框 + 写 weekly.md 复盘
  数据：W5 起用云盘同步 datasets 目录（不进 Git）
```

---

## 8. 现在做哪三件事

1. **在办公室电脑**：装 Git、注册账号、建仓库、跑 1.4 节的 5 条命令
2. **回家**：装 Miniconda + `pip install numpy scipy matplotlib` + `git clone`
3. **把 `PROGRESS.md` 里"阶段 0"的三项勾上**

做完这三件，你就有了一个**跨两台机器、自动同步、还能当作品集**的学习系统。

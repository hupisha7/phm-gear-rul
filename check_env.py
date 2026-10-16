"""
W1 环境自检脚本
----------------
用法：
    conda activate phm
    python check_env.py

作用：一次性验证你的 PHM 开发环境是否完整可用。
它会检查包、验证 GPU、并真实读取一个 .mat 文件算出第一个健康指标。
"""
import sys
import time
from pathlib import Path

OK, BAD, WARN = "[OK]  ", "[FAIL]", "[WARN]"
problems = []


def line(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------- 1. Python
line("1. 当前解释器（最先看这里）")
print(f"  版本   : {sys.version.split()[0]}")
print(f"  路径   : {sys.executable}")

EXPECTED = "envs\\phm\\python.exe"
if EXPECTED.lower() not in sys.executable.lower():
    print(f"\n  {BAD} 你现在用的不是 phm 环境！")
    print("         " + "-" * 50)
    print("         修复：在终端里执行")
    print("             conda activate phm")
    print("             python check_env.py")
    print("         提示符应该从 (base) 变成 (phm)")
    print("         " + "-" * 50)
    print(f"  {WARN} 常见误区：不要急着 pip install！")
    print("         先确认解释器对不对，否则会装出两份互相打架的环境。")
    problems.append("解释器不是 phm 环境")
elif sys.version_info[:2] != (3, 10):
    print(f"{WARN} 预期 Python 3.10，当前是 {sys.version_info.major}.{sys.version_info.minor}")


# ---------------------------------------------------------------- 2. 依赖包
line("2. 依赖包")

REQUIRED = {
    "numpy": "矩阵运算（一切的基础）",
    "scipy": "读 .mat 文件 + 信号处理（fft、signal、stats）",
    "matplotlib": "画图",
    "pandas": "表格数据（阶段 4 会用）",
    "sklearn": "传统 ML 基线（阶段 4 会用）",
    "torch": "深度学习",
}
OPTIONAL = {
    "tqdm": "训练进度条",
    "h5py": "读 HDF5 格式数据",
    "openpyxl": "导出 Excel",
}

for name, why in REQUIRED.items():
    try:
        mod = __import__(name)
        ver = getattr(mod, "__version__", "?")
        print(f"  {OK} {name:<12} {ver:<14} {why}")
    except ImportError:
        print(f"  {BAD} {name:<12} {'未安装':<14} {why}")
        problems.append(f"缺少必需包：{name}")

print()
for name, why in OPTIONAL.items():
    try:
        mod = __import__(name)
        print(f"  {OK} {name:<12} {getattr(mod, '__version__', '?'):<14} {why}")
    except ImportError:
        print(f"  {WARN} {name:<12} {'未安装':<14} {why}（可选）")


# ---------------------------------------------------------------- 3. GPU
line("3. PyTorch 与 GPU")
try:
    import torch

    print(f"  torch        : {torch.__version__}")
    print(f"  CUDA build   : {torch.version.cuda}")
    print(f"  CUDA 可用    : {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        print(f"  显卡         : {torch.cuda.get_device_name(0)}")
        props = torch.cuda.get_device_properties(0)
        print(f"  显存         : {props.total_memory / 1024**3:.1f} GB")
        print(f"  cuDNN        : {torch.backends.cudnn.version()}")

        # 真跑一次，不只是问"能不能用"
        t0 = time.perf_counter()
        x = torch.randn(2000, 2000, device="cuda")
        _ = (x @ x).sum().item()
        torch.cuda.synchronize()
        dt = time.perf_counter() - t0
        print(f"  {OK} GPU 矩阵乘法实测通过（2000x2000 用时 {dt*1000:.1f} ms）")
    else:
        print(f"  {BAD} CUDA 不可用 —— 训练会慢很多")
        problems.append("CUDA 不可用")
except ImportError:
    print(f"  {BAD} torch 未安装")
    problems.append("缺少 torch")
except Exception as e:
    print(f"  {BAD} GPU 测试异常：{e}")
    problems.append(f"GPU 测试异常：{e}")


# ---------------------------------------------------------------- 4. 真读一份数据
line("4. 真实读取一个 .mat 文件")

MAT_DIR = Path(r"C:\bishe2\datasets\Lubricated Test")
if not MAT_DIR.exists():
    print(f"  {WARN} 找不到数据集目录：{MAT_DIR}")
    print("         请修改本脚本开头的 MAT_DIR 变量")
else:
    try:
        import scipy.io as sio
        import numpy as np

        files = sorted(MAT_DIR.glob("*.mat"))
        print(f"  找到 {len(files)} 个 .mat 文件")

        f0 = files[0]
        t0 = time.perf_counter()
        d = sio.loadmat(f0)
        dt = time.perf_counter() - t0

        print(f"\n  读取 {f0.name}（用时 {dt:.2f}s）")
        for k in ("Fs", "vib1", "vib2", "tacIN", "encOUT"):
            if k in d:
                a = np.asarray(d[k]).reshape(-1)
                print(f"    {k:<8} shape={str(a.shape):<14} "
                      f"min={a.min():>10.4f}  max={a.max():>10.4f}")
            else:
                print(f"    {k:<8} 不存在")

        fs = float(np.asarray(d["Fs"]).reshape(-1)[0])
        vib = np.asarray(d["vib1"]).reshape(-1)

        # 你的第一个健康指标
        rms = float(np.sqrt(np.mean(vib ** 2)))
        peak = float(np.max(np.abs(vib)))

        from scipy.stats import kurtosis
        kurt = float(kurtosis(vib, fisher=False))

        # 第一个频谱
        from scipy.fft import rfft, rfftfreq
        X = np.abs(rfft(vib * np.hanning(len(vib))))
        f = rfftfreq(len(vib), 1 / fs)
        peak_freq = float(f[np.argmax(X)])

        print(f"\n  --- 你的第一个健康指标 ---")
        print(f"      采样率 Fs        : {fs:.0f} Hz")
        print(f"      频率分辨率       : {fs/len(vib):.4f} Hz")
        print(f"      RMS              : {rms:.6f}")
        print(f"      峰值             : {peak:.6f}")
        print(f"      峭度             : {kurt:.4f}")
        print(f"      频谱主峰频率     : {peak_freq:.2f} Hz")
        print(f"      理论啮合频率 GMF : {19 * 16} Hz（输入16Hz × 19齿）")
        print(f"\n  下一步：把 GMF 附近 5 Hz 内的幅值取出来，对 20 个文件各算一遍，画趋势图。")

    except Exception as e:
        print(f"  {BAD} 读取失败：{type(e).__name__}: {e}")
        problems.append(f"读取 .mat 失败：{e}")


# ---------------------------------------------------------------- 总结
line("自检结果")
if problems:
    print("  发现以下问题：")
    for p in problems:
        print(f"    - {p}")
    print("\n  修复建议见 W1 环境搭建说明。")
else:
    print("  全部通过。可以开始 W1 的练习了。")
    print("\n  今天的目标：不看任何现成代码，用 for 循环手写一遍矩阵乘法，")
    print("  再和 np.dot 的结果对比。做完你就知道张量乘法到底在干什么了。")

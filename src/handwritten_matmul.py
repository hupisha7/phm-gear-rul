"""
W1 任务 2：手写矩阵乘法
========================

目标：搞明白「张量运算到底在做什么」。

为什么要做这个？
    你现在用 PyTorch 写模型，本质上 90% 的运算都是矩阵乘法。
    如果你不理解矩阵乘法在内存里是怎么发生的、为什么向量化快，
    那你就永远只能"照着别人的代码改"，而不知道为什么这么写。

要求：
    实现两个函数，都用 np.allclose 和 A @ B 对比验证：
    1. matmul_loops(A, B)       —— 纯 Python 三重循环
    2. matmul_vectorized(A, B)  —— NumPy 广播，不许用 @ / np.dot / np.matmul

    然后对比两者在 200×200 矩阵上的耗时。
"""

import time
import numpy as np


# ---------------------------------------------------------------------------
# 1. 纯 Python 三重循环版
# ---------------------------------------------------------------------------
def matmul_loops(A, B):
    """
    用三重循环实现 C = A @ B。

    定义（照抄数学定义，这就是全部提示）：
        A 形状 (n, k)，B 形状 (k, m)，C 形状 (n, m)
        C[i][j] = Σ_p  A[i][p] * B[p][j]        （p 从 0 到 k-1）

    注意：
        - A、B 传进来是 np.ndarray，但你要**当普通列表用**（用 .tolist() 转一下更纯粹）
        - 不许用 np.dot / @ / np.matmul / np.einsum
        - 返回可以是 list 或 np.ndarray，验证时都能比

    提示：先建一个 n 行 m 列的全零结构，再三重循环填。

    TODO: 你来写
    """
    raise NotImplementedError("matmul_loops 还没写")


# ---------------------------------------------------------------------------
# 2. NumPy 向量化版
# ---------------------------------------------------------------------------
def matmul_vectorized(A, B):
    """
    用 NumPy 广播实现，同样不许用 @ / np.dot / np.matmul。

    核心思路（这是本任务真正要学的东西）：
        三重循环里，最内层是在「对第 p 维求和」。
        向量化的做法就是：先把这一维「撑开」成一个独立的轴，
        让所有 (i, p, j) 组合同时算出来，最后再沿着这个轴求和。

    思考步骤：
        A 是 (n, k)，B 是 (k, m)。
        你想得到 (n, k, m) 这样一个三维数组，
        其中 [i, p, j] = A[i, p] * B[p, j]
        然后沿着 axis=? 求和，就得到 (n, m)。

    提示：用 None 给数组「加一个长度为 1 的轴」，触发放射（broadcast）。
        想想 A 该变成什么形状、B 该变成什么形状，才能相乘得到 (n, k, m)。

    TODO: 你来写
    """
    raise NotImplementedError("matmul_vectorized 还没写")


# ---------------------------------------------------------------------------
# 测试框架（这个不用改）
# ---------------------------------------------------------------------------
def check(name, fn, A, B):
    """跑一个实现，和标准答案对比，并计时。"""
    try:
        t0 = time.perf_counter()
        C = fn(A, B)
        dt = time.perf_counter() - t0
    except NotImplementedError as e:
        print(f"  {name:<24} 未实现（{e}）")
        return False
    except Exception as e:
        print(f"  {name:<24} 报错：{type(e).__name__}: {e}")
        return False

    ref = A @ B
    C = np.asarray(C, dtype=float)
    ok = C.shape == ref.shape and np.allclose(C, ref, atol=1e-10)

    mark = "通过" if ok else "失败"
    print(f"  {name:<24} {mark}   耗时 {dt*1000:9.2f} ms")
    if not ok:
        print(f"      形状：得到 {C.shape}，期望 {ref.shape}")
        if C.shape == ref.shape:
            print(f"      最大误差：{np.abs(C - ref).max():.3e}")
    return ok


if __name__ == "__main__":
    rng = np.random.default_rng(42)

    print("=" * 60)
    print("第一步：小矩阵正确性验证  (3×4) @ (4×2)")
    print("=" * 60)
    A_s = rng.random((3, 4))
    B_s = rng.random((4, 2))
    print("\nA =\n", np.round(A_s, 3))
    print("\nB =\n", np.round(B_s, 3))
    print("\n标准答案 A @ B =\n", np.round(A_s @ B_s, 4), "\n")

    check("纯 Python 三重循环", matmul_loops, A_s, B_s)
    check("NumPy 向量化", matmul_vectorized, A_s, B_s)

    print()
    print("=" * 60)
    print("第二步：大矩阵性能对比  (200×200) @ (200×200)")
    print("=" * 60, "\n")
    A_b = rng.random((200, 200))
    B_b = rng.random((200, 200))

    check("纯 Python 三重循环", matmul_loops, A_b, B_b)
    check("NumPy 向量化", matmul_vectorized, A_b, B_b)

    t0 = time.perf_counter()
    _ = A_b @ B_b
    dt = (time.perf_counter() - t0) * 1000
    print(f"  {'numpy @ (标准答案)':<24}  —      耗时 {dt:9.2f} ms")

    print()
    print("=" * 60)
    print("做完之后，用你自己的话回答这三个问题（写在 notes/blindspots.md 里）：")
    print("=" * 60)
    print("  1. 为什么向量化版本快了这么多？快在哪一步？")
    print("  2. np.sum(x, axis=1) 里的 axis=1 到底在做什么？")
    print("  3. A 形状 (200, 200)、B 形状 (200, 1) 相加时，B 是怎么被「撑开」的？")

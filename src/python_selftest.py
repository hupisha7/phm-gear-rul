"""
Python / NumPy 诊断（W1 补充材料）
===================================

用法：
    conda activate phm
    python src/python_selftest.py

规则：
    - 15 道题，每道限 2 分钟
    - 不许查资料、不许问 AI、不许看别人的代码
    - 写不出来就跳过，直接跑脚本看结果
    - 打不通的那几道，就是你的学习清单

写完再跑一次，看着 ☐ 一个个变成 ✓。
"""

import numpy as np


# ===========================================================================
# A 组 · Python 基础语法
# ===========================================================================

def t1_even_squares():
    """
    用【列表推导式】返回 1~100（含）中所有偶数的平方。
    期望：list，长度 50，第一个元素是 4，最后一个元素是 10000
    """
    # TODO: 你来写（提示：一行列表推导式就够）
    raise NotImplementedError


def t2_minmax(lst):
    """
    返回 (最小值, 最大值)，【不许用 max() / min()】。
    """
    # TODO: 你来写
    raise NotImplementedError


def t3_greet(name, greeting="你好"):
    """
    带默认参数的函数。
    返回字符串 f"{greeting}，{name}！"
    期望：t3_greet("单家炜") == "你好，单家炜！"
          t3_greet("单家炜", "Hello") == "Hello，单家炜！"
    """
    # TODO: 你来写
    raise NotImplementedError


def t4_format_rms(filename, rms):
    """
    用 f-string 返回："{filename} 的 RMS 是 {rms}"
    其中 rms 保留 4 位小数。
    期望：t4_format_rms("Lubricated-00h00m.mat", 0.0282098) == "Lubricated-00h00m.mat 的 RMS 是 0.0282"

    注意：0.0282098 保留 4 位小数是 0.0282（末尾的 0 会被省略吗？自己试）
    """
    # TODO: 你来写
    raise NotImplementedError


def t5_count_items(lst):
    """
    用 dict 统计列表中每个元素出现的次数，返回这个 dict。
    期望：t5_count_items(["a","b","a","c","a"]) == {"a": 3, "b": 1, "c": 1}
    """
    # TODO: 你来写
    raise NotImplementedError


# ===========================================================================
# B 组 · 常用工具
# ===========================================================================

def t6_enumerate(words):
    """
    用 enumerate 返回列表 ["0: apple", "1: banana", "2: cherry"]
    期望：t6_enumerate(["apple","banana","cherry"]) == ["0: apple", "1: banana", "2: cherry"]
    """
    # TODO: 你来写
    raise NotImplementedError


def t7_zip_sum(a, b):
    """
    用 zip 把两个列表逐元素相加，返回新列表。
    期望：t7_zip_sum([1,2,3], [10,20,30]) == [11, 22, 33]
    """
    # TODO: 你来写
    raise NotImplementedError


def t8_sort_by_score(records):
    """
    records 是 [{"name": "A", "score": 80}, ...]，
    按 score 从大到小排序并返回。
    期望：第一条的 score 最大
    """
    # TODO: 你来写（提示：sorted(..., key=lambda x: ..., reverse=True)）
    raise NotImplementedError


def t9_safe_int(s):
    """
    把字符串转成 int；转换失败时返回 None（用 try/except）。
    期望：t9_safe_int("123") == 123
          t9_safe_int("abc") is None
    """
    # TODO: 你来写
    raise NotImplementedError


def t10_read_lines(path):
    """
    用 with open(...) 读取文本文件，返回一个列表，每行去掉结尾换行符。
    如果文件不存在，返回空列表 []。
    """
    # TODO: 你来写
    raise NotImplementedError


# ===========================================================================
# C 组 · NumPy（最重要的一组）
# ===========================================================================

def t11_zeros_set_row():
    """
    创建形状 (3, 4) 的全零数组，把【第 2 行】（索引 1）全部设为 1，返回该数组。
    期望：a[1] == [1,1,1,1]，其余为 0
    """
    # TODO: 你来写
    raise NotImplementedError


def t12_broadcast_shape():
    """
    形状 (5,) 的数组 + 一个标量，结果的形状是什么？
    直接返回这个形状（tuple），例如 (5,)
    """
    # TODO: 你来写（不要真的去算，直接返回你判断的形状 tuple）
    raise NotImplementedError


def t13_axis_shapes():
    """
    对形状 (3, 4) 的数组：
      np.sum(a, axis=0) 的形状是什么？
      np.sum(a, axis=1) 的形状是什么？
    返回一个 tuple：(axis0的形状, axis1的形状)
    注意：这里返回的是【形状】，不是求和结果。
    """
    # TODO: 你来写
    raise NotImplementedError


def t14_boolean_index(a):
    """
    返回数组 a 中所有大于 0 的元素（用布尔索引，一行搞定）。
    期望：返回一维数组，只含正数
    """
    # TODO: 你来写
    raise NotImplementedError


def t15_reshape_neg1():
    """
    形状 (6,) 的数组调用 a.reshape(2, -1) 之后，形状是什么？
    返回这个形状 tuple。
    """
    # TODO: 你来写
    raise NotImplementedError


# ===========================================================================
# 测试框架（这部分不用改）
# ===========================================================================

PASS, FAIL, SKIP = "✓", "✗", "-"


def run(label, fn, validator):
    try:
        got = fn()
    except NotImplementedError:
        print(f"  {SKIP}  {label:<34} 没写")
        return 0
    except Exception as e:
        print(f"  {FAIL}  {label:<34} 报错：{type(e).__name__}: {e}")
        return 0
    try:
        ok, detail = validator(got)
    except Exception as e:
        print(f"  {FAIL}  {label:<34} 校验异常：{e}")
        return 0
    if ok:
        print(f"  {PASS}  {label:<34} {detail}")
        return 1
    print(f"  {FAIL}  {label:<34} {detail}")
    return 0


def main():
    total = 0

    print("\n" + "=" * 62)
    print("A 组 · Python 基础语法")
    print("=" * 62)

    total += run("1  列表推导式：偶数的平方", t1_even_squares,
                 lambda g: (isinstance(g, list) and len(g) == 50 and g[0] == 4 and g[-1] == 10000,
                            f"长度 {len(g) if hasattr(g,'__len__') else '?'}, 首 {g[0] if g else '?'}, 末 {g[-1] if g else '?'}"))
    total += run("2  手写 minmax（不用 max/min）", lambda: t2_minmax([3, 1, 4, 1, 5, 9, 2, 6]),
                 lambda g: (g == (1, 9), f"得到 {g}，期望 (1, 9)"))
    total += run("3  默认参数", lambda: (t3_greet("单家炜"), t3_greet("单家炜", "Hello")),
                 lambda g: (g == ("你好，单家炜！", "Hello，单家炜！"), f"得到 {g}"))
    total += run("4  f-string 保留 4 位小数", lambda: t4_format_rms("Lubricated-00h00m.mat", 0.0282098),
                 lambda g: (g == "Lubricated-00h00m.mat 的 RMS 是 0.0282", f"得到 {g!r}"))
    total += run("5  dict 统计词频", lambda: t5_count_items(["a", "b", "a", "c", "a"]),
                 lambda g: (g == {"a": 3, "b": 1, "c": 1}, f"得到 {g}"))

    print("\n" + "=" * 62)
    print("B 组 · 常用工具")
    print("=" * 62)

    total += run("6  enumerate", lambda: t6_enumerate(["apple", "banana", "cherry"]),
                 lambda g: (g == ["0: apple", "1: banana", "2: cherry"], f"得到 {g}"))
    total += run("7  zip 逐元素相加", lambda: t7_zip_sum([1, 2, 3], [10, 20, 30]),
                 lambda g: (list(g) == [11, 22, 33], f"得到 {g}"))
    total += run("8  sorted(key=) 降序", lambda: t8_sort_by_score(
        [{"name": "A", "score": 80}, {"name": "B", "score": 95}, {"name": "C", "score": 70}]),
        lambda g: (len(g) == 3 and g[0]["score"] == 95, f"第一条是 {g[0] if g else '?'}"))
    total += run("9  try/except 安全转换", lambda: (t9_safe_int("123"), t9_safe_int("abc")),
                 lambda g: (g == (123, None), f"得到 {g}"))

    import tempfile, os
    tf = os.path.join(tempfile.gettempdir(), "_selftest_t10.txt")
    with open(tf, "w", encoding="utf-8") as f:
        f.write("line1\nline2\nline3\n")
    total += run("10 with open 逐行读取", lambda: t10_read_lines(tf),
                 lambda g: (list(g) == ["line1", "line2", "line3"], f"得到 {g}"))
    total += run("10b 文件不存在返回 []", lambda: t10_read_lines("C:/no_such_file_xyz.txt"),
                 lambda g: (list(g) == [], f"得到 {g}"))

    print("\n" + "=" * 62)
    print("C 组 · NumPy（这组最重要）")
    print("=" * 62)

    total += run("11 zeros + 设置第 2 行", t11_zeros_set_row,
                 lambda g: (isinstance(g, np.ndarray) and g.shape == (3, 4)
                            and np.all(g[1] == 1) and np.all(g[[0, 2]] == 0), f"形状 {getattr(g,'shape',None)}"))
    total += run("12 标量广播后的形状", t12_broadcast_shape,
                 lambda g: (tuple(g) == (5,), f"得到 {g}，期望 (5,)"))
    total += run("13 axis 求和后的形状", t13_axis_shapes,
                 lambda g: (tuple(g) == ((4,), (3,)), f"得到 {g}，期望 ((4,), (3,))"))
    total += run("14 布尔索引取正数", lambda: t14_boolean_index(np.array([-2, 5, -1, 3, 0, 7])),
                 lambda g: (sorted(list(g)) == [3, 5, 7], f"得到 {g}"))
    total += run("15 reshape(-1) 的形状", t15_reshape_neg1,
                 lambda g: (tuple(g) == (2, 3), f"得到 {g}，期望 (2, 3)"))

    print("\n" + "=" * 62)
    print(f"  通过 {total} / 16")
    print("=" * 62)
    if total <= 10:
        print("  打不通的那几道，就是接下来 4 周的学习清单。")
        print("  见 notes/python_补漏计划.md")
    elif total <= 14:
        print("  基础还行，按计划走 4 周就能补上。")
    else:
        print("  你比自己以为的强。直接推进 PHM 项目，缺什么补什么。")
    print()


if __name__ == "__main__":
    main()

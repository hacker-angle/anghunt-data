# -*- coding: utf-8 -*-
"""自检：数据包里的 CSV 是否与报告里的数字一致。"""
import csv
import io
import os
import sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, "data")


def rows(name):
    with io.open(os.path.join(OUT, name), encoding="utf-8") as f:
        return list(csv.DictReader(f))


CHECKS = []


def chk(label, ok):
    CHECKS.append((label, bool(ok)))


x8 = rows("x8_enforce.csv")
chk("x8 有 5 行", len(x8) == 5)
chk("x8 第三轮 129,792", any(int(r["requests"]) == 129792 for r in x8))
chk("x8 off-1 外部 24", any(r["condition"] == "off" and int(r["foreign_names"]) == 24 for r in x8))
chk("x8 开启臂外部均为 0", all(int(r["foreign_names"]) == 0 for r in x8 if r["condition"] == "on"))

x2 = rows("x2_quota.csv")
chk("配额 315→60→255", any(int(r["attempts"]) == 315 and int(r["delivered"]) == 60
                          and int(r["refused_429"]) == 255 for r in x2))

cov = rows("covertness.csv")
chk("5,417 次请求", any(int(r["before"]) == 5417 for r in cov))
chk("4,576 自报家门", any(int(r["before"]) == 4576 and int(r["after"]) == 0 for r in cov))

x3 = rows("x3_damage.csv")
chk("破坏性 9/10", sum(int(r["match"]) for r in x3) == 9)

x5 = rows("x5_evidence.csv")
chk("证据门禁 8/8", sum(int(r["match"]) for r in x5) == 8)

x6 = rows("x6_coverage.csv")
d = {r["state"]: int(r["cells"]) for r in x6}
chk("覆盖 15/0/57/72", d.get("confirmed") == 15 and d.get("excluded") == 0
    and d.get("untested") == 57 and d.get("total") == 72)

rl = rows("resilience.csv")
chk("韧性实测 3 项", sum(1 for r in rl if r["status"] == "measured") == 3)

bad = [c for c in CHECKS if not c[1]]
for label, ok in CHECKS:
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
print("\n  结果: %s" % ("全部一致" if not bad else "不一致 %d 项" % len(bad)))
sys.exit(0 if not bad else 1)

# 数字索引

每个报告数字对应 `data/` 中的一行，`source` 列指出来自哪次运行。

| 章节 | 数字 | 数据文件 | 列 |
|---|---|---|---|
| 围栏 | 外部到达 24 → 0 | `data/x8_enforce.csv` | `foreign_names` |
| 围栏 | 容器到达 2 | `data/x8_enforce.csv` | `container_arrivals` |
| 围栏 | 拦截 73 次 | `data/x1_scope.csv` | `intercepted_out_of_scope_attempts` |
| 音量 | 129,792 次请求 | `data/x8_enforce.csv` | `requests`（run 3） |
| 音量 | 315 尝试 / 60 投递 / 255 拒绝 | `data/x2_quota.csv` | 同名三列 |
| 指纹 | 5,417 / 4,576 / 254 / 677 | `data/covertness.csv` | `before` |
| 指纹 | 改写后 0 | `data/covertness.csv` | `after` |
| 对比 | 各系统每轮请求量 | `data/x8_enforce.csv`、`data/x2_quota.csv` | 见 README |
| 门禁 | 1,004 判定 / 侦察零打断 | `data/x4_approval.csv` | `value` |
| 门禁 | 9/10 分级正确 | `data/x3_damage.csv` | `match` 求和 |
| 门禁 | 8/8 证据门禁 | `data/x5_evidence.csv` | `match` 求和 |
| 记账 | 72 格：15 / 0 / 57 | `data/x6_coverage.csv` | `cells` |
| 韧性 | 三项实测 | `data/resilience.csv` | `status = measured` |

未覆盖项：真实目标日志的完整副本不在本仓库（体积与脱敏原因），
`logs/access_sample.tsv` 是与之同构的合成样本。

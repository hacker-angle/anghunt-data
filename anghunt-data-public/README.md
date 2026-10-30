# anghunt-data

实验数据与自检脚本，用于核验一项关于自主红队智能体强制机制的研究中的数字。
本仓库**不含任何研究文稿、署名信息、凭据或真实主机名**。

## 内容

```
data/                       9 个 CSV，每行对应一次实验运行
  x1_scope.csv              范围强制：越界尝试与到达
  x2_quota.csv              按主机配额：尝试 / 投递 / 拒绝
  x3_damage.csv             破坏性动作分级 10 例
  x4_approval.csv           审批判定与人工打断次数
  x5_evidence.csv           证据门禁 8 例
  x6_coverage.csv           覆盖账本（三态）
  x8_enforce.csv            强制开/关六轮对照
  covertness.csv            目标侧指纹观测（归一化前/后）
  resilience.csv            失效模式与验证状态
logs/
  access_sample.tsv         目标访问日志样本（400 行，合成数据）
  audit_sample.jsonl        代理判定审计样本（200 条，合成数据）
scripts/
  check_numbers.py          自检：逐项比对 CSV 与研究报告中的数字
```

## 数据怎么来的

实验室环境：一台执行机（Linux）跑工具服务与按任务的网络命名空间，
一个 HTTP 靶场服务挂在单一地址之后并承载 20 个虚拟主机，
模型经公开 API 调用。**所有计数取自靶场自己的访问日志**，而不是被测系统的计数器。

表中 `source` 列标明该行来自哪次运行。

## 自检

```
python scripts/check_numbers.py
```

全部通过会输出 `全部一致`；任何一项不符会输出 `不一致 N 项` 并以非零码退出。

## 隐私说明

- 日志样本为**合成数据**：来源地址写作 `SRC_n`，主机名统一为 `target.lab.internal`；
- 仓库不含姓名、邮箱、机构、真实 IP、域名、凭据或任何文稿文件；
- `data/` 中的 CSV 只含计数与判定结果，不含任何目标内容。

## 许可

数据（`data/`、`logs/`）以 CC BY 4.0 发布；脚本（`scripts/`）以 MIT 发布。

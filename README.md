# Mathematical Modeling Judge Skill

面向 CUMCM、MCM/ICM 等数学建模竞赛的独立盲审 Codex Skill。它审查冻结后的题目、论文、代码、数据、结果文件和已核验规则，重点发现题意偏差、数学错误、不可行方案、数值矛盾、复现缺口和提交风险。

这是“裁判”而不是“共同作者”：默认只读提交包并输出审稿报告，不在评分过程中替作者修改论文。

## 核心机制

```text
冻结提交包并计算 SHA-256
          ↓
新上下文首轮盲审
          ↓
需求覆盖与操作化语义
          ↓
子问题依赖与方法适配
          ↓
结论—证据链与假设影响
          ↓
数学反例、数值复算与可复现性
          ↓
论文、附件、人工证据与合规检查
          ↓
冻结盲评分数和报告
          ↓
再进行历史优秀论文基准对照
          ↓
P0 / P1 / P2 修订与复审
```

首轮不得读取作者聊天、自评、修改计划、旧审稿结论或历史获奖论文答案。无法使用独立新上下文时，报告必须标记为 `same-context review` 并降低独立性置信度。

## 审查重点

- 把题面中的对象、量词、时间/空间粒度、集合运算和汇总方式写成可检验的数学语义。
- 检查后续子问题是否真正使用前面得到的变量、估计、状态或约束。
- 要求每个复杂方法说明任务、前提、简单基线、危险失效模式、验证和增量价值。
- 将关键假设追踪到受影响的公式、代码、结果和敏感性分析。
- 对每个关键表图追问“相对什么、变化多少、为什么重要、结论是什么”。
- 对登录模拟器、有限次正式测试、物理实验、未来结果等标记 `NOT_VERIFIED`，不凭叙述判定通过。

这些是内部质量控制，不冒充官方评分规则；文章、课程和历年论文是二级证据，当前题面与已核验规则优先。

## 审查模式

- **Fast gate**：快速检查漏题、错目标、不可行、数字冲突、附件和合规阻断项。
- **Full blind review**：完整审查、复算、评分和修订队列。
- **Adversarial audit**：针对一个关键模型或结论主动寻找反例。
- **Re-review**：按照旧问题清单检查新冻结版本，不悄悄改变评分标准。

## 目录

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── review-rubric.md
│   ├── report-schema.md
│   ├── method-fit-and-coherence.md
│   └── historical-lessons.md
├── scripts/build_review_manifest.py
└── tests/test_build_review_manifest.py
```

## 安装

Windows PowerShell：

```powershell
git clone https://github.com/111aaa327/math-modeling-judge-skill.git "$env:USERPROFILE\.codex\skills\math-modeling-judge"
```

安装后可显式调用：`$math-modeling-judge`。

## 冻结清单

```powershell
python scripts/build_review_manifest.py <frozen-packet> --out review_manifest.json --label "submission-v1"
```

清单不记录本机绝对目录，方便跨电脑复核并避免泄漏本地账户路径。

## 测试

```powershell
python -m unittest discover -s tests -v
```

## 与主竞赛 Skill 的关系

- [math-modeling-competition-skill](https://github.com/111aaa327/math-modeling-competition-skill) 负责审题、建模、实验、写作和提交准备。
- 本仓库只对冻结成果进行独立审查。
- 论文修改回到主任务完成，修改后生成新冻结包再交给本 Skill 复审。

## License

暂未指定开源许可证。公开仓库允许浏览；如需复制、修改或再分发，请先联系仓库所有者确认授权。

# Cathay Agent-Hermes

<p align="center">
  <a href="https://github.com/NousResearch/hermes-agent"><img src="https://img.shields.io/badge/Upstream-Hermes%20Agent-FFD700?style=for-the-badge" alt="Upstream"></a>
  <a href="https://github.com/luckyLo99/Cathay-Agent-Hermes/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.13-blue?style=for-the-badge" alt="Python">
</p>

**Cathay Agent-Hermes** 是基于 [Hermes Agent](https://github.com/NousResearch/hermes-agent) 的影子扩展（Shadow Extension）项目。它在不修改 Hermes 原生代码的前提下，通过 `hermes_ext/` 扩展层提供安全审计、影子记忆、人工评审、金丝雀回放等能力。

> **核心原则**: 只增加，不侵入。所有扩展位于 `hermes_ext/` 目录，Hermes 生命线文件零触碰。

---

## 架构概览

```text
hermes_ext/
├── runtime/            # 离线运行时骨架 + mock provider
├── schema/             # 可移植请求/响应 schema
├── hooks/              # 钩子契约 + 分发器 + 内置钩子
├── security/           # PreToolUse 安全守卫（路径/URL/命令）
├── cathay/             # Cathay 只读信号适配器
├── memoryx/            # 影子记忆层（SQLite shadow_ 前缀隔离）
├── orchestration/      # 影子编排 + 检查点回放
├── harness/            # 特性开关 + 集成诊断
├── adapter_scan/       # 只读 AST 扫描器（749 文件，1464 扩展点）
├── integration_spec/   # 零触碰集成规范矩阵
├── native_boundary/    # No-op 原生边界合约
├── golden_trace/       # 金丝雀回放包（确定性 hash 验证）
├── assembly/           # 影子组装清单 + 发布门
├── finalization/       # 最终稳定化 + 合并就绪证据包
├── human_review/       # 人工评审 + 合并决策门
└── common/             # 公共工具
```

---

## 快速安装

### 依赖要求

| 依赖 | 说明 |
|------|------|
| Python 3.11 / 3.12 / 3.13 | 核心运行时 |
| `pydantic` | hermes_ext 唯一外部依赖 |
| git | 版本管理 |
| 标准库 | 其余全部使用 Python 标准库 |

**hermes_ext 无任何网络调用、无额外系统依赖、纯 Python 实现。**

### Debian / Ubuntu

```bash
# 安装 Python 3.12
sudo apt update && sudo apt install -y python3.12 python3.12-venv python3-pip git

# 克隆仓库
git clone https://github.com/luckyLo99/Cathay-Agent-Hermes.git
cd Cathay-Agent-Hermes

# 创建虚拟环境
python3.12 -m venv .venv
source .venv/bin/activate

# 安装依赖（仅 pydantic）
pip install pydantic==2.13.4

# 验证安装
python -m py_compile hermes_ext/runtime/agent_doctor.py && echo "OK"
```

### Ubuntu 24.04+（Minimal）

```bash
# 如果 Python 3.12 未预装
sudo apt install -y python3.12 python3.12-venv git

git clone https://github.com/luckyLo99/Cathay-Agent-Hermes.git
cd Cathay-Agent-Hermes

python3.12 -m venv .venv
source .venv/bin/activate
pip install pydantic==2.13.4
```

### WSL2 (Windows Subsystem for Linux)

```bash
# 在 WSL2 终端中执行
sudo apt update && sudo apt install -y python3.12 python3.12-venv python3-pip git

git clone https://github.com/luckyLo99/Cathay-Agent-Hermes.git
cd Cathay-Agent-Hermes

python3.12 -m venv .venv
source .venv/bin/activate
pip install pydantic==2.13.4

# 验证
python -m pytest tests/hermes_ext -q
```

### 完整安装（含 Hermes 原生依赖）

如需运行完整的 Hermes Agent（含 CLI、Gateway、所有工具），请使用 uv：

```bash
# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 克隆并安装
git clone https://github.com/luckyLo99/Cathay-Agent-Hermes.git
cd Cathay-Agent-Hermes

uv venv .venv --python 3.12
source .venv/bin/activate
uv pip install -e ".[all,dev]"

# 启动 Hermes
hermes
```

---

## 验证

```bash
# 编译检查（7 个模块）
python -m py_compile hermes_ext/human_review/contracts.py
python -m py_compile hermes_ext/human_review/evidence_loader.py
python -m py_compile hermes_ext/human_review/dossier.py
python -m py_compile hermes_ext/human_review/decision_gate.py
python -m py_compile hermes_ext/human_review/experiment_proposal.py
python -m py_compile hermes_ext/human_review/report.py
python -m py_compile hermes_ext/human_review/cli.py

# 运行全部测试（279 tests）
python -m pytest tests/hermes_ext -q

# agent_doctor 诊断
python -m hermes_ext.runtime.agent_doctor --json --project-root .

# harness 诊断
python -m hermes_ext.harness.cli doctor --project-root . --state-dir .hermes_ext_shadow --json

# 生成 Phase 13 人工评审报告
python -m hermes_ext.human_review.cli --project-root . --output-dir reports/phase13 --json
```

---

## 模块说明

### Phase 1-2: 运行时骨架 + 安全守卫
- `runtime/` — 离线 agent_doctor、mock provider、可移植请求封装
- `schema/` — 严格 Pydantic schema（`extra="forbid"`）
- `hooks/` — 钩子契约、分发器、内置审计钩子
- `security/` — PreToolUse 安全策略（路径守卫、URL 守卫、命令守卫）

### Phase 3-4: 信号适配器 + 影子记忆
- `cathay/` — 只读 Cathay 信号适配器（禁止写入 Hermes 记忆）
- `memoryx/` — 影子记忆层，SQLite 表使用 `shadow_` 前缀隔离，HIGH PII 自动隔离

### Phase 5-6: 编排 + 特性开关
- `orchestration/` — 影子编排器、检查点存储、回放引擎、熔断器
- `harness/` — 特性开关（全部默认关闭）、kill switch 优先级、集成诊断

### Phase 7-8: 适配器扫描 + 集成规范
- `adapter_scan/` — 只读 AST 扫描器，分析 749 个文件，识别 1464 个扩展点
- `integration_spec/` — 零触碰集成规范矩阵，定义安全边界

### Phase 9-10: 原生边界 + 金丝雀回放
- `native_boundary/` — No-op 原生边界，永远不调用 Hermes 核心
- `golden_trace/` — 金丝雀回放包，5 个场景，确定性 hash 验证

### Phase 11-12: 组装 + 最终稳定化
- `assembly/` — 影子组装清单、不变式套件、发布门
- `finalization/` — 合并就绪证据包、文档打包、退出检查清单

### Phase 13: 人工评审
- `human_review/` — 人工评审档案、合并决策门、冷启动验证计划、原生实验提案

---

## 安全保证

| 保证项 | 实现方式 |
|--------|----------|
| 不修改 Hermes 生命线 | `hermes_ext/` 完全隔离，AST 扫描为只读 |
| 不调用真实 provider | 所有 provider 调用通过 mock 或 no-op 边界 |
| 不执行真实工具 | PreToolUse 守卫默认拦截 |
| 不写原生记忆 | memoryx 使用 `shadow_` 前缀隔离 |
| 特性开关默认关闭 | 所有 HERMES_EXT_* 标志默认 false |
| kill switch 优先 | kill_switch 覆盖所有其他标志 |
| 无网络调用 | memoryx 和 cathay 模块零网络请求 |

---

## 回滚

```bash
# 回到 Phase 13
git checkout phase13-human-review-merge-decision

# 回到 Phase 12
git reset --hard phase12-final-stabilization-merge-readiness

# 回到 Phase 11
git reset --hard phase11-shadow-assembly-manifest
```

---

## 许可

MIT — 基于 [Hermes Agent](https://github.com/NousResearch/hermes-agent) by [Nous Research](https://nousresearch.com)。
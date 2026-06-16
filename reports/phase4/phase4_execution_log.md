# Phase 4 执行日志

> 时间: 2026-06-16
> 分支: refactor/hermes-cathay-fusion-stage0

## 1. 目标

Phase 4 创建 memoryx Provider Adapter 只读影子记忆层。

本阶段只允许写入隔离的 shadow memory SQLite 数据库，不接入 Hermes 原生 memory，不写 skills，不调用模型，不执行工具。

## 2. 新增目录

- hermes_ext/memoryx/
- reports/phase4/

## 3. 新增源文件

| 文件 | 内容 |
|------|------|
| hermes_ext/memoryx/__init__.py | memoryx shadow layer 导出 |
| hermes_ext/memoryx/contracts.py | ShadowMemoryNode / Edge / Query / RecallResult |
| hermes_ext/memoryx/pii.py | PII 检测与脱敏 |
| hermes_ext/memoryx/dag.py | 影子记忆 DAG 验证 |
| hermes_ext/memoryx/provider.py | 隔离 SQLite shadow memory provider |
| hermes_ext/memoryx/recall.py | Recall facade |
| hermes_ext/memoryx/promotion.py | 只标记候选，不写 Hermes memory |
| hermes_ext/memoryx/fusion.py | Cathay bundle / Envelope metadata → shadow nodes |

## 4. 新增测试

| 文件 | 覆盖 |
|------|------|
| test_memoryx_contracts.py | strict DTO / high PII quarantine / edge validation |
| test_memoryx_pii.py | API key / email / redaction |
| test_memoryx_dag.py | DAG acyclic / missing node / cycle |
| test_memoryx_provider.py | SQLite write/get/count/recall/quarantine |
| test_memoryx_recall.py | Recall service |
| test_memoryx_promotion.py | Promotion eligibility only |
| test_memoryx_fusion.py | Cathay bundle → shadow nodes |
| test_memoryx_no_imports.py | 禁止 import memoryx / cathay_agent |

## 5. 验证结果

- py_compile: 7/7 通过
- pytest: 108/108 通过 (Phase 1: 21 + Phase 2: 34 + Phase 3: 27 + Phase 4: 26)
- agent_doctor: ok=true (git_status WARN 预期内)
- cli.py --help: 通过
- hermes doctor: 通过
- git status --short: 仅 hermes_ext/memoryx/、test_memoryx_*.py

## 6. 生命线文件

未触碰：
- cli.py
- run_agent.py
- hermes_cli/main.py
- gateway/run.py
- tools/registry.py
- model_tools.py
- toolsets.py
- agent/memory_provider.py
- agent/memory_manager.py
- tools/memory_tool.py
- agent/system_prompt.py
- agent/prompt_builder.py
- agent/context_compressor.py
- hermes_state.py
- providers/__init__.py
- providers/base.py
- tools/threat_patterns.py
- agent/redact.py
- cron/jobs.py
- cron/scheduler.py
- gateway/platforms/base.py
- gateway/session.py
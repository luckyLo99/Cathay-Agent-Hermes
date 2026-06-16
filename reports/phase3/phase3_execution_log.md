# Phase 3 执行日志

> 时间: 2026-06-16
> 分支: refactor/hermes-cathay-fusion-stage0

## 1. 目标

Phase 3 创建 Cathay Contract Adapter 只读旁路接入层。

本阶段只允许把 Cathay 风格 payload 和当前 turn observation 标准化为只读 advisory signals，不接入 Hermes 主循环，不写 memory，不写 skills，不执行工具，不调用模型。

## 2. 新增目录

- hermes_ext/cathay/
- reports/phase3/

## 3. 新增源文件

| 文件 | 内容 |
|------|------|
| hermes_ext/cathay/__init__.py | Cathay adapter 导出 |
| hermes_ext/cathay/contracts.py | CathayAdapterInput / SignalBundle / Safety/Profile/Learning/Proactive DTO |
| hermes_ext/cathay/adapter.py | CathayContractAdapter 总入口 |
| hermes_ext/cathay/safety_bridge.py | Safety 信号提取 |
| hermes_ext/cathay/profile_bridge.py | Profile hypothesis 只读提取 |
| hermes_ext/cathay/learning_bridge.py | Learning signal 只读提取 |
| hermes_ext/cathay/proactive_bridge.py | Non-notifying proactive suggestion |
| hermes_ext/cathay/signal_fusion.py | Envelope metadata 融合 |

## 4. 新增测试

| 文件 | 覆盖 |
|------|------|
| test_cathay_contracts.py | DTO strict/extra、敏感画像、主动通知禁止 |
| test_cathay_safety_bridge.py | prompt injection / crisis / raw safety |
| test_cathay_profile_bridge.py | profile hypothesis / secret forbidden |
| test_cathay_learning_bridge.py | learning signal |
| test_cathay_proactive_bridge.py | non-notifying proactive suggestion |
| test_cathay_signal_fusion.py | metadata-only fusion |
| test_cathay_adapter.py | adapter observe_only/off/review |
| test_cathay_no_imports.py | 禁止 import Cathay-Agent / memoryx |

## 5. 验证结果

- py_compile: 7/7 通过
- pytest: 82/82 通过 (Phase 1: 21 + Phase 2: 34 + Phase 3: 27)
- agent_doctor: ok=true (git_status WARN 预期内)
- cli.py --help: 通过
- hermes doctor: 通过
- git diff --stat: 空 (仅有新增文件)
- git status --short: 仅 hermes_ext/cathay/、test_cathay_*.py

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
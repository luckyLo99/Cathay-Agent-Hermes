# Phase 11 退出检查清单

> 时间: 2026-06-16
> 分支: refactor/hermes-cathay-fusion-stage0

## 代码边界

- [x] 只新增 hermes_ext/assembly/
- [x] 只新增 tests/hermes_ext/test_assembly_*.py
- [x] 只新增 reports/phase11/
- [x] 未修改 Hermes 生命线文件
- [x] 未修改 Hermes CLI 入口
- [x] 未修改 pyproject.toml
- [x] 未修改 lock 文件
- [x] 未安装新依赖

## Assembly 保证

- [x] 未 import Hermes core loop
- [x] 未 import hermes_cli
- [x] 未 import gateway
- [x] 未 import tools.registry
- [x] 未 import model_tools
- [x] 未 import providers
- [x] 未 import agent.memory_provider
- [x] 未 import hermes_state
- [x] 未 import dotenv
- [x] 未 import model SDK
- [x] 未执行 Hermes runtime
- [x] 未调用真实模型
- [x] 未调用真实 provider
- [x] 未执行真实工具
- [x] 未读取 .env
- [x] 未读取 API key/token
- [x] 未写 Hermes native memory
- [x] 未写 Hermes skills
- [x] 未修改 state db
- [x] 未生成 patch

## Invariant 保证

- [x] assembly.artifacts_exist PASS
- [x] assembly.no_lifeline_source_artifacts PASS
- [x] assembly.feature_flags_default_disabled PASS
- [x] assembly.no_forbidden_imports PASS
- [x] assembly.phase10_golden_trace_stable PASS
- [x] assembly.phase9_native_boundary_no_side_effects PASS
- [x] release_gate ok=true

## 产物

- [x] reports/phase11/shadow_assembly_manifest.md 已生成
- [x] reports/phase11/shadow_assembly_manifest.json 已生成
- [x] reports/phase11/release_gate_report.md 已生成
- [x] reports/phase11/release_gate_report.json 已生成

## 测试

- [x] py_compile 全部通过 (7/7)
- [x] tests/hermes_ext 全部通过 (241/241)
- [x] agent_doctor 可运行 (ok=true)
- [x] harness doctor 可运行 (ok=true)
- [x] assembly CLI 可运行 (exit_code=0)
- [x] cli.py --help 仍通过
- [x] hermes doctor 仍通过

## Git

- [x] git diff --stat 已记录 (0 lifeline files)
- [x] git status --short 已记录
- [x] diff 不包含生命线文件
- [x] rollback 命令已记录

## 结论

- [x] Phase 11 可以提交
- [x] 可以进入 Phase 12：Final Stabilization / Documentation Pack / Merge Readiness
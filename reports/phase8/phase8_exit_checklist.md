# Phase 8 退出检查清单

> 时间: 2026-06-16
> 分支: refactor/hermes-cathay-fusion-stage0

## 代码边界

- [x] 只新增 hermes_ext/integration_spec/
- [x] 只新增 tests/hermes_ext/test_integration_spec_*.py
- [x] 只新增 reports/phase8/
- [x] 未修改 Hermes 生命线文件
- [x] 未修改 Hermes CLI 入口
- [x] 未修改 pyproject.toml
- [x] 未修改 lock 文件
- [x] 未安装新依赖

## 零触碰保证

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
- [x] 未执行真实工具
- [x] 未读取 .env
- [x] 未读取 API key/token
- [x] 未写 Hermes native memory
- [x] 未写 Hermes skills
- [x] 未生成 patch

## Design Matrix 保证

- [x] 读取 reports/phase7/hermes_adapter_scan.json
- [x] 生成 reports/phase8/zero_touch_integration_spec.md
- [x] 生成 reports/phase8/zero_touch_integration_spec.json
- [x] forbidden candidates 保持 forbidden (344)
- [x] forbidden candidates 状态为 blocked (344)
- [x] wrapper_only candidates 转为 external_wrapper (355) 或 sidecar_observer (420)
- [x] feature_flag_required candidates 转为 feature_flag_shadow (345)
- [x] tool-related entries 要求 HERMES_EXT_PRETOOL_GUARD
- [x] memory-related entries 要求 HERMES_EXT_MEMORYX
- [x] 所有未来工作只允许进入 phase9_shadow_adapter_contract_only

## 测试

- [x] py_compile 全部通过 (6/6)
- [x] tests/hermes_ext 全部通过 (187/187)
- [x] agent_doctor 可运行 (ok=true)
- [x] harness doctor 可运行 (ok=true)
- [x] integration_spec CLI 可运行
- [x] cli.py --help 仍通过
- [x] hermes doctor 仍通过

## Git

- [x] git diff --stat 已记录 (0 modifications)
- [x] git status --short 已记录 (only new files)
- [x] diff 不包含生命线文件
- [x] rollback 命令已记录: `git reset --hard phase7-readonly-adapter-scan`

## 结论

- [x] Phase 8 可以提交
- [x] 可以进入 Phase 9：Shadow Adapter Contract Tests / No-op Native Boundary
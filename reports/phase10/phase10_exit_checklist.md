# Phase 10 退出检查清单

> 时间: 2026-06-16
> 分支: refactor/hermes-cathay-fusion-stage0

## 代码边界

- [x] 只新增 hermes_ext/golden_trace/
- [x] 只新增 tests/hermes_ext/test_golden_trace_*.py
- [x] 只新增 reports/phase10/
- [x] 未修改 Hermes 生命线文件
- [x] 未修改 Hermes CLI 入口
- [x] 未修改 pyproject.toml
- [x] 未修改 lock 文件
- [x] 未安装新依赖

## Golden Trace 保证

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

## Replay 稳定性

- [x] repeat=2 所有 case hash 稳定
- [x] diagnostic-default-off: 2 iterations, 1 unique hash
- [x] shadow-basic-all-enabled: 2 iterations, 1 unique hash
- [x] shadow-dangerous-tool-blocked: 2 iterations, 1 unique hash
- [x] shadow-minimal-no-cathay-no-memory: 2 iterations, 1 unique hash
- [x] native-boundary-spec-noop: 2 iterations, 1 unique hash
- [x] 0 violations

## 跨阶段串联

- [x] Phase 1: agent_doctor 仍 ok
- [x] Phase 2: PreToolGuard 在 shadow-dangerous-tool-blocked 中验证
- [x] Phase 3: cathay 假体在 shadow-basic-all-enabled 中串联
- [x] Phase 4: shadow memory 在 shadow-basic-all-enabled 中串联
- [x] Phase 5: checkpoint replay 在 shadow-basic-all-enabled 中串联
- [x] Phase 6: integration harness 是 golden trace runner 的底层
- [x] Phase 9: native boundary 在 native-boundary-spec-noop 中串联

## 测试

- [x] py_compile 全部通过 (7/7)
- [x] tests/hermes_ext 全部通过 (223/223)
- [x] agent_doctor 可运行 (ok=true)
- [x] harness doctor 可运行 (ok=true)
- [x] golden_trace CLI 可运行
- [x] cli.py --help 仍通过
- [x] hermes doctor 仍通过

## Git

- [x] git diff --stat 已记录 (0 modifications)
- [x] git status --short 已记录 (only new files)
- [x] diff 不包含生命线文件
- [x] rollback 命令已记录: `git reset --hard phase9-noop-native-boundary-contracts`

## 结论

- [x] Phase 10 可以提交
- [x] 可以进入 Phase 11：End-to-end Shadow Assembly / Assembly Manifest
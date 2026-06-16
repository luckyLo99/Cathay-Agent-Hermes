# Phase 5 退出检查清单

> 时间: 2026-06-16
> 分支: refactor/hermes-cathay-fusion-stage0

## 代码边界

- [x] 只新增 hermes_ext/orchestration/
- [x] 只新增 tests/hermes_ext/test_orchestration_*.py
- [x] 只新增 tests/hermes_ext/test_checkpoint_store.py
- [x] 只新增 tests/hermes_ext/test_shadow_runner.py
- [x] 只新增 tests/hermes_ext/test_replay.py
- [x] 只新增 tests/hermes_ext/test_circuit_breaker.py
- [x] 只新增 tests/hermes_ext/test_span_log.py
- [x] 只新增 reports/phase5/
- [x] 未修改 Hermes 生命线文件
- [x] 未修改 pyproject.toml
- [x] 未修改 lock 文件
- [x] 未安装新依赖

## 影子编排保证

- [x] 未 import Hermes core loop
- [x] 未 import langgraph
- [x] 未 import opentelemetry
- [x] 未 import memoryx
- [x] 未 import cathay_agent
- [x] 未调用真实模型
- [x] 未执行真实工具
- [x] 未读取 .env
- [x] 未读取 API key/token
- [x] 未写 Hermes native memory
- [x] 未写 Hermes skills
- [x] 未触发 proactive 通知
- [x] Checkpoint DB 由调用方指定路径，测试使用 tmp_path
- [x] Checkpoint 表名均为 shadow_ / idx_shadow_ 前缀

## 安全保证

- [x] Dangerous tool intent 可被 PreToolGuard 阻断
- [x] Circuit breaker 可阻断重复失败
- [x] Replay 只读 checkpoint，不重放真实工具/模型
- [x] ShadowRunner 支持 disable_cathay
- [x] ShadowRunner 支持 disable_shadow_memory

## 测试

- [x] py_compile 全部通过 (7/7)
- [x] tests/hermes_ext 全部通过 (128/128)
- [x] agent_doctor 可运行 (ok=true)
- [x] cli.py --help 仍通过
- [x] hermes doctor 仍通过

## Git

- [x] git status --short 已记录
- [x] diff 不包含生命线文件
- [x] rollback: `git reset --hard phase4-memoryx-shadow-provider`

## 结论

- [x] Phase 5 可以提交
- [x] 可以进入 Phase 6：Feature Flag Integration Harness
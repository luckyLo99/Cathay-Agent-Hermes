# Phase 4 退出检查清单

> 时间: 2026-06-16
> 分支: refactor/hermes-cathay-fusion-stage0

## 代码边界

- [x] 只新增 hermes_ext/memoryx/
- [x] 只新增 tests/hermes_ext/test_memoryx_*.py
- [x] 只新增 reports/phase4/
- [x] 未修改 Hermes 生命线文件
- [x] 未修改 agent/memory_provider.py
- [x] 未修改 agent/memory_manager.py
- [x] 未修改 hermes_state.py
- [x] 未修改 tools/memory_tool.py
- [x] 未修改 pyproject.toml
- [x] 未修改 lock 文件
- [x] 未安装新依赖

## 影子记忆保证

- [x] 未 import memoryx
- [x] 未 import cathay_agent
- [x] 未执行 memoryx runtime
- [x] 未调用真实模型
- [x] 未读取 .env
- [x] 未读取 API key/token
- [x] 未写 Hermes native memory
- [x] 未写 Hermes skills
- [x] 未触发 proactive 通知
- [x] 未执行工具
- [x] SQLite 表名均以 shadow_ 开头
- [x] shadow database 由调用方指定路径，测试使用 tmp_path

## 安全保证

- [x] HIGH PII 自动 quarantined
- [x] Recall 默认排除 quarantined
- [x] Promotion 不处理 MEDIUM/HIGH PII
- [x] Promotion 只标记 candidate，不写 Hermes memory
- [x] Envelope metadata 只作为 shadow node

## 测试

- [x] py_compile 全部通过 (7/7)
- [x] tests/hermes_ext 全部通过 (108/108)
- [x] agent_doctor 可运行 (ok=true)
- [x] cli.py --help 仍通过
- [x] hermes doctor 仍通过

## Git

- [x] git status --short 已记录
- [x] diff 不包含生命线文件
- [x] rollback: `git reset --hard phase3-cathay-readonly-adapter`

## 结论

- [x] Phase 4 可以提交
- [x] 可以进入 Phase 5：Shadow Orchestration 与 Checkpoint Replay
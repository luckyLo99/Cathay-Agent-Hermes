# Phase 6 退出检查清单

> 时间: 2026-06-16
> 分支: refactor/hermes-cathay-fusion-stage0

## 代码边界

- [x] 只新增 hermes_ext/harness/
- [x] 只新增 tests/hermes_ext/test_harness_*.py
- [x] 只新增 tests/hermes_ext/test_feature_flags.py
- [x] 只新增 reports/phase6/
- [x] 未修改 Hermes 生命线文件
- [x] 未修改 Hermes CLI 入口
- [x] 未修改 pyproject.toml
- [x] 未修改 lock 文件
- [x] 未安装新依赖

## Feature Flag 保证

- [x] 默认全部关闭
- [x] HERMES_EXT_ENABLED=false 时功能全部关闭
- [x] HERMES_EXT_KILL_SWITCH=true 时功能全部关闭
- [x] diagnostics 可独立运行
- [x] shadow_runner 必须显式启用
- [x] cathay 必须显式启用
- [x] memoryx 必须显式启用
- [x] checkpoint_replay 必须显式启用
- [x] pretool_guard 必须显式启用

## Harness 安全保证

- [x] 未 import Hermes core loop
- [x] 未 import openfeature
- [x] 未 import pydantic_settings
- [x] 未 import dotenv
- [x] 未 import memoryx
- [x] 未 import cathay_agent
- [x] 未调用真实模型
- [x] 未执行真实工具
- [x] 未读取 .env
- [x] 未读取 API key/token
- [x] 未写 Hermes native memory
- [x] 未写 Hermes skills
- [x] state_dir 由调用方显式指定

## 测试

- [x] py_compile 全部通过 (5/5)
- [x] tests/hermes_ext 全部通过 (149/149)
- [x] agent_doctor 可运行 (ok=true)
- [x] harness doctor 可运行 (ok=true, all flags default false)
- [x] cli.py --help 仍通过

## Git

- [x] git diff --stat 已记录（空）
- [x] git status --short 已记录（仅 untracked Phase 6 文件）
- [x] diff 不包含生命线文件
- [x] rollback: `git reset --hard phase5-shadow-orchestration-replay`

## 结论

- [x] Phase 6 可以提交
- [x] 可以进入 Phase 7：Read-only Hermes Adapter Scan / Extension Point Mapping
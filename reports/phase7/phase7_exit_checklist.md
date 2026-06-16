# Phase 7 退出检查清单

> 时间: 2026-06-16
> 分支: refactor/hermes-cathay-fusion-stage0

## 代码边界

- [x] 只新增 hermes_ext/adapter_scan/
- [x] 只新增 tests/hermes_ext/test_adapter_scan_*.py
- [x] 只新增 reports/phase7/
- [x] 未修改 Hermes 生命线文件
- [x] 未修改 Hermes CLI 入口
- [x] 未修改 pyproject.toml
- [x] 未修改 lock 文件
- [x] 未安装新依赖

## 只读扫描保证

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

## Adapter Map 保证

- [x] 生成 reports/phase7/hermes_adapter_scan.md
- [x] 生成 reports/phase7/hermes_adapter_scan.json
- [x] lifeline files 标记为 forbidden
- [x] provider-like symbols 已分类
- [x] memory-like symbols 已分类
- [x] tool/registry-like symbols 已分类
- [x] gateway/session-like symbols 已分类
- [x] 所有候选只作为 future adapter hint，不生成 patch

## 测试

- [x] py_compile 全部通过 (7/7)
- [x] tests/hermes_ext 全部通过 (169/169)
- [x] agent_doctor 可运行 (ok=true)
- [x] harness doctor 可运行 (ok=true)
- [x] adapter_scan CLI 可运行
- [x] cli.py --help 仍通过
- [x] hermes doctor 仍通过

## Git

- [x] git diff --stat 已记录 (0 modifications)
- [x] git status --short 已记录 (only new files)
- [x] diff 不包含生命线文件
- [x] rollback 命令已记录: `git reset --hard phase6-feature-flag-harness`

## 结论

- [x] Phase 7 可以提交
- [x] 可以进入 Phase 8：Adapter Design Matrix / Zero-touch Integration Spec
# Phase 3 退出检查清单

> 时间: 2026-06-16
> 分支: refactor/hermes-cathay-fusion-stage0

## 代码边界

- [x] 只新增 hermes_ext/cathay/
- [x] 只新增 tests/hermes_ext/test_cathay_*.py
- [x] 只新增 reports/phase3/
- [x] 未修改 Hermes 生命线文件
- [x] 未修改 pyproject.toml
- [x] 未修改 lock 文件
- [x] 未安装新依赖

## 只读保证

- [x] 未 import cathay_agent
- [x] 未 import memoryx
- [x] 未执行 Cathay runtime
- [x] 未调用真实模型
- [x] 未读取 .env
- [x] 未读取 API key/token
- [x] 未写 Hermes memory
- [x] 未写 Hermes skills
- [x] 未触发 proactive 通知
- [x] 未执行工具
- [x] SignalFusion 只写 envelope.metadata

## 安全保证

- [x] Prompt injection 生成 requires_review safety signal
- [x] Crisis 表达生成 critical + requires_review signal
- [x] Sensitive profile write_permission=forbidden
- [x] Memory/skill 写入只生成 requires_review 信号
- [x] Proactive suggestion allowed_to_notify=False

## 测试

- [x] py_compile 全部通过 (7/7)
- [x] tests/hermes_ext 全部通过 (82/82)
- [x] agent_doctor 可运行 (ok=true)
- [x] cli.py --help 仍通过
- [x] hermes doctor 仍通过

## Git

- [x] git diff --stat 已记录 (空)
- [x] git status --short 已记录
- [x] diff 不包含生命线文件
- [x] rollback: `git reset --hard phase2-hook-pretool-policy`

## 结论

- [x] Phase 3 可以提交
- [x] 可以进入 Phase 4：memoryx Provider Adapter 只读影子记忆层
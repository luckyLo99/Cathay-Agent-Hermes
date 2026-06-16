# Phase 2 测试结果

> 时间: 2026-06-16

## 测试汇总

| 指标 | 值 |
|------|-----|
| Phase 1 测试 | 21 |
| Phase 2 新增测试 | 34 |
| 总通过 | 55 |
| 失败 | 0 |
| 跳过 | 0 |
| 耗时 | ~1.6s |

## 关键验证

- [x] HookEvent strict + extra forbid
- [x] HookDispatcher 决策优先级 DENY > ASK > WARN > ALLOW > NOOP
- [x] PathGuard 拒绝 workspace escape
- [x] PathGuard 拒绝 .env / .ssh / 私钥
- [x] URLGuard 拒绝 file:// / localhost / private IP
- [x] CommandGuard 拒绝 rm -rf /
- [x] CommandGuard 对 shell metacharacter 要求 approval
- [x] ExecPolicy 允许 git status / git diff
- [x] ExecPolicy 拒绝 git push --force
- [x] PreToolGuard 聚合 schema + path + url + command + exec policy
- [x] 默认 dispatcher 可运行 PreToolUse Guard

## 回归验证

- [x] cli.py --help 通过
- [x] hermes doctor 通过
- [x] agent_doctor 通过 (ok=true)
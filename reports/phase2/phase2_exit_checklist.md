# Phase 2 退出检查清单

> 时间: 2026-06-16
> 分支: refactor/hermes-cathay-fusion-stage0

## 代码边界

- [x] 只新增 hermes_ext/hooks/
- [x] 只新增 hermes_ext/security/
- [x] 只新增 tests/hermes_ext/test_* Phase 2 测试
- [x] 只新增 reports/phase2/
- [x] 未修改 Hermes 生命线文件
- [x] 未修改 pyproject.toml
- [x] 未修改 lock 文件
- [x] 未安装新依赖

## 运行时安全

- [x] HookDispatcher 不执行外部命令
- [x] PreToolGuard 不执行真实工具
- [x] PathGuard 不写文件
- [x] URLGuard 不发网络请求
- [x] CommandGuard 不执行命令
- [x] ExecPolicy 只做匹配判断
- [x] unknown tool 默认 ask
- [x] unknown command 默认 ask
- [x] rm -rf / 默认 deny
- [x] git push --force 默认 deny
- [x] memory_write 默认 ask

## 测试

- [x] py_compile 全部通过 (9/9)
- [x] tests/hermes_ext 全部通过 (55/55)
- [x] agent_doctor 可运行 (ok=true)
- [x] cli.py --help 仍通过
- [x] hermes doctor 仍通过

## Git

- [x] git diff --stat 已记录
- [x] git status --short 已记录
- [x] diff 不包含生命线文件
- [x] rollback 命令已记录

## 结论

- [x] Phase 2 可以提交
- [x] 可以进入 Phase 3：Cathay Contract Adapter 只读旁路接入
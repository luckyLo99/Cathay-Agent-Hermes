# Phase 2 执行日志

> 时间: 2026-06-16
> 分支: refactor/hermes-cathay-fusion-stage0

## 1. 目标

Phase 2 创建 Hook 总线、PreToolUse Guard 与 ExecPolicy。

本阶段只新增扩展层代码，不接入 Hermes 主干，不执行真实工具，不调用真实模型。

## 2. 新增目录

- hermes_ext/hooks/
- hermes_ext/security/
- reports/phase2/

## 3. 新增源文件

| 文件 | 内容 |
|------|------|
| hermes_ext/hooks/__init__.py | Hook 总线导出 |
| hermes_ext/hooks/contracts.py | HookEvent / HookDecision / HookResult |
| hermes_ext/hooks/dispatcher.py | 确定性 HookDispatcher |
| hermes_ext/hooks/builtin_hooks.py | 默认 PreToolGuardHook |
| hermes_ext/security/__init__.py | Security 导出 |
| hermes_ext/security/decisions.py | SecurityDecision |
| hermes_ext/security/path_guard.py | 工作区路径边界 |
| hermes_ext/security/url_guard.py | URL scheme/host/IP 防护 |
| hermes_ext/security/command_guard.py | 命令形状与危险模式检查 |
| hermes_ext/security/exec_policy.py | prefix-rule ExecPolicy |
| hermes_ext/security/pretool_guard.py | PreToolUse 统一安全门 |

## 4. 新增测试

| 文件 | 覆盖 |
|------|------|
| test_hooks_contracts.py | Hook 契约 strict/extra |
| test_hook_dispatcher.py | 决策优先级与 payload update |
| test_path_guard.py | workspace escape / sensitive path |
| test_url_guard.py | https/http/file/localhost/private IP |
| test_command_guard.py | rm -rf /、shell meta、pip、null byte |
| test_exec_policy.py | allow/ask/deny prefix rule |
| test_pretool_guard.py | bash/write/read/url/memory/unknown tool |

## 5. 验证结果

- py_compile: 9/9 通过
- pytest: 55/55 通过
- agent_doctor: ok=true (git_status WARN 预期内)
- cli.py --help: 通过
- hermes doctor: 通过
- git diff --stat: 仅新增文件
- git status --short: 仅 hermes_ext/ 和 tests/hermes_ext/

## 6. 生命线文件

未触碰：
- cli.py
- run_agent.py
- tools/registry.py
- model_tools.py
- toolsets.py
- agent/memory_provider.py
- agent/memory_manager.py
- agent/system_prompt.py
- agent/prompt_builder.py
- agent/context_compressor.py
- hermes_state.py
- providers/__init__.py
- providers/base.py
- tools/threat_patterns.py
- agent/redact.py
- cron/jobs.py
- cron/scheduler.py
- gateway/run.py
- gateway/platforms/base.py
- gateway/session.py
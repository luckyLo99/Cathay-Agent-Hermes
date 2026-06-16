# Phase 5 测试结果

> 时间: 2026-06-16

## 测试汇总

| 指标 | 值 |
|------|-----|
| Phase 1 测试 | 21 |
| Phase 2 测试 | 34 |
| Phase 3 测试 | 27 |
| Phase 4 测试 | 26 |
| Phase 5 新增测试 | 20 |
| 总通过 | 128 |
| 失败 | 0 |
| 跳过 | 0 |
| 耗时 | ~3.96s |

## 关键验证

- [x] ShadowRunConfig strict + extra forbid
- [x] Checkpoint hash 稳定
- [x] CheckpointStore 只创建 shadow_ / idx_shadow_ 表
- [x] CheckpointStore write/get/list/latest 可用
- [x] CircuitBreaker 超阈值打开
- [x] SpanLog 可记录 audit spans
- [x] ShadowRunner 可完成完整影子链路
- [x] ShadowRunner 可被 PreToolGuard 阻断危险工具意图
- [x] ShadowRunner 可禁用 Cathay 和 shadow memory
- [x] ReplayService 可读取完整 run checkpoints
- [x] ReplayService 可从 checkpoint 返回 tail
- [x] ShadowRunReporter 可生成 Markdown report
- [x] 禁止 import Hermes core / langgraph / opentelemetry / memoryx / cathay_agent

## 回归验证

- [x] Phase 1 测试仍通过
- [x] Phase 2 测试仍通过
- [x] Phase 3 测试仍通过
- [x] Phase 4 测试仍通过
- [x] cli.py --help 通过
- [x] hermes doctor 通过
- [x] agent_doctor 通过 (ok=true)
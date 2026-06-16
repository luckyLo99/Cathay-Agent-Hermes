# Phase 8 测试结果

> 时间: 2026-06-16

## 测试汇总

| 指标 | 值 |
|------|-----|
| Phase 1 测试 | 21 |
| Phase 2 测试 | 34 |
| Phase 3 测试 | 27 |
| Phase 4 测试 | 26 |
| Phase 5 测试 | 20 |
| Phase 6 测试 | 21 |
| Phase 7 测试 | 20 |
| Phase 8 新增测试 | 18 |
| 总通过 | 187 |
| 失败 | 0 |
| 跳过 | 0 |
| 耗时 | 5.77s |

## 关键验证

- [x] IntegrationSpecConfig strict + extra forbid
- [x] forbidden source posture 不可降级
- [x] DesignMatrixEntry stable id 稳定
- [x] FORBIDDEN → IntegrationMode.FORBIDDEN
- [x] WRAPPER_ONLY gateway/cron → SIDE_CAR_OBSERVER
- [x] WRAPPER_ONLY provider/memory → EXTERNAL_WRAPPER
- [x] FEATURE_FLAG_REQUIRED → FEATURE_FLAG_SHADOW
- [x] TOOL_REGISTRY / TOOL_ORCHESTRATION 必须要求 PreToolGuard flag
- [x] MEMORY 必须要求 MEMORYX flag
- [x] MatrixBuilder 生成 surface plans
- [x] SpecBuilder 可消费 reports/phase7/hermes_adapter_scan.json
- [x] Reporter 可生成 markdown/json
- [x] CLI 可写 reports/phase8 输出
- [x] 禁止 import Hermes core / providers / tools / dotenv / model SDK

## 回归验证

- [x] Phase 1 测试仍通过
- [x] Phase 2 测试仍通过
- [x] Phase 3 测试仍通过
- [x] Phase 4 测试仍通过
- [x] Phase 5 测试仍通过
- [x] Phase 6 测试仍通过
- [x] Phase 7 测试仍通过
- [x] cli.py --help 通过
- [x] hermes doctor 通过
- [x] agent_doctor 通过
- [x] harness doctor 通过
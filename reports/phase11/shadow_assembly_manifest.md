# Shadow Assembly Manifest

- manifest_id: `2eef7b3d-b1ec-452a-b350-7691ce62b7f8`
- phase: `11`
- manifest_hash: `da522fc95449850a4efca58a94f0ac5dfdecdf091377d960913503d6c94a553f`
- project_root: `D:\projects\hermes-agent-main`
- created_at: `2026-06-16T08:37:14.787444+00:00`

## Summary

| Metric | Value |
|---|---:|
| source_artifacts | 88 |
| test_artifacts | 79 |
| report_artifacts | 35 |
| total_artifacts | 202 |
| invariants_passed | 6 |
| invariants_warned | 0 |
| invariants_failed | 0 |

## Invariants

| ID | Status | Severity | Message |
|---|---|---|---|
| `assembly.artifacts_exist` | pass | info | All collected artifact records exist. |
| `assembly.no_lifeline_source_artifacts` | pass | critical | Assembly source inventory contains only hermes_ext sources, not Hermes lifeline files. |
| `assembly.feature_flags_default_disabled` | pass | critical | All extension feature flags are effectively disabled by default. |
| `assembly.no_forbidden_imports` | pass | critical | No forbidden Hermes core/model SDK imports detected in hermes_ext. |
| `assembly.phase10_golden_trace_stable` | pass | critical | Phase 10 golden trace replay is stable. |
| `assembly.phase9_native_boundary_no_side_effects` | pass | critical | Phase 9 no-op native boundary report has no side effects. |

## Artifacts

| Path | Kind | Exists | Size | SHA-256 |
|---|---|---:|---:|---|
| `reports/phase10/golden_trace_replay_report.json` | report | True | 35207 | `74e17b28854a8d11206d05deeaa68250e4a637ff19f1f6f93eb8ef9d7cfcf814` |
| `reports/phase10/golden_trace_replay_report.md` | report | True | 2284 | `5d0ee17a6a4e5dd8df1fc47eb7d4f1d7e7cebe15079cc627fc56e5d919066a58` |
| `reports/phase10/phase10_execution_log.md` | report | True | 2868 | `cb2ccbbeca4b7a67c1fb9fd0a009b5beb42144cb13e2448bbda698af7c60c7ed` |
| `reports/phase10/phase10_exit_checklist.md` | report | True | 2489 | `fd677158fb551f8fbad7e37a8d46c685795fad347318a3a14bccba1ab92ef49c` |
| `reports/phase10/phase10_test_result.md` | report | True | 1336 | `3b0c096f919ed99e82b1c8a42088bf48cf1c45522bf8b52f8ae9d5ba86b0b711` |
| `reports/phase2/phase2_execution_log.md` | report | True | 2328 | `b3abc7c1c5984b380943632612feb4f863330d97fa765c90ca1b07cd04f5732d` |
| `reports/phase2/phase2_exit_checklist.md` | report | True | 1235 | `6c1dfa8956196a45b4acb8322d3b9b1360a90ec0896b617bfcad66f8aeadb764` |
| `reports/phase2/phase2_test_result.md` | report | True | 891 | `e86c333a2ac73deadf54f9ba10fe5d5dcf9c7a34daf3a9339be59739401a5299` |
| `reports/phase3/phase3_execution_log.md` | report | True | 2481 | `d0b80c8dce16400b1338989ab16b506d351c3ee0597c22d3f440f6d372b24360` |
| `reports/phase3/phase3_exit_checklist.md` | report | True | 1475 | `7b17e351eff97190cd9b1415a1bc492e0d560cf20d49381458c42842595e0b21` |
| `reports/phase3/phase3_test_result.md` | report | True | 1079 | `fd897a45a732e44aee034873c98050f9085ef87442325d6f173277e690794fa0` |
| `reports/phase4/phase4_execution_log.md` | report | True | 2341 | `a9b10d750119523d04a107f8b98064c7af247b93db8c44c3c1ebd35ccf0f0f89` |
| `reports/phase4/phase4_exit_checklist.md` | report | True | 1612 | `942a907e89059a51e76286de065e4e536a8a9618a167ceef3709c30dab1437c6` |
| `reports/phase4/phase4_test_result.md` | report | True | 1056 | `0c331263cea1df561f0a549e9ee10a4fc7ad363ec2cb9680fd116551ffec0331` |
| `reports/phase5/phase5_execution_log.md` | report | True | 2492 | `d6b43a777ceaf3ccd0640baef0b3212d8b1d5359134e324bcc1be8bde7904f96` |
| `reports/phase5/phase5_exit_checklist.md` | report | True | 1845 | `1ac90111f68d5ea961ad843722bd5f289e19e8405a3ed1f9e26b26c57dd12e55` |
| `reports/phase5/phase5_test_result.md` | report | True | 1193 | `9b526627c8bea3431be6bbadb23448a9a135a9aba62727cdac434a0068429a00` |
| `reports/phase6/phase6_execution_log.md` | report | True | 2399 | `5c8316a4527d2fab53b8766d7810ea9e2a6d267a2a1cf0f9a5a8c4a5117ca82f` |
| `reports/phase6/phase6_exit_checklist.md` | report | True | 1815 | `c3bcf99ceb4faa49b5abeb555e58304551fc8cc31867f77a1c6cfa0aa9610c31` |
| `reports/phase6/phase6_test_result.md` | report | True | 1263 | `5894ceda14a7823281b1b65040e722ea145e0d23d0eeb41b0290901ebd87ca7c` |
| `reports/phase7/hermes_adapter_scan.json` | report | True | 17623677 | `03333d6b8b009ba8bd517d6d1a432ad4f6caf8118e683853044265525d088a9d` |
| `reports/phase7/hermes_adapter_scan.md` | report | True | 411901 | `e768f8d17fa799df2c0ebe51e2b1589959b1bee3e09673a0a0cc740359b5fc3d` |
| `reports/phase7/phase7_execution_log.md` | report | True | 3068 | `ed9b05d68c6a3aeefa5b4d553ee1e77d8c2b59aac2f828b884adc2888d92aac9` |
| `reports/phase7/phase7_exit_checklist.md` | report | True | 1929 | `6afbf3eb00d8ca3735a2fd77e6f5c8afb987ae9e5aa4aff1f2e76624dba62655` |
| `reports/phase7/phase7_test_result.md` | report | True | 1331 | `911b4beb7af8e4f6d0c877de8e929ef027b16c1ef3382e232bc93bc7b88cc07f` |
| `reports/phase8/phase8_execution_log.md` | report | True | 3056 | `40e94edfcfc06e22a218cc9826fcc213cd0eb43c790e558b6c69b1bce6b6a7ee` |
| `reports/phase8/phase8_exit_checklist.md` | report | True | 2215 | `45d57514fdb090dfc5d6d7cde4722de2e209f1e0973a969ac8bc84c526882be1` |
| `reports/phase8/phase8_test_result.md` | report | True | 1429 | `9a5bf4924637d005b82ed3d2456cf820c010e46f576d6edce4dccb8536e06f6f` |
| `reports/phase8/zero_touch_integration_spec.json` | report | True | 3668819 | `4d4a3281db3419fccd5996465af711a986eae82654ede0cbd0040b90b79db791` |
| `reports/phase8/zero_touch_integration_spec.md` | report | True | 428376 | `5d53917b12989ae651ff5ce3ae71936a874fa027a76ca71dd5db2e45effa091f` |
| `reports/phase9/native_boundary_contract_report.json` | report | True | 1505277 | `85d4e2db4713bb906a977e0be6554f7f58614fa76387ac942db8b92006690fc5` |
| `reports/phase9/native_boundary_contract_report.md` | report | True | 222918 | `86d1afcf744921aa5cb9cbac6aaa26f753e41cd7eb5c177b4b9bd24cc7b0ff5a` |
| `reports/phase9/phase9_execution_log.md` | report | True | 3087 | `cec74a7a2090085ccee89d97bef61eb11dc821d0fd42358e9bbe5d1bae92c2ae` |
| `reports/phase9/phase9_exit_checklist.md` | report | True | 2212 | `509c4a9452e325f1ed8ab564141322ead8520cbe51d53203d52ace033366fefc` |
| `reports/phase9/phase9_test_result.md` | report | True | 1513 | `b397e87fb32af7b876989cffed8c3b431abde38e6af631f6c4ad73b442fcb2fc` |
| `hermes_ext/__init__.py` | source | True | 333 | `94e13740b59943dc942106ba306c4c0ba701b75bb7280ae1bd02106a472e677d` |
| `hermes_ext/adapter_scan/__init__.py` | source | True | 783 | `37b12832cb2bb0c4151f5bdea1e49b830b19f986ccaa3c15a02170478fb5a297` |
| `hermes_ext/adapter_scan/ast_scanner.py` | source | True | 6377 | `7c2c649a5987007ebb3c7f4ae5cde3c16b098216a4ff2851e04fcd21c0eb455e` |
| `hermes_ext/adapter_scan/cli.py` | source | True | 1901 | `10228db1b277ab8eb94b55ca4ef315282ec6caaf05e92c9ac2f62e876148cb48` |
| `hermes_ext/adapter_scan/contracts.py` | source | True | 7881 | `cd3eba9fda58343567e14e7eda6e930b0a013df1374fb66ea9e4650d9bc1b2d6` |
| `hermes_ext/adapter_scan/extension_points.py` | source | True | 10810 | `36533f648ab5baca7e5165cbeba211f0fe1c85a116de47fc54d5f7528eef32a4` |
| `hermes_ext/adapter_scan/filesystem.py` | source | True | 1306 | `c6d736cac94943e1f28afe64d98b6856536149bbdc6b53c973d2a7408833a630` |
| `hermes_ext/adapter_scan/report.py` | source | True | 3719 | `8302b359f706edac33f441a8abb06fb210da9e0abe2f712574bbe2409d0c0bfe` |
| `hermes_ext/adapter_scan/scanner.py` | source | True | 2532 | `40534defaa0c921d5d340f40a71d8085a9748ddadab4c4bf36dd0079265d4291` |
| `hermes_ext/assembly/__init__.py` | source | True | 1021 | `842b18dc6407d02308f0dfd9d0d9d7f2be41c55c9f361a1263142c3bd5604649` |
| `hermes_ext/assembly/artifact_inventory.py` | source | True | 2797 | `6834866f67eaddef28db55feef2cc5a1e4b4480cbf807e5b2ea3d5cc61b58752` |
| `hermes_ext/assembly/cli.py` | source | True | 2179 | `1aa93cebd8075dced51aaadc8e67afb1f1af89b51e2c3f268312c1143449763a` |
| `hermes_ext/assembly/contracts.py` | source | True | 5931 | `0ffd071fb4b8ed50981d61a0573d4f224735adf4cece8ba6ce0c366a23f39cb0` |
| `hermes_ext/assembly/invariant_suite.py` | source | True | 13526 | `b9c809c1a7f7449694a3145813aee73be6dbaf691c4f966c2497c029a44534d5` |
| `hermes_ext/assembly/manifest_builder.py` | source | True | 1957 | `4d4a76907c0e8ca1282e7675eaf5ef4fa22269b6ee92b31676092a041d47b239` |
| `hermes_ext/assembly/release_gate.py` | source | True | 1157 | `a449cd61659f66cdfea0ebbb759b09f33eeece168d4690a1df307cdd104caa35` |
| `hermes_ext/assembly/report.py` | source | True | 4847 | `6826b66c81038f08ccb4095e59ade682a09b732ee98c7148346e9d0d4e40b734` |
| `hermes_ext/cathay/__init__.py` | source | True | 1063 | `02bbe548502a3ec1e70ff8fcba4d2a000538da0c621b51b71c6b096132c6b272` |
| `hermes_ext/cathay/adapter.py` | source | True | 3821 | `a48058e0e0534b6c024cd1bad47992a47500eb26dbb71e9d2602d618361d8fae` |
| `hermes_ext/cathay/contracts.py` | source | True | 11405 | `d136f8125ed3599cefa01b62719dcda8b0692e243cc7590db021eb3821f523e8` |
| `hermes_ext/cathay/learning_bridge.py` | source | True | 5210 | `a78de4f3ed20805656fb930e111bfa3e5775895f73df88620873d14184c63e72` |
| `hermes_ext/cathay/proactive_bridge.py` | source | True | 4086 | `eb4410ed71056d41211bdad1dc25d7e4ac13ae0e2a52c4d34de69aa3458e96b4` |
| `hermes_ext/cathay/profile_bridge.py` | source | True | 6273 | `803522020a390d9a2a5e97ceae422c710fc278bf36d41883e5c8d4d54ebc8243` |
| `hermes_ext/cathay/safety_bridge.py` | source | True | 6130 | `fb9cf9f4fc5d019428e2061ac6f554d11dd9d3327b1f9f3f60e934734ec37924` |
| `hermes_ext/cathay/signal_fusion.py` | source | True | 3508 | `49bdd8ceefe0d88bb77ab49af67869c893dd7f29ce64a7f50c4c6c30beb1c656` |
| `hermes_ext/common/__init__.py` | source | True | 134 | `8db82d5f8a15d30b271fdc854b12c0d6a1e9ad8d30555274b29693d96fa050a6` |
| `hermes_ext/common/utils.py` | source | True | 423 | `de4a21663f32ac1759d974e4578f681f8776bc598ea537337c44ed81e7548b1c` |
| `hermes_ext/golden_trace/__init__.py` | source | True | 835 | `e04a195eefd96f18b2335f650225abb2ed68ee8dbc3f5610643aa0768cbe64c3` |
| `hermes_ext/golden_trace/cli.py` | source | True | 1926 | `15f7a001c5f40b9a50f23212b07f838ca30b1bb913c3be31d17ef0c8c1bef80e` |
| `hermes_ext/golden_trace/contracts.py` | source | True | 6182 | `b30b8664017dab15c94b18049744b363e92d3051b702ff7ea831620f4bcf153e` |
| `hermes_ext/golden_trace/normalizer.py` | source | True | 3224 | `1f0107212951c4617d9ed29c8b7e93ca494e1d235cc934fcd5b4d9330ae069a9` |
| `hermes_ext/golden_trace/report.py` | source | True | 3201 | `ea08818ecb342b0b630a3794ca0f57c4315985dba489d55b7a3cfaef329e9e6c` |
| `hermes_ext/golden_trace/runner.py` | source | True | 7307 | `228727ea93415b063d25787d288e080cb6e4b3c0aa5e8da8d7dee74e23a21179` |
| `hermes_ext/golden_trace/trace_pack.py` | source | True | 3737 | `088880cb39fa9a864d35a2a84a277719c8547483832c650a7c707f6c8595e7e9` |
| `hermes_ext/golden_trace/verifier.py` | source | True | 1915 | `37e016f9b3be520adb031f5198a1b30a73bb7121aedde1827b8755fa3972ae9e` |
| `hermes_ext/harness/__init__.py` | source | True | 787 | `681e9f032dbd879ea601f07e6285560ca762a2ee123477db7e554d129fc6c8eb` |
| `hermes_ext/harness/cli.py` | source | True | 3627 | `f56085a0beb40189b2e3f7a322fee2ed8cecdaf24c973e52e3c23cdcf74a8783` |
| `hermes_ext/harness/contracts.py` | source | True | 5680 | `7714c949f2385745e96c0650154a8bc1bb86c5f8cfc247b40183a5cdb6b7ddc8` |
| `hermes_ext/harness/diagnostics.py` | source | True | 5152 | `7449d9c4147db6864c61fcf1928d98ec79eba3456a171197a854b1075d31f54d` |
| `hermes_ext/harness/feature_flags.py` | source | True | 4258 | `c682b795c25ea6ddda0911068882840f32674315aef61fd77fe52843be3581e5` |
| `hermes_ext/harness/integration_harness.py` | source | True | 5046 | `a87c8deff79abdca43b6c753334f420f9d21228ba3eeb9df2bd604f3d9bdad8f` |
| `hermes_ext/hooks/__init__.py` | source | True | 621 | `eedf5305f69db80edf4754456123067d48051341cfa25f520bb2437aa190a020` |
| `hermes_ext/hooks/builtin_hooks.py` | source | True | 989 | `9bf05fe06ea60d10ef8174e66af42006aa65175aa76ad7f856bcabaf132e794a` |
| `hermes_ext/hooks/contracts.py` | source | True | 5195 | `b3b1c841c2bf0081c5d5d8e21135404d241c0092f3e0483fc12c67bb67e50244` |
| `hermes_ext/hooks/dispatcher.py` | source | True | 3313 | `87d66da30cfea5f0bd8767b20d312a4da8b78930514866272a94f453e534a007` |
| `hermes_ext/integration_spec/__init__.py` | source | True | 770 | `c1b305577384a4b372bf4bbb2a0521c196323594d1277811da6a0beabaab6f4e` |
| `hermes_ext/integration_spec/cli.py` | source | True | 1790 | `db1e9bb38a3e15165cf4dd34120e68238a0cc303076c65bb6170ef75d221e948` |
| `hermes_ext/integration_spec/contracts.py` | source | True | 8400 | `52af26476c43feba6f0b4d6d1ca9afd6472394e38daa691d50f2c6166f5cafdf` |
| `hermes_ext/integration_spec/guardrails.py` | source | True | 11479 | `151c800be091f05189a515bf664355a59ed40ec5e660c07d18906f9836e6f9d9` |
| `hermes_ext/integration_spec/matrix_builder.py` | source | True | 5633 | `a9d08c2d6aa3dffc6a0d934c24959c9a29f37448d440f80615d51f0fdd948eaf` |
| `hermes_ext/integration_spec/report.py` | source | True | 4825 | `eccde9a188895a2b863b0d9f7a5ab858e85e14695ff78208dc4fb573f4b5adf1` |
| `hermes_ext/integration_spec/spec_builder.py` | source | True | 4876 | `36873a2c9312def77ffe49e29e57e06d1f44c8c00fb79e7ac30e9ba123017a48` |
| `hermes_ext/memoryx/__init__.py` | source | True | 860 | `6c68ac2417835cf5e972adebc9a4c45d4ed800afb0145f169c1f235737b76479` |
| `hermes_ext/memoryx/contracts.py` | source | True | 5625 | `c95863d25ddcefbf6137a43d42efcaf5af3f680dc7f0f32e9060152fea63611d` |
| `hermes_ext/memoryx/dag.py` | source | True | 2405 | `af80ad85f26e0c3183b0c98cbf973feef4e065ee8d03da93b1d45b09f07e7c6b` |
| `hermes_ext/memoryx/fusion.py` | source | True | 5726 | `9b48368e6339a374512cbcfa70d125098a9c491f536f9b76c76f85be312a3e65` |
| `hermes_ext/memoryx/pii.py` | source | True | 2005 | `096c2befa4e19a5a44b88bf76a5c98c70114e8e3a1ced65093b728860291b02a` |
| `hermes_ext/memoryx/promotion.py` | source | True | 1672 | `93a1878ebdbc9e8adc2acc47a72272ee3c8591b6654c810816c83222a488e307` |
| `hermes_ext/memoryx/provider.py` | source | True | 10437 | `ba8e40f9d4857b2d281c95608efacc7eb5f1687bd84c2e7f0a6a52677d4886c7` |
| `hermes_ext/memoryx/recall.py` | source | True | 940 | `e86f7307fdd1121594dbcde3bb2eb1ec3b6aa51c4bf0422402ba1de3403d2dab` |
| `hermes_ext/native_boundary/__init__.py` | source | True | 1237 | `ea4630ac2e2dc28341fd7336ccd00e713a3b53c809308d638c869d99f199a0dc` |
| `hermes_ext/native_boundary/adapters.py` | source | True | 4719 | `9cd7887fb12f8d2f2dce397a4c17ed306e06e316b3e8c20b54e94d2de12bea37` |
| `hermes_ext/native_boundary/cli.py` | source | True | 1765 | `f4912d94f6a9d4da32a96359309d4ef01513c57f4fbe7a834934f8ea7cd2bda3` |
| `hermes_ext/native_boundary/contract_suite.py` | source | True | 9000 | `1f4eb24f14160c37c9dcdd5bfb6ba8c502336610e0adee55614cb1b0f0cd6e3e` |
| `hermes_ext/native_boundary/contracts.py` | source | True | 7402 | `2cf87681b30560daf9a0a458b308e2d524bef7b77bbca7911db235a4ac230314` |
| `hermes_ext/native_boundary/noop_boundary.py` | source | True | 2506 | `cd54e125b04acb26cb069737b2c17dcfe07cf2b33dd532be140dd1e72a2dcf63` |
| `hermes_ext/native_boundary/report.py` | source | True | 3023 | `0edf47a26eb6a4977c8d306bfdda8cbfea71ebee0882b1d59716f6aa9b925299` |
| `hermes_ext/orchestration/__init__.py` | source | True | 937 | `514f3ebb2a96dcebe26c6e90437d61ad744ef6133293dfd8082e8aa54e3fb3b3` |
| `hermes_ext/orchestration/checkpoint_store.py` | source | True | 6295 | `1abd5852a5e366e696801c8e12e82f29eff67c7a20ff0e35391cef7d3f4d31ec` |
| `hermes_ext/orchestration/circuit_breaker.py` | source | True | 1679 | `882e65d5b949f42236bf8843061afc2372fb55479e365916fc729382fb426ab3` |
| `hermes_ext/orchestration/contracts.py` | source | True | 4026 | `581f35e8080bb3510da7fb4716046cbf555d3ac0c5f75374fee1d43dc6d6e82b` |
| `hermes_ext/orchestration/replay.py` | source | True | 2138 | `fe4b7b4fa108277b361941066265d8d85068e2f15f02860328063546e64b8f65` |
| `hermes_ext/orchestration/report.py` | source | True | 1433 | `c2daa98e25ee04218d9d380261db338f973f2e799e11072843555dcc66761d1a` |
| `hermes_ext/orchestration/shadow_runner.py` | source | True | 11073 | `84ac63f70cf508802175e972b3a33e16b1541600de2359268dc64843887d3a83` |
| `hermes_ext/orchestration/span_log.py` | source | True | 2278 | `506496bc1bc4c79cf667afb6b88d651f1c86e5ab07cec75df1e2e6a12f1a8079` |
| `hermes_ext/runtime/__init__.py` | source | True | 686 | `d117c5d5d94af388212ba306134262689a8833be2c0b1113e29f08f6272fadcc` |
| `hermes_ext/runtime/agent_doctor.py` | source | True | 8862 | `f7b188171f87e77f2643d2487b842dfa1040acca41c71bd1f5ba1dd07160920b` |
| `hermes_ext/runtime/mock_provider.py` | source | True | 3711 | `fef0b9319df799e51344dd46584fabe9e5f21353e43020d0e979041b985059b6` |
| `hermes_ext/runtime/request_envelope.py` | source | True | 8409 | `789cb81fa55594fcd7e8fdc8048460df74c07fce4e367fe81e194be417ed4f88` |
| `hermes_ext/schema/__init__.py` | source | True | 458 | `9d7230c1c62c4e3e7fe5bc135b677fd515f0a65c764e891bb50ce67827c41ed1` |
| `hermes_ext/schema/portable_schema.py` | source | True | 5088 | `9fc67ea9f90191bcc50f4a3b43c7002dbb99ae86d1b8da43a6dfb10bf98a8642` |
| `hermes_ext/security/__init__.py` | source | True | 543 | `87b04cc2e8102728d7002fd84bf49d666610b3f947595bf5b15f88efd01e3906` |
| `hermes_ext/security/command_guard.py` | source | True | 4524 | `d966b1ac58bc31284665472c1bf6260505c9e2b0c1eda9af6488229f58329b27` |
| `hermes_ext/security/decisions.py` | source | True | 2611 | `d3a4b4b167641f1617d65194859dcc9c291a9344ffc0ad50ec2e356914b38306` |
| `hermes_ext/security/exec_policy.py` | source | True | 7738 | `46b8284955ff2ca02adab110dd8018228b74f36160ff6f35d0bbdd1760b14c17` |
| `hermes_ext/security/path_guard.py` | source | True | 4507 | `0f3fd6d0d14d31f6e6587ca31269db72c2621cec1d30a7cc848aa35edf4080ac` |
| `hermes_ext/security/pretool_guard.py` | source | True | 8339 | `05f2f5dce75b2a7e0ea67a315edaa29ae9ee3c50c669149e2cb647d762723ec4` |
| `hermes_ext/security/url_guard.py` | source | True | 3538 | `dafeb5f2d9a9f389dc1627635eaf7681a7d75c9e130acfc7724daf6d0149b4d3` |
| `tests/hermes_ext/test_adapter_scan_ast_scanner.py` | test | True | 1826 | `8642458a94d87ab12e3d8c99d105997d7af825dbcf6633705867ea2f7496a34a` |
| `tests/hermes_ext/test_adapter_scan_cli.py` | test | True | 1489 | `30c7cd146f736b17a97ed68c309ed67e2173a84014863513548ad6c944de6c27` |
| `tests/hermes_ext/test_adapter_scan_contracts.py` | test | True | 1787 | `d6dec1697ca409219f81683aef39d9538c62f308acf485dc6595003b5ea7f400` |
| `tests/hermes_ext/test_adapter_scan_engine.py` | test | True | 1341 | `23d4f98c5ed35bdc9aad50c1a096d7f493ce2a9928bb8c82b9b1835b61b18955` |
| `tests/hermes_ext/test_adapter_scan_extension_points.py` | test | True | 2156 | `5de2d6f6f95ed6cdea2e09d492f6324eb5b925d3a9f8608025f410eb44c5b16b` |
| `tests/hermes_ext/test_adapter_scan_filesystem.py` | test | True | 1184 | `4e870d29c6d425bb8c25c27ab03cc8ce90c9b2a6bacbef01f145ccb9781077a3` |
| `tests/hermes_ext/test_adapter_scan_no_imports.py` | test | True | 1493 | `992e41502e6dd2eb70fce612fdbc6f0e895872ee788cb00a47897be869dace0a` |
| `tests/hermes_ext/test_adapter_scan_report.py` | test | True | 790 | `aa62f08399c4a127980b9453885f55f93c08b119b8714b43c82cf0f0ccaa80b6` |
| `tests/hermes_ext/test_agent_doctor.py` | test | True | 785 | `86da239f26bfb9c7c1517e7f0d622fa00b721b794c23368826d98ea42f8bdea8` |
| `tests/hermes_ext/test_assembly_artifact_inventory.py` | test | True | 1648 | `bbbe49aa29f937c804d25c3445bb2a673466cceeb664d05f73c3f8d54fcfb5eb` |
| `tests/hermes_ext/test_assembly_cli.py` | test | True | 2366 | `ffc08d6bd9bdf912d2b5f8bd8456f8df6a21e1bb1e82344f4bbcd177bea63b65` |
| `tests/hermes_ext/test_assembly_contracts.py` | test | True | 2038 | `1d9058d2a71913b339c570a18cd5aa4231860ee69e4776bbe3d5a353d2bca6a4` |
| `tests/hermes_ext/test_assembly_invariant_suite.py` | test | True | 3736 | `d9d3d0c97d397555db83d250c9c0f96f5ed3154ac82bf79b023ea5f69bf52a7c` |
| `tests/hermes_ext/test_assembly_manifest_builder.py` | test | True | 1291 | `08a1901012f729fa5925674e773f7478639d8d6f181a9aa3f6b50235b8db484d` |
| `tests/hermes_ext/test_assembly_no_imports.py` | test | True | 1534 | `7ed4ed61a7e298f7f2301137075baff7d8ed52e2559b34f04f59b8cd9be26ed0` |
| `tests/hermes_ext/test_assembly_release_gate.py` | test | True | 2091 | `2fee45825252a82a40a869396e7702b83e0f917c800776a8e7262bd68ca7350c` |
| `tests/hermes_ext/test_assembly_report.py` | test | True | 1459 | `5ccee96190650dc2c9cbbf00033525f21363207c5da506488430871b8b9bab33` |
| `tests/hermes_ext/test_cathay_adapter.py` | test | True | 2108 | `2537a6a52b2da86ffc342ceba987c65293ee72721abb2021c6633bad33c99fad` |
| `tests/hermes_ext/test_cathay_contracts.py` | test | True | 3207 | `994a741c30c3b99bb063f7ef745a0bb4e8807a12242989baae3a607852a1df83` |
| `tests/hermes_ext/test_cathay_learning_bridge.py` | test | True | 1328 | `be024ee0bd547c7147a245a52d1e6e68ce920572846e4ce0ede8b6db8a6c61c5` |
| `tests/hermes_ext/test_cathay_no_imports.py` | test | True | 999 | `4ff41459226c11e01db7442155de41070e4c857ac5ae77af9b4df2b95d532bfb` |
| `tests/hermes_ext/test_cathay_proactive_bridge.py` | test | True | 1176 | `3ff42d1f0fb9a55ee946673e8c4c3552312e7a50ef72b953d675b1599f453358` |
| `tests/hermes_ext/test_cathay_profile_bridge.py` | test | True | 1367 | `e78d884e1b510e0956e8168c0ee2d8a84c92a85dcc5d306fd138cec44129627d` |
| `tests/hermes_ext/test_cathay_safety_bridge.py` | test | True | 1517 | `0429c045b6a86e43edea7b5519dbc08fb8dd0984a67e78c257e9d9ce0ef33f9a` |
| `tests/hermes_ext/test_cathay_signal_fusion.py` | test | True | 1798 | `82d35967fd41920b277b740501f31b031305d8c0715f09903283a6d618ae3517` |
| `tests/hermes_ext/test_checkpoint_store.py` | test | True | 1750 | `c7dd5de217de9d6b2b589c5c343530d1adac25d46e6a4ced8e3dfbd948aa0cc7` |
| `tests/hermes_ext/test_circuit_breaker.py` | test | True | 937 | `7233213cae627937cd1164710c60cf7799c6ef9b4a9b6ee8c808e9cfe77c855b` |
| `tests/hermes_ext/test_command_guard.py` | test | True | 1130 | `4157fb2fae9e3e49d477c2e5efbe701792d668be8f6c763f1b7926ee457c5fa1` |
| `tests/hermes_ext/test_exec_policy.py` | test | True | 1461 | `8327b780d668fcc5d5f79ea7b476ad94fd72fe466123b2bc08995f27a7e401b2` |
| `tests/hermes_ext/test_feature_flags.py` | test | True | 2034 | `a80852c6373d27344ac7d29a07fd7562e12295e7c147bc11d437c872d258cc40` |
| `tests/hermes_ext/test_golden_trace_cli.py` | test | True | 1370 | `bca66f31f7146f7358ca9a8b45619248d40f7e278e09151c42a3310ed963efc8` |
| `tests/hermes_ext/test_golden_trace_contracts.py` | test | True | 1382 | `3d39ea1010b88bfa482cb5fe09b89437bf91ec9d99d32afc23a48ec6ca94251c` |
| `tests/hermes_ext/test_golden_trace_no_imports.py` | test | True | 1542 | `04bd1ffad5a4b79c23d67a9c7b2e66ac06e978c1b7c47a9b90a39ae2d4b564a3` |
| `tests/hermes_ext/test_golden_trace_normalizer.py` | test | True | 1419 | `097528d742662f18045609c83a5800fafb3edb44c18d21df77a013f3fb9edf9d` |
| `tests/hermes_ext/test_golden_trace_pack.py` | test | True | 849 | `b312073dac4a6b944f9e9a52c07a370189cdb5fe2e93b7e95ddc4d1e2a55553e` |
| `tests/hermes_ext/test_golden_trace_report.py` | test | True | 908 | `79052764b8a4703cace1b58fbe61b637f6bedfea6cc91b81285698975f90142e` |
| `tests/hermes_ext/test_golden_trace_runner.py` | test | True | 1251 | `208d544446f08d38ed06f7167011a635fb3121823d134b913716d62948eac0dd` |
| `tests/hermes_ext/test_golden_trace_verifier.py` | test | True | 2176 | `5eb4cd47f4d1f0e5212ff4204d2e0006ac526214611ddfed92031c765c44b73a` |
| `tests/hermes_ext/test_harness_cli.py` | test | True | 1936 | `96892bef675b76ac6ebf848b82a38bdef721ee8dc2b6d3c3016a866468bc7d2a` |
| `tests/hermes_ext/test_harness_contracts.py` | test | True | 2080 | `a362d971e2cfbb40e775ee0c503d678400b9c5dca92b9ee490422f5dae5a4b23` |
| `tests/hermes_ext/test_harness_diagnostics.py` | test | True | 1092 | `966b541878319444af9a6435fb087c94f63c8d99d744388560827e5145337013` |
| `tests/hermes_ext/test_harness_no_imports.py` | test | True | 1338 | `dccbc95d2c246b051d7f679c5b5a144667b85848b078564f727ac850dbdbdce0` |
| `tests/hermes_ext/test_hook_dispatcher.py` | test | True | 2350 | `f49fb91e14da679b82a1b78bb789791898daf0eedb3cfc1d951fd8e6a1c70739` |
| `tests/hermes_ext/test_hooks_contracts.py` | test | True | 1187 | `84daee16647d61ea779d58b82e5c5fe606df4177567b49bbde606b273923ed03` |
| `tests/hermes_ext/test_integration_harness.py` | test | True | 3457 | `7fb132e7d67692875d5498678aaae47b291947f5599779385af4269fd43d30d9` |
| `tests/hermes_ext/test_integration_spec_builder.py` | test | True | 2491 | `e0e3de9017e72610e80ff6e73de2d8cc739869ebef6c1228b7c65f1f1a3b2f38` |
| `tests/hermes_ext/test_integration_spec_cli.py` | test | True | 2122 | `81d7ff565977c3a94a720f30f28737227a9019281afec362abf17e36cf5ffa45` |
| `tests/hermes_ext/test_integration_spec_contracts.py` | test | True | 2399 | `36547a60948b129b61dfc60a34756c7e714b0b95fb3342015d6f90eb62deb94e` |
| `tests/hermes_ext/test_integration_spec_guardrails.py` | test | True | 2410 | `1ffc9e513ada6e2df6808b6fc15c3f845f1d4a66215694531f5fa4a0cf2cce7d` |
| `tests/hermes_ext/test_integration_spec_matrix_builder.py` | test | True | 2493 | `05a34036c18e601c3a990c5334808d0434d2ac59a9354438116da62825f9191a` |
| `tests/hermes_ext/test_integration_spec_no_imports.py` | test | True | 1505 | `c38149324ad19dfda77928144c0f8b869581cc6387768a87805880991a3bbfe7` |
| `tests/hermes_ext/test_integration_spec_report.py` | test | True | 1390 | `1debc7a08b0fa75cc7a014325f0b0fc0051d1a794c3b622c8b9110405606c4e0` |
| `tests/hermes_ext/test_memoryx_contracts.py` | test | True | 1637 | `5ac7e013145adfe391890a01f548cc7cd7d3bb90b7726c59c467c9eb4d57669a` |
| `tests/hermes_ext/test_memoryx_dag.py` | test | True | 1584 | `427c253404c45084be5cd6c33c6cfe6acc764b7ff882474684d8f60b449942d9` |
| `tests/hermes_ext/test_memoryx_fusion.py` | test | True | 2572 | `e6e1386edef7229f7b27fe2ab84d743b15a54cde7e2f0dca3e3c7e537384ac52` |
| `tests/hermes_ext/test_memoryx_no_imports.py` | test | True | 1012 | `9faccfc11626c878be6a8e129a11706d63b00c79f0157b1f7817ac2217b4e0cd` |
| `tests/hermes_ext/test_memoryx_pii.py` | test | True | 953 | `58e0cff5d6bd739501717a27dd71c7a59f20dc8d306bb4e8db46cf5d67e6aeeb` |
| `tests/hermes_ext/test_memoryx_promotion.py` | test | True | 1509 | `2bab02d7dd4e1376042da93f81f091be29a1df33d6bf536f899c9503f1e7ff22` |
| `tests/hermes_ext/test_memoryx_provider.py` | test | True | 2818 | `762160b0174e5ec4a8c75fed494e0faf72297a695ee4ca382f66d2e2c449d707` |
| `tests/hermes_ext/test_memoryx_recall.py` | test | True | 1033 | `56dfded9c09618c01c6d7c583ac0772892450dd6a6c0470d947985ee9da8682e` |
| `tests/hermes_ext/test_mock_provider.py` | test | True | 2403 | `88d5fc3ac16d297685f8d35cf2422af04ae21e8197093a09b5a17b0c930226db` |
| `tests/hermes_ext/test_native_boundary_adapters.py` | test | True | 1790 | `3012471ee3e0d39638fbdf3aa43af6fe6751e5de10d53f3da9ced9823c82d9dc` |
| `tests/hermes_ext/test_native_boundary_cli.py` | test | True | 958 | `bb7b36a064cc8cd0a08cd45fccc12d0d666056691c551d42c985222c04c3808b` |
| `tests/hermes_ext/test_native_boundary_contract_suite.py` | test | True | 2740 | `b1479a19aa652645b31656c5e9addb33308c9cc1230c8818f1090e19968c49b0` |
| `tests/hermes_ext/test_native_boundary_contracts.py` | test | True | 1527 | `f93276340f7a750d32cc1b168d24faa62352d36576b07bfddde16c7f8082edc5` |
| `tests/hermes_ext/test_native_boundary_no_imports.py` | test | True | 1549 | `0c59df2556a45afb112a34feb0e086dd5736811f98063cd64a49203fda4b1e90` |
| `tests/hermes_ext/test_native_boundary_noop.py` | test | True | 1577 | `81c6fac7265bc6bdd32f0d21ad7e75fa580e628f905c9b5db3d7f5ba5f1bf58d` |
| `tests/hermes_ext/test_native_boundary_report.py` | test | True | 685 | `7265d5560c425d88ec04ddc20992bf6d60c603b71b4366aad7230c044edf0c38` |
| `tests/hermes_ext/test_orchestration_contracts.py` | test | True | 1372 | `4a967988518b07b7cf4dc927e3b0d1d0970d576bb5efd513dcf79d810e4d0552` |
| `tests/hermes_ext/test_orchestration_no_imports.py` | test | True | 1279 | `11a2765e9dba76c30fb1009b5493bd48608d9261dcf4f04a878ee81a21854485` |
| `tests/hermes_ext/test_orchestration_report.py` | test | True | 980 | `1a2779da50d49518da847b1b9a75c90ecda6913951f5f8238dc4cefe8cbc2924` |
| `tests/hermes_ext/test_path_guard.py` | test | True | 1301 | `f09232f7d618a9077fbdb6e91f063a315ccd835a86c4d0874ad604443e1a4b10` |
| `tests/hermes_ext/test_portable_schema.py` | test | True | 2329 | `0083708744a5c117e7035503c703bfd9b72777592dd8a0a38b098cc34b372a5a` |
| `tests/hermes_ext/test_pretool_guard.py` | test | True | 2837 | `60237f1990e67873ebed48b7b9e9f42b43da631bda2de3b2e803f2f7c809bffd` |
| `tests/hermes_ext/test_replay.py` | test | True | 1775 | `d2432e1a667d0cec264df76026c758057b97f4940a8afe5f588042968ec751ff` |
| `tests/hermes_ext/test_request_envelope.py` | test | True | 2020 | `a8f6e37dc6a7e318384476dd44026ccb0e893856a47278dde0fba46f0b16b1dd` |
| `tests/hermes_ext/test_shadow_runner.py` | test | True | 2120 | `c97a349ff9f41b940208d25178d762d4c53a3a34dc29058c570cf2a1d4c48141` |
| `tests/hermes_ext/test_span_log.py` | test | True | 640 | `08f202542bdf78920211008c2129f37c5f7251a05da32b50c480f33b9fb659b9` |
| `tests/hermes_ext/test_url_guard.py` | test | True | 1032 | `2fdd162f63363e1aad35c2e5baaddf67c46e847bcfb7a3958b09568b44c0313f` |

## Non-negotiable Rule

This manifest documents hermes_ext shadow assembly only. It is not approval to modify Hermes core files.
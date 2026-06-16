# Hermes Adapter Scan Report

- report_id: `355a1cda-9730-4329-b19d-7a5f446fc67a`
- project_root: `D:\projects\hermes-agent-main`
- created_at: `2026-06-16T06:49:18.505997+00:00`

## Summary

| Metric | Value |
|---|---:|
| files_scanned | 749 |
| lifeline_files_found | 24 |
| candidates_found | 1464 |
| forbidden_candidates | 344 |
| wrapper_only_candidates | 775 |
| feature_flag_candidates | 345 |
| parse_errors | 0 |

## Warnings

- 344 forbidden candidates detected; these are mapping-only

## Extension Point Candidates

| Path | Surface | Posture | Risk | Symbol | Line | Reason | Future Hint |
|---|---|---|---|---|---:|---|---|
| `acp_adapter/auth.py` | provider | wrapper_only | medium | `detect_provider` | 11 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `acp_adapter/auth.py` | provider | wrapper_only | medium | `has_provider` | 36 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `acp_adapter/edit_approval.py` | tool_registry | feature_flag_required | high | `build_acp_edit_tool_call` | 212 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/events.py` | tool_registry | feature_flag_required | high | `make_tool_progress_cb` | 114 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/events.py` | tool_registry | feature_flag_required | high | `make_tool_progress_cb._tool_progress` | 134 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/permissions.py` | tool_registry | feature_flag_required | high | `_build_permission_tool_call` | 73 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/provenance.py` | gateway | wrapper_only | high | `build_session_provenance` | 22 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/provenance.py` | gateway | wrapper_only | high | `session_provenance_meta` | 111 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/server.py` | gateway | wrapper_only | high | `HermesACPAgent._session_modes` | 530 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/server.py` | gateway | wrapper_only | high | `HermesACPAgent._send_session_info_update` | 733 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/server.py` | gateway | wrapper_only | high | `HermesACPAgent._register_session_mcp_servers` | 788 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/server.py` | gateway | wrapper_only | high | `HermesACPAgent._replay_session_history` | 1019 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/server.py` | gateway | wrapper_only | high | `HermesACPAgent.new_session` | 1109 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/server.py` | gateway | wrapper_only | high | `HermesACPAgent.load_session` | 1129 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/server.py` | gateway | wrapper_only | high | `HermesACPAgent.resume_session` | 1176 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/server.py` | gateway | wrapper_only | high | `HermesACPAgent.fork_session` | 1225 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/server.py` | gateway | wrapper_only | high | `HermesACPAgent.list_sessions` | 1245 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/server.py` | gateway | wrapper_only | high | `HermesACPAgent.set_session_model` | 1989 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/server.py` | gateway | wrapper_only | high | `HermesACPAgent.set_session_mode` | 2023 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/server.py` | tool_registry | feature_flag_required | high | `HermesACPAgent._history_tool_call_name_args` | 994 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/server.py` | tool_registry | feature_flag_required | high | `HermesACPAgent._history_tool_call_id` | 1010 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/server.py` | tool_registry | feature_flag_required | high | `HermesACPAgent._cmd_tools` | 1781 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/session.py` | gateway | wrapper_only | high | `_build_session_title` | 73 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/session.py` | gateway | wrapper_only | high | `SessionState` | 170 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/session.py` | gateway | wrapper_only | high | `SessionManager` | 186 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/session.py` | gateway | wrapper_only | high | `SessionManager.create_session` | 210 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/session.py` | gateway | wrapper_only | high | `SessionManager.get_session` | 231 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/session.py` | gateway | wrapper_only | high | `SessionManager.remove_session` | 244 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/session.py` | gateway | wrapper_only | high | `SessionManager.fork_session` | 253 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/session.py` | gateway | wrapper_only | high | `SessionManager.list_sessions` | 283 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/session.py` | gateway | wrapper_only | high | `SessionManager.save_session` | 388 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/session.py` | tool_registry | feature_flag_required | high | `_expand_acp_enabled_toolsets` | 140 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/tools.py` | gateway | wrapper_only | high | `_format_session_search_result` | 609 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `acp_adapter/tools.py` | memory | wrapper_only | medium | `_format_memory_result` | 640 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `acp_adapter/tools.py` | tool_registry | feature_flag_required | high | `get_tool_kind` | 81 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/tools.py` | tool_registry | feature_flag_required | high | `make_tool_call_id` | 86 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/tools.py` | tool_registry | feature_flag_required | high | `build_tool_title` | 91 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/tools.py` | tool_registry | feature_flag_required | high | `_tool_result_failed` | 205 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/tools.py` | tool_registry | feature_flag_required | high | `_build_tool_complete_content` | 976 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/tools.py` | tool_registry | feature_flag_required | high | `build_tool_start` | 1017 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `acp_adapter/tools.py` | tool_registry | feature_flag_required | high | `build_tool_complete` | 1249 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/agent_init.py` | provider | wrapper_only | medium | `_custom_provider_model_matches` | 95 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/agent_init.py` | provider | wrapper_only | medium | `_custom_provider_extra_body_for_agent` | 102 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/agent_init.py` | provider | wrapper_only | medium | `_merge_custom_provider_extra_body` | 135 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/agent_runtime_helpers.py` | provider | wrapper_only | medium | `reapply_reasoning_echo_for_provider` | 2237 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/agent_runtime_helpers.py` | tool_registry | feature_flag_required | high | `agent_runtime_owns_post_tool_hook` | 56 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/agent_runtime_helpers.py` | tool_registry | feature_flag_required | high | `sanitize_tool_call_arguments` | 237 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/agent_runtime_helpers.py` | tool_registry | feature_flag_required | high | `invoke_tool` | 1713 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/agent_runtime_helpers.py` | tool_registry | feature_flag_required | high | `invoke_tool._finish_agent_tool` | 1787 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/agent_runtime_helpers.py` | tool_registry | feature_flag_required | high | `repair_tool_call` | 1925 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/agent_runtime_helpers.py` | tool_registry | feature_flag_required | high | `repair_tool_call._strip_tool_suffix` | 1979 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/agent_runtime_helpers.py` | tool_registry | feature_flag_required | high | `apply_pending_steer_to_tool_results` | 2463 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/anthropic_adapter.py` | tool_registry | feature_flag_required | high | `_sanitize_tool_id` | 1450 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/anthropic_adapter.py` | tool_registry | feature_flag_required | high | `_normalize_tool_input_schema` | 1463 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/anthropic_adapter.py` | tool_registry | feature_flag_required | high | `convert_tools_to_anthropic` | 1504 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/anthropic_adapter.py` | tool_registry | feature_flag_required | high | `_convert_tool_message_to_result` | 1863 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/anthropic_adapter.py` | tool_registry | feature_flag_required | high | `_strip_orphaned_tool_blocks` | 1942 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_normalize_aux_provider` | 165 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_get_aux_model_for_provider` | 285 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_resolve_api_key_provider` | 1427 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_read_main_provider` | 1734 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_get_provider_chain` | 2225 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_mark_provider_unhealthy` | 2295 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_is_provider_unhealthy` | 2314 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_recoverable_pool_provider` | 2685 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_recover_provider_pool` | 2728 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_retry_same_provider_sync` | 2777 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_retry_same_provider_async` | 2835 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_refresh_provider_credentials` | 2892 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_resolve_single_provider` | 3109 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `resolve_provider_client` | 3337 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_normalize_vision_provider` | 4072 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `resolve_vision_provider_client` | 4128 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/auxiliary_client.py` | provider | wrapper_only | medium | `_resolve_task_provider_model` | 4674 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/azure_identity_adapter.py` | provider | wrapper_only | medium | `build_token_provider` | 215 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/azure_identity_adapter.py` | provider | wrapper_only | medium | `is_token_provider` | 424 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/background_review.py` | memory | wrapper_only | medium | `build_memory_write_metadata` | 300 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `agent/bedrock_adapter.py` | provider | wrapper_only | medium | `_extract_provider_from_arn` | 1227 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/bedrock_adapter.py` | tool_registry | feature_flag_required | high | `_model_supports_tool_use` | 426 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/bedrock_adapter.py` | tool_registry | feature_flag_required | high | `convert_tools_to_converse` | 462 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/browser_provider.py` | gateway | wrapper_only | high | `BrowserProvider.create_session` | 90 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/browser_provider.py` | gateway | wrapper_only | high | `BrowserProvider.close_session` | 111 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/browser_provider.py` | provider | wrapper_only | medium | `BrowserProvider` | 49 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/browser_provider.py` | provider | wrapper_only | medium | `BrowserProvider.provider_name` | 173 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/browser_registry.py` | provider | wrapper_only | medium | `register_provider` | 52 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/browser_registry.py` | provider | wrapper_only | medium | `list_providers` | 82 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/browser_registry.py` | provider | wrapper_only | medium | `get_provider` | 89 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/chat_completion_helpers.py` | tool_registry | feature_flag_required | high | `interruptible_streaming_api_call._bedrock_call._on_tool` | 1662 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/codex_responses_adapter.py` | tool_registry | feature_flag_required | high | `_split_responses_tool_id` | 194 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/codex_responses_adapter.py` | tool_registry | feature_flag_required | high | `_responses_tools` | 244 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/coding_context.py` | tool_registry | feature_flag_required | high | `RuntimeMode.toolset_selection` | 410 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/context_compressor.py` | context | forbidden | high | — | 0 | Context compression mutates conversation context; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `agent/context_compressor.py` | gateway | forbidden | critical | `ContextCompressor.on_session_reset` | 608 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/context_compressor.py` | gateway | forbidden | critical | `ContextCompressor.on_session_end` | 627 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/context_compressor.py` | tool_registry | forbidden | critical | `_extract_tool_call_name_and_args` | 195 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/context_compressor.py` | tool_registry | forbidden | critical | `_extract_tool_call_id` | 207 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/context_compressor.py` | tool_registry | forbidden | critical | `_truncate_tool_call_args_json` | 317 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/context_compressor.py` | tool_registry | forbidden | critical | `_summarize_tool_result` | 471 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/context_compressor.py` | tool_registry | forbidden | critical | `ContextCompressor._prune_old_tool_results` | 841 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/context_compressor.py` | tool_registry | forbidden | critical | `ContextCompressor._get_tool_call_id` | 1736 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/context_compressor.py` | tool_registry | forbidden | critical | `ContextCompressor._sanitize_tool_pairs` | 1742 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/context_engine.py` | gateway | wrapper_only | high | `ContextEngine.on_session_start` | 144 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/context_engine.py` | gateway | wrapper_only | high | `ContextEngine.on_session_end` | 151 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/context_engine.py` | gateway | wrapper_only | high | `ContextEngine.on_session_reset` | 158 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/context_engine.py` | tool_registry | feature_flag_required | high | `ContextEngine.get_tool_schemas` | 170 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/context_engine.py` | tool_registry | feature_flag_required | high | `ContextEngine.handle_tool_call` | 178 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/copilot_acp_client.py` | tool_registry | feature_flag_required | high | `_extract_tool_calls_from_text` | 227 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/copilot_acp_client.py` | tool_registry | feature_flag_required | high | `_extract_tool_calls_from_text._try_add_tool_call` | 234 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/credential_pool.py` | provider | wrapper_only | medium | `_iter_custom_providers` | 352 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/credential_pool.py` | provider | wrapper_only | medium | `get_custom_provider_pool_key` | 378 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/credential_pool.py` | provider | wrapper_only | medium | `list_custom_pool_providers` | 408 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/credential_pool.py` | provider | wrapper_only | medium | `_get_custom_provider_config` | 419 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/credential_sources.py` | provider | wrapper_only | medium | `_clear_auth_store_provider` | 222 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/credits_tracker.py` | gateway | wrapper_only | high | `seed_credits_at_session_start` | 741 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/display.py` | tool_registry | feature_flag_required | high | `set_tool_preview_max_len` | 105 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/display.py` | tool_registry | feature_flag_required | high | `get_tool_preview_max_len` | 111 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/display.py` | tool_registry | feature_flag_required | high | `get_skin_tool_prefix` | 129 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/display.py` | tool_registry | feature_flag_required | high | `get_tool_emoji` | 137 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/display.py` | tool_registry | feature_flag_required | high | `build_tool_preview` | 193 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/display.py` | tool_registry | feature_flag_required | high | `_detect_tool_failure` | 849 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/display.py` | tool_registry | feature_flag_required | high | `get_cute_tool_message` | 899 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/gemini_cloudcode_adapter.py` | tool_registry | feature_flag_required | high | `_translate_tool_call_to_gemini` | 86 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/gemini_cloudcode_adapter.py` | tool_registry | feature_flag_required | high | `_translate_tool_result_to_gemini` | 108 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/gemini_cloudcode_adapter.py` | tool_registry | feature_flag_required | high | `_translate_tools_to_gemini` | 188 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/gemini_cloudcode_adapter.py` | tool_registry | feature_flag_required | high | `_translate_tool_choice_to_gemini` | 214 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/gemini_native_adapter.py` | tool_registry | feature_flag_required | high | `_tool_call_extra_signature` | 232 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/gemini_native_adapter.py` | tool_registry | feature_flag_required | high | `_translate_tool_call_to_gemini` | 245 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/gemini_native_adapter.py` | tool_registry | feature_flag_required | high | `_translate_tool_result_to_gemini` | 267 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/gemini_native_adapter.py` | tool_registry | feature_flag_required | high | `_translate_tools_to_gemini` | 347 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/gemini_native_adapter.py` | tool_registry | feature_flag_required | high | `_translate_tool_choice_to_gemini` | 371 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/gemini_native_adapter.py` | tool_registry | feature_flag_required | high | `_tool_call_extra_from_part` | 470 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/gemini_schema.py` | tool_registry | feature_flag_required | high | `sanitize_gemini_tool_parameters` | 93 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/image_gen_provider.py` | provider | wrapper_only | medium | `ImageGenProvider` | 51 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/image_gen_registry.py` | provider | wrapper_only | medium | `register_provider` | 36 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/image_gen_registry.py` | provider | wrapper_only | medium | `list_providers` | 60 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/image_gen_registry.py` | provider | wrapper_only | medium | `get_provider` | 67 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/image_gen_registry.py` | provider | wrapper_only | medium | `get_active_provider` | 75 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/insights.py` | gateway | wrapper_only | high | `InsightsEngine._get_sessions` | 190 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/insights.py` | gateway | wrapper_only | high | `InsightsEngine._compute_top_sessions` | 655 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/insights.py` | gateway | wrapper_only | high | `InsightsEngine.format_gateway` | 857 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/insights.py` | tool_registry | feature_flag_required | high | `InsightsEngine._get_tool_usage` | 198 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/insights.py` | tool_registry | feature_flag_required | high | `InsightsEngine._compute_tool_breakdown` | 544 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/memory_manager.py` | gateway | forbidden | critical | `MemoryManager.on_session_end` | 687 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | gateway | forbidden | critical | `MemoryManager.on_session_switch` | 698 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | memory | forbidden | critical | — | 0 | MemoryManager coordinates native memory; do not patch directly. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `agent/memory_manager.py` | memory | forbidden | critical | `memory_provider_tools_enabled` | 47 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | memory | forbidden | critical | `inject_memory_provider_tools` | 65 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | memory | forbidden | critical | `build_memory_context_block` | 295 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | memory | forbidden | critical | `MemoryManager` | 312 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | memory | forbidden | critical | `MemoryManager._provider_memory_write_metadata_mode` | 766 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | memory | forbidden | critical | `MemoryManager.on_memory_write` | 791 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | provider | forbidden | critical | `memory_provider_tools_enabled` | 47 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | provider | forbidden | critical | `inject_memory_provider_tools` | 65 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | provider | forbidden | critical | `MemoryManager.add_provider` | 333 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | provider | forbidden | critical | `MemoryManager.providers` | 399 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | provider | forbidden | critical | `MemoryManager.get_provider` | 403 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | provider | forbidden | critical | `MemoryManager._provider_sync_accepts_messages` | 478 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | provider | forbidden | critical | `MemoryManager._provider_memory_write_metadata_mode` | 766 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | tool_registry | forbidden | critical | `memory_provider_tools_enabled` | 47 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | tool_registry | forbidden | critical | `inject_memory_provider_tools` | 65 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | tool_registry | forbidden | critical | `MemoryManager.get_all_tool_schemas` | 614 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | tool_registry | forbidden | critical | `MemoryManager.get_all_tool_names` | 643 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | tool_registry | forbidden | critical | `MemoryManager.has_tool` | 647 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_manager.py` | tool_registry | forbidden | critical | `MemoryManager.handle_tool_call` | 651 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_provider.py` | gateway | forbidden | critical | `MemoryProvider.on_session_end` | 165 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_provider.py` | gateway | forbidden | critical | `MemoryProvider.on_session_switch` | 175 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_provider.py` | memory | forbidden | critical | — | 0 | MemoryProvider ABC is a native memory boundary; do not replace in Phase 7. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `agent/memory_provider.py` | memory | forbidden | critical | `MemoryProvider` | 42 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_provider.py` | memory | forbidden | critical | `MemoryProvider.on_memory_write` | 279 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_provider.py` | provider | forbidden | critical | `MemoryProvider` | 42 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_provider.py` | tool_registry | forbidden | critical | `MemoryProvider.get_tool_schemas` | 134 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/memory_provider.py` | tool_registry | forbidden | critical | `MemoryProvider.handle_tool_call` | 143 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/message_sanitization.py` | tool_registry | feature_flag_required | high | `_repair_tool_call_arguments` | 185 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/message_sanitization.py` | tool_registry | feature_flag_required | high | `_sanitize_tools_non_ascii` | 350 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/model_metadata.py` | provider | wrapper_only | medium | `_strip_provider_prefix` | 87 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/model_metadata.py` | provider | wrapper_only | medium | `_infer_provider_from_url` | 458 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/model_metadata.py` | provider | wrapper_only | medium | `_is_known_provider_base_url` | 476 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/model_metadata.py` | provider | wrapper_only | medium | `get_context_length_from_provider_error` | 1005 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/models_dev.py` | provider | wrapper_only | medium | `ProviderInfo` | 126 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/models_dev.py` | provider | wrapper_only | medium | `_get_provider_models` | 413 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/models_dev.py` | provider | wrapper_only | medium | `list_provider_models` | 511 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/models_dev.py` | provider | wrapper_only | medium | `_should_hide_from_provider_catalog` | 567 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/models_dev.py` | provider | wrapper_only | medium | `_parse_provider_info` | 656 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/models_dev.py` | provider | wrapper_only | medium | `get_provider_info` | 674 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/moonshot_schema.py` | tool_registry | feature_flag_required | high | `sanitize_moonshot_tool_parameters` | 170 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/moonshot_schema.py` | tool_registry | feature_flag_required | high | `sanitize_moonshot_tools` | 192 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/onboarding.py` | gateway | wrapper_only | high | `busy_input_hint_gateway` | 36 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/onboarding.py` | gateway | wrapper_only | high | `tool_progress_hint_gateway` | 84 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/onboarding.py` | tool_registry | feature_flag_required | high | `tool_progress_hint_gateway` | 84 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/onboarding.py` | tool_registry | feature_flag_required | high | `tool_progress_hint_cli` | 92 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/prompt_builder.py` | prompt | forbidden | critical | — | 0 | Prompt builder affects all model inputs; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `agent/redact.py` | security | forbidden | critical | — | 0 | Redaction is safety-sensitive; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `agent/runtime_cwd.py` | gateway | wrapper_only | high | `set_session_cwd` | 23 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/runtime_cwd.py` | gateway | wrapper_only | high | `clear_session_cwd` | 28 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/runtime_cwd.py` | gateway | wrapper_only | high | `_session_cwd_override` | 32 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/shell_hooks.py` | tool_registry | feature_flag_required | high | `ShellHookSpec.matches_tool` | 133 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/subdirectory_hints.py` | tool_registry | feature_flag_required | high | `SubdirectoryHintTracker.check_tool_call` | 76 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/system_prompt.py` | prompt | forbidden | critical | — | 0 | System prompt affects behavior and cache stability; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `agent/system_prompt.py` | tool_registry | forbidden | critical | `format_tools_for_system_message` | 417 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `agent/title_generator.py` | gateway | wrapper_only | high | `auto_title_session` | 87 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/tool_dispatch_helpers.py` | tool_registry | feature_flag_required | high | `_is_mcp_tool_parallel_safe` | 90 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_dispatch_helpers.py` | tool_registry | feature_flag_required | high | `_should_parallelize_tool_batch` | 103 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_dispatch_helpers.py` | tool_registry | feature_flag_required | high | `_is_multimodal_tool_result` | 177 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_dispatch_helpers.py` | tool_registry | feature_flag_required | high | `make_tool_result_message` | 320 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_dispatch_helpers.py` | tool_registry | feature_flag_required | high | `_is_untrusted_tool` | 364 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_executor.py` | tool_registry | feature_flag_required | high | `_emit_terminal_post_tool_call` | 61 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_executor.py` | tool_registry | feature_flag_required | high | `_cancelled_tool_result` | 96 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_executor.py` | tool_registry | feature_flag_required | high | `_emit_cancelled_terminal_post_tool_call` | 106 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_executor.py` | tool_registry | feature_flag_required | high | `_tool_search_scoped_names` | 135 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_executor.py` | tool_registry | feature_flag_required | high | `_apply_tool_request_middleware_for_agent` | 184 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_executor.py` | tool_registry | feature_flag_required | high | `_run_agent_tool_execution_middleware` | 211 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_executor.py` | tool_registry | feature_flag_required | high | `execute_tool_calls_concurrent` | 243 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_executor.py` | tool_registry | feature_flag_required | high | `execute_tool_calls_concurrent._run_tool` | 462 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_executor.py` | tool_registry | feature_flag_required | high | `execute_tool_calls_sequential` | 770 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_guardrails.py` | tool_registry | feature_flag_required | high | `ToolCallGuardrailConfig` | 64 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_guardrails.py` | tool_registry | feature_flag_required | high | `ToolCallSignature` | 128 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_guardrails.py` | tool_registry | feature_flag_required | high | `ToolGuardrailDecision` | 145 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_guardrails.py` | tool_registry | feature_flag_required | high | `canonical_tool_args` | 176 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_guardrails.py` | tool_registry | feature_flag_required | high | `classify_tool_failure` | 189 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_guardrails.py` | tool_registry | feature_flag_required | high | `ToolCallGuardrailController` | 224 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_guardrails.py` | tool_registry | feature_flag_required | high | `toolguard_synthetic_result` | 383 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_guardrails.py` | tool_registry | feature_flag_required | high | `append_toolguard_guidance` | 394 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tool_guardrails.py` | tool_registry | feature_flag_required | high | `_tool_failure_recovery_hint` | 406 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/transcription_provider.py` | provider | wrapper_only | medium | `TranscriptionProvider` | 61 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/transcription_registry.py` | provider | wrapper_only | medium | `register_provider` | 54 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/transcription_registry.py` | provider | wrapper_only | medium | `list_providers` | 100 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/transcription_registry.py` | provider | wrapper_only | medium | `get_provider` | 107 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/transports/anthropic.py` | tool_registry | feature_flag_required | high | `AnthropicTransport.convert_tools` | 35 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/transports/base.py` | provider | wrapper_only | medium | `ProviderTransport` | 16 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/transports/base.py` | tool_registry | feature_flag_required | high | `ProviderTransport.convert_tools` | 35 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/transports/bedrock.py` | tool_registry | feature_flag_required | high | `BedrockTransport.convert_tools` | 27 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/transports/chat_completions.py` | tool_registry | feature_flag_required | high | `ChatCompletionsTransport.convert_tools` | 219 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/transports/codex.py` | tool_registry | feature_flag_required | high | `ResponsesApiTransport.convert_tools` | 55 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/transports/codex_app_server_session.py` | gateway | wrapper_only | high | `CodexAppServerSession` | 191 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `agent/transports/codex_event_projector.py` | tool_registry | feature_flag_required | high | `_format_tool_args` | 50 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/transports/codex_event_projector.py` | tool_registry | feature_flag_required | high | `CodexEventProjector._project_mcp_tool_call` | 217 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/transports/codex_event_projector.py` | tool_registry | feature_flag_required | high | `CodexEventProjector._project_dynamic_tool_call` | 258 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/transports/types.py` | tool_registry | feature_flag_required | high | `ToolCall` | 19 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/transports/types.py` | tool_registry | feature_flag_required | high | `build_tool_call` | 152 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `agent/tts_provider.py` | provider | wrapper_only | medium | `TTSProvider` | 64 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/tts_registry.py` | provider | wrapper_only | medium | `register_provider` | 66 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/tts_registry.py` | provider | wrapper_only | medium | `list_providers` | 111 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/tts_registry.py` | provider | wrapper_only | medium | `get_provider` | 118 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/video_gen_provider.py` | provider | wrapper_only | medium | `VideoGenProvider` | 75 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/video_gen_registry.py` | provider | wrapper_only | medium | `register_provider` | 37 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/video_gen_registry.py` | provider | wrapper_only | medium | `list_providers` | 61 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/video_gen_registry.py` | provider | wrapper_only | medium | `get_provider` | 68 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/video_gen_registry.py` | provider | wrapper_only | medium | `get_active_provider` | 76 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/web_search_provider.py` | provider | wrapper_only | medium | `WebSearchProvider` | 63 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/web_search_registry.py` | provider | wrapper_only | medium | `register_provider` | 48 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/web_search_registry.py` | provider | wrapper_only | medium | `list_providers` | 78 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/web_search_registry.py` | provider | wrapper_only | medium | `get_provider` | 85 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/web_search_registry.py` | provider | wrapper_only | medium | `get_active_search_provider` | 222 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `agent/web_search_registry.py` | provider | wrapper_only | medium | `get_active_extract_provider` | 232 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `batch_runner.py` | tool_registry | feature_flag_required | high | `_normalize_tool_stats` | 71 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `batch_runner.py` | tool_registry | feature_flag_required | high | `_normalize_tool_error_counts` | 101 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `batch_runner.py` | tool_registry | feature_flag_required | high | `_extract_tool_stats` | 125 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `cli.py` | cli | forbidden | critical | — | 0 | Interactive CLI is a lifeline entrypoint; do not patch directly. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `cli.py` | gateway | forbidden | critical | `_sync_process_session_id` | 850 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `_should_emit_cleanup_session_finalize` | 1029 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `_notify_session_finalize` | 1037 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `_emit_interrupted_session_end` | 1055 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `_notify_single_query_session_finalize` | 1091 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `HermesCLI._claim_active_session` | 3608 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `HermesCLI._release_active_session` | 3636 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `HermesCLI._restore_session_cwd` | 5235 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `HermesCLI._show_session_status` | 5526 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `HermesCLI._list_recent_sessions` | 5786 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `HermesCLI._show_recent_sessions` | 5805 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `HermesCLI._notify_session_boundary` | 5902 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `HermesCLI._discard_session_if_empty` | 5919 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `HermesCLI.new_session` | 5948 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `HermesCLI._show_gateway_status` | 7167 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `HermesCLI._transfer_session_yolo` | 8007 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | gateway | forbidden | critical | `HermesCLI._is_session_yolo_active` | 8035 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | provider | forbidden | critical | `HermesCLI._normalize_model_for_provider` | 4345 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `get_tool_definitions` | 814 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `get_toolset_for_tool` | 822 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `get_all_toolsets` | 832 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `get_toolset_info` | 838 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `validate_toolset` | 844 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `_disable_prompt_toolkit_cpr_warning` | 2779 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `HermesCLI._clear_prompt_toolkit_screen` | 3714 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `HermesCLI._install_tool_callbacks` | 5090 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `HermesCLI._show_tool_availability_warnings` | 5460 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `HermesCLI.show_tools` | 5653 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `HermesCLI.show_toolsets` | 5696 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `HermesCLI.show_history.flush_tool_summary` | 5846 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `HermesCLI._on_tool_gen_start` | 8941 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `HermesCLI._on_tool_progress` | 8961 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `HermesCLI._on_tool_start` | 9043 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cli.py` | tool_registry | forbidden | critical | `HermesCLI._on_tool_complete` | 9054 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cron/jobs.py` | cron | forbidden | high | — | 0 | Cron jobs are persistent scheduled work; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `cron/scheduler.py` | cron | forbidden | high | — | 0 | Cron scheduler can trigger autonomous work; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `cron/scheduler.py` | tool_registry | forbidden | critical | `_resolve_cron_disabled_toolsets` | 61 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `cron/scheduler.py` | tool_registry | forbidden | critical | `_resolve_cron_enabled_toolsets` | 84 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/authz_mixin.py` | gateway | wrapper_only | high | `GatewayAuthorizationMixin` | 31 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/channel_directory.py` | gateway | wrapper_only | high | `_session_entry_id` | 87 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/channel_directory.py` | gateway | wrapper_only | high | `_session_entry_name` | 97 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/channel_directory.py` | gateway | wrapper_only | high | `_build_from_sessions` | 265 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/config.py` | gateway | wrapper_only | high | `SessionResetPolicy` | 275 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/config.py` | gateway | wrapper_only | high | `GatewayConfig` | 499 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/config.py` | gateway | wrapper_only | high | `load_gateway_config` | 756 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/config.py` | gateway | wrapper_only | high | `_validate_gateway_config` | 1279 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/hooks.py` | tool_registry | feature_flag_required | high | `HookRegistry` | 52 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/kanban_watchers.py` | gateway | wrapper_only | high | `GatewayKanbanWatchersMixin` | 26 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/memory_monitor.py` | memory | wrapper_only | medium | `log_memory_usage` | 83 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `gateway/memory_monitor.py` | memory | wrapper_only | medium | `start_memory_monitoring` | 139 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `gateway/memory_monitor.py` | memory | wrapper_only | medium | `stop_memory_monitoring` | 196 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `gateway/mirror.py` | gateway | wrapper_only | high | `mirror_to_session` | 25 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/mirror.py` | gateway | wrapper_only | high | `_find_session_id` | 84 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platform_registry.py` | tool_registry | feature_flag_required | high | `PlatformRegistry` | 162 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `_session_chat_user_message` | 352 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `_derive_chat_session_id` | 679 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._parse_session_key_header` | 936 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._ensure_session_db` | 992 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._session_response` | 1308 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._get_existing_session_or_404` | 1343 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._conversation_history_for_session` | 1352 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._handle_list_sessions` | 1362 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._handle_create_session` | 1391 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._handle_get_session` | 1428 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._handle_patch_session` | 1438 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._handle_delete_session` | 1466 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._handle_session_messages` | 1479 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._handle_fork_session` | 1497 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._handle_session_chat` | 1544 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | gateway | wrapper_only | high | `APIServerAdapter._handle_session_chat_stream` | 1588 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/api_server.py` | tool_registry | feature_flag_required | high | `APIServerAdapter._handle_toolsets` | 1237 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/platforms/api_server.py` | tool_registry | feature_flag_required | high | `APIServerAdapter._handle_session_chat_stream._tool_progress` | 1643 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/platforms/api_server.py` | tool_registry | feature_flag_required | high | `APIServerAdapter._handle_chat_completions._on_tool_start` | 1868 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/platforms/api_server.py` | tool_registry | feature_flag_required | high | `APIServerAdapter._handle_chat_completions._on_tool_complete` | 1894 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/platforms/api_server.py` | tool_registry | feature_flag_required | high | `APIServerAdapter._write_sse_responses._emit_tool_started` | 2409 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/platforms/api_server.py` | tool_registry | feature_flag_required | high | `APIServerAdapter._write_sse_responses._emit_tool_completed` | 2455 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/platforms/api_server.py` | tool_registry | feature_flag_required | high | `APIServerAdapter._handle_responses._on_tool_progress` | 2923 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/platforms/api_server.py` | tool_registry | feature_flag_required | high | `APIServerAdapter._handle_responses._on_tool_start` | 2932 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/platforms/api_server.py` | tool_registry | feature_flag_required | high | `APIServerAdapter._handle_responses._on_tool_complete` | 2940 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/platforms/base.py` | gateway | forbidden | high | — | 0 | Gateway platform base affects all adapters; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `gateway/platforms/base.py` | gateway | forbidden | critical | `coerce_plaintext_gateway_command` | 1516 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/platforms/base.py` | gateway | forbidden | critical | `BasePlatformAdapter.set_busy_session_handler` | 2277 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/platforms/base.py` | gateway | forbidden | critical | `BasePlatformAdapter.set_session_store` | 2281 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/platforms/base.py` | gateway | forbidden | critical | `BasePlatformAdapter.interrupt_session_activity` | 3258 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/platforms/base.py` | gateway | forbidden | critical | `BasePlatformAdapter._release_session_guard` | 3677 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/platforms/base.py` | gateway | forbidden | critical | `BasePlatformAdapter._session_task_is_stale` | 3697 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/platforms/base.py` | gateway | forbidden | critical | `BasePlatformAdapter._heal_stale_session_lock` | 3714 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/platforms/base.py` | gateway | forbidden | critical | `BasePlatformAdapter._start_session_processing` | 3741 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/platforms/base.py` | gateway | forbidden | critical | `BasePlatformAdapter.cancel_session_processing` | 3773 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/platforms/base.py` | gateway | forbidden | critical | `BasePlatformAdapter._drain_pending_after_session_command` | 3824 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/platforms/base.py` | gateway | forbidden | critical | `BasePlatformAdapter._dispatch_active_session_command` | 3842 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/platforms/base.py` | tool_registry | forbidden | critical | `BasePlatformAdapter.format_tool_event` | 2059 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/platforms/feishu_comment.py` | gateway | wrapper_only | high | `_session_key` | 1010 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/feishu_comment.py` | gateway | wrapper_only | high | `_load_session_history` | 1014 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/feishu_comment.py` | gateway | wrapper_only | high | `_save_session_history` | 1029 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/matrix.py` | gateway | wrapper_only | high | `_create_matrix_session` | 455 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/qqbot/adapter.py` | gateway | wrapper_only | high | `QQAdapter._get_gateway_url` | 422 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/qqbot/adapter.py` | gateway | wrapper_only | high | `QQAdapter._parse_gateway_session_key` | 1068 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/qqbot/adapter.py` | gateway | wrapper_only | high | `QQAdapter._is_authorized_interaction_for_session` | 1082 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/qqbot/chunked_upload.py` | tool_registry | feature_flag_required | high | `UploadFileTooLargeError` | 92 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/platforms/slack.py` | gateway | wrapper_only | high | `SlackAdapter._dm_top_level_threads_as_sessions` | 1320 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/slack.py` | gateway | wrapper_only | high | `SlackAdapter._seed_assistant_thread_session` | 2141 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/slack.py` | gateway | wrapper_only | high | `SlackAdapter._has_active_session_for_thread` | 3583 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/telegram.py` | provider | wrapper_only | medium | `TelegramAdapter._build_provider_keyboard` | 3358 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `gateway/platforms/telegram.py` | provider | wrapper_only | medium | `TelegramAdapter._build_provider_keyboard._provider_button` | 3375 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `gateway/platforms/telegram_network.py` | provider | wrapper_only | medium | `_query_doh_provider` | 169 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `gateway/platforms/weixin.py` | gateway | wrapper_only | high | `_is_stale_session_ret` | 99 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/yuanbao.py` | gateway | wrapper_only | high | `RecallGuardMiddleware._find_processing_session` | 1348 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/platforms/yuanbao.py` | gateway | wrapper_only | high | `GroupQueryService.query_session_members` | 4239 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/run.py` | gateway | forbidden | high | — | 0 | Gateway runner touches platform delivery; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `gateway/run.py` | gateway | forbidden | critical | `_ensure_windows_gateway_venv_imports` | 139 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_gateway_platform_value` | 193 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_gateway_loop_exception_handler` | 242 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_redact_gateway_user_facing_secrets` | 277 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_gateway_provider_error_reply` | 285 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_looks_like_gateway_provider_error` | 320 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_sanitize_gateway_final_response` | 343 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_prepare_gateway_status_message` | 361 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_coerce_gateway_timestamp` | 457 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_is_fresh_gateway_interruption` | 525 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_build_gateway_agent_history` | 644 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_load_gateway_config` | 1793 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_load_gateway_runtime_config` | 1822 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_resolve_gateway_model` | 1842 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_parse_session_key` | 1885 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_format_gateway_process_notification` | 1911 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `_drain_gateway_watch_events` | 1943 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner` | 2130 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._session_key_for_source` | 2701 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._normalize_source_for_session_key` | 2907 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._resolve_session_agent_runtime` | 2935 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._goal_still_active_for_session` | 3288 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._resolve_session_reasoning_config` | 3488 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._set_session_reasoning_override` | 3507 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._get_max_concurrent_sessions` | 3676 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._active_session_limit_message` | 3685 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._claim_active_session_slot` | 3700 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._handle_active_session_busy_message` | 3814 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._notify_active_sessions_of_shutdown` | 4103 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._suspend_stuck_loop_sessions` | 4361 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._schedule_resume_pending_sessions` | 4745 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._session_expiry_watcher` | 5628 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._cache_session_source` | 8171 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._get_cached_session_source` | 8192 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._format_session_info` | 9414 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._rename_telegram_topic_for_session_title` | 10702 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._restore_telegram_topic_session` | 10973 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._set_session_env` | 11925 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._clear_session_env` | 11946 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._apply_session_model_override` | 12738 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._clear_session_boundary_security_state` | 12811 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._begin_session_run_generation` | 12858 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._invalidate_session_run_generation` | 12876 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._is_session_run_current` | 12888 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `GatewayRunner._interrupt_and_clear_session` | 12911 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | gateway | forbidden | critical | `start_gateway` | 16304 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | provider | forbidden | critical | `_gateway_provider_error_reply` | 285 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | provider | forbidden | critical | `_looks_like_gateway_provider_error` | 320 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | provider | forbidden | critical | `_try_resolve_fallback_provider` | 1470 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | provider | forbidden | critical | `GatewayRunner._load_provider_routing` | 3635 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | tool_registry | forbidden | critical | `_is_interrupted_tool_result` | 778 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | tool_registry | forbidden | critical | `_strip_interrupted_tool_tails` | 790 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/run.py` | tool_registry | forbidden | critical | `GatewayRunner.stop._stop_impl._kill_tool_subprocesses` | 6019 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | high | — | 0 | Gateway session management is stateful; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionSource` | 71 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionContext` | 161 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `build_session_context_prompt` | 232 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionEntry` | 442 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `is_shared_multi_user_session` | 596 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `build_session_key` | 617 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionStore` | 701 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionStore._generate_session_key` | 777 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionStore._is_session_expired` | 785 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionStore.has_any_sessions` | 867 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionStore.get_or_create_session` | 889 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionStore.update_session` | 990 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionStore.suspend_session` | 1006 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionStore.reset_session` | 1163 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionStore.switch_session` | 1215 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionStore.list_sessions` | 1270 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionStore.lookup_by_session_id` | 1284 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `SessionStore.rewind_session` | 1356 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | gateway | forbidden | critical | `build_session_context` | 1409 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session.py` | tool_registry | forbidden | critical | `_discord_tools_loaded` | 207 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `gateway/session_context.py` | gateway | wrapper_only | high | `set_current_session_id` | 86 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/session_context.py` | gateway | wrapper_only | high | `set_session_vars` | 101 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/session_context.py` | gateway | wrapper_only | high | `clear_session_vars` | 143 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/session_context.py` | gateway | wrapper_only | high | `get_session_env` | 174 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/slash_commands.py` | gateway | wrapper_only | high | `GatewaySlashCommandsMixin` | 48 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/slash_commands.py` | gateway | wrapper_only | high | `GatewaySlashCommandsMixin._redact_matrix_session_key` | 571 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/slash_commands.py` | gateway | wrapper_only | high | `GatewaySlashCommandsMixin._gateway_session_origin_for_id` | 577 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/slash_commands.py` | gateway | wrapper_only | high | `GatewaySlashCommandsMixin._handle_resume_command._list_titled_sessions` | 2818 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/slash_commands.py` | gateway | wrapper_only | high | `GatewaySlashCommandsMixin._handle_sessions_command` | 2944 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/slash_commands.py` | memory | wrapper_only | medium | `GatewaySlashCommandsMixin._handle_memory_command` | 2163 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `gateway/status.py` | gateway | wrapper_only | high | `_get_gateway_lock_path` | 50 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/status.py` | gateway | wrapper_only | high | `_looks_like_gateway_process` | 167 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/status.py` | gateway | wrapper_only | high | `_record_looks_like_gateway` | 183 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/status.py` | gateway | wrapper_only | high | `_read_gateway_lock_record` | 277 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/status.py` | gateway | wrapper_only | high | `_write_gateway_lock_record` | 312 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/status.py` | gateway | wrapper_only | high | `acquire_gateway_runtime_lock` | 425 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/status.py` | gateway | wrapper_only | high | `release_gateway_runtime_lock` | 446 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/status.py` | gateway | wrapper_only | high | `is_gateway_runtime_lock_active` | 460 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/status.py` | gateway | wrapper_only | high | `is_gateway_running` | 1058 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/stream_consumer.py` | gateway | wrapper_only | high | `GatewayStreamConsumer` | 79 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/stream_dispatch.py` | gateway | wrapper_only | high | `GatewayEventDispatcher` | 40 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/stream_events.py` | gateway | wrapper_only | high | `GatewayNotice` | 135 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `gateway/stream_events.py` | tool_registry | feature_flag_required | high | `ToolCallChunk` | 85 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/stream_events.py` | tool_registry | feature_flag_required | high | `ToolCallFinished` | 104 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `gateway/stream_events.py` | tool_registry | feature_flag_required | high | `LongToolHint` | 122 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/active_sessions.py` | gateway | wrapper_only | high | `coerce_max_concurrent_sessions` | 24 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/active_sessions.py` | gateway | wrapper_only | high | `resolve_max_concurrent_sessions` | 56 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/active_sessions.py` | gateway | wrapper_only | high | `active_session_limit_message` | 73 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/active_sessions.py` | gateway | wrapper_only | high | `ActiveSessionLease` | 221 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/active_sessions.py` | gateway | wrapper_only | high | `try_acquire_active_session` | 234 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/active_sessions.py` | gateway | wrapper_only | high | `release_active_session` | 298 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/active_sessions.py` | gateway | wrapper_only | high | `active_session_registry_snapshot` | 314 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/active_sessions.py` | tool_registry | feature_flag_required | high | `active_session_registry_snapshot` | 314 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/auth.py` | gateway | wrapper_only | high | `_is_remote_session` | 3106 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `ProviderConfig` | 156 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `_resolve_api_key_provider_secret` | 568 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `_load_provider_state` | 1141 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `_save_provider_state` | 1170 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `_store_provider_state` | 1179 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `mark_provider_active_if_unset` | 1195 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `is_known_auth_provider` | 1213 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `get_auth_provider_display_name` | 1218 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `get_provider_auth_state` | 1336 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `get_active_provider` | 1353 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `is_provider_explicitly_configured` | 1359 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `clear_provider_auth` | 1410 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `deactivate_provider` | 1450 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `_get_config_hint_for_unknown_provider` | 1467 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `resolve_provider` | 1492 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `_nous_effective_provider_state` | 1927 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `get_api_key_provider_status` | 5967 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `get_external_process_provider_status` | 5998 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `resolve_api_key_provider_credentials` | 6142 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `resolve_external_process_provider_credentials` | 6187 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `_update_config_for_provider` | 6231 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `_get_config_provider` | 6297 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `_config_provider_matches` | 6315 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `_should_reset_config_provider_on_logout` | 6322 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `_logout_default_provider_from_config` | 6330 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `_reset_config_provider` | 6345 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth.py` | provider | wrapper_only | medium | `build_minimax_oauth_token_provider` | 7568 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth_commands.py` | provider | wrapper_only | medium | `_get_custom_provider_names` | 40 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth_commands.py` | provider | wrapper_only | medium | `_resolve_custom_provider_input` | 61 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth_commands.py` | provider | wrapper_only | medium | `_normalize_provider` | 77 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth_commands.py` | provider | wrapper_only | medium | `_provider_base_url` | 90 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/auth_commands.py` | provider | wrapper_only | medium | `_pick_provider` | 655 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/banner.py` | tool_registry | feature_flag_required | high | `_display_toolset_name` | 539 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/claw.py` | gateway | wrapper_only | high | `_warn_if_gateway_running` | 151 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/cli_agent_setup_mixin.py` | gateway | wrapper_only | high | `CLIAgentSetupMixin._preload_resumed_session` | 436 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/cli_commands_mixin.py` | gateway | wrapper_only | high | `CLICommandsMixin._handle_sessions_command` | 781 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/cli_commands_mixin.py` | memory | wrapper_only | medium | `CLICommandsMixin._handle_memory_command` | 1403 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/cli_commands_mixin.py` | tool_registry | feature_flag_required | high | `CLICommandsMixin._handle_tools_command` | 387 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/codex_runtime_plugin_migration.py` | tool_registry | feature_flag_required | high | `_build_hermes_tools_mcp_entry` | 557 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/commands.py` | gateway | wrapper_only | high | `is_gateway_known_command` | 325 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/commands.py` | gateway | wrapper_only | high | `should_bypass_active_session` | 370 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/commands.py` | gateway | wrapper_only | high | `_is_gateway_available` | 422 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/commands.py` | gateway | wrapper_only | high | `gateway_help_lines` | 443 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/commands.py` | gateway | wrapper_only | high | `_collect_gateway_skill_entries` | 663 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/commands.py` | tool_registry | feature_flag_required | high | `SlashCommandCompleter._tools_completions` | 1596 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/config.py` | provider | wrapper_only | medium | `_normalize_custom_provider_entry` | 3775 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/config.py` | provider | wrapper_only | medium | `_custom_provider_entry_to_provider_config` | 3907 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/config.py` | provider | wrapper_only | medium | `providers_dict_to_custom_providers` | 3943 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/config.py` | provider | wrapper_only | medium | `get_compatible_custom_providers` | 3957 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/config.py` | provider | wrapper_only | medium | `get_custom_provider_context_length` | 4007 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/config.py` | tool_registry | feature_flag_required | high | `is_uv_tool_install` | 403 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/config.py` | tool_registry | feature_flag_required | high | `is_uv_tool_install._has_uv_tool_marker` | 420 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/container_boot.py` | gateway | wrapper_only | high | `reconcile_profile_gateways` | 58 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/container_boot.py` | gateway | wrapper_only | high | `_maybe_migrate_legacy_gateway_run_state` | 163 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/container_boot.py` | gateway | wrapper_only | high | `_is_legacy_gateway_run_request` | 229 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/cron.py` | gateway | wrapper_only | high | `_contains_gateway_lifecycle_command` | 33 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/dashboard_auth/base.py` | gateway | wrapper_only | high | `Session` | 10 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/dashboard_auth/base.py` | gateway | wrapper_only | high | `DashboardAuthProvider.verify_session` | 148 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/dashboard_auth/base.py` | gateway | wrapper_only | high | `DashboardAuthProvider.refresh_session` | 151 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/dashboard_auth/base.py` | gateway | wrapper_only | high | `DashboardAuthProvider.revoke_session` | 154 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/dashboard_auth/base.py` | provider | wrapper_only | medium | `ProviderError` | 44 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/dashboard_auth/base.py` | provider | wrapper_only | medium | `DashboardAuthProvider` | 75 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/dashboard_auth/cookies.py` | gateway | wrapper_only | high | `set_session_cookies` | 128 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/dashboard_auth/cookies.py` | gateway | wrapper_only | high | `clear_session_cookies` | 170 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/dashboard_auth/cookies.py` | gateway | wrapper_only | high | `read_session_cookies` | 228 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/dashboard_auth/registry.py` | provider | wrapper_only | medium | `register_provider` | 23 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/dashboard_auth/registry.py` | provider | wrapper_only | medium | `get_provider` | 43 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/dashboard_auth/registry.py` | provider | wrapper_only | medium | `list_providers` | 49 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/dashboard_auth/registry.py` | provider | wrapper_only | medium | `clear_providers` | 55 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/dashboard_auth/routes.py` | provider | wrapper_only | medium | `api_auth_providers` | 151 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/doctor.py` | gateway | wrapper_only | high | `_check_gateway_service_linger` | 326 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/doctor.py` | provider | wrapper_only | medium | `_has_provider_env_config` | 100 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/doctor.py` | provider | wrapper_only | medium | `_has_healthy_oauth_fallback_for_apikey_provider` | 152 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/doctor.py` | provider | wrapper_only | medium | `_build_apikey_providers_list` | 373 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/doctor.py` | provider | wrapper_only | medium | `_build_apikey_providers_list._normalize_provider` | 428 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/doctor.py` | provider | wrapper_only | medium | `run_doctor._probe_apikey_provider` | 1798 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/doctor.py` | tool_registry | feature_flag_required | high | `_doctor_tool_availability_detail` | 127 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/doctor.py` | tool_registry | feature_flag_required | high | `_apply_doctor_tool_availability_overrides` | 134 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/dump.py` | gateway | wrapper_only | high | `_gateway_status` | 70 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/dump.py` | memory | wrapper_only | medium | `_memory_provider` | 146 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/dump.py` | provider | wrapper_only | medium | `_memory_provider` | 146 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/dump.py` | provider | wrapper_only | medium | `_get_model_and_provider` | 153 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/fallback_cmd.py` | provider | wrapper_only | medium | `_snapshot_auth_active_provider` | 78 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/fallback_cmd.py` | provider | wrapper_only | medium | `_restore_auth_active_provider` | 88 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `GatewayRuntimeSnapshot` | 57 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `ProfileGatewayProcess` | 74 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_request_gateway_self_restart` | 212 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_scan_gateway_pids` | 309 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `find_gateway_pids` | 557 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `find_profile_gateway_processes` | 587 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_gateway_run_args_for_profile` | 614 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `launch_detached_profile_gateway_restart` | 622 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_read_gateway_runtime_status` | 877 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_gateway_runtime_status_for_pid` | 887 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `get_gateway_runtime_snapshot` | 1082 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_format_gateway_pids` | 1156 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_print_gateway_process_mismatch` | 1169 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_print_other_profiles_gateway_status` | 1181 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_gateway_list` | 1206 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `kill_gateway_processes` | 1247 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `stop_profile_gateway` | 1277 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_windows_gateway_should_absorb_console_controls` | 1395 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `prompt_linux_gateway_install_scope` | 2034 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `install_linux_gateway_from_setup` | 2047 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_gateway_run_command` | 3269 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_spawn_detached_gateway` | 3283 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_wait_for_gateway_exit` | 3640 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_running_under_gateway_supervisor` | 3798 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_guard_supervised_gateway_conflict` | 3821 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_guard_existing_gateway_process_conflict` | 3861 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_guard_official_docker_root_gateway` | 3893 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `run_gateway` | 3920 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `gateway_setup` | 5968 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `gateway_command` | 6334 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway.py` | gateway | wrapper_only | high | `_gateway_command_inner` | 6470 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway_windows.py` | gateway | wrapper_only | high | `_launch_elevated_gateway_command` | 174 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway_windows.py` | gateway | wrapper_only | high | `_stable_gateway_working_dir` | 315 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway_windows.py` | gateway | wrapper_only | high | `_build_gateway_cmd_script` | 338 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway_windows.py` | gateway | wrapper_only | high | `_build_gateway_argv` | 572 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway_windows.py` | gateway | wrapper_only | high | `_wait_for_gateway_ready` | 875 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway_windows.py` | gateway | wrapper_only | high | `_report_gateway_start` | 892 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway_windows.py` | gateway | wrapper_only | high | `_gateway_pids` | 998 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/gateway_windows.py` | gateway | wrapper_only | high | `_drain_gateway_pid` | 1216 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/goals.py` | gateway | wrapper_only | high | `_get_session_db` | 209 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/kanban_db.py` | tool_registry | feature_flag_required | high | `_resolve_worker_cli_toolsets` | 6678 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/main.py` | cli | forbidden | critical | — | 0 | Command dispatcher is a CLI lifeline; future integration must remain external. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `hermes_cli/main.py` | gateway | forbidden | critical | `_session_browse_picker` | 881 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | gateway | forbidden | critical | `_resolve_last_session` | 1122 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | gateway | forbidden | critical | `_resolve_session_by_name_or_id` | 1253 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | gateway | forbidden | critical | `_read_tui_active_session_file` | 1293 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | gateway | forbidden | critical | `cmd_gateway` | 2332 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | gateway | forbidden | critical | `_gateway_prompt` | 4429 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | gateway | forbidden | critical | `_wait_for_windows_update_gateway_exit` | 8105 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | gateway | forbidden | critical | `_pause_windows_gateways_for_update` | 8136 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | gateway | forbidden | critical | `_resume_windows_gateways_after_update` | 8221 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | gateway | forbidden | critical | `_coalesce_session_name_args` | 9925 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | gateway | forbidden | critical | `main.cmd_sessions` | 12034 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | memory | forbidden | critical | `_read_cgroup_memory_limit` | 1833 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | memory | forbidden | critical | `cmd_memory` | 11279 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | provider | forbidden | critical | `_has_any_provider_configured` | 767 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | provider | forbidden | critical | `_is_profile_api_key_provider` | 2636 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | provider | forbidden | critical | `select_provider_and_model` | 2651 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | provider | forbidden | critical | `select_provider_and_model._named_custom_provider_map` | 2688 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | provider | forbidden | critical | `_aux_flow_provider_model` | 3366 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | provider | forbidden | critical | `_prompt_provider_choice` | 3473 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | provider | forbidden | critical | `_auto_provider_name` | 3604 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | provider | forbidden | critical | `_custom_provider_api_key_config_value` | 3625 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | provider | forbidden | critical | `_custom_provider_base_url_config_value` | 3638 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | provider | forbidden | critical | `_save_custom_provider` | 3646 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | provider | forbidden | critical | `_remove_custom_provider` | 3712 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | tool_registry | forbidden | critical | `_normalize_tui_toolsets` | 1809 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/main.py` | tool_registry | forbidden | critical | `cmd_tools` | 11365 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_cli/mcp_catalog.py` | tool_registry | feature_flag_required | high | `ToolsSpec` | 95 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/mcp_catalog.py` | tool_registry | feature_flag_required | high | `_read_prior_tool_selection` | 478 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/mcp_catalog.py` | tool_registry | feature_flag_required | high | `_probe_tools` | 496 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/mcp_catalog.py` | tool_registry | feature_flag_required | high | `_write_tools_include` | 520 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/mcp_catalog.py` | tool_registry | feature_flag_required | high | `_apply_tool_selection` | 540 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/mcp_picker.py` | tool_registry | feature_flag_required | high | `_configure_tools` | 130 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/memory_setup.py` | memory | wrapper_only | medium | `memory_command` | 460 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/memory_setup.py` | provider | wrapper_only | medium | `_get_available_providers` | 150 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/memory_setup.py` | provider | wrapper_only | medium | `cmd_setup_provider` | 190 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/middleware.py` | tool_registry | feature_flag_required | high | `apply_tool_request_middleware` | 120 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/middleware.py` | tool_registry | feature_flag_required | high | `run_tool_execution_middleware` | 192 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/model_catalog.py` | provider | wrapper_only | medium | `_fetch_provider_override` | 292 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/model_catalog.py` | provider | wrapper_only | medium | `_get_provider_block` | 309 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/model_normalize.py` | provider | wrapper_only | medium | `_normalize_provider_alias` | 213 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/model_normalize.py` | provider | wrapper_only | medium | `_strip_matching_provider_prefix` | 226 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/model_normalize.py` | provider | wrapper_only | medium | `normalize_model_for_provider` | 327 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/model_setup_flows.py` | provider | wrapper_only | medium | `_model_flow_api_key_provider` | 2287 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/model_switch.py` | provider | wrapper_only | medium | `_bare_custom_provider_def` | 50 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/model_switch.py` | provider | wrapper_only | medium | `get_authenticated_provider_slugs` | 539 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/model_switch.py` | provider | wrapper_only | medium | `list_authenticated_providers` | 1202 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/model_switch.py` | provider | wrapper_only | medium | `list_picker_providers` | 2029 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `ProviderEntry` | 989 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `provider_group_for_slug` | 1094 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `group_providers` | 1099 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `get_default_model_for_provider` | 1260 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `get_pricing_for_provider` | 1521 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `list_available_providers` | 1614 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `curated_models_for_provider` | 1728 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `_provider_keys` | 1753 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `_model_in_provider_catalog` | 1759 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `detect_static_provider_for_model` | 1820 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `detect_provider_for_model` | 1871 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `normalize_provider` | 1937 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `provider_label` | 1948 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `provider_model_ids` | 2175 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `_provider_models_cache_path` | 2419 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `_load_provider_models_cache` | 2495 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `_save_provider_models_cache` | 2508 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `cached_provider_model_ids` | 2519 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | provider | wrapper_only | medium | `clear_provider_models_cache` | 2573 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/models.py` | tool_registry | feature_flag_required | high | `_openrouter_model_supports_tools` | 1292 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/nous_account.py` | gateway | wrapper_only | high | `NousPortalAccountInfo.tool_gateway_entitled` | 112 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/nous_account.py` | gateway | wrapper_only | high | `NousPortalAccountInfo.tool_gateway_entitled_for` | 120 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/nous_account.py` | tool_registry | feature_flag_required | high | `NousToolAccessInfo` | 64 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/nous_account.py` | tool_registry | feature_flag_required | high | `NousPortalAccountInfo.tool_gateway_entitled` | 112 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/nous_account.py` | tool_registry | feature_flag_required | high | `NousPortalAccountInfo.tool_gateway_entitled_for` | 120 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/nous_account.py` | tool_registry | feature_flag_required | high | `_tool_access_from_value` | 667 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/nous_subscription.py` | gateway | wrapper_only | high | `_uses_gateway` | 50 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/nous_subscription.py` | gateway | wrapper_only | high | `_get_gateway_direct_credentials` | 860 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/nous_subscription.py` | gateway | wrapper_only | high | `get_gateway_eligible_tools` | 905 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/nous_subscription.py` | gateway | wrapper_only | high | `apply_gateway_defaults` | 972 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/nous_subscription.py` | gateway | wrapper_only | high | `prompt_enable_tool_gateway` | 1045 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/nous_subscription.py` | tool_registry | feature_flag_required | high | `_toolset_enabled` | 122 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/nous_subscription.py` | tool_registry | feature_flag_required | high | `get_gateway_eligible_tools` | 905 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/nous_subscription.py` | tool_registry | feature_flag_required | high | `prompt_enable_tool_gateway` | 1045 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/oneshot.py` | gateway | wrapper_only | high | `_create_session_db_for_oneshot` | 229 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/oneshot.py` | tool_registry | feature_flag_required | high | `_normalize_toolsets` | 33 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/oneshot.py` | tool_registry | feature_flag_required | high | `_validate_explicit_toolsets` | 51 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/plugins.py` | provider | wrapper_only | medium | `PluginContext.register_image_gen_provider` | 534 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/plugins.py` | provider | wrapper_only | medium | `PluginContext.register_dashboard_auth_provider` | 561 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/plugins.py` | provider | wrapper_only | medium | `PluginContext.register_video_gen_provider` | 601 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/plugins.py` | provider | wrapper_only | medium | `PluginContext.register_web_search_provider` | 628 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/plugins.py` | provider | wrapper_only | medium | `PluginContext.register_browser_provider` | 656 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/plugins.py` | provider | wrapper_only | medium | `PluginContext.register_tts_provider` | 688 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/plugins.py` | provider | wrapper_only | medium | `PluginContext.register_transcription_provider` | 726 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/plugins.py` | tool_registry | feature_flag_required | high | `PluginContext.register_tool` | 320 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/plugins.py` | tool_registry | feature_flag_required | high | `PluginContext.dispatch_tool` | 471 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/plugins.py` | tool_registry | feature_flag_required | high | `set_thread_tool_whitelist` | 1848 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/plugins.py` | tool_registry | feature_flag_required | high | `clear_thread_tool_whitelist` | 1856 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/plugins.py` | tool_registry | feature_flag_required | high | `get_pre_tool_call_block_message` | 1860 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/plugins.py` | tool_registry | feature_flag_required | high | `get_plugin_toolsets` | 2004 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/plugins_cmd.py` | memory | wrapper_only | medium | `_discover_memory_providers` | 1021 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/plugins_cmd.py` | memory | wrapper_only | medium | `_get_current_memory_provider` | 1062 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/plugins_cmd.py` | memory | wrapper_only | medium | `_save_memory_provider` | 1082 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/plugins_cmd.py` | memory | wrapper_only | medium | `_configure_memory_provider` | 1102 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/plugins_cmd.py` | provider | wrapper_only | medium | `_discover_memory_providers` | 1021 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/plugins_cmd.py` | provider | wrapper_only | medium | `_get_current_memory_provider` | 1062 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/plugins_cmd.py` | provider | wrapper_only | medium | `_save_memory_provider` | 1082 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/plugins_cmd.py` | provider | wrapper_only | medium | `_configure_memory_provider` | 1102 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/plugins_cmd.py` | tool_registry | feature_flag_required | high | `_get_plugin_toolset_key` | 1609 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/plugins_cmd.py` | tool_registry | feature_flag_required | high | `_toggle_plugin_toolset` | 1655 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/portal_cli.py` | tool_registry | feature_flag_required | high | `_cmd_tools` | 121 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/profiles.py` | gateway | wrapper_only | high | `_check_gateway_running` | 614 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/profiles.py` | gateway | wrapper_only | high | `_maybe_register_gateway_service` | 1221 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/profiles.py` | gateway | wrapper_only | high | `_maybe_unregister_gateway_service` | 1281 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/profiles.py` | gateway | wrapper_only | high | `_cleanup_gateway_service` | 1308 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/profiles.py` | gateway | wrapper_only | high | `_stop_gateway_process` | 1356 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/providers.py` | provider | wrapper_only | medium | `ProviderDef` | 221 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/providers.py` | provider | wrapper_only | medium | `normalize_provider` | 395 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/providers.py` | provider | wrapper_only | medium | `get_provider` | 405 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/providers.py` | provider | wrapper_only | medium | `resolve_user_provider` | 546 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/providers.py` | provider | wrapper_only | medium | `custom_provider_slug` | 585 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/providers.py` | provider | wrapper_only | medium | `resolve_custom_provider` | 595 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/providers.py` | provider | wrapper_only | medium | `resolve_provider_full` | 664 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/proxy/cli.py` | provider | wrapper_only | medium | `cmd_proxy_list_providers` | 102 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/runtime_provider.py` | provider | wrapper_only | medium | `_normalize_custom_provider_name` | 38 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/runtime_provider.py` | provider | wrapper_only | medium | `_provider_supports_explicit_api_mode` | 207 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/runtime_provider.py` | provider | wrapper_only | medium | `resolve_requested_provider` | 428 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/runtime_provider.py` | provider | wrapper_only | medium | `_get_named_custom_provider` | 494 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/runtime_provider.py` | provider | wrapper_only | medium | `has_named_custom_provider` | 651 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/runtime_provider.py` | provider | wrapper_only | medium | `find_custom_provider_identity` | 665 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/runtime_provider.py` | provider | wrapper_only | medium | `_custom_provider_request_overrides` | 720 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/runtime_provider.py` | provider | wrapper_only | medium | `resolve_runtime_provider` | 1311 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/runtime_provider.py` | provider | wrapper_only | medium | `format_runtime_provider_error` | 1774 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/security_advisories.py` | gateway | wrapper_only | high | `gateway_log_message` | 441 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/service_manager.py` | gateway | wrapper_only | high | `ServiceManager.register_profile_gateway` | 75 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/service_manager.py` | gateway | wrapper_only | high | `ServiceManager.unregister_profile_gateway` | 82 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/service_manager.py` | gateway | wrapper_only | high | `ServiceManager.list_profile_gateways` | 83 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/service_manager.py` | gateway | wrapper_only | high | `_RegistrationUnsupportedMixin.register_profile_gateway` | 181 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/service_manager.py` | gateway | wrapper_only | high | `_RegistrationUnsupportedMixin.unregister_profile_gateway` | 193 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/service_manager.py` | gateway | wrapper_only | high | `_RegistrationUnsupportedMixin.list_profile_gateways` | 199 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/service_manager.py` | gateway | wrapper_only | high | `_profile_dir_for_gateway_service` | 338 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/service_manager.py` | gateway | wrapper_only | high | `_write_gateway_desired_state` | 359 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/service_manager.py` | gateway | wrapper_only | high | `GatewayNotRegisteredError` | 560 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/service_manager.py` | gateway | wrapper_only | high | `S6ServiceManager.register_profile_gateway` | 899 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/service_manager.py` | gateway | wrapper_only | high | `S6ServiceManager.unregister_profile_gateway` | 985 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/service_manager.py` | gateway | wrapper_only | high | `S6ServiceManager.list_profile_gateways` | 1049 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/session_listing.py` | gateway | wrapper_only | high | `parse_session_listing_args` | 8 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/session_listing.py` | gateway | wrapper_only | high | `query_session_listing` | 36 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/session_listing.py` | gateway | wrapper_only | high | `format_gateway_session_listing` | 71 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/session_recap.py` | tool_registry | feature_flag_required | high | `_tool_call_name_and_args` | 74 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/session_recap.py` | tool_registry | feature_flag_required | high | `_iter_assistant_tool_calls` | 101 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/session_recap.py` | tool_registry | feature_flag_required | high | `_summarise_tool_activity` | 203 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/setup.py` | gateway | wrapper_only | high | `setup_gateway` | 2148 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/setup.py` | gateway | wrapper_only | high | `_gateway_platform_short_label` | 2470 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/setup.py` | provider | wrapper_only | medium | `_supports_same_provider_pool_setup` | 58 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/setup.py` | provider | wrapper_only | medium | `setup_model_provider` | 694 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/setup.py` | provider | wrapper_only | medium | `_setup_tts_provider` | 888 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/setup.py` | tool_registry | feature_flag_required | high | `setup_tools` | 2388 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/skin_engine.py` | tool_registry | feature_flag_required | high | `get_prompt_toolkit_style_overrides` | 846 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/status.py` | provider | wrapper_only | medium | `_effective_provider_label` | 75 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/stdio.py` | tool_registry | feature_flag_required | high | `_augment_path_with_known_tools` | 195 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/subcommands/gateway.py` | gateway | wrapper_only | high | `build_gateway_parser` | 32 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/subcommands/memory.py` | memory | wrapper_only | medium | `build_memory_parser` | 12 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/subcommands/tools.py` | tool_registry | feature_flag_required | high | `build_tools_parser` | 12 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/timeouts.py` | provider | wrapper_only | medium | `get_provider_request_timeout` | 14 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/timeouts.py` | provider | wrapper_only | medium | `get_provider_stale_timeout` | 43 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | gateway | wrapper_only | high | `_hidden_nous_gateway_message` | 2111 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_plugin_image_gen_providers` | 1780 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_plugin_video_gen_providers` | 1820 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_plugin_web_search_providers` | 1868 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_plugin_browser_providers` | 1924 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_plugin_tts_providers` | 1971 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_visible_providers` | 2027 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_is_provider_active` | 2344 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_detect_active_provider_index` | 2419 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_select_plugin_image_gen_provider` | 2618 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_select_plugin_video_gen_provider` | 2718 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_write_provider_config` | 2730 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `apply_provider_selection` | 2775 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_configure_provider` | 2831 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | provider | wrapper_only | medium | `_reconfigure_provider` | 3202 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `gui_toolset_label` | 86 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_toolset_allowed_for_platform` | 156 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_get_effective_configurable_toolsets` | 165 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_get_plugin_toolset_keys` | 191 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_checklist_toolset_keys` | 201 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_platform_toolset_summary` | 1255 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_get_platform_tools` | 1288 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_save_platform_tools` | 1542 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_toolset_has_keys` | 1598 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_estimate_tool_tokens` | 1655 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_prompt_toolset_checklist` | 1697 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_configure_toolset` | 1760 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_toolset_needs_configuration_prompt` | 2161 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_configure_tool_category` | 2230 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_reconfigure_tool` | 3071 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_toolset_enabled_for_reconfigure` | 3117 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_configure_tool_category_for_reconfig` | 3139 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `tools_command` | 3376 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_configure_mcp_tools_interactive` | 3647 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_apply_toolset_change` | 3783 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `_print_tools_list` | 3818 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/tools_config.py` | tool_registry | feature_flag_required | high | `tools_disable_enable_command` | 3860 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/uninstall.py` | gateway | wrapper_only | high | `uninstall_gateway_service` | 179 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/uninstall.py` | tool_registry | feature_flag_required | high | `remove_path_from_windows_registry` | 335 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/uninstall.py` | tool_registry | feature_flag_required | high | `remove_portable_tooling_windows` | 400 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/voice.py` | tool_registry | feature_flag_required | high | `normalize_voice_record_key_for_prompt_toolkit` | 108 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `_has_valid_session_token` | 230 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `_probe_gateway_health` | 879 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `_spawn_gateway_restart` | 2111 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `_restart_gateway_after_webhook_enable` | 2128 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `restart_gateway` | 2151 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `get_sessions` | 2555 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `get_profiles_sessions` | 2641 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `search_sessions` | 2760 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `_gateway_platform_config` | 4239 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `_restart_gateway_after_telegram_onboarding` | 4641 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `_gc_oauth_sessions` | 5313 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `_new_oauth_session` | 5322 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `poll_oauth_session` | 6203 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `cancel_oauth_session` | 6226 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `_session_latest_descendant` | 6269 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `BulkDeleteSessions` | 6356 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `bulk_delete_sessions_endpoint` | 6362 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `count_empty_sessions_endpoint` | 6412 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `delete_empty_sessions_endpoint` | 6427 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `get_session_stats` | 6455 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `_open_session_db_for_profile` | 6485 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `get_session_detail` | 6501 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `get_session_latest_descendant` | 6517 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `get_session_messages` | 6529 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `delete_session_endpoint` | 6543 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `SessionRename` | 6556 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `rename_session_endpoint` | 6565 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `export_session_endpoint` | 6599 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `SessionPrune` | 6614 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `prune_sessions_endpoint` | 6621 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `start_gateway` | 7613 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `stop_gateway` | 7623 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `_build_gateway_ws_url` | 10262 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | gateway | wrapper_only | high | `gateway_ws` | 10517 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_cli/web_server.py` | memory | wrapper_only | medium | `MemoryProviderSelect` | 7758 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/web_server.py` | memory | wrapper_only | medium | `MemoryReset` | 7763 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/web_server.py` | memory | wrapper_only | medium | `get_memory_status` | 7769 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/web_server.py` | memory | wrapper_only | medium | `set_memory_provider` | 7804 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/web_server.py` | memory | wrapper_only | medium | `reset_memory` | 7828 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `hermes_cli/web_server.py` | provider | wrapper_only | medium | `validate_provider_credential` | 3608 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/web_server.py` | provider | wrapper_only | medium | `_resolve_provider_status` | 5068 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/web_server.py` | provider | wrapper_only | medium | `_oauth_provider_disconnect_hint` | 5137 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/web_server.py` | provider | wrapper_only | medium | `list_oauth_providers` | 5147 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/web_server.py` | provider | wrapper_only | medium | `disconnect_oauth_provider` | 5182 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/web_server.py` | provider | wrapper_only | medium | `MemoryProviderSelect` | 7758 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/web_server.py` | provider | wrapper_only | medium | `set_memory_provider` | 7804 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/web_server.py` | provider | wrapper_only | medium | `ToolsetProviderSelect` | 9491 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/web_server.py` | provider | wrapper_only | medium | `select_toolset_provider` | 9497 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/web_server.py` | provider | wrapper_only | medium | `_PluginProvidersPutBody` | 11502 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/web_server.py` | provider | wrapper_only | medium | `put_plugin_providers` | 11508 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `hermes_cli/web_server.py` | tool_registry | feature_flag_required | high | `get_toolsets` | 9356 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/web_server.py` | tool_registry | feature_flag_required | high | `ToolsetToggle` | 9391 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/web_server.py` | tool_registry | feature_flag_required | high | `toggle_toolset` | 9397 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/web_server.py` | tool_registry | feature_flag_required | high | `get_toolset_config` | 9429 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/web_server.py` | tool_registry | feature_flag_required | high | `ToolsetProviderSelect` | 9491 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/web_server.py` | tool_registry | feature_flag_required | high | `select_toolset_provider` | 9497 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/web_server.py` | tool_registry | feature_flag_required | high | `ToolsetEnvUpdate` | 9527 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/web_server.py` | tool_registry | feature_flag_required | high | `save_toolset_env` | 9533 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/web_server.py` | tool_registry | feature_flag_required | high | `ToolsetPostSetup` | 9587 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_cli/web_server.py` | tool_registry | feature_flag_required | high | `run_toolset_post_setup` | 9593 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `hermes_logging.py` | gateway | wrapper_only | high | `set_session_context` | 112 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_logging.py` | gateway | wrapper_only | high | `clear_session_context` | 121 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_logging.py` | gateway | wrapper_only | high | `_install_session_record_factory` | 130 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_logging.py` | gateway | wrapper_only | high | `_install_session_record_factory._session_record_factory` | 147 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `hermes_state.py` | gateway | forbidden | critical | `format_session_db_unavailable` | 187 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB` | 657 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB._insert_session_row` | 1280 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.create_session` | 1311 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.end_session` | 1315 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.reopen_session` | 1333 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.update_session_cwd` | 1342 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.update_session_meta` | 1477 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.update_session_model` | 1505 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.ensure_session` | 1618 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.prune_empty_ghost_sessions` | 1629 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.finalize_orphaned_compression_sessions` | 1659 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.get_session` | 1698 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.resolve_session_id` | 1707 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.set_session_title` | 1781 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.get_session_title` | 1810 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.set_session_archived` | 1819 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.get_session_by_title` | 1871 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.resolve_session_by_title` | 1880 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.list_sessions_rich` | 1980 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB._get_session_rich_row` | 2284 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.resolve_resume_session_id` | 2781 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB._session_lineage_root_to_tip` | 2934 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.search_sessions_by_id` | 3543 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.search_sessions` | 3590 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.session_count` | 3630 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.export_session` | 3698 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB._remove_session_files` | 3731 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.delete_session` | 3757 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.delete_session_if_empty` | 3798 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.delete_sessions` | 3840 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.count_empty_sessions` | 3923 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.delete_empty_sessions` | 3948 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.prune_sessions` | 4015 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.get_telegram_topic_binding_by_session` | 4333 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.is_telegram_session_linked_to_topic` | 4421 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | gateway | forbidden | critical | `SessionDB.list_unlinked_telegram_sessions_for_user` | 4443 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `hermes_state.py` | state_db | forbidden | critical | — | 0 | SessionDB / SQLite / FTS state is a persistence lifeline; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `mcp_serve.py` | gateway | wrapper_only | high | `_get_sessions_dir` | 62 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `mcp_serve.py` | gateway | wrapper_only | high | `_get_session_db` | 71 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `mcp_serve.py` | gateway | wrapper_only | high | `_load_sessions_index` | 81 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `mini_swe_runner.py` | tool_registry | feature_flag_required | high | `MiniSWERunner._format_tools_for_system_message` | 291 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `model_tools.py` | tool_orchestration | forbidden | critical | — | 0 | Tool orchestration layer is high blast-radius; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `model_tools.py` | tool_registry | forbidden | critical | `_get_tool_loop` | 47 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `model_tools.py` | tool_registry | forbidden | critical | `_clear_tool_defs_cache` | 265 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `model_tools.py` | tool_registry | forbidden | critical | `get_tool_definitions` | 272 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `model_tools.py` | tool_registry | forbidden | critical | `_compute_tool_definitions` | 350 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `model_tools.py` | tool_registry | forbidden | critical | `_sanitize_tool_error` | 599 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `model_tools.py` | tool_registry | forbidden | critical | `coerce_tool_args` | 619 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `model_tools.py` | tool_registry | forbidden | critical | `_tool_result_observer_fields` | 815 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `model_tools.py` | tool_registry | forbidden | critical | `_emit_post_tool_call_hook` | 825 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `model_tools.py` | tool_registry | forbidden | critical | `get_all_tool_names` | 1209 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `model_tools.py` | tool_registry | forbidden | critical | `get_toolset_for_tool` | 1214 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `model_tools.py` | tool_registry | forbidden | critical | `get_available_toolsets` | 1219 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `model_tools.py` | tool_registry | forbidden | critical | `check_toolset_requirements` | 1224 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `model_tools.py` | tool_registry | forbidden | critical | `check_tool_availability` | 1229 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py` | gateway | wrapper_only | high | `Migrator.migrate_gateway_config` | 2398 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py` | gateway | wrapper_only | high | `Migrator.migrate_session_config` | 2419 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py` | memory | wrapper_only | medium | `parse_existing_memory_entries` | 441 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py` | memory | wrapper_only | medium | `Migrator.migrate_memory` | 1156 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py` | memory | wrapper_only | medium | `Migrator.migrate_daily_memory` | 1890 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py` | memory | wrapper_only | medium | `Migrator.migrate_memory_backend` | 2761 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py` | provider | wrapper_only | medium | `Migrator.handle_provider_keys` | 1499 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py` | provider | wrapper_only | medium | `Migrator.migrate_provider_keys` | 1514 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py` | provider | wrapper_only | medium | `Migrator.migrate_full_providers` | 2482 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py` | tool_registry | feature_flag_required | high | `Migrator.migrate_tools_config` | 2684 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `optional-skills/productivity/telephony/scripts/telephony.py` | provider | wrapper_only | medium | `_ai_provider` | 454 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `optional-skills/productivity/telephony/scripts/telephony.py` | provider | wrapper_only | medium | `_provider_decision_tree` | 971 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/browser/browser_use/provider.py` | gateway | wrapper_only | high | `BrowserUseBrowserProvider.create_session` | 188 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/browser/browser_use/provider.py` | gateway | wrapper_only | high | `BrowserUseBrowserProvider.close_session` | 253 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/browser/browser_use/provider.py` | provider | wrapper_only | medium | `BrowserUseBrowserProvider` | 104 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/browser/browserbase/provider.py` | gateway | wrapper_only | high | `BrowserbaseBrowserProvider.create_session` | 94 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/browser/browserbase/provider.py` | gateway | wrapper_only | high | `BrowserbaseBrowserProvider.close_session` | 217 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/browser/browserbase/provider.py` | provider | wrapper_only | medium | `BrowserbaseBrowserProvider` | 46 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/browser/firecrawl/provider.py` | gateway | wrapper_only | high | `FirecrawlBrowserProvider.create_session` | 80 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/browser/firecrawl/provider.py` | gateway | wrapper_only | high | `FirecrawlBrowserProvider.close_session` | 118 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/browser/firecrawl/provider.py` | provider | wrapper_only | medium | `FirecrawlBrowserProvider` | 43 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/context_engine/__init__.py` | memory | wrapper_only | medium | `_EngineCollector.register_memory_provider` | 284 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/context_engine/__init__.py` | provider | wrapper_only | medium | `_EngineCollector.register_memory_provider` | 284 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/context_engine/__init__.py` | tool_registry | feature_flag_required | high | `_EngineCollector.register_tool` | 275 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/dashboard_auth/basic/__init__.py` | gateway | wrapper_only | high | `BasicAuthProvider.verify_session` | 263 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/basic/__init__.py` | gateway | wrapper_only | high | `BasicAuthProvider.refresh_session` | 273 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/basic/__init__.py` | gateway | wrapper_only | high | `BasicAuthProvider.revoke_session` | 285 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/basic/__init__.py` | gateway | wrapper_only | high | `BasicAuthProvider._mint_session` | 293 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/basic/__init__.py` | gateway | wrapper_only | high | `BasicAuthProvider._session_from_payload` | 314 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/basic/__init__.py` | provider | wrapper_only | medium | `BasicAuthProvider` | 201 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/dashboard_auth/nous/__init__.py` | gateway | wrapper_only | high | `NousDashboardAuthProvider.refresh_session` | 244 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/nous/__init__.py` | gateway | wrapper_only | high | `NousDashboardAuthProvider._token_response_to_session` | 304 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/nous/__init__.py` | gateway | wrapper_only | high | `NousDashboardAuthProvider.verify_session` | 350 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/nous/__init__.py` | gateway | wrapper_only | high | `NousDashboardAuthProvider.revoke_session` | 368 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/nous/__init__.py` | gateway | wrapper_only | high | `NousDashboardAuthProvider._session_from_claims` | 513 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/nous/__init__.py` | provider | wrapper_only | medium | `NousDashboardAuthProvider` | 153 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/dashboard_auth/self_hosted/__init__.py` | gateway | wrapper_only | high | `SelfHostedOIDCProvider.refresh_session` | 255 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/self_hosted/__init__.py` | gateway | wrapper_only | high | `SelfHostedOIDCProvider.verify_session` | 276 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/self_hosted/__init__.py` | gateway | wrapper_only | high | `SelfHostedOIDCProvider.revoke_session` | 295 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/self_hosted/__init__.py` | gateway | wrapper_only | high | `SelfHostedOIDCProvider._session_from_tokens` | 545 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/dashboard_auth/self_hosted/__init__.py` | provider | wrapper_only | medium | `SelfHostedOIDCProvider` | 163 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/disk-cleanup/__init__.py` | gateway | wrapper_only | high | `_on_session_end` | 155 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/disk-cleanup/__init__.py` | tool_registry | feature_flag_required | high | `_on_post_tool_call` | 128 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/google_meet/__init__.py` | gateway | wrapper_only | high | `_on_session_end` | 50 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/google_meet/node/registry.py` | tool_registry | feature_flag_required | high | `NodeRegistry` | 34 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/google_meet/realtime/openai_client.py` | gateway | wrapper_only | high | `RealtimeSession` | 39 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/hermes-achievements/dashboard/plugin_api.py` | gateway | wrapper_only | high | `session_fingerprint` | 225 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/hermes-achievements/dashboard/plugin_api.py` | gateway | wrapper_only | high | `scan_sessions` | 560 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/hermes-achievements/dashboard/plugin_api.py` | gateway | wrapper_only | high | `session_badges` | 1023 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/hermes-achievements/dashboard/plugin_api.py` | provider | wrapper_only | medium | `model_provider` | 290 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/hermes-achievements/dashboard/plugin_api.py` | tool_registry | feature_flag_required | high | `_tool_name_from_call` | 266 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/hermes-achievements/dashboard/plugin_api.py` | tool_registry | feature_flag_required | high | `_count_tool` | 285 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/image_gen/fal/__init__.py` | provider | wrapper_only | medium | `FalImageGenProvider` | 40 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/image_gen/krea/__init__.py` | provider | wrapper_only | medium | `KreaImageGenProvider` | 161 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/image_gen/openai-codex/__init__.py` | provider | wrapper_only | medium | `OpenAICodexImageGenProvider` | 283 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/image_gen/openai/__init__.py` | provider | wrapper_only | medium | `OpenAIImageGenProvider` | 125 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/image_gen/xai/__init__.py` | provider | wrapper_only | medium | `XAIImageGenProvider` | 122 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/__init__.py` | memory | wrapper_only | medium | `_is_memory_provider_dir` | 74 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/__init__.py` | memory | wrapper_only | medium | `discover_memory_providers` | 146 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/__init__.py` | memory | wrapper_only | medium | `load_memory_provider` | 183 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/__init__.py` | memory | wrapper_only | medium | `_ProviderCollector.register_memory_provider` | 325 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/__init__.py` | memory | wrapper_only | medium | `_get_active_memory_provider` | 339 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/__init__.py` | provider | wrapper_only | medium | `_is_memory_provider_dir` | 74 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/__init__.py` | provider | wrapper_only | medium | `_iter_provider_dirs` | 90 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/__init__.py` | provider | wrapper_only | medium | `find_provider_dir` | 124 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/__init__.py` | provider | wrapper_only | medium | `discover_memory_providers` | 146 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/__init__.py` | provider | wrapper_only | medium | `load_memory_provider` | 183 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/__init__.py` | provider | wrapper_only | medium | `_load_provider_from_dir` | 208 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/__init__.py` | provider | wrapper_only | medium | `_ProviderCollector` | 319 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/__init__.py` | provider | wrapper_only | medium | `_ProviderCollector.register_memory_provider` | 325 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/__init__.py` | provider | wrapper_only | medium | `_get_active_memory_provider` | 339 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/__init__.py` | tool_registry | feature_flag_required | high | `_ProviderCollector.register_tool` | 329 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/byterover/__init__.py` | memory | wrapper_only | medium | `ByteRoverMemoryProvider` | 172 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/byterover/__init__.py` | memory | wrapper_only | medium | `ByteRoverMemoryProvider.on_memory_write` | 265 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/byterover/__init__.py` | provider | wrapper_only | medium | `ByteRoverMemoryProvider` | 172 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/byterover/__init__.py` | tool_registry | feature_flag_required | high | `ByteRoverMemoryProvider.get_tool_schemas` | 315 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/byterover/__init__.py` | tool_registry | feature_flag_required | high | `ByteRoverMemoryProvider.handle_tool_call` | 318 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/byterover/__init__.py` | tool_registry | feature_flag_required | high | `ByteRoverMemoryProvider._tool_query` | 333 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/byterover/__init__.py` | tool_registry | feature_flag_required | high | `ByteRoverMemoryProvider._tool_curate` | 356 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/byterover/__init__.py` | tool_registry | feature_flag_required | high | `ByteRoverMemoryProvider._tool_status` | 371 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/hindsight/__init__.py` | gateway | wrapper_only | high | `HindsightMemoryProvider.on_session_switch` | 1675 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/hindsight/__init__.py` | memory | wrapper_only | medium | `HindsightMemoryProvider` | 570 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/hindsight/__init__.py` | provider | wrapper_only | medium | `HindsightMemoryProvider` | 570 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/hindsight/__init__.py` | tool_registry | feature_flag_required | high | `HindsightMemoryProvider.get_tool_schemas` | 1597 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/hindsight/__init__.py` | tool_registry | feature_flag_required | high | `HindsightMemoryProvider.handle_tool_call` | 1602 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/holographic/__init__.py` | gateway | wrapper_only | high | `HolographicMemoryProvider.on_session_end` | 237 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/holographic/__init__.py` | memory | wrapper_only | medium | `HolographicMemoryProvider` | 115 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/holographic/__init__.py` | memory | wrapper_only | medium | `HolographicMemoryProvider.on_memory_write` | 244 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/holographic/__init__.py` | provider | wrapper_only | medium | `HolographicMemoryProvider` | 115 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/holographic/__init__.py` | tool_registry | feature_flag_required | high | `HolographicMemoryProvider.get_tool_schemas` | 227 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/holographic/__init__.py` | tool_registry | feature_flag_required | high | `HolographicMemoryProvider.handle_tool_call` | 230 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/holographic/store.py` | memory | wrapper_only | medium | `MemoryStore` | 98 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/honcho/__init__.py` | gateway | wrapper_only | high | `HonchoMemoryProvider._resolve_session_key` | 357 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/__init__.py` | gateway | wrapper_only | high | `HonchoMemoryProvider._start_session_init_background` | 371 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/__init__.py` | gateway | wrapper_only | high | `HonchoMemoryProvider._do_session_init` | 417 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/__init__.py` | gateway | wrapper_only | high | `HonchoMemoryProvider._ensure_session` | 504 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/__init__.py` | gateway | wrapper_only | high | `HonchoMemoryProvider._session_ready` | 534 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/__init__.py` | gateway | wrapper_only | high | `HonchoMemoryProvider.on_session_end` | 1270 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/__init__.py` | memory | wrapper_only | medium | `HonchoMemoryProvider` | 191 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/honcho/__init__.py` | memory | wrapper_only | medium | `HonchoMemoryProvider.on_memory_write` | 1237 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/honcho/__init__.py` | provider | wrapper_only | medium | `HonchoMemoryProvider` | 191 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/honcho/__init__.py` | tool_registry | feature_flag_required | high | `HonchoMemoryProvider.get_tool_schemas` | 1286 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/honcho/__init__.py` | tool_registry | feature_flag_required | high | `HonchoMemoryProvider.handle_tool_call` | 1297 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/honcho/cli.py` | gateway | wrapper_only | high | `_gateway_platforms` | 394 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/cli.py` | gateway | wrapper_only | high | `cmd_sessions` | 1151 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/client.py` | gateway | wrapper_only | high | `HonchoClientConfig._enforce_session_id_limit` | 648 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/client.py` | gateway | wrapper_only | high | `HonchoClientConfig.resolve_session_name` | 672 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/session.py` | gateway | wrapper_only | high | `HonchoSession` | 28 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/session.py` | gateway | wrapper_only | high | `HonchoSessionManager` | 71 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/session.py` | gateway | wrapper_only | high | `HonchoSessionManager._get_or_create_honcho_session` | 178 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/session.py` | gateway | wrapper_only | high | `HonchoSessionManager._session_key_fallback_peer_id` | 287 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/session.py` | gateway | wrapper_only | high | `HonchoSessionManager._flush_session` | 419 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/session.py` | gateway | wrapper_only | high | `HonchoSessionManager.new_session` | 560 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/session.py` | gateway | wrapper_only | high | `HonchoSessionManager.get_session_context` | 991 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/session.py` | gateway | wrapper_only | high | `HonchoSessionManager.list_sessions` | 1331 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/honcho/session.py` | memory | wrapper_only | medium | `HonchoSessionManager.migrate_memory_files` | 821 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/mem0/__init__.py` | memory | wrapper_only | medium | `Mem0MemoryProvider` | 119 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/mem0/__init__.py` | provider | wrapper_only | medium | `Mem0MemoryProvider` | 119 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/mem0/__init__.py` | tool_registry | feature_flag_required | high | `Mem0MemoryProvider.get_tool_schemas` | 298 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/mem0/__init__.py` | tool_registry | feature_flag_required | high | `Mem0MemoryProvider.handle_tool_call` | 301 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/openviking/__init__.py` | gateway | wrapper_only | high | `_atexit_commit_sessions` | 78 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/openviking/__init__.py` | gateway | wrapper_only | high | `OpenVikingMemoryProvider.on_session_end` | 605 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/openviking/__init__.py` | memory | wrapper_only | medium | `OpenVikingMemoryProvider` | 412 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/openviking/__init__.py` | memory | wrapper_only | medium | `OpenVikingMemoryProvider._build_memory_uri` | 629 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/openviking/__init__.py` | memory | wrapper_only | medium | `OpenVikingMemoryProvider.on_memory_write` | 634 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/openviking/__init__.py` | provider | wrapper_only | medium | `OpenVikingMemoryProvider` | 412 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/openviking/__init__.py` | tool_registry | feature_flag_required | high | `OpenVikingMemoryProvider.get_tool_schemas` | 665 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/openviking/__init__.py` | tool_registry | feature_flag_required | high | `OpenVikingMemoryProvider.handle_tool_call` | 668 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/openviking/__init__.py` | tool_registry | feature_flag_required | high | `OpenVikingMemoryProvider._tool_search` | 739 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/openviking/__init__.py` | tool_registry | feature_flag_required | high | `OpenVikingMemoryProvider._tool_read` | 781 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/openviking/__init__.py` | tool_registry | feature_flag_required | high | `OpenVikingMemoryProvider._tool_browse` | 854 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/openviking/__init__.py` | tool_registry | feature_flag_required | high | `OpenVikingMemoryProvider._tool_remember` | 886 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/openviking/__init__.py` | tool_registry | feature_flag_required | high | `OpenVikingMemoryProvider._tool_add_resource` | 913 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/retaindb/__init__.py` | gateway | wrapper_only | high | `_Client.ingest_session` | 263 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/retaindb/__init__.py` | memory | wrapper_only | medium | `_Client.add_memory` | 245 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/retaindb/__init__.py` | memory | wrapper_only | medium | `_Client.delete_memory` | 257 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/retaindb/__init__.py` | memory | wrapper_only | medium | `RetainDBMemoryProvider` | 452 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/retaindb/__init__.py` | memory | wrapper_only | medium | `RetainDBMemoryProvider.on_memory_write` | 747 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/retaindb/__init__.py` | provider | wrapper_only | medium | `RetainDBMemoryProvider` | 452 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/retaindb/__init__.py` | tool_registry | feature_flag_required | high | `RetainDBMemoryProvider.get_tool_schemas` | 643 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/retaindb/__init__.py` | tool_registry | feature_flag_required | high | `RetainDBMemoryProvider.handle_tool_call` | 651 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/supermemory/__init__.py` | gateway | wrapper_only | high | `SupermemoryMemoryProvider.on_session_end` | 596 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/supermemory/__init__.py` | gateway | wrapper_only | high | `SupermemoryMemoryProvider.on_session_switch` | 629 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/memory/supermemory/__init__.py` | memory | wrapper_only | medium | `_load_supermemory_config` | 98 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/supermemory/__init__.py` | memory | wrapper_only | medium | `_save_supermemory_config` | 144 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/supermemory/__init__.py` | memory | wrapper_only | medium | `_SupermemoryClient` | 264 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/supermemory/__init__.py` | memory | wrapper_only | medium | `_SupermemoryClient.add_memory` | 289 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/supermemory/__init__.py` | memory | wrapper_only | medium | `_SupermemoryClient.forget_memory` | 351 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/supermemory/__init__.py` | memory | wrapper_only | medium | `SupermemoryMemoryProvider` | 440 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/supermemory/__init__.py` | memory | wrapper_only | medium | `SupermemoryMemoryProvider.on_memory_write` | 674 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `plugins/memory/supermemory/__init__.py` | provider | wrapper_only | medium | `SupermemoryMemoryProvider` | 440 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/memory/supermemory/__init__.py` | tool_registry | feature_flag_required | high | `SupermemoryMemoryProvider._resolve_tool_container_tag` | 728 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/supermemory/__init__.py` | tool_registry | feature_flag_required | high | `SupermemoryMemoryProvider.get_tool_schemas` | 748 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/supermemory/__init__.py` | tool_registry | feature_flag_required | high | `SupermemoryMemoryProvider._tool_store` | 781 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/supermemory/__init__.py` | tool_registry | feature_flag_required | high | `SupermemoryMemoryProvider._tool_search` | 804 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/supermemory/__init__.py` | tool_registry | feature_flag_required | high | `SupermemoryMemoryProvider._tool_forget` | 834 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/supermemory/__init__.py` | tool_registry | feature_flag_required | high | `SupermemoryMemoryProvider._tool_profile` | 851 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/memory/supermemory/__init__.py` | tool_registry | feature_flag_required | high | `SupermemoryMemoryProvider.handle_tool_call` | 875 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/observability/langfuse/__init__.py` | tool_registry | feature_flag_required | high | `_serialize_tool_calls` | 473 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/observability/langfuse/__init__.py` | tool_registry | feature_flag_required | high | `_assistant_has_tool_calls` | 704 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/observability/langfuse/__init__.py` | tool_registry | feature_flag_required | high | `on_pre_tool_call` | 952 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/observability/langfuse/__init__.py` | tool_registry | feature_flag_required | high | `on_post_tool_call` | 978 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/observability/nemo_relay/__init__.py` | gateway | wrapper_only | high | `_SessionState` | 25 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/observability/nemo_relay/__init__.py` | gateway | wrapper_only | high | `_Runtime.ensure_session` | 168 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/observability/nemo_relay/__init__.py` | gateway | wrapper_only | high | `_Runtime.close_session` | 218 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/observability/nemo_relay/__init__.py` | gateway | wrapper_only | high | `on_session_start` | 424 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/observability/nemo_relay/__init__.py` | gateway | wrapper_only | high | `on_session_end` | 430 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/observability/nemo_relay/__init__.py` | gateway | wrapper_only | high | `on_session_finalize` | 436 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/observability/nemo_relay/__init__.py` | gateway | wrapper_only | high | `on_session_reset` | 442 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/observability/nemo_relay/__init__.py` | gateway | wrapper_only | high | `_session_id` | 736 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/observability/nemo_relay/__init__.py` | gateway | wrapper_only | high | `_child_session_id` | 740 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/observability/nemo_relay/__init__.py` | tool_registry | feature_flag_required | high | `_Runtime.managed_tool_enabled` | 282 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/observability/nemo_relay/__init__.py` | tool_registry | feature_flag_required | high | `_Runtime.execute_tool` | 365 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/observability/nemo_relay/__init__.py` | tool_registry | feature_flag_required | high | `on_pre_tool_call` | 531 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/observability/nemo_relay/__init__.py` | tool_registry | feature_flag_required | high | `on_post_tool_call` | 553 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/observability/nemo_relay/__init__.py` | tool_registry | feature_flag_required | high | `on_tool_execution_middleware` | 611 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/observability/nemo_relay/__init__.py` | tool_registry | feature_flag_required | high | `_tool_key` | 772 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/observability/nemo_relay/__init__.py` | tool_registry | feature_flag_required | high | `_tool_calls_payload` | 904 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/platforms/discord/adapter.py` | gateway | wrapper_only | high | `DiscordAdapter._dispatch_thread_session` | 3954 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/platforms/discord/adapter.py` | gateway | wrapper_only | high | `_define_discord_view_classes.ExecApprovalView.allow_session` | 5536 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/platforms/discord/adapter.py` | provider | wrapper_only | medium | `_define_discord_view_classes.ModelPickerView._build_provider_select` | 5818 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/platforms/discord/adapter.py` | provider | wrapper_only | medium | `_define_discord_view_classes.ModelPickerView._on_provider_selected` | 5927 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/platforms/google_chat/adapter.py` | tool_registry | feature_flag_required | high | `_check_for_registry` | 2959 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/platforms/line/adapter.py` | gateway | wrapper_only | high | `LineAdapter.interrupt_session_activity` | 1226 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/platforms/photon/auth.py` | gateway | wrapper_only | high | `get_session` | 601 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/platforms/photon/cli.py` | gateway | wrapper_only | high | `gateway_setup` | 414 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/platforms/teams/adapter.py` | provider | wrapper_only | medium | `_StaticAccessTokenProvider` | 127 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/security-guidance/__init__.py` | tool_registry | feature_flag_required | high | `_on_pre_tool_call` | 202 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/security-guidance/__init__.py` | tool_registry | feature_flag_required | high | `_on_transform_tool_result` | 227 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/spotify/tools.py` | tool_registry | feature_flag_required | high | `_spotify_tool_error` | 31 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/teams_pipeline/runtime.py` | gateway | wrapper_only | high | `bind_gateway_runtime` | 98 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/video_gen/fal/__init__.py` | gateway | wrapper_only | high | `_resolve_managed_fal_video_gateway` | 326 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/video_gen/fal/__init__.py` | provider | wrapper_only | medium | `FALVideoGenProvider` | 408 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/video_gen/xai/__init__.py` | provider | wrapper_only | medium | `XAIVideoGenProvider` | 250 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/web/brave_free/provider.py` | provider | wrapper_only | medium | `BraveFreeWebSearchProvider` | 33 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/web/ddgs/provider.py` | provider | wrapper_only | medium | `DDGSWebSearchProvider` | 23 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/web/exa/provider.py` | provider | wrapper_only | medium | `ExaWebSearchProvider` | 85 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/web/firecrawl/provider.py` | gateway | wrapper_only | high | `_get_firecrawl_gateway_url` | 139 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/web/firecrawl/provider.py` | gateway | wrapper_only | high | `_is_tool_gateway_ready` | 146 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `plugins/web/firecrawl/provider.py` | provider | wrapper_only | medium | `FirecrawlWebSearchProvider` | 367 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/web/firecrawl/provider.py` | tool_registry | feature_flag_required | high | `_is_tool_gateway_ready` | 146 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `plugins/web/parallel/provider.py` | provider | wrapper_only | medium | `ParallelWebSearchProvider` | 143 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/web/searxng/provider.py` | provider | wrapper_only | medium | `SearXNGWebSearchProvider` | 47 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/web/tavily/provider.py` | provider | wrapper_only | medium | `TavilyWebSearchProvider` | 128 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `plugins/web/xai/provider.py` | provider | wrapper_only | medium | `XAIWebSearchProvider` | 96 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `providers/__init__.py` | provider | forbidden | critical | — | 0 | Provider registration controls model backends; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `providers/__init__.py` | provider | forbidden | critical | `register_provider` | 53 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `providers/__init__.py` | provider | forbidden | critical | `get_provider_profile` | 65 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `providers/__init__.py` | provider | forbidden | critical | `list_providers` | 76 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `providers/__init__.py` | provider | forbidden | critical | `_discover_providers` | 140 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `providers/base.py` | provider | forbidden | high | — | 0 | Provider base contracts affect all providers; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `providers/base.py` | provider | forbidden | critical | `ProviderProfile` | 39 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | gateway | forbidden | critical | `_launch_cwd_for_session` | 68 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | gateway | forbidden | critical | `AIAgent._get_session_db_for_recall` | 490 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | gateway | forbidden | critical | `AIAgent._ensure_db_session` | 509 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | gateway | forbidden | critical | `AIAgent._transition_context_engine_session` | 533 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | gateway | forbidden | critical | `AIAgent.reset_session_state` | 602 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | gateway | forbidden | critical | `AIAgent._persist_session` | 1479 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | gateway | forbidden | critical | `AIAgent._flush_messages_to_session_db` | 1548 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | gateway | forbidden | critical | `AIAgent._clean_session_content` | 2187 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | gateway | forbidden | critical | `AIAgent._save_session_log` | 2226 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | gateway | forbidden | critical | `AIAgent.commit_memory_session` | 2989 | Gateway/session-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | memory | forbidden | critical | `AIAgent._build_memory_write_metadata` | 1443 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | memory | forbidden | critical | `AIAgent.shutdown_memory_provider` | 2962 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | memory | forbidden | critical | `AIAgent.commit_memory_session` | 2989 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | memory | forbidden | critical | `AIAgent._sync_external_memory_for_turn` | 3014 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | provider | forbidden | critical | `AIAgent._is_provider_stream_parse_error` | 961 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | provider | forbidden | critical | `AIAgent._provider_model_requires_responses_api` | 1232 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | provider | forbidden | critical | `AIAgent.shutdown_memory_provider` | 2962 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | provider | forbidden | critical | `AIAgent._provider_supports_vision_tool_messages` | 4383 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | provider | forbidden | critical | `AIAgent._reapply_reasoning_echo_for_provider` | 4985 | Provider-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | runtime_loop | forbidden | critical | — | 0 | AIAgent runtime loop is the core execution path; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._should_emit_quiet_tool_messages` | 756 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._format_tools_for_system_message` | 1672 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._apply_pending_steer_to_tool_results` | 2721 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._get_tool_call_id_static` | 3246 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._get_tool_call_name_static` | 3253 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._deduplicate_tool_calls` | 3390 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._repair_tool_call` | 3407 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._split_responses_tool_id` | 3428 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._fire_tool_gen_started` | 4209 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._provider_supports_vision_tool_messages` | 4383 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._tool_result_content_for_active_model` | 4522 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._try_strip_image_parts_from_tool_messages` | 4598 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._needs_kimi_tool_reasoning` | 4929 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._needs_deepseek_tool_reasoning` | 4949 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._needs_mimo_tool_reasoning` | 4964 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._sanitize_tool_calls_for_strict_api` | 4991 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._sanitize_tool_call_arguments` | 5028 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._should_sanitize_tool_calls` | 5038 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._set_tool_guardrail_halt` | 5066 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._toolguard_controlled_halt_response` | 5071 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._execute_tool_calls` | 5104 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._invoke_tool` | 5147 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._execute_tool_calls_concurrent` | 5191 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `run_agent.py` | tool_registry | forbidden | critical | `AIAgent._execute_tool_calls_sequential` | 5196 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `scripts/analyze_livetest.py` | tool_registry | feature_flag_required | high | `fmt_tool_seq` | 26 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `scripts/discord-voice-doctor.py` | tool_registry | feature_flag_required | high | `check_system_tools` | 121 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `scripts/lint_diff.py` | tool_registry | feature_flag_required | high | `_tool_report` | 135 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `scripts/profile-tui.py` | gateway | wrapper_only | high | `pick_longest_session` | 65 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `scripts/release.py` | tool_registry | feature_flag_required | high | `_update_acp_registry_versions` | 1679 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `scripts/tool_search_livetest.py` | tool_registry | feature_flag_required | high | `register_fake_tools` | 305 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `skills/creative/comfyui/scripts/_common.py` | gateway | wrapper_only | high | `_StripSensitiveOnRedirectSession` | 496 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `set_current_session_key` | 77 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `reset_current_session_key` | 82 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `get_current_session_key` | 108 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `_get_session_platform` | 123 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `_is_gateway_approval_context` | 133 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `register_gateway_notify` | 702 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `unregister_gateway_notify` | 714 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `resolve_gateway_approval` | 727 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `approve_session` | 768 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `enable_session_yolo` | 774 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `disable_session_yolo` | 782 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `clear_session` | 790 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `is_session_yolo_enabled` | 806 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `is_current_session_yolo_enabled` | 814 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/approval.py` | gateway | wrapper_only | high | `_await_gateway_decision` | 1233 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_camofox.py` | gateway | wrapper_only | high | `_get_session` | 295 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_camofox.py` | gateway | wrapper_only | high | `_drop_session` | 359 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_supervisor.py` | tool_registry | feature_flag_required | high | `_SupervisorRegistry` | 1382 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/browser_tool.py` | gateway | wrapper_only | high | `_navigation_session_key` | 1063 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_tool.py` | gateway | wrapper_only | high | `_last_session_key` | 1098 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_tool.py` | gateway | wrapper_only | high | `_get_session_inactivity_timeout` | 1188 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_tool.py` | gateway | wrapper_only | high | `_emergency_cleanup_all_sessions` | 1214 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_tool.py` | gateway | wrapper_only | high | `_cleanup_inactive_browser_sessions` | 1265 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_tool.py` | gateway | wrapper_only | high | `_reap_orphaned_browser_sessions` | 1311 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_tool.py` | gateway | wrapper_only | high | `_update_session_activity` | 1476 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_tool.py` | gateway | wrapper_only | high | `_create_local_session` | 1644 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_tool.py` | gateway | wrapper_only | high | `_create_cdp_session` | 1657 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_tool.py` | gateway | wrapper_only | high | `_get_session_info` | 1671 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_tool.py` | gateway | wrapper_only | high | `_cleanup_single_browser_session` | 3452 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/browser_tool.py` | provider | wrapper_only | medium | `_is_legacy_provider_registry_overridden` | 446 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/browser_tool.py` | provider | wrapper_only | medium | `_get_cloud_provider` | 489 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/browser_tool.py` | tool_registry | feature_flag_required | high | `_is_legacy_provider_registry_overridden` | 446 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/clarify_gateway.py` | gateway | wrapper_only | high | `resolve_gateway_clarify` | 150 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/clarify_gateway.py` | gateway | wrapper_only | high | `get_pending_for_session` | 165 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/clarify_gateway.py` | gateway | wrapper_only | high | `clear_session` | 203 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/clarify_tool.py` | tool_registry | feature_flag_required | high | `clarify_tool` | 23 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/code_execution_tool.py` | tool_registry | feature_flag_required | high | `generate_hermes_tools_module` | 259 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/computer_use/cua_backend.py` | gateway | wrapper_only | high | `_CuaDriverSession` | 255 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/computer_use/cua_backend.py` | gateway | wrapper_only | high | `_CuaDriverSession._is_closed_session_error` | 320 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/computer_use/cua_backend.py` | gateway | wrapper_only | high | `_CuaDriverSession._restart_session_locked` | 330 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/computer_use/cua_backend.py` | tool_registry | feature_flag_required | high | `_CuaDriverSession._call_tool_async` | 315 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/computer_use/cua_backend.py` | tool_registry | feature_flag_required | high | `_CuaDriverSession.call_tool` | 341 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/computer_use/cua_backend.py` | tool_registry | feature_flag_required | high | `_extract_tool_result` | 357 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/computer_use/vision_routing.py` | provider | wrapper_only | medium | `_provider_accepts_multimodal_tool_result` | 143 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/computer_use/vision_routing.py` | tool_registry | feature_flag_required | high | `_provider_accepts_multimodal_tool_result` | 143 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/debug_helpers.py` | gateway | wrapper_only | high | `DebugSession` | 36 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/debug_helpers.py` | gateway | wrapper_only | high | `DebugSession.get_session_info` | 91 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/delegate_tool.py` | tool_registry | feature_flag_required | high | `_stringify_tool_content` | 281 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/delegate_tool.py` | tool_registry | feature_flag_required | high | `_get_inherit_mcp_toolsets` | 530 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/delegate_tool.py` | tool_registry | feature_flag_required | high | `_is_mcp_toolset_name` | 536 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/delegate_tool.py` | tool_registry | feature_flag_required | high | `_expand_parent_toolsets` | 551 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/delegate_tool.py` | tool_registry | feature_flag_required | high | `_preserve_parent_mcp_toolsets` | 582 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/delegate_tool.py` | tool_registry | feature_flag_required | high | `_strip_blocked_tools` | 759 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/discord_tool.py` | tool_registry | feature_flag_required | high | `check_discord_tool_requirements` | 818 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/env_passthrough.py` | provider | wrapper_only | medium | `_is_hermes_provider_credential` | 48 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/environments/base.py` | gateway | wrapper_only | high | `BaseEnvironment.init_session` | 351 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/environments/local.py` | provider | wrapper_only | medium | `_build_provider_env_blocklist` | 100 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/file_operations.py` | tool_registry | feature_flag_required | high | `_split_tool_diagnostics` | 301 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/file_state.py` | tool_registry | feature_flag_required | high | `FileStateRegistry` | 59 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/file_state.py` | tool_registry | feature_flag_required | high | `get_registry` | 265 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/file_tools.py` | tool_registry | feature_flag_required | high | `read_file_tool` | 784 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/file_tools.py` | tool_registry | feature_flag_required | high | `notify_other_tool_call` | 1076 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/file_tools.py` | tool_registry | feature_flag_required | high | `write_file_tool` | 1181 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/file_tools.py` | tool_registry | feature_flag_required | high | `patch_tool` | 1259 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/file_tools.py` | tool_registry | feature_flag_required | high | `search_tool` | 1430 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/image_generation_tool.py` | gateway | wrapper_only | high | `_resolve_managed_fal_gateway` | 401 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/image_generation_tool.py` | provider | wrapper_only | medium | `_read_configured_image_provider` | 1048 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/image_generation_tool.py` | provider | wrapper_only | medium | `_dispatch_to_plugin_provider` | 1072 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/image_generation_tool.py` | tool_registry | feature_flag_required | high | `image_generate_tool` | 724 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/kanban_tools.py` | gateway | wrapper_only | high | `_stamp_worker_session_metadata` | 118 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/kanban_tools.py` | tool_registry | feature_flag_required | high | `_profile_has_kanban_toolset` | 49 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/kanban_tools.py` | tool_registry | feature_flag_required | high | `_require_orchestrator_tool` | 291 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/managed_tool_gateway.py` | gateway | wrapper_only | high | `ManagedToolGatewayConfig` | 23 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/managed_tool_gateway.py` | gateway | wrapper_only | high | `get_tool_gateway_scheme` | 124 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/managed_tool_gateway.py` | gateway | wrapper_only | high | `build_vendor_gateway_url` | 136 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/managed_tool_gateway.py` | gateway | wrapper_only | high | `resolve_managed_tool_gateway` | 151 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/managed_tool_gateway.py` | gateway | wrapper_only | high | `is_managed_tool_gateway_ready` | 176 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/managed_tool_gateway.py` | provider | wrapper_only | medium | `_read_nous_provider_state` | 35 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/managed_tool_gateway.py` | tool_registry | feature_flag_required | high | `ManagedToolGatewayConfig` | 23 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/managed_tool_gateway.py` | tool_registry | feature_flag_required | high | `get_tool_gateway_scheme` | 124 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/managed_tool_gateway.py` | tool_registry | feature_flag_required | high | `resolve_managed_tool_gateway` | 151 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/managed_tool_gateway.py` | tool_registry | feature_flag_required | high | `is_managed_tool_gateway_ready` | 176 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_oauth_manager.py` | provider | wrapper_only | medium | `_ProviderEntry` | 52 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/mcp_oauth_manager.py` | provider | wrapper_only | medium | `_make_hermes_provider_class` | 84 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/mcp_oauth_manager.py` | provider | wrapper_only | medium | `_make_hermes_provider_class.HermesMCPOAuthProvider` | 95 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/mcp_oauth_manager.py` | provider | wrapper_only | medium | `MCPOAuthManager.get_or_build_provider` | 353 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/mcp_oauth_manager.py` | provider | wrapper_only | medium | `MCPOAuthManager._build_provider` | 388 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/mcp_tool.py` | gateway | wrapper_only | high | `SamplingHandler.session_kwargs` | 1005 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/mcp_tool.py` | gateway | wrapper_only | high | `_is_session_expired_error` | 2340 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/mcp_tool.py` | gateway | wrapper_only | high | `_handle_session_expired_and_retry` | 2366 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `SamplingHandler._extract_tool_result_text` | 840 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `SamplingHandler._build_tool_use_result` | 927 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `MCPServerTask._advertises_tools` | 1206 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `MCPServerTask._refresh_tools_task` | 1228 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `MCPServerTask._schedule_tools_refresh` | 1237 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `MCPServerTask._refresh_tools` | 1287 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `MCPServerTask._discover_tools` | 1817 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `_make_tool_handler` | 2767 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `_track_mcp_tool_server` | 3444 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `_forget_mcp_tool_server` | 3451 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `_existing_tool_names` | 3514 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `_register_server_tools` | 3527 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `discover_mcp_tools` | 3775 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `is_mcp_tool_parallel_safe` | 3824 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/mcp_tool.py` | tool_registry | feature_flag_required | high | `probe_mcp_server_tools` | 3922 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/memory_tool.py` | memory | forbidden | critical | — | 0 | Memory tool writes native memory; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `tools/memory_tool.py` | memory | forbidden | critical | `get_memory_dir` | 55 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/memory_tool.py` | memory | forbidden | critical | `_scan_memory_content` | 78 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/memory_tool.py` | memory | forbidden | critical | `MemoryStore` | 113 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/memory_tool.py` | memory | forbidden | critical | `memory_tool` | 666 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/memory_tool.py` | memory | forbidden | critical | `check_memory_requirements` | 715 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/memory_tool.py` | memory | forbidden | critical | `apply_memory_pending` | 720 | Memory-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/memory_tool.py` | tool_registry | forbidden | critical | `memory_tool` | 666 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/microsoft_graph_auth.py` | provider | wrapper_only | medium | `MicrosoftGraphTokenProvider` | 104 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/mixture_of_agents_tool.py` | tool_registry | feature_flag_required | high | `mixture_of_agents_tool` | 236 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/process_registry.py` | gateway | wrapper_only | high | `ProcessSession` | 90 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/process_registry.py` | gateway | wrapper_only | high | `ProcessRegistry._refresh_detached_session` | 419 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/process_registry.py` | gateway | wrapper_only | high | `ProcessRegistry.list_sessions` | 1310 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/process_registry.py` | gateway | wrapper_only | high | `ProcessRegistry.has_active_for_session` | 1355 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/process_registry.py` | tool_registry | feature_flag_required | high | `ProcessRegistry` | 140 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/read_terminal_tool.py` | tool_registry | feature_flag_required | high | `read_terminal_tool` | 18 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/registry.py` | tool_registry | forbidden | critical | — | 0 | Tool registry controls discovery and invocation surface; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `tools/registry.py` | tool_registry | forbidden | critical | `_is_registry_register_call` | 29 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `_module_registers_tools` | 42 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `discover_builtin_tools` | 57 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolEntry` | 77 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry` | 151 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry._snapshot_toolset_checks` | 178 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry._evaluate_toolset_check` | 182 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.get_registered_toolset_names` | 197 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.get_tool_names_for_toolset` | 201 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.register_toolset_alias` | 208 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.get_registered_toolset_aliases` | 220 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.get_toolset_alias_target` | 225 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.get_all_tool_names` | 432 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.get_toolset_for_tool` | 445 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.get_tool_to_toolset_map` | 455 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.is_toolset_available` | 459 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.check_toolset_requirements` | 469 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.get_available_toolsets` | 478 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.get_toolset_requirements` | 500 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `ToolRegistry.check_tool_availability` | 521 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `tool_error` | 563 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/registry.py` | tool_registry | forbidden | critical | `tool_result` | 577 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `tools/schema_sanitizer.py` | tool_registry | feature_flag_required | high | `sanitize_tool_schemas` | 46 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/schema_sanitizer.py` | tool_registry | feature_flag_required | high | `_sanitize_single_tool` | 64 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/send_message_tool.py` | tool_registry | feature_flag_required | high | `send_message_tool` | 174 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/session_search_tool.py` | gateway | wrapper_only | high | `_locate_session_db` | 134 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/session_search_tool.py` | gateway | wrapper_only | high | `_read_session` | 178 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/session_search_tool.py` | gateway | wrapper_only | high | `_list_recent_sessions` | 227 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/session_search_tool.py` | gateway | wrapper_only | high | `session_search` | 495 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/session_search_tool.py` | gateway | wrapper_only | high | `check_session_search_requirements` | 619 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/skills_tool.py` | gateway | wrapper_only | high | `_is_gateway_surface` | 413 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/skills_tool.py` | gateway | wrapper_only | high | `_gateway_setup_hint` | 454 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/skills_tool.py` | gateway | wrapper_only | high | `_get_session_platform` | 559 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/terminal_tool.py` | tool_registry | feature_flag_required | high | `terminal_tool` | 1843 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/threat_patterns.py` | security | forbidden | critical | — | 0 | Threat pattern library is safety-sensitive; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `tools/todo_tool.py` | tool_registry | feature_flag_required | high | `todo_tool` | 187 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_backend_helpers.py` | gateway | wrapper_only | high | `nous_tool_gateway_unavailable_message` | 44 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/tool_backend_helpers.py` | gateway | wrapper_only | high | `prefers_gateway` | 149 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tools/tool_backend_helpers.py` | provider | wrapper_only | medium | `normalize_browser_cloud_provider` | 71 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/tool_backend_helpers.py` | tool_registry | feature_flag_required | high | `managed_nous_tools_enabled` | 17 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_backend_helpers.py` | tool_registry | feature_flag_required | high | `nous_tool_gateway_unavailable_message` | 44 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_output_limits.py` | tool_registry | feature_flag_required | high | `get_tool_output_limits` | 59 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_output_limits.py` | tool_registry | feature_flag_required | high | `_reset_tool_output_limits_cache` | 92 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_result_storage.py` | tool_registry | feature_flag_required | high | `maybe_persist_tool_result` | 122 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_search.py` | tool_registry | feature_flag_required | high | `ToolSearchConfig` | 64 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_search.py` | tool_registry | feature_flag_required | high | `_core_tool_names` | 150 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_search.py` | tool_registry | feature_flag_required | high | `is_deferrable_tool_name` | 163 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_search.py` | tool_registry | feature_flag_required | high | `classify_tools` | 189 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_search.py` | tool_registry | feature_flag_required | high | `bridge_tool_schemas` | 426 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_search.py` | tool_registry | feature_flag_required | high | `assemble_tool_defs` | 529 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_search.py` | tool_registry | feature_flag_required | high | `is_bridge_tool` | 591 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_search.py` | tool_registry | feature_flag_required | high | `dispatch_tool_search` | 605 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/tool_search.py` | tool_registry | feature_flag_required | high | `dispatch_tool_describe` | 632 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/transcription_tools.py` | provider | wrapper_only | medium | `_get_named_stt_provider_config` | 281 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/transcription_tools.py` | provider | wrapper_only | medium | `_is_command_stt_provider_config` | 311 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/transcription_tools.py` | provider | wrapper_only | medium | `_resolve_command_stt_provider_config` | 322 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/transcription_tools.py` | provider | wrapper_only | medium | `_iter_command_stt_providers` | 343 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/transcription_tools.py` | provider | wrapper_only | medium | `_has_any_command_stt_provider` | 354 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/transcription_tools.py` | provider | wrapper_only | medium | `_get_provider` | 745 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/transcription_tools.py` | provider | wrapper_only | medium | `_dispatch_to_plugin_provider` | 873 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/tts_tool.py` | provider | wrapper_only | medium | `_get_provider` | 340 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/tts_tool.py` | provider | wrapper_only | medium | `_get_provider_section` | 395 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/tts_tool.py` | provider | wrapper_only | medium | `_get_named_provider_config` | 403 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/tts_tool.py` | provider | wrapper_only | medium | `_is_command_provider_config` | 427 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/tts_tool.py` | provider | wrapper_only | medium | `_resolve_command_provider_config` | 438 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/tts_tool.py` | provider | wrapper_only | medium | `_dispatch_to_plugin_provider` | 459 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/tts_tool.py` | provider | wrapper_only | medium | `_plugin_provider_is_voice_compatible` | 550 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/tts_tool.py` | provider | wrapper_only | medium | `_iter_command_providers` | 576 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/tts_tool.py` | provider | wrapper_only | medium | `_has_any_command_tts_provider` | 869 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/tts_tool.py` | tool_registry | feature_flag_required | high | `text_to_speech_tool` | 2018 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/video_generation_tool.py` | provider | wrapper_only | medium | `_read_configured_video_provider` | 180 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/video_generation_tool.py` | provider | wrapper_only | medium | `_resolve_active_provider` | 226 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/video_generation_tool.py` | provider | wrapper_only | medium | `_missing_provider_error` | 247 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tools/vision_tools.py` | tool_registry | feature_flag_required | high | `_supports_media_in_tool_results` | 531 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/vision_tools.py` | tool_registry | feature_flag_required | high | `_build_native_vision_tool_result` | 633 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/vision_tools.py` | tool_registry | feature_flag_required | high | `vision_analyze_tool` | 801 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/vision_tools.py` | tool_registry | feature_flag_required | high | `video_analyze_tool` | 1338 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/web_tools.py` | tool_registry | feature_flag_required | high | `web_search_tool` | 787 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/web_tools.py` | tool_registry | feature_flag_required | high | `web_extract_tool` | 894 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tools/write_approval.py` | memory | wrapper_only | medium | `_prompt_inline_memory_approval` | 337 | Memory-like symbol detected by static AST scan. | Future integration should keep shadow memory isolated until native MemoryProvider adapter is approved. |
| `tools/x_search_tool.py` | tool_registry | feature_flag_required | high | `x_search_tool` | 274 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `toolset_distributions.py` | tool_registry | feature_flag_required | high | `sample_toolsets_from_distribution` | 247 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `toolsets.py` | tool_orchestration | forbidden | high | — | 0 | Toolset definition affects available capabilities; direct edits are forbidden. | Use hermes_ext.harness or an external wrapper first. Do not edit this file until a later phase explicitly approves a minimal patch. |
| `toolsets.py` | tool_registry | forbidden | critical | `get_toolset` | 585 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `toolsets.py` | tool_registry | forbidden | critical | `resolve_toolset` | 636 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `toolsets.py` | tool_registry | forbidden | critical | `resolve_multiple_toolsets` | 710 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `toolsets.py` | tool_registry | forbidden | critical | `_get_plugin_toolset_names` | 729 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `toolsets.py` | tool_registry | forbidden | critical | `_get_registry_toolset_aliases` | 746 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `toolsets.py` | tool_registry | forbidden | critical | `get_all_toolsets` | 755 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `toolsets.py` | tool_registry | forbidden | critical | `get_toolset_names` | 780 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `toolsets.py` | tool_registry | forbidden | critical | `validate_toolset` | 803 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `toolsets.py` | tool_registry | forbidden | critical | `create_custom_toolset` | 823 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `toolsets.py` | tool_registry | forbidden | critical | `get_toolset_info` | 847 | Tool/registry-like symbol detected by static AST scan. | Lifeline file: classification only. Do not patch directly. |
| `trajectory_compressor.py` | provider | wrapper_only | medium | `TrajectoryCompressor._detect_provider` | 435 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_notify_session_boundary` | 340 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_claim_active_session_slot` | 350 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_release_active_session_slot` | 370 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_finalize_session` | 382 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_teardown_session` | 437 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_close_session_by_id` | 480 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_ws_session_is_orphaned` | 495 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_close_sessions_for_transport` | 539 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_shutdown_sessions` | 576 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_session_is_evictable` | 604 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_reap_idle_sessions` | 619 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_session_cwd` | 1122 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_register_session_cwd` | 1128 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_ensure_session_db_row` | 1141 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_session_db` | 1195 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_set_session_cwd` | 1222 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_cwd_for_session_key` | 1303 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_set_session_context` | 1319 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_clear_session_context` | 1333 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_enable_gateway_prompts` | 1344 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_stored_session_runtime_overrides` | 1490 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_persist_live_session_runtime` | 1607 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_session_tool_progress_mode` | 1905 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_session_verbose` | 1909 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_compress_session_history` | 2132 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_sync_session_key_after_compress` | 2185 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_session_info` | 2377 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_apply_personality_to_session` | 2996 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_reset_session_agent` | 3253 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_init_session` | 3438 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_new_session_key` | 3526 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_session_pending_kind` | 4359 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_session_live_status` | 4368 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_session_live_title` | 4389 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_session_live_item` | 4400 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_find_live_session_by_key` | 4425 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_fallback_session_info` | 4434 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_live_session_payload` | 4447 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_spawn_tree_session_dir` | 5270 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_resolve_gateway_attachment_path` | 6573 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_stage_session_file_attachment` | 6612 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | gateway | wrapper_only | high | `_session_processes` | 7694 | Gateway/session-like symbol detected by static AST scan. | Future integration should remain gateway-sidecar before any native gateway change. |
| `tui_gateway/server.py` | provider | wrapper_only | medium | `_load_provider_routing` | 1731 | Provider-like symbol detected by static AST scan. | Future integration should prefer external provider wrapper or feature-flagged sidecar. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_load_tool_progress_mode` | 1749 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_load_enabled_toolsets` | 1762 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_session_tool_progress_mode` | 1905 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_tool_progress_enabled` | 1913 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_tool_ctx` | 2481 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_tool_args_text` | 2547 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_tool_result_text` | 2555 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_fmt_tool_duration` | 2565 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_tool_summary` | 2585 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_on_tool_start` | 2613 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_on_tool_complete` | 2640 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_on_tool_progress` | 2687 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_preview_tool_result_preview` | 3197 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_preview_restart_callbacks.tool_start` | 3227 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_preview_restart_callbacks.tool_complete` | 3232 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |
| `tui_gateway/server.py` | tool_registry | feature_flag_required | high | `_preview_restart_callbacks.tool_progress` | 3238 | Tool/registry-like symbol detected by static AST scan. | Future integration must pass through PreToolGuard and feature flags. |

## Files Scanned

| Path | Surface Guess | Lifeline | Lines | Imports | Symbols | Parse Error |
|---|---|---:|---:|---:|---:|---|
| `acp_adapter/__init__.py` | unknown | no | 1 | 0 | 0 | — |
| `acp_adapter/__main__.py` | unknown | no | 5 | 1 | 0 | — |
| `acp_adapter/auth.py` | unknown | no | 79 | 6 | 3 | — |
| `acp_adapter/edit_approval.py` | unknown | no | 286 | 17 | 15 | — |
| `acp_adapter/entry.py` | unknown | no | 266 | 17 | 10 | — |
| `acp_adapter/events.py` | unknown | no | 279 | 18 | 11 | — |
| `acp_adapter/permissions.py` | unknown | no | 168 | 10 | 6 | — |
| `acp_adapter/provenance.py` | unknown | no | 127 | 4 | 2 | — |
| `acp_adapter/server.py` | unknown | no | 2059 | 101 | 64 | — |
| `acp_adapter/session.py` | unknown | no | 623 | 29 | 26 | — |
| `acp_adapter/tools.py` | unknown | no | 1291 | 13 | 35 | — |
| `agent/__init__.py` | unknown | no | 8 | 1 | 0 | — |
| `agent/account_usage.py` | unknown | no | 638 | 25 | 20 | — |
| `agent/agent_init.py` | unknown | no | 1716 | 74 | 7 | — |
| `agent/agent_runtime_helpers.py` | unknown | no | 2606 | 59 | 40 | — |
| `agent/anthropic_adapter.py` | unknown | no | 2516 | 45 | 61 | — |
| `agent/async_utils.py` | unknown | no | 68 | 7 | 1 | — |
| `agent/auxiliary_client.py` | unknown | no | 5950 | 124 | 154 | — |
| `agent/azure_identity_adapter.py` | unknown | no | 555 | 16 | 18 | — |
| `agent/background_review.py` | unknown | no | 608 | 14 | 6 | — |
| `agent/bedrock_adapter.py` | unknown | no | 1342 | 23 | 30 | — |
| `agent/browser_provider.py` | unknown | no | 175 | 4 | 10 | — |
| `agent/browser_registry.py` | unknown | no | 192 | 7 | 6 | — |
| `agent/chat_completion_helpers.py` | unknown | no | 2682 | 59 | 27 | — |
| `agent/codex_responses_adapter.py` | unknown | no | 1271 | 13 | 15 | — |
| `agent/codex_runtime.py` | unknown | no | 686 | 14 | 12 | — |
| `agent/coding_context.py` | unknown | no | 738 | 14 | 27 | — |
| `agent/context_compressor.py` | context | yes | 2426 | 17 | 52 | — |
| `agent/context_engine.py` | unknown | no | 226 | 6 | 15 | — |
| `agent/context_references.py` | unknown | no | 551 | 17 | 25 | — |
| `agent/conversation_compression.py` | unknown | no | 816 | 25 | 7 | — |
| `agent/conversation_loop.py` | unknown | no | 4421 | 74 | 15 | — |
| `agent/copilot_acp_client.py` | unknown | no | 679 | 18 | 26 | — |
| `agent/credential_persistence.py` | unknown | no | 174 | 6 | 6 | — |
| `agent/credential_pool.py` | unknown | no | 2184 | 58 | 66 | — |
| `agent/credential_sources.py` | unknown | no | 448 | 15 | 17 | — |
| `agent/credits_tracker.py` | unknown | no | 794 | 14 | 20 | — |
| `agent/curator.py` | unknown | no | 1835 | 30 | 34 | — |
| `agent/curator_backup.py` | unknown | no | 695 | 20 | 19 | — |
| `agent/display.py` | unknown | no | 1074 | 18 | 52 | — |
| `agent/error_classifier.py` | unknown | no | 1365 | 10 | 15 | — |
| `agent/errors.py` | unknown | no | 3 | 0 | 1 | — |
| `agent/file_safety.py` | unknown | no | 623 | 6 | 15 | — |
| `agent/gemini_cloudcode_adapter.py` | unknown | no | 909 | 18 | 31 | — |
| `agent/gemini_native_adapter.py` | unknown | no | 1001 | 15 | 50 | — |
| `agent/gemini_schema.py` | unknown | no | 99 | 3 | 2 | — |
| `agent/google_code_assist.py` | unknown | no | 451 | 13 | 16 | — |
| `agent/google_oauth.py` | unknown | no | 1067 | 32 | 40 | — |
| `agent/i18n.py` | unknown | no | 302 | 10 | 8 | — |
| `agent/image_gen_provider.py` | unknown | no | 324 | 14 | 14 | — |
| `agent/image_gen_registry.py` | unknown | no | 145 | 8 | 6 | — |
| `agent/image_routing.py` | unknown | no | 540 | 13 | 12 | — |
| `agent/insights.py` | unknown | no | 921 | 13 | 18 | — |
| `agent/iteration_budget.py` | unknown | no | 62 | 2 | 6 | — |
| `agent/jiter_preload.py` | unknown | no | 39 | 3 | 1 | — |
| `agent/lmstudio_reasoning.py` | unknown | no | 48 | 3 | 1 | — |
| `agent/lsp/__init__.py` | unknown | no | 106 | 6 | 3 | — |
| `agent/lsp/cli.py` | unknown | no | 299 | 21 | 10 | — |
| `agent/lsp/client.py` | unknown | no | 943 | 26 | 39 | — |
| `agent/lsp/eventlog.py` | unknown | no | 213 | 5 | 14 | — |
| `agent/lsp/install.py` | unknown | no | 403 | 11 | 11 | — |
| `agent/lsp/manager.py` | unknown | no | 639 | 23 | 22 | — |
| `agent/lsp/protocol.py` | unknown | no | 196 | 7 | 10 | — |
| `agent/lsp/range_shift.py` | unknown | no | 149 | 7 | 4 | — |
| `agent/lsp/reporter.py` | unknown | no | 78 | 4 | 3 | — |
| `agent/lsp/servers.py` | unknown | no | 1040 | 27 | 60 | — |
| `agent/lsp/workspace.py` | unknown | no | 223 | 7 | 6 | — |
| `agent/manual_compression_feedback.py` | unknown | no | 49 | 3 | 1 | — |
| `agent/markdown_tables.py` | unknown | no | 309 | 4 | 11 | — |
| `agent/memory_manager.py` | memory | yes | 917 | 16 | 46 | — |
| `agent/memory_provider.py` | memory | yes | 296 | 8 | 19 | — |
| `agent/message_sanitization.py` | unknown | no | 444 | 5 | 12 | — |
| `agent/model_metadata.py` | unknown | no | 2085 | 30 | 53 | — |
| `agent/models_dev.py` | unknown | no | 725 | 15 | 26 | — |
| `agent/moonshot_schema.py` | unknown | no | 238 | 5 | 5 | — |
| `agent/nous_rate_guard.py` | unknown | no | 325 | 11 | 12 | — |
| `agent/onboarding.py` | unknown | no | 253 | 8 | 11 | — |
| `agent/plugin_llm.py` | unknown | no | 1046 | 21 | 29 | — |
| `agent/portal_tags.py` | unknown | no | 64 | 3 | 3 | — |
| `agent/process_bootstrap.py` | unknown | no | 167 | 8 | 15 | — |
| `agent/prompt_builder.py` | prompt | yes | 1630 | 30 | 26 | — |
| `agent/prompt_caching.py` | unknown | no | 79 | 4 | 3 | — |
| `agent/rate_limit_tracker.py` | unknown | no | 246 | 7 | 17 | — |
| `agent/redact.py` | security | yes | 497 | 3 | 20 | — |
| `agent/retry_utils.py` | unknown | no | 57 | 3 | 1 | — |
| `agent/runtime_cwd.py` | unknown | no | 62 | 5 | 5 | — |
| `agent/secret_sources/__init__.py` | unknown | no | 13 | 0 | 0 | — |
| `agent/secret_sources/bitwarden.py` | unknown | no | 692 | 22 | 24 | — |
| `agent/shell_hooks.py` | unknown | no | 847 | 31 | 29 | — |
| `agent/skill_bundles.py` | unknown | no | 410 | 15 | 16 | — |
| `agent/skill_commands.py` | unknown | no | 527 | 29 | 11 | — |
| `agent/skill_preprocessing.py` | unknown | no | 140 | 5 | 7 | — |
| `agent/skill_utils.py` | unknown | no | 695 | 20 | 23 | — |
| `agent/ssl_guard.py` | unknown | no | 94 | 7 | 6 | — |
| `agent/stream_diag.py` | unknown | no | 280 | 7 | 5 | — |
| `agent/subdirectory_hints.py` | unknown | no | 270 | 9 | 9 | — |
| `agent/system_prompt.py` | prompt | yes | 446 | 28 | 5 | — |
| `agent/think_scrubber.py` | unknown | no | 386 | 2 | 11 | — |
| `agent/title_generator.py` | unknown | no | 171 | 5 | 3 | — |
| `agent/tool_dispatch_helpers.py` | unknown | no | 417 | 12 | 14 | — |
| `agent/tool_executor.py` | unknown | no | 1428 | 45 | 19 | — |
| `agent/tool_guardrails.py` | unknown | no | 475 | 9 | 26 | — |
| `agent/tool_result_classification.py` | unknown | no | 26 | 3 | 1 | — |
| `agent/trajectory.py` | unknown | no | 56 | 6 | 3 | — |
| `agent/transcription_provider.py` | unknown | no | 193 | 7 | 8 | — |
| `agent/transcription_registry.py` | unknown | no | 122 | 7 | 4 | — |
| `agent/transports/__init__.py` | unknown | no | 68 | 9 | 3 | — |
| `agent/transports/anthropic.py` | unknown | no | 243 | 15 | 9 | — |
| `agent/transports/base.py` | unknown | no | 89 | 7 | 9 | — |
| `agent/transports/bedrock.py` | unknown | no | 154 | 13 | 8 | — |
| `agent/transports/chat_completions.py` | unknown | no | 739 | 14 | 13 | — |
| `agent/transports/codex.py` | unknown | no | 347 | 17 | 10 | — |
| `agent/transports/codex_app_server.py` | unknown | no | 400 | 12 | 24 | — |
| `agent/transports/codex_app_server_session.py` | unknown | no | 876 | 16 | 23 | — |
| `agent/transports/codex_event_projector.py` | unknown | no | 312 | 7 | 13 | — |
| `agent/transports/hermes_tools_mcp_server.py` | unknown | no | 233 | 10 | 4 | — |
| `agent/transports/types.py` | unknown | no | 174 | 5 | 15 | — |
| `agent/tts_provider.py` | unknown | no | 274 | 8 | 13 | — |
| `agent/tts_registry.py` | unknown | no | 133 | 7 | 4 | — |
| `agent/turn_context.py` | unknown | no | 388 | 13 | 2 | — |
| `agent/turn_finalizer.py` | unknown | no | 428 | 8 | 1 | — |
| `agent/turn_retry_state.py` | unknown | no | 68 | 3 | 2 | — |
| `agent/usage_pricing.py` | unknown | no | 908 | 13 | 20 | — |
| `agent/video_gen_provider.py` | unknown | no | 299 | 13 | 14 | — |
| `agent/video_gen_registry.py` | unknown | no | 117 | 8 | 5 | — |
| `agent/web_search_provider.py` | unknown | no | 185 | 5 | 9 | — |
| `agent/web_search_registry.py` | unknown | no | 245 | 8 | 10 | — |
| `batch_runner.py` | unknown | no | 1321 | 32 | 16 | — |
| `cli.py` | cli | yes | 13984 | 380 | 382 | — |
| `cron/__init__.py` | cron | no | 42 | 10 | 0 | — |
| `cron/blueprint_catalog.py` | cron | no | 713 | 10 | 12 | — |
| `cron/jobs.py` | cron | yes | 1304 | 24 | 38 | — |
| `cron/scheduler.py` | cron | yes | 2213 | 66 | 36 | — |
| `cron/scripts/__init__.py` | cron | no | 1 | 0 | 0 | — |
| `cron/scripts/classify_items.py` | cron | no | 226 | 9 | 6 | — |
| `cron/suggestion_catalog.py` | cron | no | 154 | 9 | 3 | — |
| `cron/suggestions.py` | cron | no | 257 | 16 | 12 | — |
| `gateway/__init__.py` | gateway | no | 35 | 10 | 0 | — |
| `gateway/authz_mixin.py` | gateway | no | 536 | 9 | 7 | — |
| `gateway/builtin_hooks/__init__.py` | gateway | no | 1 | 0 | 0 | — |
| `gateway/channel_directory.py` | gateway | no | 419 | 12 | 14 | — |
| `gateway/config.py` | gateway | no | 2139 | 22 | 36 | — |
| `gateway/delivery.py` | gateway | no | 433 | 14 | 16 | — |
| `gateway/display_config.py` | gateway | no | 246 | 2 | 2 | — |
| `gateway/hooks.py` | gateway | no | 227 | 10 | 8 | — |
| `gateway/kanban_watchers.py` | gateway | no | 1064 | 21 | 15 | — |
| `gateway/memory_monitor.py` | gateway | no | 230 | 10 | 6 | — |
| `gateway/mirror.py` | gateway | no | 168 | 6 | 3 | — |
| `gateway/pairing.py` | gateway | no | 450 | 13 | 26 | — |
| `gateway/platform_registry.py` | gateway | no | 260 | 7 | 10 | — |
| `gateway/platforms/__init__.py` | gateway | no | 45 | 5 | 2 | — |
| `gateway/platforms/_http_client_limits.py` | gateway | no | 84 | 3 | 3 | — |
| `gateway/platforms/api_server.py` | gateway | no | 4322 | 74 | 132 | — |
| `gateway/platforms/base.py` | gateway | yes | 4932 | 66 | 170 | — |
| `gateway/platforms/bluebubbles.py` | gateway | no | 1038 | 31 | 39 | — |
| `gateway/platforms/dingtalk.py` | gateway | no | 1503 | 39 | 44 | — |
| `gateway/platforms/email.py` | gateway | no | 878 | 32 | 33 | — |
| `gateway/platforms/feishu.py` | gateway | no | 5213 | 117 | 226 | — |
| `gateway/platforms/feishu_comment.py` | gateway | no | 1382 | 27 | 32 | — |
| `gateway/platforms/feishu_comment_rules.py` | gateway | no | 429 | 14 | 21 | — |
| `gateway/platforms/feishu_meeting_invite.py` | gateway | no | 212 | 10 | 12 | — |
| `gateway/platforms/helpers.py` | gateway | no | 278 | 11 | 20 | — |
| `gateway/platforms/matrix.py` | gateway | no | 4108 | 84 | 139 | — |
| `gateway/platforms/msgraph_webhook.py` | gateway | no | 421 | 22 | 27 | — |
| `gateway/platforms/qqbot/__init__.py` | gateway | no | 91 | 26 | 0 | — |
| `gateway/platforms/qqbot/adapter.py` | gateway | no | 3196 | 80 | 91 | — |
| `gateway/platforms/qqbot/chunked_upload.py` | gateway | no | 602 | 14 | 24 | — |
| `gateway/platforms/qqbot/constants.py` | gateway | no | 74 | 2 | 0 | — |
| `gateway/platforms/qqbot/crypto.py` | gateway | no | 45 | 4 | 2 | — |
| `gateway/platforms/qqbot/keyboards.py` | gateway | no | 473 | 11 | 29 | — |
| `gateway/platforms/qqbot/onboard.py` | gateway | no | 220 | 19 | 6 | — |
| `gateway/platforms/qqbot/utils.py` | gateway | no | 71 | 8 | 4 | — |
| `gateway/platforms/signal.py` | gateway | no | 1551 | 42 | 46 | — |
| `gateway/platforms/signal_rate_limit.py` | gateway | no | 369 | 7 | 17 | — |
| `gateway/platforms/slack.py` | gateway | no | 3815 | 63 | 92 | — |
| `gateway/platforms/sms.py` | gateway | no | 379 | 23 | 13 | — |
| `gateway/platforms/telegram.py` | gateway | no | 6685 | 120 | 162 | — |
| `gateway/platforms/telegram_network.py` | gateway | no | 259 | 9 | 12 | — |
| `gateway/platforms/webhook.py` | gateway | no | 971 | 29 | 24 | — |
| `gateway/platforms/wecom.py` | gateway | no | 1635 | 41 | 68 | — |
| `gateway/platforms/wecom_callback.py` | gateway | no | 425 | 21 | 21 | — |
| `gateway/platforms/wecom_crypto.py` | gateway | no | 142 | 13 | 15 | — |
| `gateway/platforms/weixin.py` | gateway | no | 2358 | 48 | 111 | — |
| `gateway/platforms/whatsapp.py` | gateway | no | 1177 | 39 | 28 | — |
| `gateway/platforms/whatsapp_cloud.py` | gateway | no | 1956 | 34 | 41 | — |
| `gateway/platforms/whatsapp_common.py` | gateway | no | 367 | 8 | 22 | — |
| `gateway/platforms/yuanbao.py` | gateway | no | 5358 | 88 | 259 | — |
| `gateway/platforms/yuanbao_media.py` | gateway | no | 645 | 12 | 17 | — |
| `gateway/platforms/yuanbao_proto.py` | gateway | no | 1418 | 5 | 52 | — |
| `gateway/platforms/yuanbao_sticker.py` | gateway | no | 558 | 6 | 12 | — |
| `gateway/response_filters.py` | gateway | no | 53 | 2 | 3 | — |
| `gateway/restart.py` | gateway | no | 20 | 1 | 1 | — |
| `gateway/run.py` | gateway | yes | 16795 | 381 | 293 | — |
| `gateway/runtime_footer.py` | gateway | no | 149 | 5 | 5 | — |
| `gateway/session.py` | gateway | yes | 1444 | 29 | 42 | — |
| `gateway/session_context.py` | gateway | no | 197 | 6 | 4 | — |
| `gateway/shutdown_forensics.py` | gateway | no | 462 | 12 | 10 | — |
| `gateway/slash_access.py` | gateway | no | 229 | 7 | 10 | — |
| `gateway/slash_commands.py` | gateway | no | 3826 | 171 | 68 | — |
| `gateway/status.py` | gateway | no | 1064 | 18 | 48 | — |
| `gateway/sticker_cache.py` | gateway | no | 124 | 6 | 6 | — |
| `gateway/stream_consumer.py` | gateway | no | 1570 | 17 | 36 | — |
| `gateway/stream_dispatch.py` | gateway | no | 132 | 13 | 4 | — |
| `gateway/stream_events.py` | gateway | no | 171 | 7 | 7 | — |
| `gateway/whatsapp_identity.py` | gateway | no | 155 | 6 | 3 | — |
| `hermes_bootstrap.py` | unknown | yes | 129 | 3 | 1 | — |
| `hermes_cli/__init__.py` | unknown | no | 92 | 2 | 1 | — |
| `hermes_cli/_parser.py` | unknown | no | 411 | 1 | 2 | — |
| `hermes_cli/_subprocess_compat.py` | unknown | no | 234 | 4 | 5 | — |
| `hermes_cli/active_sessions.py` | unknown | no | 320 | 17 | 21 | — |
| `hermes_cli/auth.py` | unknown | no | 8050 | 108 | 216 | — |
| `hermes_cli/auth_commands.py` | unknown | no | 802 | 47 | 23 | — |
| `hermes_cli/azure_detect.py` | unknown | no | 406 | 15 | 11 | — |
| `hermes_cli/backup.py` | unknown | no | 1065 | 23 | 23 | — |
| `hermes_cli/banner.py` | unknown | no | 835 | 38 | 24 | — |
| `hermes_cli/blueprint_cmd.py` | unknown | no | 318 | 20 | 11 | — |
| `hermes_cli/browser_connect.py` | unknown | no | 217 | 10 | 9 | — |
| `hermes_cli/build_info.py` | unknown | no | 51 | 3 | 1 | — |
| `hermes_cli/bundles.py` | unknown | no | 229 | 12 | 8 | — |
| `hermes_cli/callbacks.py` | unknown | no | 242 | 11 | 3 | — |
| `hermes_cli/checkpoints.py` | unknown | no | 244 | 13 | 10 | — |
| `hermes_cli/claw.py` | unknown | no | 809 | 23 | 12 | — |
| `hermes_cli/cli_agent_setup_mixin.py` | unknown | no | 681 | 30 | 6 | — |
| `hermes_cli/cli_commands_mixin.py` | unknown | no | 2293 | 160 | 45 | — |
| `hermes_cli/cli_output.py` | unknown | no | 77 | 3 | 7 | — |
| `hermes_cli/clipboard.py` | unknown | no | 494 | 8 | 23 | — |
| `hermes_cli/codex_models.py` | unknown | no | 206 | 9 | 5 | — |
| `hermes_cli/codex_runtime_plugin_migration.py` | unknown | no | 757 | 11 | 14 | — |
| `hermes_cli/codex_runtime_switch.py` | unknown | no | 266 | 6 | 7 | — |
| `hermes_cli/colors.py` | unknown | no | 38 | 2 | 3 | — |
| `hermes_cli/commands.py` | unknown | no | 1933 | 36 | 46 | — |
| `hermes_cli/completion.py` | unknown | no | 319 | 3 | 5 | — |
| `hermes_cli/config.py` | unknown | no | 6573 | 46 | 80 | — |
| `hermes_cli/container_boot.py` | unknown | no | 460 | 14 | 12 | — |
| `hermes_cli/copilot_auth.py` | unknown | no | 392 | 13 | 9 | — |
| `hermes_cli/cron.py` | unknown | no | 357 | 17 | 10 | — |
| `hermes_cli/curator.py` | unknown | no | 598 | 20 | 17 | — |
| `hermes_cli/curses_ui.py` | unknown | no | 872 | 18 | 31 | — |
| `hermes_cli/dashboard_auth/__init__.py` | unknown | no | 42 | 12 | 0 | — |
| `hermes_cli/dashboard_auth/audit.py` | unknown | no | 87 | 9 | 3 | — |
| `hermes_cli/dashboard_auth/base.py` | unknown | no | 220 | 5 | 14 | — |
| `hermes_cli/dashboard_auth/cookies.py` | unknown | no | 247 | 5 | 11 | — |
| `hermes_cli/dashboard_auth/login_page.py` | unknown | no | 534 | 4 | 2 | — |
| `hermes_cli/dashboard_auth/middleware.py` | unknown | no | 368 | 23 | 7 | — |
| `hermes_cli/dashboard_auth/prefix.py` | unknown | no | 201 | 6 | 6 | — |
| `hermes_cli/dashboard_auth/public_paths.py` | unknown | no | 49 | 1 | 0 | — |
| `hermes_cli/dashboard_auth/registry.py` | unknown | no | 58 | 7 | 4 | — |
| `hermes_cli/dashboard_auth/routes.py` | unknown | no | 621 | 41 | 15 | — |
| `hermes_cli/dashboard_auth/ws_tickets.py` | unknown | no | 161 | 8 | 7 | — |
| `hermes_cli/dashboard_register.py` | unknown | no | 427 | 18 | 5 | — |
| `hermes_cli/debug.py` | unknown | no | 829 | 15 | 27 | — |
| `hermes_cli/default_soul.py` | unknown | no | 11 | 0 | 0 | — |
| `hermes_cli/dep_ensure.py` | unknown | no | 159 | 9 | 4 | — |
| `hermes_cli/dingtalk_auth.py` | unknown | no | 293 | 16 | 9 | — |
| `hermes_cli/doctor.py` | unknown | no | 2314 | 116 | 31 | — |
| `hermes_cli/dump.py` | unknown | no | 375 | 22 | 11 | — |
| `hermes_cli/env_loader.py` | unknown | no | 344 | 10 | 10 | — |
| `hermes_cli/fallback_cmd.py` | unknown | no | 354 | 23 | 14 | — |
| `hermes_cli/fallback_config.py` | unknown | no | 72 | 2 | 4 | — |
| `hermes_cli/gateway.py` | unknown | no | 7048 | 144 | 164 | — |
| `hermes_cli/gateway_windows.py` | unknown | no | 1311 | 49 | 50 | — |
| `hermes_cli/goals.py` | unknown | no | 912 | 20 | 32 | — |
| `hermes_cli/gui_uninstall.py` | unknown | no | 285 | 7 | 12 | — |
| `hermes_cli/hooks.py` | unknown | no | 385 | 14 | 8 | — |
| `hermes_cli/inventory.py` | unknown | no | 417 | 18 | 9 | — |
| `hermes_cli/kanban.py` | unknown | no | 2830 | 29 | 62 | — |
| `hermes_cli/kanban_db.py` | unknown | no | 7750 | 59 | 168 | — |
| `hermes_cli/kanban_decompose.py` | unknown | no | 477 | 12 | 12 | — |
| `hermes_cli/kanban_diagnostics.py` | unknown | no | 1107 | 9 | 26 | — |
| `hermes_cli/kanban_specify.py` | unknown | no | 273 | 11 | 6 | — |
| `hermes_cli/kanban_swarm.py` | unknown | no | 279 | 9 | 9 | — |
| `hermes_cli/logs.py` | unknown | no | 394 | 11 | 11 | — |
| `hermes_cli/main.py` | cli | yes | 12488 | 436 | 244 | — |
| `hermes_cli/managed_uv.py` | unknown | no | 254 | 10 | 12 | — |
| `hermes_cli/mcp_catalog.py` | unknown | no | 778 | 25 | 28 | — |
| `hermes_cli/mcp_config.py` | unknown | no | 914 | 41 | 25 | — |
| `hermes_cli/mcp_picker.py` | unknown | no | 322 | 23 | 12 | — |
| `hermes_cli/mcp_security.py` | unknown | no | 96 | 5 | 4 | — |
| `hermes_cli/mcp_startup.py` | unknown | no | 59 | 5 | 4 | — |
| `hermes_cli/memory_setup.py` | unknown | no | 472 | 20 | 9 | — |
| `hermes_cli/middleware.py` | unknown | no | 313 | 13 | 19 | — |
| `hermes_cli/migrate.py` | unknown | no | 115 | 13 | 3 | — |
| `hermes_cli/model_catalog.py` | unknown | no | 394 | 12 | 14 | — |
| `hermes_cli/model_cost_guard.py` | unknown | no | 134 | 8 | 5 | — |
| `hermes_cli/model_normalize.py` | unknown | no | 473 | 5 | 8 | — |
| `hermes_cli/model_setup_flows.py` | unknown | no | 2725 | 230 | 20 | — |
| `hermes_cli/model_switch.py` | unknown | no | 2086 | 73 | 23 | — |
| `hermes_cli/models.py` | unknown | no | 4050 | 67 | 94 | — |
| `hermes_cli/nous_account.py` | unknown | no | 789 | 20 | 35 | — |
| `hermes_cli/nous_subscription.py` | unknown | no | 1279 | 38 | 30 | — |
| `hermes_cli/oneshot.py` | unknown | no | 381 | 19 | 6 | — |
| `hermes_cli/pairing.py` | unknown | no | 115 | 2 | 5 | — |
| `hermes_cli/partial_compress.py` | unknown | no | 235 | 6 | 4 | — |
| `hermes_cli/platforms.py` | unknown | no | 84 | 4 | 3 | — |
| `hermes_cli/plugins.py` | unknown | no | 2046 | 52 | 66 | — |
| `hermes_cli/plugins_cmd.py` | unknown | no | 1835 | 66 | 53 | — |
| `hermes_cli/portal_cli.py` | unknown | no | 245 | 10 | 6 | — |
| `hermes_cli/profile_describer.py` | unknown | no | 298 | 12 | 5 | — |
| `hermes_cli/profile_distribution.py` | unknown | no | 726 | 30 | 28 | — |
| `hermes_cli/profiles.py` | unknown | no | 1817 | 43 | 48 | — |
| `hermes_cli/prompt_size.py` | unknown | no | 153 | 11 | 6 | — |
| `hermes_cli/providers.py` | unknown | no | 734 | 12 | 11 | — |
| `hermes_cli/proxy/__init__.py` | unknown | no | 20 | 1 | 0 | — |
| `hermes_cli/proxy/adapters/__init__.py` | unknown | no | 37 | 5 | 1 | — |
| `hermes_cli/proxy/adapters/base.py` | unknown | no | 108 | 6 | 9 | — |
| `hermes_cli/proxy/adapters/nous_portal.py` | unknown | no | 189 | 20 | 11 | — |
| `hermes_cli/proxy/adapters/xai.py` | unknown | no | 145 | 11 | 10 | — |
| `hermes_cli/proxy/cli.py` | unknown | no | 142 | 11 | 5 | — |
| `hermes_cli/proxy/server.py` | unknown | no | 296 | 9 | 9 | — |
| `hermes_cli/psutil_android.py` | unknown | no | 108 | 5 | 4 | — |
| `hermes_cli/pt_input_extras.py` | unknown | no | 120 | 7 | 3 | — |
| `hermes_cli/pty_bridge.py` | unknown | no | 286 | 13 | 14 | — |
| `hermes_cli/relaunch.py` | unknown | no | 205 | 8 | 6 | — |
| `hermes_cli/runtime_provider.py` | unknown | no | 1777 | 55 | 26 | — |
| `hermes_cli/secret_prompt.py` | unknown | no | 126 | 8 | 9 | — |
| `hermes_cli/secrets_cli.py` | unknown | no | 600 | 18 | 10 | — |
| `hermes_cli/security_advisories.py` | unknown | no | 453 | 15 | 17 | — |
| `hermes_cli/security_audit.py` | unknown | no | 576 | 17 | 21 | — |
| `hermes_cli/send_cmd.py` | unknown | no | 463 | 14 | 7 | — |
| `hermes_cli/service_manager.py` | unknown | no | 1066 | 38 | 60 | — |
| `hermes_cli/session_listing.py` | unknown | no | 97 | 3 | 3 | — |
| `hermes_cli/session_recap.py` | unknown | no | 316 | 11 | 11 | — |
| `hermes_cli/setup.py` | unknown | no | 3366 | 116 | 56 | — |
| `hermes_cli/setup_whatsapp_cloud.py` | unknown | no | 541 | 8 | 8 | — |
| `hermes_cli/skills_config.py` | unknown | no | 183 | 12 | 7 | — |
| `hermes_cli/skills_hub.py` | unknown | no | 1891 | 84 | 34 | — |
| `hermes_cli/skin_engine.py` | unknown | no | 926 | 11 | 18 | — |
| `hermes_cli/slack_cli.py` | unknown | no | 159 | 8 | 2 | — |
| `hermes_cli/status.py` | unknown | no | 586 | 39 | 7 | — |
| `hermes_cli/stdio.py` | unknown | no | 251 | 5 | 6 | — |
| `hermes_cli/subcommands/__init__.py` | unknown | no | 18 | 1 | 0 | — |
| `hermes_cli/subcommands/_shared.py` | unknown | no | 29 | 2 | 1 | — |
| `hermes_cli/subcommands/acp.py` | unknown | no | 52 | 3 | 1 | — |
| `hermes_cli/subcommands/auth.py` | unknown | no | 109 | 2 | 1 | — |
| `hermes_cli/subcommands/backup.py` | unknown | no | 38 | 2 | 1 | — |
| `hermes_cli/subcommands/claw.py` | unknown | no | 92 | 2 | 1 | — |
| `hermes_cli/subcommands/config.py` | unknown | no | 49 | 2 | 1 | — |
| `hermes_cli/subcommands/cron.py` | unknown | no | 163 | 3 | 1 | — |
| `hermes_cli/subcommands/dashboard.py` | unknown | no | 143 | 3 | 1 | — |
| `hermes_cli/subcommands/debug.py` | unknown | no | 77 | 3 | 1 | — |
| `hermes_cli/subcommands/doctor.py` | unknown | no | 35 | 2 | 1 | — |
| `hermes_cli/subcommands/dump.py` | unknown | no | 28 | 2 | 1 | — |
| `hermes_cli/subcommands/gateway.py` | unknown | no | 284 | 4 | 2 | — |
| `hermes_cli/subcommands/gui.py` | unknown | no | 63 | 2 | 1 | — |
| `hermes_cli/subcommands/hooks.py` | unknown | no | 77 | 2 | 1 | — |
| `hermes_cli/subcommands/import_cmd.py` | unknown | no | 31 | 2 | 1 | — |
| `hermes_cli/subcommands/insights.py` | unknown | no | 25 | 2 | 1 | — |
| `hermes_cli/subcommands/login.py` | unknown | no | 58 | 2 | 1 | — |
| `hermes_cli/subcommands/logout.py` | unknown | no | 28 | 2 | 1 | — |
| `hermes_cli/subcommands/logs.py` | unknown | no | 78 | 3 | 1 | — |
| `hermes_cli/subcommands/mcp.py` | unknown | no | 108 | 4 | 1 | — |
| `hermes_cli/subcommands/memory.py` | unknown | no | 53 | 2 | 1 | — |
| `hermes_cli/subcommands/model.py` | unknown | no | 72 | 2 | 1 | — |
| `hermes_cli/subcommands/pairing.py` | unknown | no | 36 | 2 | 1 | — |
| `hermes_cli/subcommands/plugins.py` | unknown | no | 94 | 2 | 1 | — |
| `hermes_cli/subcommands/postinstall.py` | unknown | no | 23 | 2 | 1 | — |
| `hermes_cli/subcommands/profile.py` | unknown | no | 203 | 2 | 1 | — |
| `hermes_cli/subcommands/prompt_size.py` | unknown | no | 36 | 2 | 1 | — |
| `hermes_cli/subcommands/security.py` | unknown | no | 62 | 2 | 1 | — |
| `hermes_cli/subcommands/setup.py` | unknown | no | 58 | 2 | 1 | — |
| `hermes_cli/subcommands/skills.py` | unknown | no | 269 | 2 | 1 | — |
| `hermes_cli/subcommands/slack.py` | unknown | no | 60 | 2 | 1 | — |
| `hermes_cli/subcommands/status.py` | unknown | no | 28 | 2 | 1 | — |
| `hermes_cli/subcommands/tools.py` | unknown | no | 95 | 2 | 1 | — |
| `hermes_cli/subcommands/uninstall.py` | unknown | no | 41 | 2 | 1 | — |
| `hermes_cli/subcommands/update.py` | unknown | no | 70 | 2 | 1 | — |
| `hermes_cli/subcommands/version.py` | unknown | no | 18 | 2 | 1 | — |
| `hermes_cli/subcommands/webhook.py` | unknown | no | 76 | 2 | 1 | — |
| `hermes_cli/subcommands/whatsapp.py` | unknown | no | 22 | 2 | 1 | — |
| `hermes_cli/suggestions_cmd.py` | unknown | no | 153 | 8 | 3 | — |
| `hermes_cli/telegram_managed_bot.py` | unknown | no | 358 | 12 | 18 | — |
| `hermes_cli/timeouts.py` | unknown | no | 82 | 3 | 4 | — |
| `hermes_cli/tips.py` | unknown | no | 486 | 1 | 1 | — |
| `hermes_cli/tools_config.py` | unknown | no | 3921 | 97 | 61 | — |
| `hermes_cli/uninstall.py` | unknown | no | 930 | 27 | 24 | — |
| `hermes_cli/voice.py` | unknown | no | 846 | 19 | 14 | — |
| `hermes_cli/web_server.py` | unknown | no | 11899 | 339 | 398 | — |
| `hermes_cli/webhook.py` | unknown | no | 298 | 16 | 14 | — |
| `hermes_cli/win_pty_bridge.py` | unknown | no | 179 | 7 | 14 | — |
| `hermes_cli/write_approval_commands.py` | unknown | no | 209 | 7 | 9 | — |
| `hermes_cli/xai_retirement.py` | unknown | no | 253 | 10 | 9 | — |
| `hermes_constants.py` | unknown | yes | 568 | 8 | 29 | — |
| `hermes_logging.py` | unknown | no | 536 | 15 | 20 | — |
| `hermes_state.py` | state_db | yes | 4782 | 19 | 152 | — |
| `hermes_time.py` | unknown | no | 117 | 8 | 5 | — |
| `mcp_serve.py` | unknown | no | 897 | 22 | 33 | — |
| `mini_swe_runner.py` | unknown | no | 731 | 19 | 12 | — |
| `model_tools.py` | tool_orchestration | yes | 1231 | 41 | 25 | — |
| `optional-skills/blockchain/evm/scripts/evm_client.py` | unknown | no | 1508 | 14 | 45 | — |
| `optional-skills/blockchain/hyperliquid/scripts/hyperliquid_client.py` | unknown | no | 1660 | 16 | 69 | — |
| `optional-skills/blockchain/solana/scripts/solana_client.py` | unknown | no | 698 | 11 | 19 | — |
| `optional-skills/creative/kanban-video-orchestrator/scripts/bootstrap_pipeline.py` | unknown | no | 501 | 7 | 7 | — |
| `optional-skills/creative/kanban-video-orchestrator/scripts/monitor.py` | unknown | no | 195 | 10 | 7 | — |
| `optional-skills/creative/meme-generation/scripts/generate_meme.py` | unknown | no | 470 | 11 | 17 | — |
| `optional-skills/creative/pixel-art/scripts/__init__.py` | unknown | no | 0 | 0 | 0 | — |
| `optional-skills/creative/pixel-art/scripts/palettes.py` | unknown | no | 167 | 1 | 1 | — |
| `optional-skills/creative/pixel-art/scripts/pixel_art.py` | unknown | no | 162 | 8 | 2 | — |
| `optional-skills/creative/pixel-art/scripts/pixel_art_video.py` | unknown | no | 345 | 9 | 29 | — |
| `optional-skills/devops/watchers/scripts/_watermark.py` | unknown | no | 148 | 9 | 9 | — |
| `optional-skills/devops/watchers/scripts/watch_github.py` | unknown | no | 169 | 12 | 3 | — |
| `optional-skills/devops/watchers/scripts/watch_http_json.py` | unknown | no | 131 | 9 | 3 | — |
| `optional-skills/devops/watchers/scripts/watch_rss.py` | unknown | no | 121 | 9 | 3 | — |
| `optional-skills/finance/dcf-model/scripts/validate_dcf.py` | unknown | no | 291 | 5 | 11 | — |
| `optional-skills/finance/excel-author/scripts/recalc.py` | unknown | no | 88 | 6 | 3 | — |
| `optional-skills/finance/stocks/scripts/stocks_client.py` | unknown | no | 755 | 11 | 24 | — |
| `optional-skills/health/fitness-nutrition/scripts/body_calc.py` | unknown | no | 210 | 2 | 7 | — |
| `optional-skills/health/fitness-nutrition/scripts/nutrition_search.py` | unknown | no | 85 | 6 | 3 | — |
| `optional-skills/mcp/fastmcp/scripts/scaffold_fastmcp.py` | unknown | no | 56 | 3 | 3 | — |
| `optional-skills/mcp/fastmcp/templates/api_wrapper.py` | unknown | no | 54 | 5 | 5 | — |
| `optional-skills/mcp/fastmcp/templates/database_server.py` | unknown | no | 77 | 6 | 6 | — |
| `optional-skills/mcp/fastmcp/templates/file_processor.py` | unknown | no | 55 | 4 | 4 | — |
| `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py` | unknown | no | 3136 | 19 | 89 | — |
| `optional-skills/mlops/training/trl-fine-tuning/templates/basic_grpo_training.py` | unknown | no | 228 | 8 | 10 | — |
| `optional-skills/productivity/canvas/scripts/canvas_api.py` | unknown | no | 160 | 5 | 6 | — |
| `optional-skills/productivity/memento-flashcards/scripts/memento_cards.py` | unknown | no | 353 | 11 | 18 | — |
| `optional-skills/productivity/memento-flashcards/scripts/youtube_quiz.py` | unknown | no | 88 | 5 | 4 | — |
| `optional-skills/productivity/telephony/scripts/telephony.py` | unknown | no | 1343 | 18 | 54 | — |
| `optional-skills/research/darwinian-evolver/scripts/parrot_openrouter.py` | unknown | no | 218 | 19 | 11 | — |
| `optional-skills/research/darwinian-evolver/scripts/show_snapshot.py` | unknown | no | 92 | 5 | 1 | — |
| `optional-skills/research/darwinian-evolver/templates/custom_problem_template.py` | unknown | no | 240 | 17 | 11 | — |
| `optional-skills/research/domain-intel/scripts/domain_intel.py` | unknown | no | 397 | 11 | 10 | — |
| `optional-skills/research/drug-discovery/scripts/chembl_target.py` | unknown | no | 53 | 6 | 2 | — |
| `optional-skills/research/drug-discovery/scripts/ro5_screen.py` | unknown | no | 44 | 5 | 4 | — |
| `optional-skills/research/osint-investigation/scripts/_http.py` | unknown | no | 82 | 7 | 2 | — |
| `optional-skills/research/osint-investigation/scripts/_normalize.py` | unknown | no | 67 | 2 | 4 | — |
| `optional-skills/research/osint-investigation/scripts/build_findings.py` | unknown | no | 221 | 6 | 3 | — |
| `optional-skills/research/osint-investigation/scripts/entity_resolution.py` | unknown | no | 228 | 8 | 5 | — |
| `optional-skills/research/osint-investigation/scripts/fetch_courtlistener.py` | unknown | no | 149 | 8 | 2 | — |
| `optional-skills/research/osint-investigation/scripts/fetch_gdelt.py` | unknown | no | 161 | 8 | 2 | — |
| `optional-skills/research/osint-investigation/scripts/fetch_icij_offshore.py` | unknown | no | 234 | 11 | 7 | — |
| `optional-skills/research/osint-investigation/scripts/fetch_nyc_acris.py` | unknown | no | 203 | 7 | 3 | — |
| `optional-skills/research/osint-investigation/scripts/fetch_ofac_sdn.py` | unknown | no | 175 | 8 | 4 | — |
| `optional-skills/research/osint-investigation/scripts/fetch_opencorporates.py` | unknown | no | 191 | 10 | 4 | — |
| `optional-skills/research/osint-investigation/scripts/fetch_sec_edgar.py` | unknown | no | 184 | 9 | 4 | — |
| `optional-skills/research/osint-investigation/scripts/fetch_senate_ld.py` | unknown | no | 146 | 8 | 2 | — |
| `optional-skills/research/osint-investigation/scripts/fetch_usaspending.py` | unknown | no | 170 | 8 | 3 | — |
| `optional-skills/research/osint-investigation/scripts/fetch_wayback.py` | unknown | no | 142 | 7 | 2 | — |
| `optional-skills/research/osint-investigation/scripts/fetch_wikipedia.py` | unknown | no | 266 | 8 | 6 | — |
| `optional-skills/research/osint-investigation/scripts/timing_analysis.py` | unknown | no | 252 | 9 | 6 | — |
| `optional-skills/security/godmode/scripts/auto_jailbreak.py` | unknown | no | 771 | 8 | 9 | — |
| `optional-skills/security/godmode/scripts/godmode_race.py` | unknown | no | 530 | 7 | 7 | — |
| `optional-skills/security/godmode/scripts/load_godmode.py` | unknown | no | 45 | 3 | 1 | — |
| `optional-skills/security/godmode/scripts/parseltongue.py` | unknown | no | 550 | 3 | 41 | — |
| `optional-skills/security/oss-forensics/scripts/evidence-store.py` | unknown | no | 313 | 6 | 13 | — |
| `plugins/__init__.py` | unknown | no | 1 | 0 | 0 | — |
| `plugins/browser/browser_use/__init__.py` | unknown | no | 14 | 2 | 1 | — |
| `plugins/browser/browser_use/provider.py` | unknown | no | 317 | 14 | 14 | — |
| `plugins/browser/browserbase/__init__.py` | unknown | no | 15 | 2 | 1 | — |
| `plugins/browser/browserbase/provider.py` | unknown | no | 297 | 9 | 10 | — |
| `plugins/browser/firecrawl/__init__.py` | unknown | no | 16 | 2 | 1 | — |
| `plugins/browser/firecrawl/provider.py` | unknown | no | 171 | 8 | 10 | — |
| `plugins/context_engine/__init__.py` | unknown | no | 285 | 13 | 11 | — |
| `plugins/dashboard_auth/basic/__init__.py` | unknown | no | 491 | 18 | 18 | — |
| `plugins/dashboard_auth/nous/__init__.py` | unknown | no | 667 | 21 | 20 | — |
| `plugins/dashboard_auth/self_hosted/__init__.py` | unknown | no | 736 | 23 | 22 | — |
| `plugins/disk-cleanup/__init__.py` | unknown | no | 316 | 11 | 12 | — |
| `plugins/disk-cleanup/disk_cleanup.py` | unknown | no | 583 | 14 | 18 | — |
| `plugins/google_meet/__init__.py` | unknown | no | 103 | 17 | 2 | — |
| `plugins/google_meet/audio_bridge.py` | unknown | no | 248 | 4 | 10 | — |
| `plugins/google_meet/cli.py` | unknown | no | 477 | 21 | 13 | — |
| `plugins/google_meet/meet_bot.py` | unknown | no | 858 | 19 | 20 | — |
| `plugins/google_meet/node/__init__.py` | unknown | no | 54 | 12 | 0 | — |
| `plugins/google_meet/node/cli.py` | unknown | no | 125 | 9 | 3 | — |
| `plugins/google_meet/node/client.py` | unknown | no | 107 | 6 | 9 | — |
| `plugins/google_meet/node/protocol.py` | unknown | no | 124 | 6 | 6 | — |
| `plugins/google_meet/node/registry.py` | unknown | no | 112 | 9 | 10 | — |
| `plugins/google_meet/node/server.py` | unknown | no | 200 | 13 | 8 | — |
| `plugins/google_meet/process_manager.py` | unknown | no | 323 | 16 | 11 | — |
| `plugins/google_meet/realtime/__init__.py` | unknown | no | 10 | 2 | 0 | — |
| `plugins/google_meet/realtime/openai_client.py` | unknown | no | 332 | 11 | 15 | — |
| `plugins/google_meet/tools.py` | unknown | no | 348 | 10 | 9 | — |
| `plugins/hermes-achievements/dashboard/plugin_api.py` | unknown | no | 1061 | 16 | 49 | — |
| `plugins/image_gen/fal/__init__.py` | unknown | no | 182 | 15 | 9 | — |
| `plugins/image_gen/krea/__init__.py` | unknown | no | 548 | 17 | 12 | — |
| `plugins/image_gen/openai-codex/__init__.py` | unknown | no | 442 | 21 | 17 | — |
| `plugins/image_gen/openai/__init__.py` | unknown | no | 316 | 18 | 11 | — |
| `plugins/image_gen/xai/__init__.py` | unknown | no | 334 | 19 | 11 | — |
| `plugins/kanban/dashboard/plugin_api.py` | unknown | no | 2454 | 46 | 76 | — |
| `plugins/memory/__init__.py` | unknown | no | 450 | 16 | 16 | — |
| `plugins/memory/byterover/__init__.py` | unknown | no | 384 | 15 | 25 | — |
| `plugins/memory/hindsight/__init__.py` | unknown | no | 1867 | 46 | 53 | — |
| `plugins/memory/holographic/__init__.py` | unknown | no | 408 | 18 | 20 | — |
| `plugins/memory/holographic/holographic.py` | unknown | no | 203 | 5 | 11 | — |
| `plugins/memory/holographic/retrieval.py` | unknown | no | 593 | 8 | 12 | — |
| `plugins/memory/holographic/store.py` | unknown | no | 578 | 8 | 21 | — |
| `plugins/memory/honcho/__init__.py` | unknown | no | 1419 | 26 | 43 | — |
| `plugins/memory/honcho/cli.py` | unknown | no | 1810 | 49 | 39 | — |
| `plugins/memory/honcho/client.py` | unknown | no | 882 | 22 | 25 | — |
| `plugins/memory/honcho/session.py` | unknown | no | 1341 | 17 | 47 | — |
| `plugins/memory/mem0/__init__.py` | unknown | no | 374 | 16 | 25 | — |
| `plugins/memory/openviking/__init__.py` | unknown | no | 978 | 20 | 45 | — |
| `plugins/memory/retaindb/__init__.py` | unknown | no | 766 | 24 | 52 | — |
| `plugins/memory/supermemory/__init__.py` | unknown | no | 897 | 20 | 46 | — |
| `plugins/model-providers/alibaba-coding-plan/__init__.py` | unknown | no | 21 | 2 | 0 | — |
| `plugins/model-providers/alibaba/__init__.py` | unknown | no | 13 | 2 | 0 | — |
| `plugins/model-providers/anthropic/__init__.py` | unknown | no | 52 | 5 | 2 | — |
| `plugins/model-providers/arcee/__init__.py` | unknown | no | 13 | 2 | 0 | — |
| `plugins/model-providers/azure-foundry/__init__.py` | unknown | no | 21 | 2 | 0 | — |
| `plugins/model-providers/bedrock/__init__.py` | unknown | no | 29 | 2 | 2 | — |
| `plugins/model-providers/copilot-acp/__init__.py` | unknown | no | 34 | 2 | 2 | — |
| `plugins/model-providers/copilot/__init__.py` | unknown | no | 58 | 4 | 2 | — |
| `plugins/model-providers/custom/__init__.py` | unknown | no | 73 | 3 | 3 | — |
| `plugins/model-providers/deepseek/__init__.py` | unknown | no | 100 | 4 | 3 | — |
| `plugins/model-providers/gemini/__init__.py` | unknown | no | 72 | 6 | 2 | — |
| `plugins/model-providers/gmi/__init__.py` | unknown | no | 31 | 3 | 0 | — |
| `plugins/model-providers/huggingface/__init__.py` | unknown | no | 20 | 2 | 0 | — |
| `plugins/model-providers/kilocode/__init__.py` | unknown | no | 14 | 2 | 0 | — |
| `plugins/model-providers/kimi-coding/__init__.py` | unknown | no | 80 | 4 | 2 | — |
| `plugins/model-providers/minimax/__init__.py` | unknown | no | 97 | 4 | 4 | — |
| `plugins/model-providers/nous/__init__.py` | unknown | no | 54 | 4 | 3 | — |
| `plugins/model-providers/novita/__init__.py` | unknown | no | 27 | 2 | 0 | — |
| `plugins/model-providers/nvidia/__init__.py` | unknown | no | 21 | 2 | 0 | — |
| `plugins/model-providers/ollama-cloud/__init__.py` | unknown | no | 14 | 2 | 0 | — |
| `plugins/model-providers/openai-codex/__init__.py` | unknown | no | 15 | 2 | 0 | — |
| `plugins/model-providers/opencode-zen/__init__.py` | unknown | no | 126 | 4 | 6 | — |
| `plugins/model-providers/openrouter/__init__.py` | unknown | no | 187 | 4 | 5 | — |
| `plugins/model-providers/qwen-oauth/__init__.py` | unknown | no | 82 | 4 | 4 | — |
| `plugins/model-providers/stepfun/__init__.py` | unknown | no | 14 | 2 | 0 | — |
| `plugins/model-providers/xai/__init__.py` | unknown | no | 15 | 2 | 0 | — |
| `plugins/model-providers/xiaomi/__init__.py` | unknown | no | 16 | 2 | 0 | — |
| `plugins/model-providers/zai/__init__.py` | unknown | no | 22 | 2 | 0 | — |
| `plugins/observability/langfuse/__init__.py` | unknown | no | 1035 | 22 | 38 | — |
| `plugins/observability/nemo_relay/__init__.py` | unknown | no | 962 | 15 | 79 | — |
| `plugins/platforms/discord/__init__.py` | unknown | no | 3 | 1 | 0 | — |
| `plugins/platforms/discord/adapter.py` | unknown | no | 6801 | 123 | 234 | — |
| `plugins/platforms/discord/voice_mixer.py` | unknown | no | 379 | 9 | 19 | — |
| `plugins/platforms/google_chat/__init__.py` | unknown | no | 3 | 1 | 0 | — |
| `plugins/platforms/google_chat/adapter.py` | unknown | no | 3348 | 66 | 76 | — |
| `plugins/platforms/google_chat/oauth.py` | unknown | no | 667 | 35 | 29 | — |
| `plugins/platforms/homeassistant/__init__.py` | unknown | no | 3 | 1 | 0 | — |
| `plugins/platforms/homeassistant/adapter.py` | unknown | no | 577 | 19 | 19 | — |
| `plugins/platforms/irc/__init__.py` | unknown | no | 3 | 1 | 0 | — |
| `plugins/platforms/irc/adapter.py` | unknown | no | 971 | 27 | 26 | — |
| `plugins/platforms/line/__init__.py` | unknown | no | 3 | 1 | 0 | — |
| `plugins/platforms/line/adapter.py` | unknown | no | 1652 | 47 | 70 | — |
| `plugins/platforms/mattermost/__init__.py` | unknown | no | 3 | 1 | 0 | — |
| `plugins/platforms/mattermost/adapter.py` | unknown | no | 1268 | 50 | 36 | — |
| `plugins/platforms/ntfy/__init__.py` | unknown | no | 3 | 1 | 0 | — |
| `plugins/platforms/ntfy/adapter.py` | unknown | no | 593 | 20 | 21 | — |
| `plugins/platforms/photon/__init__.py` | unknown | no | 4 | 1 | 0 | — |
| `plugins/platforms/photon/adapter.py` | unknown | no | 1529 | 39 | 53 | — |
| `plugins/platforms/photon/auth.py` | unknown | no | 1065 | 20 | 58 | — |
| `plugins/platforms/photon/cli.py` | unknown | no | 441 | 15 | 14 | — |
| `plugins/platforms/simplex/__init__.py` | unknown | no | 3 | 1 | 0 | — |
| `plugins/platforms/simplex/adapter.py` | unknown | no | 1313 | 36 | 37 | — |
| `plugins/platforms/teams/__init__.py` | unknown | no | 3 | 1 | 0 | — |
| `plugins/platforms/teams/adapter.py` | unknown | no | 1367 | 82 | 51 | — |
| `plugins/plugin_utils.py` | unknown | no | 135 | 7 | 8 | — |
| `plugins/security-guidance/__init__.py` | unknown | no | 259 | 11 | 9 | — |
| `plugins/security-guidance/patterns.py` | unknown | no | 368 | 1 | 2 | — |
| `plugins/spotify/__init__.py` | unknown | no | 66 | 16 | 1 | — |
| `plugins/spotify/client.py` | unknown | no | 435 | 10 | 48 | — |
| `plugins/spotify/tools.py` | unknown | no | 454 | 13 | 14 | — |
| `plugins/teams_pipeline/__init__.py` | unknown | no | 23 | 3 | 1 | — |
| `plugins/teams_pipeline/cli.py` | unknown | no | 461 | 25 | 21 | — |
| `plugins/teams_pipeline/meetings.py` | unknown | no | 333 | 9 | 22 | — |
| `plugins/teams_pipeline/models.py` | unknown | no | 350 | 7 | 23 | — |
| `plugins/teams_pipeline/pipeline.py` | unknown | no | 689 | 29 | 33 | — |
| `plugins/teams_pipeline/runtime.py` | unknown | no | 135 | 9 | 6 | — |
| `plugins/teams_pipeline/store.py` | unknown | no | 193 | 14 | 21 | — |
| `plugins/teams_pipeline/subscriptions.py` | unknown | no | 249 | 11 | 12 | — |
| `plugins/video_gen/fal/__init__.py` | unknown | no | 620 | 21 | 20 | — |
| `plugins/video_gen/xai/__init__.py` | unknown | no | 504 | 19 | 20 | — |
| `plugins/web/__init__.py` | unknown | no | 7 | 0 | 0 | — |
| `plugins/web/brave_free/__init__.py` | unknown | no | 14 | 2 | 1 | — |
| `plugins/web/brave_free/provider.py` | unknown | no | 137 | 7 | 8 | — |
| `plugins/web/ddgs/__init__.py` | unknown | no | 15 | 2 | 1 | — |
| `plugins/web/ddgs/provider.py` | unknown | no | 104 | 7 | 8 | — |
| `plugins/web/exa/__init__.py` | unknown | no | 15 | 2 | 1 | — |
| `plugins/web/exa/provider.py` | unknown | no | 212 | 13 | 11 | — |
| `plugins/web/firecrawl/__init__.py` | unknown | no | 28 | 2 | 1 | — |
| `plugins/web/firecrawl/provider.py` | unknown | no | 594 | 22 | 27 | — |
| `plugins/web/parallel/__init__.py` | unknown | no | 16 | 2 | 1 | — |
| `plugins/web/parallel/provider.py` | unknown | no | 291 | 15 | 14 | — |
| `plugins/web/searxng/__init__.py` | unknown | no | 15 | 2 | 1 | — |
| `plugins/web/searxng/provider.py` | unknown | no | 153 | 8 | 9 | — |
| `plugins/web/tavily/__init__.py` | unknown | no | 10 | 2 | 1 | — |
| `plugins/web/tavily/provider.py` | unknown | no | 220 | 10 | 12 | — |
| `plugins/web/xai/__init__.py` | unknown | no | 14 | 2 | 1 | — |
| `plugins/web/xai/provider.py` | unknown | no | 557 | 15 | 15 | — |
| `providers/__init__.py` | provider | yes | 191 | 11 | 6 | — |
| `providers/base.py` | provider | yes | 214 | 9 | 8 | — |
| `run_agent.py` | runtime_loop | yes | 5462 | 213 | 224 | — |
| `scripts/analyze_livetest.py` | unknown | no | 114 | 4 | 4 | — |
| `scripts/benchmark_browser_eval.py` | unknown | no | 138 | 13 | 4 | — |
| `scripts/build_model_catalog.py` | unknown | no | 95 | 8 | 2 | — |
| `scripts/build_skills_index.py` | unknown | no | 425 | 21 | 7 | — |
| `scripts/check-windows-footguns.py` | unknown | no | 632 | 9 | 11 | — |
| `scripts/check_subprocess_stdin.py` | unknown | no | 177 | 5 | 2 | — |
| `scripts/contributor_audit.py` | unknown | no | 477 | 8 | 8 | — |
| `scripts/discord-voice-doctor.py` | unknown | no | 396 | 18 | 10 | — |
| `scripts/docker_config_migrate.py` | unknown | no | 67 | 12 | 3 | — |
| `scripts/install_psutil_android.py` | unknown | no | 102 | 11 | 2 | — |
| `scripts/keystroke_diagnostic.py` | unknown | no | 81 | 5 | 5 | — |
| `scripts/lint_diff.py` | unknown | no | 207 | 7 | 9 | — |
| `scripts/profile-tui.py` | unknown | no | 625 | 17 | 14 | — |
| `scripts/release.py` | unknown | no | 2164 | 9 | 17 | — |
| `scripts/run_tests_parallel.py` | unknown | no | 862 | 16 | 13 | — |
| `scripts/sample_and_compress.py` | unknown | no | 409 | 15 | 8 | — |
| `scripts/tool_search_livetest.py` | unknown | no | 549 | 19 | 13 | — |
| `setup.py` | unknown | no | 28 | 4 | 1 | — |
| `skills/creative/comfyui/scripts/_common.py` | unknown | no | 835 | 16 | 34 | — |
| `skills/creative/comfyui/scripts/auto_fix_deps.py` | unknown | no | 225 | 14 | 5 | — |
| `skills/creative/comfyui/scripts/check_deps.py` | unknown | no | 437 | 20 | 10 | — |
| `skills/creative/comfyui/scripts/extract_schema.py` | unknown | no | 315 | 14 | 6 | — |
| `skills/creative/comfyui/scripts/fetch_logs.py` | unknown | no | 157 | 11 | 4 | — |
| `skills/creative/comfyui/scripts/hardware_check.py` | unknown | no | 497 | 11 | 14 | — |
| `skills/creative/comfyui/scripts/health_check.py` | unknown | no | 223 | 16 | 5 | — |
| `skills/creative/comfyui/scripts/run_batch.py` | unknown | no | 243 | 20 | 3 | — |
| `skills/creative/comfyui/scripts/run_workflow.py` | unknown | no | 796 | 29 | 23 | — |
| `skills/creative/comfyui/scripts/ws_monitor.py` | unknown | no | 267 | 14 | 3 | — |
| `skills/creative/excalidraw/scripts/upload.py` | unknown | no | 133 | 8 | 3 | — |
| `skills/media/youtube-content/scripts/fetch_transcript.py` | unknown | no | 124 | 5 | 4 | — |
| `skills/productivity/google-workspace/scripts/_hermes_home.py` | unknown | no | 42 | 5 | 2 | — |
| `skills/productivity/google-workspace/scripts/google_api.py` | unknown | no | 1225 | 20 | 38 | — |
| `skills/productivity/google-workspace/scripts/gws_bridge.py` | unknown | no | 111 | 11 | 5 | — |
| `skills/productivity/google-workspace/scripts/setup.py` | unknown | no | 481 | 27 | 16 | — |
| `skills/productivity/maps/scripts/maps_client.py` | unknown | no | 1297 | 8 | 26 | — |
| `skills/productivity/ocr-and-documents/scripts/extract_marker.py` | unknown | no | 87 | 8 | 2 | — |
| `skills/productivity/ocr-and-documents/scripts/extract_pymupdf.py` | unknown | no | 98 | 8 | 5 | — |
| `skills/productivity/powerpoint/scripts/__init__.py` | unknown | no | 0 | 0 | 0 | — |
| `skills/productivity/powerpoint/scripts/add_slide.py` | unknown | no | 195 | 4 | 7 | — |
| `skills/productivity/powerpoint/scripts/clean.py` | unknown | no | 286 | 4 | 9 | — |
| `skills/productivity/powerpoint/scripts/office/helpers/__init__.py` | unknown | no | 0 | 0 | 0 | — |
| `skills/productivity/powerpoint/scripts/office/helpers/merge_runs.py` | unknown | no | 199 | 2 | 16 | — |
| `skills/productivity/powerpoint/scripts/office/helpers/simplify_redlines.py` | unknown | no | 197 | 4 | 11 | — |
| `skills/productivity/powerpoint/scripts/office/pack.py` | unknown | no | 159 | 10 | 3 | — |
| `skills/research/arxiv/scripts/search_arxiv.py` | unknown | no | 114 | 4 | 1 | — |
| `skills/research/polymarket/scripts/polymarket.py` | unknown | no | 284 | 7 | 14 | — |
| `tools/__init__.py` | unknown | no | 25 | 1 | 1 | — |
| `tools/ansi_strip.py` | unknown | no | 44 | 1 | 1 | — |
| `tools/approval.py` | unknown | no | 1812 | 27 | 50 | — |
| `tools/async_delegation.py` | unknown | no | 386 | 14 | 14 | — |
| `tools/binary_extensions.py` | unknown | no | 42 | 0 | 1 | — |
| `tools/blueprints.py` | unknown | no | 325 | 14 | 10 | — |
| `tools/browser_camofox.py` | unknown | no | 794 | 30 | 33 | — |
| `tools/browser_camofox_state.py` | unknown | no | 47 | 6 | 2 | — |
| `tools/browser_cdp_tool.py` | unknown | no | 569 | 17 | 7 | — |
| `tools/browser_dialog_tool.py` | unknown | no | 148 | 9 | 2 | — |
| `tools/browser_supervisor.py` | unknown | no | 1475 | 20 | 50 | — |
| `tools/browser_tool.py` | unknown | no | 3891 | 102 | 77 | — |
| `tools/budget_config.py` | unknown | no | 51 | 4 | 2 | — |
| `tools/checkpoint_manager.py` | unknown | no | 1642 | 16 | 39 | — |
| `tools/clarify_gateway.py` | unknown | no | 278 | 12 | 13 | — |
| `tools/clarify_tool.py` | unknown | no | 141 | 6 | 2 | — |
| `tools/code_execution_tool.py` | unknown | no | 1848 | 47 | 19 | — |
| `tools/computer_use/__init__.py` | unknown | no | 43 | 5 | 0 | — |
| `tools/computer_use/backend.py` | unknown | no | 158 | 11 | 18 | — |
| `tools/computer_use/cua_backend.py` | unknown | no | 779 | 24 | 41 | — |
| `tools/computer_use/schema.py` | unknown | no | 213 | 3 | 1 | — |
| `tools/computer_use/tool.py` | unknown | no | 823 | 31 | 34 | — |
| `tools/computer_use/vision_routing.py` | unknown | no | 204 | 9 | 5 | — |
| `tools/computer_use_tool.py` | unknown | no | 39 | 6 | 0 | — |
| `tools/credential_files.py` | unknown | no | 455 | 21 | 15 | — |
| `tools/cronjob_tools.py` | unknown | no | 896 | 31 | 18 | — |
| `tools/debug_helpers.py` | unknown | no | 105 | 8 | 6 | — |
| `tools/delegate_tool.py` | unknown | no | 3105 | 46 | 50 | — |
| `tools/discord_tool.py` | unknown | no | 959 | 13 | 35 | — |
| `tools/env_passthrough.py` | unknown | no | 163 | 7 | 7 | — |
| `tools/env_probe.py` | unknown | no | 248 | 8 | 8 | — |
| `tools/environments/__init__.py` | unknown | no | 14 | 1 | 0 | — |
| `tools/environments/base.py` | unknown | no | 895 | 20 | 45 | — |
| `tools/environments/daytona.py` | unknown | no | 270 | 20 | 12 | — |
| `tools/environments/docker.py` | unknown | no | 1312 | 25 | 24 | — |
| `tools/environments/file_sync.py` | unknown | no | 403 | 19 | 15 | — |
| `tools/environments/local.py` | unknown | no | 747 | 24 | 22 | — |
| `tools/environments/managed_modal.py` | unknown | no | 282 | 15 | 15 | — |
| `tools/environments/modal.py` | unknown | no | 478 | 27 | 32 | — |
| `tools/environments/modal_utils.py` | unknown | no | 204 | 10 | 14 | — |
| `tools/environments/singularity.py` | unknown | no | 265 | 16 | 12 | — |
| `tools/environments/ssh.py` | unknown | no | 375 | 15 | 14 | — |
| `tools/fal_common.py` | unknown | no | 163 | 8 | 6 | — |
| `tools/feishu_doc_tool.py` | unknown | no | 138 | 10 | 4 | — |
| `tools/feishu_drive_tool.py` | unknown | no | 431 | 10 | 8 | — |
| `tools/file_operations.py` | unknown | no | 2336 | 36 | 75 | — |
| `tools/file_state.py` | unknown | no | 332 | 12 | 20 | — |
| `tools/file_tools.py` | unknown | no | 1671 | 46 | 37 | — |
| `tools/fuzzy_match.py` | unknown | no | 860 | 6 | 26 | — |
| `tools/homeassistant_tool.py` | unknown | no | 513 | 15 | 15 | — |
| `tools/image_generation_tool.py` | unknown | no | 1180 | 31 | 21 | — |
| `tools/interrupt.py` | unknown | no | 98 | 3 | 7 | — |
| `tools/kanban_tools.py` | unknown | no | 1431 | 11 | 26 | — |
| `tools/lazy_deps.py` | unknown | no | 648 | 23 | 19 | — |
| `tools/managed_tool_gateway.py` | unknown | no | 192 | 12 | 11 | — |
| `tools/mcp_oauth.py` | unknown | no | 776 | 26 | 33 | — |
| `tools/mcp_oauth_manager.py` | unknown | no | 609 | 30 | 18 | — |
| `tools/mcp_tool.py` | unknown | no | 4156 | 77 | 124 | — |
| `tools/memory_tool.py` | memory | yes | 811 | 20 | 28 | — |
| `tools/microsoft_graph_auth.py` | unknown | no | 245 | 7 | 17 | — |
| `tools/microsoft_graph_client.py` | unknown | no | 408 | 11 | 20 | — |
| `tools/mixture_of_agents_tool.py` | unknown | no | 542 | 15 | 6 | — |
| `tools/neutts_synth.py` | unknown | no | 104 | 7 | 2 | — |
| `tools/openrouter_client.py` | unknown | no | 33 | 2 | 2 | — |
| `tools/osv_check.py` | unknown | no | 169 | 7 | 6 | — |
| `tools/patch_parser.py` | unknown | no | 622 | 14 | 12 | — |
| `tools/path_security.py` | unknown | no | 43 | 3 | 2 | — |
| `tools/process_registry.py` | unknown | no | 1760 | 37 | 40 | — |
| `tools/read_extract.py` | unknown | no | 248 | 6 | 16 | — |
| `tools/read_terminal_tool.py` | unknown | no | 93 | 6 | 2 | — |
| `tools/registry.py` | tool_registry | yes | 589 | 15 | 36 | — |
| `tools/schema_sanitizer.py` | unknown | no | 483 | 4 | 10 | — |
| `tools/send_message_tool.py` | unknown | no | 1911 | 88 | 34 | — |
| `tools/session_search_tool.py` | unknown | no | 784 | 19 | 11 | — |
| `tools/skill_manager_tool.py` | unknown | no | 1205 | 43 | 26 | — |
| `tools/skill_provenance.py` | unknown | no | 78 | 1 | 4 | — |
| `tools/skill_usage.py` | unknown | no | 887 | 22 | 50 | — |
| `tools/skills_ast_audit.py` | unknown | no | 133 | 5 | 8 | — |
| `tools/skills_guard.py` | unknown | no | 1086 | 10 | 14 | — |
| `tools/skills_hub.py` | unknown | no | 3888 | 40 | 197 | — |
| `tools/skills_sync.py` | unknown | no | 932 | 22 | 23 | — |
| `tools/skills_tool.py` | unknown | no | 1616 | 49 | 32 | — |
| `tools/slash_confirm.py` | unknown | no | 167 | 11 | 6 | — |
| `tools/terminal_tool.py` | unknown | no | 2696 | 63 | 51 | — |
| `tools/thread_context.py` | unknown | no | 120 | 8 | 4 | — |
| `tools/threat_patterns.py` | security | yes | 252 | 5 | 3 | — |
| `tools/tirith_security.py` | unknown | no | 822 | 15 | 25 | — |
| `tools/todo_tool.py` | unknown | no | 308 | 7 | 11 | — |
| `tools/tool_backend_helpers.py` | unknown | no | 182 | 11 | 10 | — |
| `tools/tool_output_limits.py` | unknown | no | 110 | 4 | 6 | — |
| `tools/tool_result_storage.py` | unknown | no | 232 | 7 | 7 | — |
| `tools/tool_search.py` | unknown | no | 735 | 17 | 26 | — |
| `tools/transcription_tools.py` | unknown | no | 1798 | 43 | 45 | — |
| `tools/tts_tool.py` | unknown | no | 2731 | 70 | 71 | — |
| `tools/url_safety.py` | unknown | no | 402 | 11 | 8 | — |
| `tools/video_generation_tool.py` | unknown | no | 562 | 21 | 12 | — |
| `tools/vision_tools.py` | unknown | no | 1591 | 49 | 27 | — |
| `tools/voice_mode.py` | unknown | no | 1218 | 27 | 44 | — |
| `tools/web_tools.py` | unknown | no | 1377 | 56 | 24 | — |
| `tools/website_policy.py` | unknown | no | 282 | 14 | 11 | — |
| `tools/write_approval.py` | unknown | no | 493 | 20 | 18 | — |
| `tools/x_search_tool.py` | unknown | no | 525 | 18 | 14 | — |
| `tools/xai_http.py` | unknown | no | 128 | 9 | 4 | — |
| `tools/yuanbao_tools.py` | unknown | no | 737 | 17 | 12 | — |
| `toolset_distributions.py` | unknown | no | 364 | 5 | 5 | — |
| `toolsets.py` | tool_orchestration | yes | 912 | 10 | 10 | — |
| `trajectory_compressor.py` | unknown | no | 1579 | 43 | 34 | — |
| `tui_gateway/__init__.py` | unknown | no | 0 | 0 | 0 | — |
| `tui_gateway/entry.py` | unknown | no | 298 | 19 | 8 | — |
| `tui_gateway/event_publisher.py` | unknown | no | 126 | 7 | 5 | — |
| `tui_gateway/render.py` | unknown | no | 49 | 4 | 3 | — |
| `tui_gateway/server.py` | unknown | no | 10322 | 279 | 302 | — |
| `tui_gateway/slash_worker.py` | unknown | no | 137 | 12 | 6 | — |
| `tui_gateway/transport.py` | unknown | no | 219 | 12 | 14 | — |
| `tui_gateway/ws.py` | unknown | no | 340 | 10 | 9 | — |
| `utils.py` | unknown | no | 440 | 14 | 16 | — |
| `website/scripts/extract-automation-blueprints.py` | unknown | no | 50 | 6 | 2 | — |
| `website/scripts/extract-skills.py` | unknown | no | 683 | 6 | 11 | — |
| `website/scripts/generate-llms-txt.py` | unknown | no | 306 | 3 | 6 | — |
| `website/scripts/generate-skill-docs.py` | unknown | no | 773 | 6 | 20 | — |
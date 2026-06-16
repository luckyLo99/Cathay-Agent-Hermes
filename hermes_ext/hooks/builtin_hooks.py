from __future__ import annotations

from hermes_ext.hooks.contracts import HookDecision, HookEvent, HookEventName
from hermes_ext.hooks.dispatcher import HookDispatcher
from hermes_ext.security.pretool_guard import PreToolGuard


class PreToolGuardHook:
    name = "pretool_guard"

    def __init__(self, guard: PreToolGuard | None = None) -> None:
        self.guard = guard or PreToolGuard()

    def handle(self, event: HookEvent) -> HookDecision:
        if event.event_name != HookEventName.PRE_TOOL_USE:
            return HookDecision.noop(handler_name=self.name)

        decision = self.guard.evaluate_event(event)
        return decision.to_hook_decision(handler_name=self.name)


def build_default_dispatcher() -> HookDispatcher:
    dispatcher = HookDispatcher()
    hook = PreToolGuardHook()
    dispatcher.register(
        HookEventName.PRE_TOOL_USE,
        hook.handle,
        name=hook.name,
        priority=10,
    )
    return dispatcher
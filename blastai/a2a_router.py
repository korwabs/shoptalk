from __future__ import annotations

"""Simple A2A router and MCP context manager."""

import asyncio
from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable, Dict, Optional


@dataclass
class AgentMessage:
    """Standardized message between agents."""

    sender: str
    receiver: str
    type: str
    payload: Dict[str, Any]


AgentHandler = Callable[[AgentMessage], Awaitable[Optional[AgentMessage]]]


class AgentRouter:
    """Central router for A2A communication."""

    def __init__(self) -> None:
        self._agents: Dict[str, AgentHandler] = {}
        self._queue: asyncio.Queue[AgentMessage] = asyncio.Queue()
        self._running = False
        self._task: Optional[asyncio.Task] = None

    def register_agent(self, name: str, handler: AgentHandler) -> None:
        """Register an agent with its message handler."""
        self._agents[name] = handler

    async def start(self) -> None:
        """Start the routing loop."""
        if not self._running:
            self._running = True
            self._task = asyncio.create_task(self._route_loop())

    async def stop(self) -> None:
        """Stop the routing loop."""
        if self._running:
            self._running = False
            if self._task:
                self._task.cancel()
                try:
                    await self._task
                except asyncio.CancelledError:
                    pass

    async def send(self, message: AgentMessage) -> None:
        """Queue a message for delivery."""
        await self._queue.put(message)

    async def _route_loop(self) -> None:
        while self._running:
            try:
                message = await self._queue.get()
            except asyncio.CancelledError:
                break
            handler = self._agents.get(message.receiver)
            if handler:
                try:
                    response = await handler(message)
                    if response:
                        await self._queue.put(response)
                except Exception:
                    # Ignore handler errors to keep router alive
                    pass


class ContextManager:
    """Minimal MCP context storage."""

    def __init__(self) -> None:
        self._contexts: Dict[str, Dict[str, Any]] = {}

    def get(self, user_id: str) -> Dict[str, Any]:
        """Get context for a user."""
        return self._contexts.setdefault(user_id, {})

    def update(self, user_id: str, data: Dict[str, Any]) -> None:
        """Update context for a user."""
        ctx = self._contexts.setdefault(user_id, {})
        ctx.update(data)

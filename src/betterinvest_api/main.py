"""FastAPI application entrypoint."""

from fastapi import FastAPI

from betterinvest_api.presentation.routers import health

app = FastAPI(
    title="BetterInvest Core API",
    version="0.1.0",
)

app.include_router(health.router)

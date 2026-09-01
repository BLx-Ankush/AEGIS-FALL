from fastapi import FastAPI

from .orchestrator import orchestrate_target
from .schemas import ScanResponse, TargetRequest

app = FastAPI(title="AEGIS-FALL")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/scan", response_model=ScanResponse)
async def scan_target(payload: TargetRequest) -> ScanResponse:
    findings = await orchestrate_target(payload.target)
    return ScanResponse(target=payload.target, findings=findings)

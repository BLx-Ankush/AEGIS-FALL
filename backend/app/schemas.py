from pydantic import BaseModel


class TargetRequest(BaseModel):
    target: str


class ScanResponse(BaseModel):
    target: str
    findings: list[str]

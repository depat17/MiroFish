from dataclasses import dataclass

@dataclass
class Signal:
    agent_type: str
    source: str
    content: str
    pain_point: str
    frequency: str
    urgency_score: int
    confidence: float
    raw_url: str
    company_id: int
    timestamp: str
    metadata: dict
    category: str
    target_user: str
    trend_velocity: float
    validation_score: float
    evidence_urls: list

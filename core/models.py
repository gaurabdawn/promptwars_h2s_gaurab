from pydantic import BaseModel
from typing import Any, Optional

class BridgeOutput(BaseModel):
    """
    The Ultimate 'Setu' Envelope: 
    Professional API structure, but the payload can be ANYTHING.
    """
    status: str
    payload: Optional[Any] = None  # Accepts List, Dict, String, etc.
    error: Optional[str] = None
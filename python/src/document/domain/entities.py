
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from __seedwork.domain.entity import Entity


@dataclass(frozen=True, kw_only=True, slots=True)
class Document(Entity):

    document: str
    created_at: Optional[datetime] = field(
        default_factory=datetime.utcnow
    )

    def __post_init__(self):
        if not self.created_at:
            self._set('created_at',  datetime.utcnow())


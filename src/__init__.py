from datetime import datetime
from .core.rev_eng import Rev_Eng

rev = Rev_Eng(origin="tsal_entry")
rev.log_event("IMPORT", timestamp=datetime.utcnow().isoformat())

__all__ = ["rev"]

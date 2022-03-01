from typing import List
from pydantic import BaseModel


class MultipleTextQuery(BaseModel):
    texts: List[str]
    echo_input: bool = True

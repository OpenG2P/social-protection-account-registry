from openg2p_fastapi_common.controller import BaseController

from ..models.participant import ParticipantsTypeIDGetResponse
from ..services.als_oracle_service import MojaloopOracleService


class ALSOracleController(BaseController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.als_oracle = MojaloopOracleService.get_component()

        self.router.tags += ["mojaloop-als-oracle"]
        self.router.prefix += "/internal/mojaloop"

        self.router.add_api_route(
            "/participants/{type}/{id}",
            self.get_participants,
            responses={200: {"model": ParticipantsTypeIDGetResponse}},
            methods=["GET"],
        )

    async def get_participants(self, type: str, id: str):
        return await self.als_oracle.get_participants(type, id)

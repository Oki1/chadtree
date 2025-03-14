from typing import Optional

from pynvim_pp.nvim import Nvim

from ..registry import rpc
from ..state.next import forward
from ..state.types import State
from ..version_ctl.git import status
from .types import Stage


@rpc(blocking=False)
async def vc_refresh(state: State) -> Optional[Stage]:
    """
    VC Refresh
    """

    if state.enable_vc:
        cwd = await Nvim.getcwd()
        vc = await status(cwd, prev=state.vc)
        new_state = await forward(state, vc=vc)
        return Stage(new_state)
    else:
        return None

import httpx, asyncio, typing as T
from src.settings import settings

class ComfyClient:
    def __init__(self, host: str = settings.comfy_host):
        self.host = host

    async def queue(self, workflow: dict) -> str:
        r = await httpx.AsyncClient().post(
            f"{self.host}/prompt", json={"prompt": workflow}
        )
        r.raise_for_status()
        return r.json()["prompt_id"]

    async def wait_images(self, prompt_id: str) -> list[str]:
        while True:
            await asyncio.sleep(1)
            hist = (
                await httpx.AsyncClient().get(f"{self.host}/history/{prompt_id}")
            ).json()
            if not hist.get(prompt_id, {}).get("outputs"):
                continue
            for node in hist[prompt_id]["outputs"].values():
                if imgs := node.get("images"):
                    return [
                        f"{self.host}/view?"
                        f"filename={i['filename']}&subfolder={i['subfolder']}&type={i['type']}"
                        for i in imgs
            ]
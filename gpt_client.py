from venv import create

import httpx
import openai
from aiogram import Bot

import config
from .enums import GPTModel
from .gpt_message import GPTMessage

class GPTService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, model: GPTModel=GPTModel.GPT_4_TURBO):
        self._model = model.value
        self._gpt_token = config.OPENAI_API_KEY
        self._proxy = config.PROXY
        self._client = self._create_client()


    def _create_client(self):
        gpt_client = openai.AsyncOpenAI(
            api_key=self._gpt_token,
            # http_client=httpx.AsyncClient(
            #     proxy=self._proxy,
            # )
        )
        return gpt_client

    async def request(self, message: GPTMessage, bot:Bot) -> str:
        try:
            response = await self._client.chat.completions.create(
                message = message.list.message_list,
                model = self._model
            )

            return response.choices[0].message.content
        except Exception as e:
            await bot.send_message(
                chat_id=config.ADMIN_ID,
                text=str(e)
            )
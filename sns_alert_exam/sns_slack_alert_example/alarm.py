import os
import logging
# from venv import logger
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from layer.common.utils import init_alarm
from layer.common.constant import SLACK_CHANNELS

init_alarm() #토큰 자동 등록 - paramstore(AWS)에서 불러옴

def main(p_channel_id:str, p_message:str):
  # 슬렉서버로 메세지를 전달할 객체 (메세지만 뿌려주는 챗봇<알람 챗봇>)
  # 따라서 필요한 건 봇 토큰만 있으면 된다.
  client = WebClient(token=os.environ.get('SLACK_BOT_TOKEN', None))

  try:
    # https://api.slack.com/methods/chat.postMessage
    # 해당 채널에 메세지 전달 
    result = client.chat_postMessage(
      channel=p_channel_id,
      text=p_message
    )
    logging.info(result)

  except SlackApiError as e:
    logging.error(f"Error posting message: {e}")

if __name__ == "__main__":
  # 슬렉 채널 아이디 
  channel_id = SLACK_CHANNELS.ALARM.value[1]
  # 전달할 메세지 
  message = "Hello World"
  main(p_channel_id=channel_id, p_message=message)

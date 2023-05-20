# 导入库
from google.cloud import speech

# 设定key
Keyfile = "C:\\Controller_Secret_settings\\GoogleApi_Key.json"

# 导入key文件
client = speech.SpeechClient.from_service_account_file(Keyfile)

# 打开音频文件对象并将内容读取为一个对象
with open("3-Audio 1 [2023-05-19 143300].wav", 'rb') as f:
    mp3Data = f.read()

#
audiofile = speech.RecognitionAudio(content=mp3Data)

config = speech.RecognitionConfig(
    sample_rate_hertz=16000,# 16000 是最佳的
    enable_automatic_punctuation=True,
    language_code='ja-JP'
    #注意必须是16bit
)

response = client.recognize(
    config=config,
    audio=audiofile
)

for result in response.results:
    print(result.alternatives[0].transcript)

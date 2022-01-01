import ibm_watson
from ibm_watson import SpeechToTextV1 
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
url_s2t="https://api.jp-tok.speech-to-text.watson.cloud.ibm.com/instances/436d4fe0-30da-445a-aa76-4f20710496e1"
iam_apikey_s2t = "ljKzGNmNnPKYN2qLQRKx026L0ok0yRUV-9Csw3P3fw5f"
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t
filename='PolynomialRegressionandPipelines.mp3'
with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
print(response.result)
from pandas import json_normalize
json_normalize(response.result['results'],"alternatives")
recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
print(recognized_text)

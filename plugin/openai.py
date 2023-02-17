# by https://github.com/fireganqQ #

import openai

class emptyInformation(RuntimeError):
   def __init__(self, arg: str):
      arg

class Ai:
    def __init__(self) -> None:
        organization = ""
        api_key = ""

        if organization=="" or api_key=="":
            raise emptyInformation('api key ile organization bilgilerinizi tam doldurunuz!')

        openai.organization = organization
        openai.api_key = api_key
    
    def ai(self, prompt: str) -> str:
        client = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=1000)
        return client["choices"][0]["text"]
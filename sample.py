import os
from aixplain.factories import ModelFactory

api_key = os.environ.get('AIXPLAIN_API_KEY')

model = ModelFactory.get("61dc52976eb5634cf06e97cc")
translation = model.run("This is a sample text")
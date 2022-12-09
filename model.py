import openai


userTemp = 0.8
userLength = 1200

poem = """Write a haiku with the following words: 
---
{input}
---
This is the haiku: """

def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key

class GeneralModel:
    def __init__(self):
        print("Model Intilization--->")
        # set_openai_key(API_KEY)

    def query(self, prompt, userTemp2, userLength2, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """

        # arguments to send the API
        #userTemp should a decimal between 0 and 1
        #userLength is the amount of Tokens, somewhere around 1000
        kwargs = {
            "engine": "text-davinci-003",
            "temperature": userTemp2,
            "max_tokens": userLength2,
            "best_of": 1,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "stop": ["###"],
        }


        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]


        r = openai.Completion.create(prompt=prompt, **kwargs)["choices"][0][
            "text"
        ].strip()
        return r

    def model_prediction(self, input, userTemp3, userLength3, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key(api_key)
        output = self.query(poem.format(input = input), userTemp3, userLength3)
        return output
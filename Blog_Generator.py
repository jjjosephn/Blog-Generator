import openai
from dotenv import dotenv_values

config = dotenv_values(".env")                                              #Hold dictionary variables

openai.api_key = config['API_KEY']                                          #Grab API key to access OpenAI

def generate_blog(topic):
    response = openai.Completion.create(                                    #Store generated response in 'response'
        model = 'text-davinci-002',                                         #Current latest and best model to use
        prompt = 'Write a paragraph about the following topic: ' + topic,   #Prompt user
        max_tokens = 400,                                                   #Average paragraph has 300 words, and 75 words/100 tokens
        temperature = 0.3                                                   #Randomness of response
    )

    retrieve_blog = response.choices[0].text                                #Returned object has many choices but I only want text

    return retrieve_blog                                                    #Return

keep_writing = True                                                         #Boolean to keep writing

while keep_writing:     #Parameter is True
    answer = input('Do you want to keep writing? Y for yes, and N for no')  #Ask if user wants to continue writing
    if answer.upper() == 'Y':                                               #Set all answers to Y
        topic = input('The topic of this paragraph would be: ')             #Ask user what the new topic would be
        print(generate_blog(topic))                                         #Print new paragraph
    else:
        keep_writing = False                                                #Stop writing
        print("\nThanks for stopping by!")                                  #Print Leave message








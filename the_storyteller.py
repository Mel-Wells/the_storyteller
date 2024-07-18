import openai 
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config['API_KEY']

def generate_story(genre, characters, location, theme): 
    response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = 'Write a story based off the genre, characters, location and theme. Give the ending a twist. ' + genre + characters + location + theme,
        max_tokens = 400, 
        temperature = 0.5
    )

    generate_story = response.choices[0].text
    return generate_story

keep_writing = True

while keep_writing: 
    answer = input('\nWelcome to the storyteller where I make things come to life. Are you ready for a story?: ')

    if answer.lower() == 'yes' and answer.lower() == 'sure': 
        genre = input('\nWhat will the genre of this story be?: ')
        characters = input("\nWhat will the name of your character or characters be? If you have no preference, just enter NONE: ")

        if characters == 'NONE': 
            print("Okay, lets move on then!\n")
        else:
            print('Interesting...\n')

        location = input("What universe/location do you want this to occur?: ")
        theme = input('What theme were you thinking of?: ')
        print("\nOkay, give me a bit... I\'m a work in progress... Processing...\n")
        
        print(generate_story(genre, characters, theme))
    else:
        print('Alright. Goodbye!')
        keep_writing = False 



    





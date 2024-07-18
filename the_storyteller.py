import openai 
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config['API_KEY']

def generate_story(genre, characters, location, theme): 
    response = openai.completions.create(
        model = 'gpt-3.5-turbo-instruct',
        prompt = 'Write a short story based off the genre, characters, location and theme. Make sure it has an ending. ' + genre + characters + location + theme,
        max_tokens = 600, 
        temperature = 0.5
    )

    generate_story = response.choices[0].text
    return generate_story

keep_writing = True

while keep_writing: 
    answer = input('\nWelcome to the storyteller where I make things come to life. Are you ready for a story?: ')

    if answer.lower() == 'yes': 
        genre = input('\nWhat will the genre of this story be?: ')
        characters = input("\nWhat will the name of your character or characters be? If you have no preference, just enter NONE: ")

        if characters == 'NONE': 
            print("Okay, lets move on then!\n")
        else:
            print('Interesting...\n')

        location = input("\nWhat universe/location do you want this to occur?: ")
        theme = input('\nWhat theme were you thinking of?: ')
        print("\nOkay, give me a bit... I\'m a work in progress... Processing...\n")
        
        print(generate_story(genre, characters, location, theme))
    else:
        print('Alright. Goodbye!')
        keep_writing = False 



    





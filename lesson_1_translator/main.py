from googletrans import Translator, LANGUAGES


def main():
    translator = Translator()
    title = "Music’s Impact and Influence on Everyday Life"
    text = """As a person who loves music and even got into playing an instrument myself, it does have an influence on my everyday life. I’m constantly listening to music whether it be while working during class, in the car on my way home, or just while practicing playing the guitar. Music is all around the world and one of the most popular forms of entertainment and escape. It consists of many different styles and opinions, whether it be just personal opinion or even a part of your culture.
    Everyone has their own taste and opinions on music, which is why it’s one of the most common things to talk about. Just like how we all hear people say, “a lot can be said about a person based on their music taste,” and it’s fun finding people who share common interests with you, such as a favorite song or favorite song artist, or maybe something just as simple as liking the same music genre. It can also have an effect on people’s emotions and mind, as well as improving mental health. 
    “Music exerts a powerful influence on human beings. It can boost memory, build task endurance, lighten your mood, reduce anxiety and depression, stave off fatigue, improve your response to pain, and help you work out more effectively,” describes Heathline.
    “Get Well Soon” is a song about Ariana confronting her anxieties and mental state.
    I’ve been listening to music for as long as I can remember, even if it was just for remembering the days of the week back in elementary school. Since being a kid, my favorite songs have changed, my favorite music artists have changed, and even my favorite genres have changed, but they’ve all helped me get to where I am now. It may not seem like it could have that effect, but I wouldn’t be the same person without it.
    I first began to really understand music’s impact a few years ago when my everyday life was full of anxiety. Music was my form of comfort that could be used for growth and improvement. After finding an artist you can connect to through lyrics, it really opened my eyes to the fact that you aren’t alone, and that even our “all perfect” celebrities deal with it from time to time. It’s a universal feeling.
    “Healing with sound is believed to date back to ancient Greece, when music was used in an attempt to cure mental disorders. Throughout history, music has been used to boost morale in military troops, help people work faster and more productively, and even ward off evil spirits by chanting,” according to Healthline.
    I’ve also been to many concerts within the past few years, and every time it’s a new experience. A single concert ended up changing my entire music taste. Concerts bring the music to life, people dance, let out their emotions, and have a good time. Nothing is better than hearing live music, especially from your favorite bands. I have even gone to see some of the same bands more than once. Although they may still have the same set and stage performance it was even more special than the first. 
    Whenever you listen to music whether it be live or not, you can always find new things about it. It’s an experimental experience, and you can always learn from it. Most artists put their very own personality into their songs and share common feelings with their listeners, allowing people to easily connect with music on their own level.
    “Music has the potential to be a powerful healing tool in a variety of ways and pervades every aspect of our existence. Songs are used to define spiritual ceremonies, toddlers learn the alphabet via rhyme and verse, and malls and restaurants, where we choose to spend our free time, are rarely silent,” describes Lia Peralta, in her blog on Save the Music’s website.
    Even though my taste in music has changed and yours may too, it’s still comforting and almost nostalgic listening to that one artist, just like how we still listen to music from when we were younger to remember the past, especially the one who helped my younger self and being able to see just how much I have improved and matured since then. I don’t know where I would be now if I hadn’t found her."""
    author = "Bryleigh Conley, Reporter"
    date = "April 12, 2023"

    lang = input(f"Список доступных языков:\n{LANGUAGES}\nНапишите один из доступных языков: ")

    res_text = translator.translate(text, src="en", dest=lang)
    res_title = translator.translate(title, src="en", dest=lang)
    res_author = translator.translate(author, src="en", dest=lang)
    res_date = translator.translate(date, src="en", dest=lang)

    print(f"{res_title.text}\n\n{res_author.text}\n{res_date.text}\n\n{res_text.text}")

if __name__ == "__main__":
    main()

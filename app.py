from flask import Flask, render_template, url_for
from title_generator import make_a_title

app = Flask(__name__)

@app.route("/")
def start():
    title = make_a_title()
    
    music = url_for('static', filename='music/7.mp3')

    image = url_for('static', filename='img/ship.png')

    text = """Cruising through the vast waves of space-time, the colony ship is approaching its destination: the lonely planet Vega 223 orbiting around the bright red dwarf people call the Last Star for some unknown reason.
    
    It's time for the crew to wake up from hibernation, and you are the first one to find yourself awake.
    """

    choices = [
        ('beginning', "Try to climb out of the stasis pod"),
        ('incident1', "Stay in the pod for a while")
    ]

    return render_template('adventure.html', title=title, text=text, track=music, image=image, choices=choices)


@app.route("/beginning")
def beginning():
    title = "Stasis Chamber"

    music = url_for('static', filename='music/4.mp3')

    image = url_for('static', filename='img/pod.png')

    text = """As your head starts to spin, you realize that climbing out of the sleeping pod right after waking up was not a very good idea. Darkness if forming in the corners of your eyes...
    
    After a while though you manage to maintain balance, look around, and get dressed. Right at this moment the alarm goes off, and a smooth voice begins repeating: 'Attention, code Pale Star!' over and over again.
    """

    choices = [
        ('incident2', "Search around for a weapon, or something to defend yourself with"),
        ('incident3', "Run to the only door and try to escape through it")    
    ]

    return render_template('adventure.html', title=title, text=text, track=music, image=image, choices=choices)

@app.route("/incident1")
def incident1():
    title = "In the Pod"

    music = url_for('static', filename='music/3.mp3')

    image = url_for('static', filename='img/pod.png')

    text = """As you lay in the pod listening to the humming of the machinery, your eyes begin to shut, and you fall asleep...

    'Attention, code Pale Star!' -  a smooth yet loud voice tears through your consciousness, and you are fully awake again hearing an alarm. You notice it's gotten darker in the room. Is it dark because of the alarm, or is it something else?
    """

    choices = [
        ('incident5', "Stay in the sleeping pod"), 
        ('incident3', "Climb out as quickly as you can")
    ]

    return render_template('adventure.html', title=title, text=text, track=music, image=image, choices=choices)

@app.route("/incident2")
def incident2():
    title = "The Note"

    music = url_for('static', filename='music/5.mp3')

    image = url_for('static', filename='img/pod.png')

    text = """Your search for a weapon abruptly stops as you see a note attached to the terminal. The alarm pitch goes up a notch and the voice starts the countdown: 'Ninety-nine, ninety-eight, ninety-seven...'
    
    You clearly have very little time left.
    """

    choices = [
        ('incident4', "Read the note"),
        ('incident3', "Ignore the note and run to the door")
    ]

    return render_template('adventure.html', title=title, text=text, track=music, image=image, choices=choices)

@app.route("/incident3")
def incident3():
    title = "The Door"

    music = url_for('static', filename='music/11.mp3')

    image = url_for('static', filename='img/pod.png')

    text = """You reach the door on the opposite end of the room, the alarm pitch goes up as you frantically press the button on the panel...
    
    Finally the door slowly begin to open. Peeking through you see moving dark shadows and black ripples in the corridor behind the door...
    """

    choices = [
        ('destruction5', "Step through the door into the corridor"),
        ('destruction3', "Run back and hide inside the pod")
    ]

    return render_template('adventure.html', title=title, text=text, track=music, image=image, choices=choices)

@app.route("/incident4")
def incident4():
    title = "The Chance"

    music = url_for('static', filename='music/9.mp3')

    image = url_for('static', filename='img/pod.png')

    text = """You grab the note and start skimming through the inked black words.

    'The Darkness can not be contained for long. As soon as a living organism awakes it senses the brain activity go up and rushes to seize it...' The next couple of paragraphs give little hope of survival.

    'Immediately get inside the sleeping pod and press the blue EVAC button!' - reads the last sentence.

    Who wrote this? Is this true or an elaborate trap? 
    """

    choices = [
        ('thewinner', "Get inside the sleeping pod and press the blue button"),
        ('destruction3', "Get inside the sleeping pod and press the yellow button")
    ]

    return render_template('adventure.html', title=title, text=text, track=music, image=image, choices=choices)

@app.route("/incident5")
def incident5():
    title = "Still in the Pod"

    music = url_for('static', filename='music/1.mp3')

    image = url_for('static', filename='img/pod.png')

    text = """You hear the voice counting: '...twenty-four, twenty-three, twenty-two...', and your stomach growls. It seems the darkness around you is getting thicker. To distract yourself from the unpleasant sensation you look around the pod.
    
    Two small lights catch your attention, blue and yellow. Looking closer you realize there are buttons underneath the lights...
    """

    choices = [
        ('thewinner', "Press the yellow button"),
        ('destruction3', "Press the blue button")
    ]

    return render_template('adventure.html', title=title, text=text, track=music, image=image, choices=choices)

@app.route("/destruction3")
def destruction3():
    title = "The Darkness"

    music = url_for('static', filename='music/2.mp3')

    image = url_for('static', filename='img/ship.png')

    text = """As you lay inside the pod and wait nothing happens for a little while...

    Then a dark shadow skips around the room, then another, and another... The countdown reaches zero, and a loud explosion shuts down your consciousness...

    You hear nothing, you see nothing, you feel nothing...
    """

    return render_template('adventure.html', title=title, track=music, image=image, text=text)

@app.route("/destruction5")
def destruction5():
    title = "The Darkness"

    music = url_for('static', filename='music/8.mp3')

    image = url_for('static', filename='img/ship.png')

    text = """You step through the door into the corridor shadows start to flow around you, and the darkness becomes thicker.

    As your mind shuts down, the last thing you hear is the smooth voice saying: '...one, zero. Activating self-destruction.'

    You hear nothing, you see nothing, you feel nothing...
    """

    return render_template('adventure.html', title=title, track=music, image=image, text=text)

@app.route("/thewinner")
def thewinner():
    title = "Escape"

    music = url_for('static', filename='music/10.mp3')

    image = url_for('static', filename='img/planet.png')

    text = """The lid of the pod closes with a swoosh, cutting off the sound of the countdown. A round opening swallows the pod and ejects it out of the colony ship...

    As you look through the glossy window of the pod, you see dozens of sparkling stasis pods moving away from the ship. Then a bright light tears through, and it explodes...

    A few hours later the pod opens the lid again, and you see blue sky above. You have escaped the darkness, you have made it to the surface of Vega 223, you have survived!   
    """

    return render_template('adventure.html', title=title, track=music, image=image, text=text)
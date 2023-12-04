#https://www.youtube.com/watch?v=LsS4G5VXi4c&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=129
from flask import Flask
import datetime


app = Flask(__name__,static_url_path="/static")
today = f"\n{datetime.date.today()}"

@app.route('/')
def home():
    page = f"""<!--#https://www.youtube.com/watch?v=phTPvb-JHYw&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=127-->
<!---->
<!DOCTYPE html>
<html lang = "en">

<head>
    <meta charset="utf-8">
    <meta name = "viewport" content = "width=device-width">
    <title>Linktree</title>   
    <link href="static/css/75.css" rel="stylesheet" type="text/css"/>
</head>

<body>
<a href='/portfolio'>portfolio</a>
    <img src= "static/images/anya.jpg" width= 30% alt="anya Image" >
    <h1 class="xdxp">Anya Forger</h1>
    <h3>The <span style="color: pink;">pinkest</span> nerd</h3>
    <h2 class="xdxp">LINKS</h2>
    <h2>👇</h2>
    <ul class="list">
        <li >
            <a href="https://twitter.com/HourlyAnya_">Twitter</a>
        </li>        
        <li>
            <a href="https://www.youtube.com/@anyaforger5025">Youtube</a>
        </li>
        <li>
            <a href="https://www.instagram.com/anyaforger_official/">instagram</a>
        </li>
    </ul>
    <h2 class="date">{today}</h2>
    
</body>

"""
    return page
@app.route('/portfolio')
def portfolio():
    page = f"""<!-- https://www.youtube.com/watch?v=CgG3h-wzwr0&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=123 -->

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>My portfolio</title>
    <link href="static/css/73and74.css" rel="stylesheet" type="text/css"/>
</head>

<body>
    <a class="indexlink" href='/'>Linktree</a>
    <h1>My Portfolio - Nono Actually a World of Baddies</h1>
    <h2>Yoru</h2>
    <p>Yor Forger, the dual-faced Berlint City Hall clerk and covert Garden assassin "Thorn Princess," navigates a delicate balance between ordinary life and deadly intrigue. Her beauty and efficiency create a captivating duality, embodying a character torn between maternal instincts and a hidden underworld.</p>
    <img src= "static/images/Yoru.png" alt="Yoru Image">

    <h2>Zero</h2>
    <p>Zero, the relentless protagonist of Drakengard, navigates a world tainted by the malevolent flower, confronting harrowing challenges that go beyond physical pain. Her journey unfolds as a symphony of sorrow, depicting a soul weighed down by tragic choices, unrelenting darkness, and a haunting quest for retribution, carving a narrative that resonates with profound melancholy.</p>
    <img src="static/images/Zero.jpeg" alt="Zero Image">

    <h2>Seras</h2>
    <p>Seras Victoria, the formidable vampire from Hellsing, embarks on a journey of blood and battles. Her transformation from human to vampire marks a pivotal point in a narrative filled with gothic horror, supernatural struggles, and a quest for identity.</p>
    <img src="static/images/Seras.jpeg" alt="seras.jpg">

    <h2>Sakuya</h2>
    <p>Sakuya Izayoi, the enigmatic chief maid of the Scarlet Devil Mansion in Touhou, moves through time with deadly elegance. Her intricate dance of knives paints a picture of servitude tainted by a haunting past, as she weaves a tapestry of manipulation, blood, and the echoes of forgotten moments.</p>
    <img src="static/images/Sakuya.jpeg" alt="Sakuya Image">

    <h2>Misato</h2>
    <p>Misato Katsuragi, the complex and tormented character from Evangelion, navigates a world on the brink of apocalypse. Her role as a NERV officer conceals layers of inner turmoil, haunted by personal demons and a fragile grasp on normalcy. In the shadows of giant mechs, Misato's journey unfolds as a symphony of chaos, blending duty and despair in a post-apocalyptic landscape.</p>
    <img class=blurb src="static/images/Misato.jpeg" alt="Misato Image">


</body>

</html>
"""
    return page
app.run(host = '127.0.0.1' , port=81)

#Opens file where data will be stored
myfile2 = open("detailsCOC.html", "w")

#Creates the foundation for the HTML (CSS)
def start_file():
    starting = '''
<!DOCTYPE html>

<html lang = 'en-US'>

<head>

<style>
h4 {
color: indianred;
font-family: avenir;
text-align: center;
}
h5 {
color: orange;
font-family: avenir;
text-align: center;
text-transform: capitalize;
}
h6 {
color: orange;
font-family: avenir;
text-align: center;
}
th:hover {
text-decoration:underline;
}
th, td {
padding: 10px;
text-align: center;
}
a:link, a:active, a:visited {
color: orange; 
background-color: transparent; 
text-decoration: none;
}
a:hover {
color: orangered;
background-color: beige;
text-decoration: underline;
}
table {
width:100%
border: 1px solid black;
border: collapse;
}
th,td {
font-family: avenir;
text-align: center;
border: 1px solid black;
border: collapse;
padding: 10px
}

img {
height:300px;
width:100px
}

</style>  

<!-- Compiled and minified CSS -->
<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css'>

<!--Import Google Icon Font-->
<link href='https://fonts.googleapis.com/icon?family=Material+Icons' rel='stylesheet'>

<title>Account Analysis</title>

</head>
'''
    myfile2.write(starting)

#Ends the file with script. Script is used to initialize items from CSS Materialized
def close_file():
    myfile2.write("<script src='https://code.jquery.com/jquery-3.3.1.min.js'></script>\n<script src='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js'></script>\n<script>$(document).ready(function(){$('.tabs').tabs();});</script>")
    myfile2.write("</body>")
    myfile2.write("</html>")
    myfile2.close()

#Receives response from the main module
def get_details(response):
#Data setting
#For the Basics tab
    user_json = response.json()

    data_thlevel = str(user_json['townHallLevel'])
    data_bhlevel = str(user_json['builderHallLevel'])
    data_exp = str(user_json['expLevel'])
    data_trophies = str(user_json['trophies'])
    data_max_trophies = str(user_json['bestTrophies'])
    data_builder_trophies = str(user_json['versusTrophies'])
    data_max_builder_trophies = str(user_json['bestVersusTrophies'])
    data_warstars = str(user_json['warStars'])
    try:
        data_league_name = (user_json['league']['name'])
    except KeyError:
        data_league_name = 'No League'
    try:
        data_clan_name = (user_json['clan']['name'])
        clan_icon = (user_json['clan']['badgeUrls']['large'])
        data_clan_level = str(user_json['clan']['clanLevel'])
        data_clan_role = str(user_json['role'])
    except KeyError:
        data_clan_name = 'No Clan'
        clan_icon = 'https://www.sccpre.cat/mypng/full/34-345385_logo-coc-png-clash-of-clans-png.png'
        data_clan_level = 'N/A'
        data_clan_role = 'N/A'
    if data_clan_name == 'No Clan':
        clan_tag = ""
    else:
        clan_tag_with_hashtag = (user_json["clan"]["tag"])
        clan_tag = clan_tag_with_hashtag[1:len(clan_tag_with_hashtag)]
    gold_taken = str(user_json['achievements'][5]['value'])
    elixer_taken = str(user_json['achievements'][6]['value'])
    dark_taken = str(user_json['achievements'][16]['value'])
    data_total_donations = str(user_json['achievements'][14]['value'])
    data_spell_donations = str(user_json['achievements'][23]['value'])
    clan_games = str(user_json['achievements'][31]['value'])
    clan_leagues = str(user_json['achievements'][33]['value'])
    gearedup_buildings = str(user_json['achievements'][29]['value'])

    # Reference - data_total_donations = str(user_json['achievements'][14]['value'])

    #Writing the foundation of the code, tabs for information, as well as tabs for each category of data there is
    myfile2.write('''
    <body style='background-color:lightgrey,0.5;'>
    
    <div class='container'>
        <h4>Player Profile - Clash of Clans</h4>
    
        <div class='row'>
            <div class='col s12'>
              <ul class='tabs'>
                  <li class='tab col s6'><a class='active' href='#info'><h5>Information</h5></a></li>
                  <li class='tab col s6'><a href='#details'><h5>Extra Details</h5></a></li>
              </ul>
            </div>
            <div id='info' class='col s12' style='text-align: center'>
            <h6><br>Here is an in depth stat sheet for '''+user_json['name']+'''.<br><br>Click on the cards or the plus sign (located in the bottom right side) for more details</h6> 
            </div>
            <div id='details' class='col s12' style='text-align: center'>
            <h6><br><a href='https://developer.clashofclans.com/#/login' target = '_blank'>Link To API Used</a><br>
            Email (It Actually Is): bob.main2132@gmail.com Password: clashofclans6<br><br>Project is written in python and HTML with the use of framework<a href='https://materializecss.com' target = '_blank'>"CSS Materialize"</a></h6>
            </div>
        </div> 
    </div>
        
    <hr>
    
    <div class='container'>
        <div class='row'>
            <div class='col s12'>
              <ul class='tabs'>
                  <li class='tab col s4'><a href='#basics' class='active'><h5>Basics</h5></a></li>
                  <li class='tab col s4'><a href='#troops'><h5>Troops</h5></a></li>
                  <li class='tab col s4'><a href='#spells'><h5>Spells</h5></a></li>
              </ul>
            </div>
    ''')
    #Writing inside the Basics tab
    myfile2.write("<div id='basics'>")
    #Three cards written in basics, when window is large takes 4 spaces, when window is medium takes 6 spaces, when window is small takes 10 spaces (max 12)
    #Cards are responsive meaning when clicked on, information pops up
    #Data is being added from the variable/data setting above, sources from the internet (photos, links)
    myfile2.write('''
      <div class='col l4 m6 s10'><br>
            <div class='card sticky-action'>
        <div class='card-image waves-effect waves-block waves-light'>
            <img class='activator' src='https://vignette.wikia.nocookie.net/clashofclans/images/f/fd/Town_Hall1.png/revision/latest?cb=20170827034930'>
        </div>
        <div class='card-content'>
            <span class='card-title activator grey-text text-darken-4'>Halls</span>
            <a class='btn red btn-floating halfway-fab pulse activator'>+</a>
        </div>
        <div class='card-reveal'>
            <span class='card-title grey-text text-darken-4'>Village & Builderbase<i class='material-icons right'>close</i></span>
            <h6>Details:</h6><p>Max Level (TH): 12<br>User Level (TH): '''+data_thlevel+'''<br>Village: home<br><br>Max Level (BH): 9<br>User Level (BH): '''+data_bhlevel+'''<br>Village: builderBase</p>
        </div>
            </div>
            </div>
            
      <div class='col l4 m6 s10'><br>
            <div class='card sticky-action'>
        <div class='card-image waves-effect waves-block waves-light'>
            <img class='activator' src='''+clan_icon+'''>
        </div>
        <div class='card-content'>
            <span class='card-title activator grey-text text-darken-4'>Essentials</span>
            <a class='btn red btn-floating halfway-fab pulse activator'>+</a>
            <p><a href='https://clashofclans.com/clans/search/#clanTag='''+clan_tag+'''' target = '_blank'>Link to clan (seen as main picture)</a></p>
        </div>
        <div class='card-reveal'>
            <span class='card-title grey-text text-darken-4'>Stats<i class='material-icons right'>close</i></span>
            <h6>Details:</h6><p>EXP Level: '''+data_exp+'''<br><br>Trophies (Best): '''+data_trophies+''' ('''+data_max_trophies+''')<br>League: '''+data_league_name+'''<br><br>VersusTrophies (Best): '''+data_builder_trophies+''' ('''+data_max_builder_trophies+''')<br><br>Warstars: '''+data_warstars+'''<br>Clan (Level): '''+data_clan_name+''' ('''+data_clan_level+''')<br>Role: '''+data_clan_role+'''</p>
        </div>
            </div>
            </div>

      <div class='col l4 m6 s10'><br>
            <div class='card sticky-action'>
        <div class='card-image waves-effect waves-block waves-light'>
            <img class='activator' src='https://steamuserimages-a.akamaihd.net/ugc/35239975375061668/ACB134564983985B087613F528F1038B1B5F6ADA/'>
        </div>
        <div class='card-content'>
            <span class='card-title activator grey-text text-darken-4'>Achievments</span>
            <a class='btn red btn-floating halfway-fab pulse activator'>+</a>
            <p><a href='https://clashofclans.fandom.com/wiki/Achievements' target = '_blank'>Achievements List</a></p>
        </div>
        <div class='card-reveal'>
            <span class='card-title grey-text text-darken-4'>Info<i class='material-icons right'>close</i></span>
            <h6>Details:</h6><p>Gold Taken: '''+gold_taken+'''<br>Elixer Taken: '''+elixer_taken+''' <br>Dark Taken: '''+dark_taken+'''<br><br>Total Donations: '''+data_total_donations+'''<br>Total Spell Donations: '''+data_spell_donations+'''<br>Clan Games: '''+clan_games+'''<br>Clan War Leagues: '''+clan_leagues+'''<br><br>Geared Up Buildings: '''+gearedup_buildings+'''</p>
        </div>
            </div>
            </div>
    ''')
    myfile2.write("</div>")
    #Writing inside the Troops tabs
    myfile2.write("<div id='troops'>")
    #Two cards written in troops, when window is large takes 6 spaces, when window is medium takes 6 spaces, when window is small takes 10 spaces (max 12)
    #Cards are responsive meaning when clicked on, information pops up
    #Data is being added directly from the data response, sources from the internet (photos, links)
    myfile2.write('''
      <div class='col l6 m6 s10'><br>
            <div class='card sticky-action'>
        <div class='card-image waves-effect waves-block waves-light'>
            <img class='activator' src='http://www.mascotdesigngallery.com/wp/wp-content/uploads/2015/03/dragon.png'>
        </div>
        <div class='card-content'>
            <span class='card-title activator grey-text text-darken-4'>Elixer Troops</span>
            <a class='btn red btn-floating halfway-fab pulse activator'>+</a>
            <p><a href='https://clashofclans.fandom.com/wiki/Elixir_Troops' target = '_blank'>Official Website</a></p>
        </div>
        <div class='card-reveal'>
            <span class='card-title grey-text text-darken-4'>Troops Levels (Max)<i class='material-icons right'>close</i></span>
            <h6>Details:</h6><p>Barbarian: '''+str(user_json['troops'][0]['level'])+''' (8)<br>Archer: '''+str(user_json['troops'][1]['level'])+''' (8)<br>Goblin: '''+str(user_json['troops'][2]['level'])+''' (7)<br>Giant: '''+str(user_json['troops'][3]['level'])+''' (9)<br>Wall Breaker: '''+str(user_json['troops'][4]['level'])+''' (8)<br>Balloon: '''+str(user_json['troops'][5]['level'])+''' (8)<br>Wizard: '''+str(user_json['troops'][6]['level'])+''' (9)<br>Healer: '''+str(user_json['troops'][7]['level'])+''' (5)<br>Dragon: '''+str(user_json['troops'][8]['level'])+''' (7)<br>P.E.K.K.A: '''+str(user_json['troops'][9]['level'])+''' (8)</p>
        </div>
            </div>
            </div>

      <div class='col l6 m6 s10'><br>
            <div class='card sticky-action'>
        <div class='card-image waves-effect waves-block waves-light'>
            <img class='activator' src='https://jesusknightscoc.files.wordpress.com/2017/07/witch.png'>
        </div>
        <div class='card-content'>
            <span class='card-title activator grey-text text-darken-4'>Dark Troops</span>
            <a class='btn red btn-floating halfway-fab pulse activator'>+</a>
            <p><a href='https://clashofclans.fandom.com/wiki/Dark_Troops' target = '_blank'>Official Website</a></p>
        </div>
        <div class='card-reveal'>
            <span class='card-title grey-text text-darken-4'>Troops Levels (Max)<i class='material-icons right'>close</i></span>
            <h6>Details:</h6><p>Minion: '''+str(user_json['troops'][10]['level'])+''' (8)<br>Hog Rider: '''+str(user_json['troops'][11]['level'])+''' (9)<br>Valkyrie: '''+str(user_json['troops'][12]['level'])+''' (7)<br>Golem: '''+str(user_json['troops'][13]['level'])+''' (9)<br>Witch: '''+str(user_json['troops'][14]['level'])+''' (5)<br>Lava Hound: '''+str(user_json['troops'][15]['level'])+''' (5)<br>Bowler: '''+str(user_json['troops'][16]['level'])+''' (4)</p>
        </div>
            </div>
            </div>
    ''')
    myfile2.write("</div>")
    #Writing inside the Spells tab
    myfile2.write("<div id='spells'>")
    #Two cards written in spells, when window is large takes 6 spaces, when window is medium takes 6 spaces, when window is small takes 10 spaces (max 12)
    #Cards are responsive meaning when clicked on, information pops up
    #Data is being added directly from the data response, sources from the internet (photos, links)
    myfile2.write('''
      <div class='col l6 m6 s10'><br>
            <div class='card sticky-action'>
        <div class='card-image waves-effect waves-block waves-light'>
            <img class='activator' src='https://www.allclash.com/wp-content/uploads/2015/09/lightning-spell.jpg'>
        </div>
        <div class='card-content'>
            <span class='card-title activator grey-text text-darken-4'>Elixer Spells</span>
            <a class='btn red btn-floating halfway-fab pulse activator'>+</a>
            <p><a href='https://clashofclans.fandom.com/wiki/Spells' target = '_blank'>Official Website</a></p>
        </div>
        <div class='card-reveal'>
            <span class='card-title grey-text text-darken-4'>Spell Levels (Max)<i class='material-icons right'>close</i></span>
            <h6>Details:</h6><p>Lightning Spell: '''+str(user_json['spells'][0]['level'])+''' (7)<br><br>Heal Spell: '''+str(user_json['spells'][1]['level'])+''' (7)<br><br>Rage Spell: '''+str(user_json['spells'][2]['level'])+''' (6)<br><br>Jump Spell: '''+str(user_json['spells'][3]['level'])+''' (3)<br><br>Freeze Spell: '''+str(user_json['spells'][4]['level'])+''' (7)<br><br>Clone Spell: '''+str(user_json['spells'][8]['level'])+''' (5)</p>
        </div>
            </div>
            </div>

      <div class='col l6 m6 s10'><br>
            <div class='card sticky-action'>
        <div class='card-image waves-effect waves-block waves-light'>
            <img class='activator' src='http://www.allclash.com/wp-content/uploads/2015/07/haste-spell-guide.jpg'>
        </div>
        <div class='card-content'>
            <span class='card-title activator grey-text text-darken-4'>Dark Spells</span>
            <a class='btn red btn-floating halfway-fab pulse activator'>+</a>
            <p><a href='https://clashofclans.fandom.com/wiki/Spells' target = '_blank'>Official Website</a></p>
        </div>
        <div class='card-reveal'>
            <span class='card-title grey-text text-darken-4'>Spell Levels (Max)<i class='material-icons right'>close</i></span>
            <h6>Details:</h6><p>Poison Spell: '''+str(user_json['spells'][5]['level'])+''' (6)<br><br>Earthquake Spell: '''+str(user_json['spells'][6]['level'])+''' (5)<br><br>Haste Spell: '''+str(user_json['spells'][7]['level'])+''' (5)<br><br>Skeleton Spell: '''+str(user_json['spells'][9]['level'])+''' (6)<br><br>Bat Spell: '''+str(user_json['spells'][10]['level'])+''' (5)</p>
        </div>
            </div>
            </div>
    ''')
    myfile2.write("</div>")
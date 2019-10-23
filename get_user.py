#Opens file where data will be stored
myfile = open("comparisonCOC.html", "w")

#Creates the foundation for the HTML (CSS)
def start_file():
    starting = '''
<!DOCTYPE html>

<html lang = "en-US">

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

</style>  

<!-- Compiled and minified CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

<!--Import Google Icon Font-->
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">

<title>COC Player Comparisons</title>

</head>

<body style="background-color:lightgrey,0.5;">

<h4>Player Comparisons - Clash of Clans</h4>

<div class="row">
    <div class="col s12">
      <ul class="tabs">
          <li class="tab col s6"><a class="active" href="#info"><h5>Information</h5></a></li>
          <li class="tab col s6"><a href="#details"><h5>Extra Details</h5></a></li>
      </ul>
    </div>
    <div id="info" class="col s12" style="text-align: center">
    <h6>Here are the basic statistics comparisons for your Clash of Clans users.<br><br>You can click on the headers to sort by aplha order or numerical order.<br><br>You can click on the clan logo for information on the clan.</h6>
    </div>
    <div id="details" class="col s12" style="text-align: center">
    <h6><a href=https://developer.clashofclans.com/#/login target = _blank>Link To API Used</a><br>
    Email (It Actually Is): bob.main2132@gmail.com Password: clashofclans6<br><br>Project is written in python and HTML with the use of framework <a href=https://materializecss.com target = _blank>"CSS Materialize"</a></h6>
    </div>
</div> 

<hr>    

<table id = \'myTable\'; style = 'width:100%'; class = "highlight"; class = "responsive-table">
   <tr>
   <th onclick = 'sortTable(0)'>Account Name</th>
   <th onclick = 'sortTable(1)'>Townhall Level</th> 
   <th onclick = 'sortTable(2)'>Builderhall Level</th>
   <th onclick = 'sortTable(3)'>EXP Level</th>
   <th onclick = 'sortTable(4)'>League</th>  
   <th onclick = 'sortTable(5)'>Trophies</th>
   <th onclick = 'sortTable(6)'>Warstars</th>
   <th onclick = 'sortTable(7)'>Total Donations</th>
   <th onclick = 'sortTable(8)'>Clan</th>
 </tr>   
        '''
    myfile.write(starting)

#Ends the file with script, some script is used to initialize items from CSS Materialized, others for features such as table sorting
def close_file():
    myfile.write("</table>")
    myfile.write("<script src='https://code.jquery.com/jquery-3.3.1.min.js'></script>\n<script src='https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js'></script>\n<script>$(document).ready(function(){$('.tabs').tabs();});</script>")
    myfile.write("\n<script>function sortTable(n) {var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;table = document.getElementById('myTable');switching = true;dir = 'asc'; while (switching) {switching = false;rows = table.rows;for (i = 1; i < (rows.length - 1); i++) {shouldSwitch = false;x = rows[i].getElementsByTagName('TD')[n];y = rows[i + 1].getElementsByTagName('TD')[n];if (dir == 'asc') {if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {shouldSwitch= true;break;}} else if (dir == 'desc') {if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {shouldSwitch = true;break;}}}if (shouldSwitch) {rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);switching = true;switchcount ++;} else {if (switchcount == 0 && dir == 'asc') {dir = 'desc';switching = true;}}}}</script>")
    myfile.write("</body>")
    myfile.write("</html>")
    myfile.close()

#Receives data from the def get_user and writes it into the HTML file row by row
def writeHTML(name_user, data_thlevel, data_bhlevel, data_exp, data_league_name, league_link, data_trophies, data_warstars, data_total_donations, data_clan_name, clan_icon, clan_tag):  # Try and find a way for chart headers to follow through
    myfile.write("<tr>")
    myfile.write("<td>"+name_user+"</td>")
    myfile.write("<td>"+data_thlevel+"</td>")
    myfile.write("<td>"+data_bhlevel+"</td>")
    myfile.write("<td>"+data_exp+"</td>")
    myfile.write("<td>"+data_league_name+"<br><img src="+league_link+" style = 'width:50px;height:50px' title = 'League Icon'> </img></td>")
    myfile.write("<td>"+data_trophies+"</td>")
    myfile.write("<td>"+data_warstars+"</td>")
    myfile.write("<td>"+data_total_donations+"</td>")
    myfile.write("<td>"+data_clan_name+"<br><a href='https://clashofclans.com/clans/search/#clanTag="+clan_tag+"'target = '_blank'><img src ='"+clan_icon+"' style='width:65px;height:65px' title='Click For More Info'></a></td>")
    myfile.write("</tr>")

#Receives response from the main module and sets data (goes into def writeHTML)
def get_user(response):

    # Gets the user profile
    user_json = response.json()

    name_user = user_json['name']
    data_thlevel = str(user_json['townHallLevel'])
    data_bhlevel = str(user_json['builderHallLevel'])
    data_exp = str(user_json['expLevel'])
    data_trophies = str(user_json['trophies'])
    data_warstars = str(user_json['warStars'])
    data_total_donations = str(user_json['achievements'][14]['value'])
    try:
        data_league_name = (user_json["league"]["name"])
        league_link = (user_json['league']['iconUrls']['tiny'])
    except KeyError:
        data_league_name = 'No League'
        league_link = 'https://vignette.wikia.nocookie.net/clashofclans/images/c/c0/Unranked_League.png/revision/latest/scale-to-width-down/92?cb=20171003011534'
    try:
        data_clan_name = (user_json["clan"]["name"])
        clan_icon = (user_json["clan"]["badgeUrls"]["small"])
    except KeyError:
        data_clan_name = 'No Clan'
        clan_icon = 'https://www.sccpre.cat/mypng/full/34-345385_logo-coc-png-clash-of-clans-png.png'
    if data_clan_name == 'No Clan':
        clan_tag = ""
    else:
        clan_tag_with_hashtag = (user_json["clan"]["tag"])
        clan_tag = clan_tag_with_hashtag[1:len(clan_tag_with_hashtag)]

    writeHTML(name_user, data_thlevel, data_bhlevel, data_exp, data_league_name, league_link, data_trophies, data_warstars, data_total_donations, data_clan_name, clan_icon, clan_tag)


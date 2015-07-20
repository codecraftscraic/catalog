from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from final_app_database_setup import Users, Team, Players, Base

engine = create_engine('sqlite:///nhlteams.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


team1 = Team(team_name="Boston Bruins")

session.add(team1)
session.commit()

players1 = Players(fname="Zedeno", lname="Chara", number="33", position="Defense", team=team1)

session.add(players1)
session.commit()

team2 = Team(team_name="Buffalo Sabres")

session.add(team2)
session.commit()

players2 = Players(fname="Jack", lname="Eichel", number="15", position="Forward", team=team2)

session.add(players2)
session.commit()

team3 = Team(team_name="Detroit Red Wings")

session.add(team3)
session.commit()

players3 = Players(fname="Steve", lname="Yzerman", number="19", position="Forward", team=team3)

session.add(players3)
session.commit()

team4 = Team(team_name="Florida Panthers")

session.add(team4)
session.commit()

players4 = Players(fname="Roberto", lname="Luongo", number="1", position="Goalie", team=team4)

session.add(players4)
session.commit()

team5 = Team(team_name="Montreal Canadiens")

session.add(team5)
session.commit()

players5 = Players(fname="PK", lname="Subban", number="76", position="Defense", team=team5)

session.add(players5)
session.commit()

team6 = Team(team_name="Ottawa Senators")

session.add(team6)
session.commit()

players6 = Players(fname="Erik", lname="Karlsson", number="65", position="Defense", team=team6)

session.add(players6)
session.commit()

team7 = Team(team_name="Tampa Bay Lightening")

session.add(team7)
session.commit()

players7 = Players(fname="Valtteri", lname="Filppula", number="51", position="Forward", team=team7)

session.add(players7)
session.commit()

team8 = Team(team_name="Toronto Maple Leafs")

session.add(team8)
session.commit()

players8 = Players(fname="Dion", lname="Phaneuf", number="3", position="Defense", team=team8)

session.add(players8)
session.commit()

team9 = Team(team_name="Carolina Hurricanes")

session.add(team9)
session.commit()

players9 = Players(fname="Andrej", lname="Nestrasil", number="15", position="Forward", team=team9)

session.add(players9)
session.commit()

team10 = Team(team_name="Columbus Blue Jackets")

session.add(team10)
session.commit()

players10 = Players(fname="Jack", lname="Johnson", number="7", position="Defense", team=team10)

session.add(players10)
session.commit()

team11 = Team(team_name="New Jersey Devils")

session.add(team11)
session.commit()

<<<<<<< .merge_file_XjnhX1
players11 = Players(fname="", lname="", number="", position="", team=team11)
=======
players1 = Players(fname="Travis", lname="Zajac", number="19", position="Forward", team=team11)
>>>>>>> .merge_file_wBrgTL

session.add(players11)
session.commit()

team12 = Team(team_name="NY Islanders")

session.add(team12)
session.commit()

players12 = Players(fname="John", lname="Tavares", number="91", position="Forward", team=team12)

session.add(players12)
session.commit()

team13 = Team(team_name="NY Rangers")

session.add(team13)
session.commit()

players13 = Players(fname="Henrik", lname="Lundqvist", number="30", position="Goalie", team=team13)

session.add(players13)
session.commit()

team14 = Team(team_name="Philadelphia Flyers")

session.add(team14)
session.commit()

players14 = Players(fname="", lname="", number="", position="", team=team14)

session.add(players14)
session.commit()

team15 = Team(team_name="Pittsburgh Penguins")

session.add(team15)
session.commit()

players15 = Players(fname="Claude", lname="Giroux", number="28", position="Forward", team=team15)

session.add(players15)
session.commit()

team16 = Team(team_name="Washington Capitals")

session.add(team16)
session.commit()

players16 = Players(fname="Alexander", lname="Ovechkin", number="8", position="Forward", team=team16)

session.add(players16)
session.commit()

team17 = Team(team_name="Anaheim Ducks")

session.add(team17)
session.commit()

players17 = Players(fname="Ryan", lname="Getzlaf", number="15", position="Forward", team=team17)

session.add(players17)
session.commit()

team18 = Team(team_name="Arizona Coyotes")

session.add(team18)
session.commit()

players18 = Players(fname="Mike", lname="Smith", number="41", position="Goalie", team=team18)

session.add(players18)
session.commit()

team19 = Team(team_name="Calgary Flames")

session.add(team19)
session.commit()

players19 = Players(fname="Johnny", lname="Gaudreau", number="13", position="Forward", team=team19)

session.add(players19)
session.commit()

team20 = Team(team_name="Edmonton Oilers")

session.add(team20)
session.commit()

players20 = Players(fname="Connor", lname="McDavid", number="97", position="Forward", team=team20)

session.add(players20)
session.commit()

team21 = Team(team_name="Los Angeles Kings")

session.add(team21)
session.commit()

players21 = Players(fname="Jonathan", lname="Quick", number="32", position="Goalie", team=team21)

session.add(players21)
session.commit()

team22 = Team(team_name="San Jose Sharks")

session.add(team22)
session.commit()

players22 = Players(fname="Joe", lname="Thornton", number="19", position="Forward", team=team22)

session.add(players22)
session.commit()

team23 = Team(team_name="Vancouver Canucks")

session.add(team23)
session.commit()

players23 = Players(fname="Ryan", lname="Miller", number="30", position="Goalie", team=team23)

session.add(players23)
session.commit()

team24 = Team(team_name="Chicago Blackhawks")

session.add(team24)
session.commit()

players24 = Players(fname="Corey", lname="Crawford", number="50", position="Goalie", team=team24)

session.add(players24)
session.commit()

team25 = Team(team_name="Colorado Avalanche")

session.add(team25)
session.commit()

players25 = Players(fname="Cody", lname="McLeod", number="55", position="Forward", team=team25)

session.add(players25)
session.commit()

team26 = Team(team_name="Dallas Stars")

session.add(team26)
session.commit()

players26 = Players(fname="Tyler", lname="Seguin", number="91", position="Forward", team=team26)

session.add(players26)
session.commit()

team27 = Team(team_name="Minnesota Wild")

session.add(team27)
session.commit()

players27 = Players(fname="Devan", lname="Dubnyk", number="40", position="Goalie", team=team27)

session.add(players27)
session.commit()

team28 = Team(team_name="Nashville Predators")

session.add(team28)
session.commit()

players28 = Players(fname="Pekka", lname="Rinne", number="35", position="Goalie", team=team28)

session.add(players28)
session.commit()

team29 = Team(team_name="St. Louis Blues")

session.add(team29)
session.commit()

players29 = Players(fname="Vladimir", lname="Tarasenko", number="91", position="Forward", team=team29)

session.add(players29)
session.commit()

team30 = Team(team_name="Winnipeg Jets")

session.add(team30)
session.commit()

players30 = Players(fname="Jacob", lname="Trouba", number="8", position="Defense", team=team30)

session.add(players30)
session.commit()

print "added teams and players!"

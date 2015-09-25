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


#Boston
players = Players(number="55",fname="Noel",lname="Acciari",position="Center",team=1)
session.add(players)
session.commit()
		
players = Players(number="49",fname="Linus",lname="Arnesson",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="39",fname="Matt",lname="Beleskey",position="Left Wing",team=1)
session.add(players)
session.commit()

players = Players(number="37",fname="Patrice",lname="Bergeron",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="81",fname="Anton",lname="Blidh",position="Left Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="42",fname="Chris",lname="Breen",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="75",fname="Anthony",lname="Camara",position="Left Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="73",fname="Brandon",lname="Carlo",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="65",fname="Chris",lname="Casto",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="57",fname="Colby",lname="Cave",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Zdeno",lname="Chara",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Brett",lname="Connolly",position="Right Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="56",fname="Tommy",lname="Cross",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="61",fname="Austin",lname="Czarnik",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="74",fname="Jake",lname="DeBrusk",position="Left Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="43",fname="Brandon",lname="DeFazio",position="Left Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Loui",lname="Eriksson",position="Right Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="91",fname="Max",lname="Everson",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="68",fname="Brian",lname="Ferlin",position="Right Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="82",fname="Jesse",lname="Gabrielle",position="Left Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Matt",lname="Ginn",position="Goaltender",team=1)
session.add(players)
session.commit()
	
players = Players(number="53",fname="Seth",lname="Griffith",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="89",fname="Jonas",lname="Gustavsson",position="Goaltender",team=1)
session.add(players)
session.commit()
	
players = Players(number="78",fname="Colton",lname="Hargrove",position="Left Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Jimmy",lname="Hayes",position="Right Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="60",fname="Justin",lname="Hickman",position="Right Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="52",fname="Matt",lname="Irwin",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="23",fname="Chris",lname="Kelly",position="Center/Left Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="41",fname="Joonas",lname="Kemppainen",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="76",fname="Alexander",lname="Khokhlachev",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="46",fname="David",lname="Krejci",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="47",fname="Torey",lname="Krug",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="79",fname="Jeremy",lname="Lauzon",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="63",fname="Brad",lname="Marchand",position="Left Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="50",fname="Zane",lname="McIntyre",position="Goaltender",team=1)
session.add(players)
session.commit()
	
players = Players(number="54",fname="Adam",lname="McQuaid",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="48",fname="Colin",lname="Miller",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="86",fname="Kevan",lname="Miller",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="45",fname="Joseph",lname="Morrow",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="92",fname="Eric",lname="Neiley",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="88",fname="David",lname="Pastrnak",position="Right Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="59",fname="Zack",lname="Phillips",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="64",fname="Tyler",lname="Randell",position="Right Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="40",fname="Tuukka",lname="Rask",position="Goaltender",team=1)
session.add(players)
session.commit()
	
players = Players(number="36",fname="Zac",lname="Rinaldo",position="Left Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Dennis",lname="Seidenberg",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="71",fname="Zach",lname="Senyshyn",position="Right Wing",team=1)
session.add(players)
session.commit()
	
players = Players(number="58",fname="Ben",lname="Sexton",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="83",fname="Frankie",lname="Simonelli",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Jeremy",lname="Smith",position="Goaltender",team=1)
session.add(players)
session.commit()
	
players = Players(number="51",fname="Ryan",lname="Spooner",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="70",fname="Malcolm",lname="Subban",position="Goaltender",team=1)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Maxime",lname="Talbot",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="62",fname="Zach",lname="Trotman",position="Defenseman",team=1)
session.add(players)
session.commit()
	
players = Players(number="72",fname="Frank",lname="Vatrano",position="Center",team=1)
session.add(players)
session.commit()
	
players = Players(number="80",fname="Dan",lname="Vladar",position="Goaltender",team=1)
session.add(players)
session.commit()
	
players = Players(number="67",fname="Jakub",lname="Zboril",position="Defenseman",team=1)
session.add(players)
session.commit()


#Buffalo
players = Players(number="47",fname="Zach",lname="Bogosian",position="Defenseman",team=2)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Carlo",lname="Colaiacovo",position="Defenseman",team=2)
session.add(players)
session.commit()
	
players = Players(number="49",fname="Jerry",lname="D'Amigo",position="Left Wing",team=2)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Nicolas",lname="Deslauriers",position="Left Wing",team=2)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Jack",lname="Eichel",position="Center",team=2)
session.add(players)
session.commit()
	
players = Players(number="63",fname="Tyler",lname="Ennis",position="Center/Left Wing",team=2)
session.add(players)
session.commit()
	
players = Players(number="82",fname="Marcus",lname="Foligno",position="Left Wing",team=2)
session.add(players)
session.commit()
	
players = Players(number="46",fname="Cody",lname="Franson",position="Defenseman",team=2)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Brian",lname="Gionta",position="Right Wing",team=2)
session.add(players)
session.commit()
	
players = Players(number="28",fname="Zemgus",lname="Girgensons",position="Center",team=2)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Josh",lname="Gorges",position="Defenseman",team=2)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Chad",lname="Johnson",position="Goaltender",team=2)
session.add(players)
session.commit()
	
players = Players(number="36",fname="Patrick",lname="Kaleta",position="Right Wing",team=2)
session.add(players)
session.commit()
	
players = Players(number="9",fname="Evander",lname="Kane",position="Left Wing",team=2)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Johan",lname="Larsson",position="Left Wing",team=2)
session.add(players)
session.commit()
	
players = Players(number="17",fname="David",lname="Legwand",position="Center",team=2)
session.add(players)
session.commit()
	
players = Players(number="40",fname="Robin",lname="Lehner",position="Goaltender",team=2)
session.add(players)
session.commit()
	
players = Players(number="8",fname="Cody",lname="McCormick",position="Center/Right Wing",team=2)
session.add(players)
session.commit()
	
players = Players(number="88",fname="Jamie",lname="McGinn",position="Left Wing",team=2)
session.add(players)
session.commit()
	
players = Players(number="41",fname="Andrej",lname="Meszaros",position="Defenseman",team=2)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Matt",lname="Moulson",position="Left Wing",team=2)
session.add(players)
session.commit()
	
players = Players(number="90",fname="Ryan",lname="O'Reilly",position="Center",team=2)
session.add(players)
session.commit()
	
players = Players(number="55",fname="Rasmus",lname="Ristolainen",position="Defenseman",team=2)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Mike",lname="Weber",position="Defenseman",team=2)
session.add(players)
session.commit()


#Detroit
players = Players(number="8",fname="Justin",lname="Abdelkader",position="Left Wing",team=3)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Joakim",lname="Andersson",position="Center",team=3)
session.add(players)
session.commit()
	
players = Players(number="13",fname="Pavel",lname="Datsyuk",position="Center",team=3)
session.add(players)
session.commit()
	
players = Players(number="65",fname="Danny",lname="DeKeyser",position="Defenseman",team=3)
session.add(players)
session.commit()
	
players = Players(number="52",fname="Jonathan",lname="Ericsson",position="Defenseman",team=3)
session.add(players)
session.commit()
	
players = Players(number="29",fname="Landon",lname="Ferraro",position="Center",team=3)
session.add(players)
session.commit()
	
players = Players(number="93",fname="Johan",lname="Franzen",position="Right Wing",team=3)
session.add(players)
session.commit()
	
players = Players(number="41",fname="Luke",lname="Glendening",position="Center",team=3)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Mike",lname="Green",position="Defenseman",team=3)
session.add(players)
session.commit()
	
players = Players(number="43",fname="Darren",lname="Helm",position="Center",team=3)
session.add(players)
session.commit()
	
players = Players(number="35",fname="Jimmy",lname="Howard",position="Goaltender",team=3)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Tomas",lname="Jurco",position="Right Wing",team=3)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Jakub",lname="Kindl",position="Defenseman",team=3)
session.add(players)
session.commit()
	
players = Players(number="55",fname="Niklas",lname="Kronwall",position="Defenseman",team=3)
session.add(players)
session.commit()
	
players = Players(number="47",fname="Alexei",lname="Marchenko",position="Defenseman",team=3)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Drew",lname="Miller",position="Left Wing",team=3)
session.add(players)
session.commit()
	
players = Players(number="34",fname="Petr",lname="Mrazek",position="Goaltender",team=3)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Gustav",lname="Nyquist",position="Right Wing",team=3)
session.add(players)
session.commit()
	
players = Players(number="56",fname="Teemu",lname="Pulkkinen",position="Right Wing",team=3)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Kyle",lname="Quincey",position="Defenseman",team=3)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Brad",lname="Richards",position="Center",team=3)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Riley",lname="Sheahan",position="Center",team=3)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Brendan",lname="Smith",position="Defenseman",team=3)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Tomas",lname="Tatar",position="Left Wing",team=3)
session.add(players)
session.commit()
	
players = Players(number="40",fname="Henrik",lname="Zetterberg",position="Center",team=3)
session.add(players)
session.commit()


#Florida4
players = Players(number="16",fname="Aleksander",lname="Barkov",position="Center",team=4)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Nick",lname="Bjugstad",position="Center",team=4)
session.add(players)
session.commit()
	
players = Players(number="63",fname="Dave",lname="Bolland",position="Center",team=4)
session.add(players)
session.commit()
	
players = Players(number="51",fname="Brian",lname="Campbell",position="Defenseman",team=4)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Aaron",lname="Ekblad",position="Defenseman",team=4)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Erik",lname="Gudbranson",position="Defenseman",team=4)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Jonathan",lname="Huberdeau",position="Left Wing",team=4)
session.add(players)
session.commit()
	
players = Players(number="68",fname="Jaromir",lname="Jagr",position="Right Wing",team=4)
session.add(players)
session.commit()
	
players = Players(number="36",fname="Jussi",lname="Jokinen",position="Left Wing",team=4)
session.add(players)
session.commit()
	
players = Players(number="3",fname="Steven",lname="Kampfer",position="Defenseman",team=4)
session.add(players)
session.commit()
	
players = Players(number="7",fname="Dmitry",lname="Kulikov",position="Defenseman",team=4)
session.add(players)
session.commit()
	
players = Players(number="1",fname="Roberto",lname="Luongo",position="G",team=4)
session.add(players)
session.commit()

players = Players(number="17",fname="Derek",lname="MacKenzie",position="Center",team=4)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Willie",lname="Mitchell",position="Defenseman",team=4)
session.add(players)
session.commit()
	
players = Players(number="35",fname="Al",lname="Montoya",position="G",team=4)
session.add(players)
session.commit()

players = Players(number="72",fname="Alex",lname="Petrovic",position="Defenseman",team=4)
session.add(players)
session.commit()
	
players = Players(number="73",fname="Brandon",lname="Pirri",position="Center",team=4)
session.add(players)
session.commit()
	
players = Players(number="91",fname="Marc",lname="Savard",position="Center",team=4)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Shawn",lname="Thornton",position="Left Wing",team=4)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Vincent",lname="Trocheck",position="Center",team=4)
session.add(players)
session.commit()


#Montreal5
players = Players(number="28",fname="Nathan",lname="Beaulieu",position="Defenseman",team=5)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Jacob",lname="de la Rose",position="Left Wing",team=5)
session.add(players)
session.commit()
	
players = Players(number="51",fname="David",lname="Desharnais",position="Center",team=5)
session.add(players)
session.commit()
	
players = Players(number="81",fname="Lars",lname="Eller",position="Center/Left Wing",team=5)
session.add(players)
session.commit()
	
players = Players(number="74",fname="Alexei",lname="Emelin",position="Defenseman",team=5)
session.add(players)
session.commit()
	
players = Players(number="32",fname="Brian",lname="Flynn",position="Right Wing",team=5)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Alex",lname="Galchenyuk",position="Center/Left Wing",team=5)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Brendan",lname="Gallagher",position="Right Wing",team=5)
session.add(players)
session.commit()
	
players = Players(number="77",fname="Tom",lname="Gilbert",position="Defenseman",team=5)
session.add(players)
session.commit()
	
players = Players(number="8",fname="Zack",lname="Kassian",position="Right Wing",team=5)
session.add(players)
session.commit()
	
players = Players(number="79",fname="Andrei",lname="Markov",position="Defenseman",team=5)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Torrey",lname="Mitchell",position="Center/Right Wing",team=5)
session.add(players)
session.commit()
	
players = Players(number="67",fname="Max",lname="Pacioretty",position="Left Wing",team=5)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Greg",lname="Pateryn",position="Defenseman",team=5)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Jeff",lname="Petry",position="Defenseman",team=5)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Tomas",lname="Plekanec",position="Center",team=5)
session.add(players)
session.commit()
	
players = Players(number="31",fname="Carey",lname="Price",position="Goaltender",team=5)
session.add(players)
session.commit()
	
players = Players(number="13",fname="Alexander",lname="Semin",position="Right Wing",team=5)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Devante",lname="Smith-Pelly",position="Right Wing",team=5)
session.add(players)
session.commit()
	
players = Players(number="76",fname="P.K.",lname="Subban",position="Defenseman",team=5)
session.add(players)
session.commit()
	
players = Players(number="35",fname="Dustin",lname="Tokarski",position="Goaltender",team=5)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Dale",lname="Weise",position="Right Wing",team=5)
session.add(players)
session.commit()
	

#Ottawa6
players = Players(number="41",fname="Craig",lname="Anderson",position="Goaltender",team=6)
session.add(players)
session.commit()
	
players = Players(number="74",fname="Mark",lname="Borowiecki",position="Defenseman",team=6)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Cody",lname="Ceci",position="Defenseman",team=6)
session.add(players)
session.commit()
	
players = Players(number="90",fname="Alex",lname="Chiasson",position="Right Wing",team=6)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Jared",lname="Cowen",position="Defenseman",team=6)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Andrew",lname="Hammond",position="Goaltender",team=6)
session.add(players)
session.commit()
	
players = Players(number="68",fname="Mike",lname="Hoffman",position="Left Wing",team=6)
session.add(players)
session.commit()
	
players = Players(number="65",fname="Erik",lname="Karlsson",position="Defenseman",team=6)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Curtis",lname="Lazar",position="Center",team=6)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Clarke",lname="MacArthur",position="Left Wing",team=6)
session.add(players)
session.commit()
	
players = Players(number="3",fname="Marc",lname="Methot",position="Defenseman",team=6)
session.add(players)
session.commit()
	
players = Players(number="9",fname="Milan",lname="Michalek",position="Left Wing",team=6)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Chris",lname="Neil",position="Right Wing",team=6)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Jean-Gabriel",lname="Pageau",position="Center",team=6)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Chris",lname="Phillips",position="Defenseman",team=6)
session.add(players)
session.commit()
	
players = Players(number="10",fname="Shane",lname="Prince",position="Center",team=6)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Bobby",lname="Ryan",position="Right Wing",team=6)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Zack",lname="Smith",position="Center",team=6)
session.add(players)
session.commit()
	
players = Players(number="61",fname="Mark",lname="Stone",position="Right Wing",team=6)
session.add(players)
session.commit()
	
players = Players(number="7",fname="Kyle",lname="Turris",position="Center",team=6)
session.add(players)
session.commit()
	
players = Players(number="46",fname="Patrick",lname="Wiercioch",position="Defenseman",team=6)
session.add(players)
session.commit()
	
players = Players(number="93",fname="Mika",lname="Zibanejad",position="Center",team=6)
session.add(players)
session.commit()
	

#Tampa7
players = Players(number="30",fname="Ben",lname="Bishop",position="Goaltender",team=7)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Brian",lname="Boyle",position="Center",team=7)
session.add(players)
session.commit()
	
players = Players(number="23",fname="J.T.",lname="Brown",position="Right Wing",team=7)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Ryan",lname="Callahan",position="Right Wing",team=7)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Matt",lname="Carle",position="Defenseman",team=7)
session.add(players)
session.commit()
	
players = Players(number="55",fname="Braydon",lname="Coburn",position="Defenseman",team=7)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Erik",lname="Condra",position="Right Wing",team=7)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Jonathan",lname="Drouin",position="Left Wing",team=7)
session.add(players)
session.commit()
	
players = Players(number="51",fname="Valtteri",lname="Filppula",position="Center",team=7)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Jason",lname="Garrison",position="Defenseman",team=7)
session.add(players)
session.commit()
	
players = Players(number="77",fname="Victor",lname="Hedman",position="Defenseman",team=7)
session.add(players)
session.commit()
	
players = Players(number="9",fname="Tyler",lname="Johnson",position="Center",team=7)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Alexander",lname="Killorn",position="Center",team=7)
session.add(players)
session.commit()
	
players = Players(number="86",fname="Nikita",lname="Kucherov",position="Right Wing",team=7)
session.add(players)
session.commit()
	
players = Players(number="42",fname="Jonathan",lname="Marchessault",position="Left Wing",team=7)
session.add(players)
session.commit()
	
players = Players(number="90",fname="Vladislav",lname="Namestnikov",position="Center",team=7)
session.add(players)
session.commit()
	
players = Players(number="89",fname="Nikita",lname="Nesterov",position="Defenseman",team=7)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Ondrej",lname="Palat",position="Left Wing",team=7)
session.add(players)
session.commit()
	
players = Players(number="13",fname="Cedric",lname="Paquette",position="Center",team=7)
session.add(players)
session.commit()
	
players = Players(number="91",fname="Steven",lname="Stamkos",position="Center",team=7)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Anton",lname="Stralman",position="Defenseman",team=7)
session.add(players)
session.commit()
	
players = Players(number="62",fname="Andrej",lname="Sustr",position="Defenseman",team=7)
session.add(players)
session.commit()
	
players = Players(number="53",fname="Luke",lname="Witkowski",position="Defenseman",team=7)
session.add(players)
session.commit()
	
players = Players(number="88",fname="Andrei",lname="Vasilevskiy",position="Goaltender",team=7)
session.add(players)
session.commit()
	

#Toronto8


#Carolina9


#Columbus10


#NJ11


#NUI12


#NYR13


#Philly14


#Pitt15


#Wash16


#ana17


#az18


#Flames19


#EDM20


#LAK21


#SJS22


#VAN23


#CHI24


#COL25


#DAL26


#MINN27


#NSH28


#STL29


#WPG30





print "added teams and players!"
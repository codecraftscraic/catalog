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
players = Players(number="33",fname="Mark",lname="Arcobello",position="Center",team=8)
session.add(players)
session.commit()
	
players = Players(number="45",fname="Jonathan",lname="Bernier",position="Goaltender",team=8)
session.add(players)
session.commit()
	
players = Players(number="29",fname="Brad",lname="Boyes",position="Right Wing",team=8)
session.add(players)
session.commit()
	
players = Players(number="42",fname="Tyler",lname="Bozak",position="Center",team=8)
session.add(players)
session.commit()
	
players = Players(number="53",fname="Sam",lname="Carrick",position="Center",team=8)
session.add(players)
session.commit()
	
players = Players(number="36",fname="Mark",lname="Fraser",position="Defenseman",team=8)
session.add(players)
session.commit()
	
players = Players(number="51",fname="Jake",lname="Gardiner",position="Defenseman",team=8)
session.add(players)
session.commit()
	
players = Players(number="28",fname="Curtis",lname="Glencross",position="Left Wing",team=8)
session.add(players)
session.commit()
	
players = Players(number="41",fname="Michael",lname="Grabner",position="Right Wing",team=8)
session.add(players)
session.commit()
	
players = Players(number="40",fname="Scott",lname="Harrington",position="Defenseman",team=8)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Peter",lname="Holland",position="Center",team=8)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Matt",lname="Hunwick",position="Defenseman",team=8)
session.add(players)
session.commit()
	
players = Players(number="43",fname="Nazem",lname="Kadri",position="Center",team=8)
session.add(players)
session.commit()
	
players = Players(number="47",fname="Leo",lname="Komarov",position="Center",team=8)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Joffrey",lname="Lupul",position="Left Wing",team=8)
session.add(players)
session.commit()
	
players = Players(number="52",fname="Martin",lname="Marincin",position="Defenseman",team=8)
session.add(players)
session.commit()
	
players = Players(number="23",fname="Shawn",lname="Matthias",position="Center",team=8)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Richard",lname="Panik",position="Right Wing",team=8)
session.add(players)
session.commit()
	
players = Players(number="15",fname="P.A.",lname="Parenteau",position="Right Wing",team=8)
session.add(players)
session.commit()
	
players = Players(number="3",fname="Dion",lname="Phaneuf",position="Defenseman",team=8)
session.add(players)
session.commit()
	
players = Players(number="46",fname="Roman",lname="Polak",position="Defenseman",team=8)
session.add(players)
session.commit()
	
players = Players(number="34",fname="James",lname="Reimer",position="Goaltender",team=8)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Morgan",lname="Rielly",position="Defenseman",team=8)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Stephane",lname="Robidas",position="Defenseman",team=8)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Devin",lname="Setoguchi",position="Right Wing",team=8)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Nick",lname="Spaling",position="Center",team=8)
session.add(players)
session.commit()
	
players = Players(number="21",fname="James",lname="van Riemsdyk",position="Left Wing",team=8)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Daniel",lname="Winnik",position="Left Wing",team=8)
session.add(players)
session.commit()
	

#Carolina9
players = Players(number="73",fname="Brett",lname="Bellemore",position="Defenseman",team=9)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Zach",lname="Boychuk",position="Center",team=9)
session.add(players)
session.commit()
	
players = Players(number="39",fname="Patrick",lname="Dwyer",position="Right Wing",team=9)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Justin",lname="Faulk",position="Defenseman",team=9)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Nathan",lname="Gerbe",position="Left Wing",team=9)
session.add(players)
session.commit()
	
players = Players(number="65",fname="Ron",lname="Hainsey",position="Defenseman",team=9)
session.add(players)
session.commit()
	
players = Players(number="38",fname="Jack",lname="Hillen",position="Defenseman",team=9)
session.add(players)
session.commit()
	
players = Players(number="47",fname="Michal",lname="Jordan",position="Defenseman",team=9)
session.add(players)
session.commit()
	
players = Players(number="31",fname="Eddie",lname="Lack",position="Goaltender",team=9)
session.add(players)
session.commit()
	
players = Players(number="26",fname="John-Michael",lname="Liles",position="Defenseman",team=9)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Elias",lname="Lindholm",position="Center",team=9)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Brad",lname="Malone",position="Center/Left Wing",team=9)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Jay",lname="McClement",position="Center",team=9)
session.add(players)
session.commit()
	
players = Players(number="7",fname="Ryan",lname="Murphy",position="Defenseman",team=9)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Riley",lname="Nash",position="Center",team=9)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Andrej",lname="Nestrasil",position="Center",team=9)
session.add(players)
session.commit()
	
players = Players(number="42",fname="Joakim",lname="Nordstrom",position="Center",team=9)
session.add(players)
session.commit()
	
players = Players(number="49",fname="Victor",lname="Rask",position="Center",team=9)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Rasmus",lname="Rissanen",position="Defenseman",team=9)
session.add(players)
session.commit()
	
players = Players(number="53",fname="Jeff",lname="Skinner",position="Left Wing",team=9)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Eric",lname="Staal",position="Center/Left Wing",team=9)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Jordan",lname="Staal",position="Center",team=9)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Chris",lname="Terry",position="Left Wing",team=9)
session.add(players)
session.commit()
	
players = Players(number="32",fname="Kris",lname="Versteeg",position="Right Wing",team=9)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Cam",lname="Ward",position="Goaltender",team=9)
session.add(players)
session.commit()
	
players = Players(number="21",fname="James",lname="Wisniewski",position="Defenseman",team=9)
session.add(players)
session.commit()
	

#Columbus10
players = Players(number="34",fname="Josh",lname="Anderson",position="Right Wing",team=10)
session.add(players)
session.commit()
	
players = Players(number="13",fname="Cam",lname="Atkinson",position="Right Wing",team=10)
session.add(players)
session.commit()
	
players = Players(number="72",fname="Sergei",lname="Bobrovsky",position="Goaltender",team=10)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Andrew",lname="Bodnarchuk",position="Defenseman",team=10)
session.add(players)
session.commit()
	
players = Players(number="40",fname="Jared",lname="Boll",position="Right Wing",team=10)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Rene",lname="Bourque",position="Right Wing",team=10)
session.add(players)
session.commit()
	
players = Players(number="62",fname="Alex",lname="Broadhurst",position="Center",team=10)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Matt",lname="Calvert",position="Left Wing",team=10)
session.add(players)
session.commit()
	
players = Players(number="9",fname="Gregory",lname="Campbell",position="Center",team=10)
session.add(players)
session.commit()
	
players = Players(number="23",fname="David",lname="Clarkson",position="Right Wing",team=10)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Kevin",lname="Connauton",position="Defenseman",team=10)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Brandon",lname="Dubinsky",position="Center/Left Wing",team=10)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Justin",lname="Falk",position="Defenseman",team=10)
session.add(players)
session.commit()
	
players = Players(number="71",fname="Nick",lname="Foligno",position="Left Wing",team=10)
session.add(players)
session.commit()
	
players = Players(number="29",fname="Cody",lname="Goloubef",position="Defenseman",team=10)
session.add(players)
session.commit()
	
players = Players(number="43",fname="Scott",lname="Hartnell",position="Left Wing",team=10)
session.add(players)
session.commit()
	
players = Players(number="38",fname="Boone",lname="Jenner",position="Center",team=10)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Ryan",lname="Johansen",position="Center",team=10)
session.add(players)
session.commit()
	
players = Players(number="7",fname="Jack",lname="Johnson",position="Defenseman",team=10)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Curtis",lname="McElhinney",position="Goaltender",team=10)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Ryan",lname="Murray",position="Defenseman",team=10)
session.add(players)
session.commit()
	
players = Players(number="36",fname="Michael",lname="Paliotta",position="Defenseman",team=10)
session.add(players)
session.commit()
	
players = Players(number="47",fname="Dalton",lname="Prout",position="Defenseman",team=10)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Kerby",lname="Rychel",position="Left Wing",team=10)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Brandon",lname="Saad",position="Left Wing",team=10)
session.add(players)
session.commit()
	
players = Players(number="58",fname="David",lname="Savard",position="Defenseman",team=10)
session.add(players)
session.commit()
	
players = Players(number="51",fname="Fedor",lname="Tyutin",position="Defenseman",team=10)
session.add(players)
session.commit()
	
players = Players(number="41",fname="Alexander",lname="Wennberg",position="Center",team=10)
session.add(players)
session.commit()
	

#NJ11
players = Players(number="13",fname="Michael",lname="Cammalleri",position="Left Wing",team=11)
session.add(players)
session.commit()
	
players = Players(number="29",fname="Ryane",lname="Clowe",position="Left Wing",team=11)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Patrik",lname="Elias",position="Center/Left Wing",team=11)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Eric",lname="Gelinas",position="Defenseman",team=11)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Stephen",lname="Gionta",position="Center",team=11)
session.add(players)
session.commit()
	
players = Players(number="38",fname="Marc-Andre",lname="Gragnani",position="Defenseman",team=11)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Andy",lname="Greene",position="Defenseman",team=11)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Seth",lname="Helgeson",position="Defenseman",team=11)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Adam",lname="Henrique",position="Center/Left Wing",team=11)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Jacob",lname="Josefson",position="Center",team=11)
session.add(players)
session.commit()
	
players = Players(number="48",fname="Tyler",lname="Kennedy",position="Center",team=11)
session.add(players)
session.commit()
	
players = Players(number="1",fname="Keith",lname="Kinkaid",position="Goaltender",team=11)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Adam",lname="Larsson",position="Defenseman",team=11)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Stefan",lname="Matteau",position="Left Wing",team=11)
session.add(players)
session.commit()
	
players = Players(number="7",fname="Jon",lname="Merrill",position="Defenseman",team=11)
session.add(players)
session.commit()
	
players = Players(number="17",fname="John",lname="Moore",position="Defenseman",team=11)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Kyle",lname="Palmieri",position="Right Wing",team=11)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Tuomo",lname="Ruutu",position="Left Wing",team=11)
session.add(players)
session.commit()
	
players = Players(number="3",fname="David",lname="Schlemko",position="Defenseman",team=11)
session.add(players)
session.commit()
	
players = Players(number="35",fname="Cory",lname="Schneider",position="Goaltender",team=11)
session.add(players)
session.commit()
	
players = Players(number="28",fname="Damon",lname="Severson",position="Defenseman",team=11)
session.add(players)
session.commit()
	
players = Players(number="91",fname="Jiri",lname="Tlusty",position="Left Wing",team=11)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Jordin",lname="Tootoo",position="Right Wing",team=11)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Travis",lname="Zajac",position="Center",team=11)
session.add(players)
session.commit()
	

#NYI12
players = Players(number="15",fname="Cal",lname="Clutterbuck",position="Right Wing",team=12)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Kevin",lname="Czuczman",position="Defenseman",team=12)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Calvin",lname="de Haan",position="Defenseman",team=12)
session.add(players)
session.commit()
	
players = Players(number="46",fname="Justin",lname="Florek",position="Left Wing",team=12)
session.add(players)
session.commit()
	
players = Players(number="84",fname="Mikhail",lname="Grabovski",position="Center",team=12)
session.add(players)
session.commit()
	
players = Players(number="1",fname="Thomas",lname="Greiss",position="Goaltender",team=12)
session.add(players)
session.commit()
	
players = Players(number="41",fname="Jaroslav",lname="Halak",position="Goaltender",team=12)
session.add(players)
session.commit()
	
players = Players(number="43",fname="Mike",lname="Halmo",position="Left Wing",team=12)
session.add(players)
session.commit()
	
players = Players(number="3",fname="Travis",lname="Hamonic",position="Defenseman",team=12)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Thomas",lname="Hickey",position="Defenseman",team=12)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Ben",lname="Holmstrom",position="Center",team=12)
session.add(players)
session.commit()
	
players = Players(number="86",fname="Nikolay",lname="Kulemin",position="Left Wing",team=12)
session.add(players)
session.commit()
	
players = Players(number="47",fname="Louis",lname="Leblanc",position="Right Wing",team=12)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Nick",lname="Leddy",position="Defenseman",team=12)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Anders",lname="Lee",position="Center",team=12)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Matt",lname="Martin",position="Left Wing",team=12)
session.add(players)
session.commit()
	
players = Players(number="42",fname="Scott",lname="Mayfield",position="Defenseman",team=12)
session.add(players)
session.commit()
	
players = Players(number="29",fname="Brock",lname="Nelson",position="Center",team=12)
session.add(players)
session.commit()
	
players = Players(number="51",fname="Frans",lname="Nielsen",position="Center",team=12)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Kyle",lname="Okposo",position="Right Wing",team=12)
session.add(players)
session.commit()
	
players = Players(number="60",fname="Kevin",lname="Poulin",position="Goaltender",team=12)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Ryan",lname="Pulock",position="Defenseman",team=12)
session.add(players)
session.commit()
	
players = Players(number="37",fname="Brian",lname="Strait",position="Defenseman",team=12)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Ryan",lname="Strome",position="Center",team=12)
session.add(players)
session.commit()
	
players = Players(number="91",fname="John",lname="Tavares",position="Center",team=12)
session.add(players)
session.commit()
	
players = Players(number="45",fname="Justin",lname="Vaive",position="Left Wing",team=12)
session.add(players)
session.commit()
	
players = Players(number="48",fname="Joe",lname="Whitney",position="Left Wing",team=12)
session.add(players)
session.commit()
	
players = Players(number="28",fname="Marek",lname="Zidlicky",position="Defenseman",team=12)
session.add(players)
session.commit()
	

#NYR13
players = Players(number="22",fname="Dan",lname="Boyle",position="Defenseman",team=13)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Derick",lname="Brassard",position="Center",team=13)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Raphael",lname="Diaz",position="Defenseman",team=13)
session.add(players)
session.commit()
	
players = Players(number="96",fname="Emerson",lname="Etem",position="Right Wing",team=13)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Jesper",lname="Fast",position="Left Wing",team=13)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Dan",lname="Girardi",position="Defenseman",team=13)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Tanner",lname="Glass",position="Left Wing",team=13)
session.add(players)
session.commit()
	
players = Players(number="13",fname="Kevin",lname="Hayes",position="Center",team=13)
session.add(players)
session.commit()
	
players = Players(number="8",fname="Kevin",lname="Klein",position="Defenseman",team=13)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Chris",lname="Kreider",position="Left Wing",team=13)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Henrik",lname="Lundqvist",position="Goaltender",team=13)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Ryan",lname="McDonagh",position="Defenseman",team=13)
session.add(players)
session.commit()
	
players = Players(number="10",fname="J.T.",lname="Miller",position="Right Wing",team=13)
session.add(players)
session.commit()
	
players = Players(number="28",fname="Dominic",lname="Moore",position="Center",team=13)
session.add(players)
session.commit()
	
players = Players(number="61",fname="Rick",lname="Nash",position="Left Wing",team=13)
session.add(players)
session.commit()
	
players = Players(number="32",fname="Antti",lname="Raanta",position="Goaltender",team=13)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Marc",lname="Staal",position="Defenseman",team=13)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Viktor",lname="Stalberg",position="Left Wing",team=13)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Derek",lname="Stepan",position="Center",team=13)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Jarret",lname="Stoll",position="Center",team=13)
session.add(players)
session.commit()
	
players = Players(number="55",fname="Chris",lname="Summers",position="Defenseman",team=13)
session.add(players)
session.commit()
	
players = Players(number="93",fname="Keith",lname="Yandle",position="Defenseman",team=13)
session.add(players)
session.commit()
	
players = Players(number="36",fname="Mats",lname="Zuccarello",position="Right Wing",team=13)
session.add(players)
session.commit()
	

#Philly14
players = Players(number="78",fname="Pierre-Edouard",lname="Bellemare",position="Left Wing",team=14)
session.add(players)
session.commit()
	
players = Players(number="37",fname="Tim",lname="Brent",position="Center",team=14)
session.add(players)
session.commit()
	
players = Players(number="34",fname="Chris",lname="Conner",position="Right Wing",team=14)
session.add(players)
session.commit()
	
players = Players(number="52",fname="Nick",lname="Cousins",position="Center",team=14)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Sean",lname="Couturier",position="Center",team=14)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Michael",lname="Del Zotto",position="Defenseman",team=14)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Davis",lname="Drewiske",position="Defenseman",team=14)
session.add(players)
session.commit()
	
players = Players(number="89",fname="Sam",lname="Gagner",position="Center",team=14)
session.add(players)
session.commit()
	
players = Players(number="28",fname="Claude",lname="Giroux",position="Center",team=14)
session.add(players)
session.commit()
	
players = Players(number="53",fname="Shayne",lname="Gostisbehere",position="Defenseman",team=14)
session.add(players)
session.commit()
	
players = Players(number="3",fname="Radko",lname="Gudas",position="Defenseman",team=14)
session.add(players)
session.commit()
	
players = Players(number="48",fname="Robert",lname="Hagg",position="Defenseman",team=14)
session.add(players)
session.commit()
	
players = Players(number="45",fname="Jason",lname="LaBarbera",position="Goaltender",team=14)
session.add(players)
session.commit()
	
players = Players(number="49",fname="Scott",lname="Laughton",position="Center",team=14)
session.add(players)
session.commit()
	
players = Players(number="40",fname="Vincent",lname="Lecavalier",position="Center",team=14)
session.add(players)
session.commit()
	
players = Players(number="47",fname="Andrew",lname="MacDonald",position="Defenseman",team=14)
session.add(players)
session.commit()
	
players = Players(number="23",fname="Brandon",lname="Manning",position="Defenseman",team=14)
session.add(players)
session.commit()
	
players = Players(number="46",fname="Christian",lname="Marti",position="Defenseman",team=14)
session.add(players)
session.commit()
	
players = Players(number="35",fname="Steve",lname="Mason",position="Goaltender",team=14)
session.add(players)
session.commit()
	
players = Players(number="36",fname="Colin",lname="McDonald",position="Right Wing",team=14)
session.add(players)
session.commit()
	
players = Players(number="82",fname="Evgeny",lname="Medvedev",position="Defenseman",team=14)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Michal",lname="Neuvirth",position="Goaltender",team=14)
session.add(players)
session.commit()
	
players = Players(number="38",fname="Aaron",lname="Palushaj",position="Right Wing",team=14)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Chris",lname="Porter",position="Left Wing",team=14)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Michael",lname="Raffl",position="Left Wing",team=14)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Matt",lname="Read",position="Right Wing",team=14)
session.add(players)
session.commit()
	
players = Players(number="10",fname="Brayden",lname="Schenn",position="Center",team=14)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Luke",lname="Schenn",position="Defenseman",team=14)
session.add(players)
session.commit()
	
players = Players(number="55",fname="Nick",lname="Schultz",position="Defenseman",team=14)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Wayne",lname="Simmonds",position="Right Wing",team=14)
session.add(players)
session.commit()
	
players = Players(number="32",fname="Mark",lname="Streit",position="Defenseman",team=14)
session.add(players)
session.commit()
	
players = Players(number="20",fname="R.J.",lname="Umberger",position="Left Wing",team=14)
session.add(players)
session.commit()
	
players = Players(number="76",fname="Chris",lname="VandeVelde",position="Center",team=14)
session.add(players)
session.commit()
	
players = Players(number="93",fname="Jakub",lname="Voracek",position="Right Wing",team=14)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Ryan",lname="White",position="Center",team=14)
session.add(players)
session.commit()
	

#Pitt15
players = Players(number="38",fname="Niclas",lname="Andersen",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="45",fname="Josh",lname="Archibald",position="Right Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Beau",lname="Bennett",position="Right Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="42",fname="Tyler",lname="Biggs",position="Right Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="13",fname="Nick",lname="Bonino",position="Center",team=15)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Adam",lname="Clendening",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="28",fname="Ian",lname="Cole",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="87",fname="Sidney",lname="Crosby",position="Center",team=15)
session.add(players)
session.commit()
	
players = Players(number="7",fname="Matt",lname="Cullen",position="Center",team=15)
session.add(players)
session.commit()
	
players = Players(number="39",fname="Jean-Sebastien",lname="Dea",position="Center",team=15)
session.add(players)
session.commit()
	
players = Players(number="8",fname="Brian",lname="Dumoulin",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="9",fname="Pascal",lname="Dupuis",position="Right Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Tim",lname="Erixon",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Bobby",lname="Farnham",position="Right Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Eric",lname="Fehr",position="Center",team=15)
session.add(players)
session.commit()
	
players = Players(number="29",fname="Marc-Andre",lname="Fleury",position="Goaltender",team=15)
session.add(players)
session.commit()
	
players = Players(number="53",fname="Barry",lname="Goers",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="55",fname="Sergei",lname="Gonchar",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="72",fname="Patric",lname="Hornqvist",position="Right Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="35",fname="Tristan",lname="Jarry",position="Goaltender",team=15)
session.add(players)
session.commit()
	
players = Players(number="81",fname="Phil",lname="Kessel",position="Right Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="34",fname="Tom",lname="Kuhnhackl",position="Right Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Chris",lname="Kunitz",position="Left Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="58",fname="Kris",lname="Letang",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Ben",lname="Lovejoy",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="3",fname="Olli",lname="Maatta",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="71",fname="Evgeni",lname="Malkin",position="Center",team=15)
session.add(players)
session.commit()
	
players = Players(number="36",fname="Matia",lname="Marcantuoni",position="Right Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Reid",lname="McNeill",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Kael",lname="Mouillierat",position="Left Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Matt",lname="Murray",position="Goaltender",team=15)
session.add(players)
session.commit()
	
players = Players(number="65",fname="Steve",lname="Oleksy",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Will",lname="O'Neill",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="57",fname="David",lname="Perron",position="Left Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="61",fname="Sergei",lname="Plotnikov",position="Left Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Kevin",lname="Porter",position="Center",team=15)
session.add(players)
session.commit()
	
players = Players(number="51",fname="Derrick",lname="Pouliot",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="32",fname="Harrison",lname="Ruopp",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Bryan",lname="Rust",position="Right Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Rob",lname="Scuderi",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="47",fname="Tom",lname="Sestito",position="Left Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="43",fname="Conor",lname="Sheary",position="Left Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="49",fname="Dominik",lname="Simon",position="Center",team=15)
session.add(players)
session.commit()
	
players = Players(number="41",fname="Daniel",lname="Sprong",position="Right Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="40",fname="Oskar",lname="Sundqvist",position="Center",team=15)
session.add(players)
session.commit()
	
players = Players(number="46",fname="Dominik",lname="Uher",position="Center",team=15)
session.add(players)
session.commit()
	
players = Players(number="5",fname="David",lname="Warsofsky",position="Defenseman",team=15)
session.add(players)
session.commit()
	
players = Players(number="23",fname="Scott",lname="Wilson",position="Left Wing",team=15)
session.add(players)
session.commit()
	
players = Players(number="37",fname="Jeff",lname="Zatkoff",position="Goaltender",team=15)
session.add(players)
session.commit()
	

#Wash16
players = Players(number="27",fname="Karl",lname="Alzner",position="Defenseman",team=16)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Nicklas",lname="Backstrom",position="Center",team=16)
session.add(players)
session.commit()
	
players = Players(number="65",fname="Andre",lname="Burakovsky",position="Left Wing",team=16)
session.add(players)
session.commit()
	
players = Players(number="74",fname="John",lname="Carlson",position="Defenseman",team=16)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Jason",lname="Chimera",position="Left Wing",team=16)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Taylor",lname="Chorney",position="Defenseman",team=16)
session.add(players)
session.commit()
	
players = Players(number="39",fname="Dan",lname="Ellis",position="Goaltender",team=16)
session.add(players)
session.commit()
	
players = Players(number="4",fname="John",lname="Erskine",position="Defenseman",team=16)
session.add(players)
session.commit()
	
players = Players(number="49",fname="Stanislav",lname="Galiev",position="Right Wing",team=16)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Tim",lname="Gleason",position="Defenseman",team=16)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Curtis",lname="Glencross",position="Left Wing",team=16)
session.add(players)
session.commit()
	
players = Players(number="70",fname="Braden",lname="Holtby",position="Goaltender",team=16)
session.add(players)
session.commit()
	
players = Players(number="90",fname="Marcus",lname="Johansson",position="Center/Left Wing",team=16)
session.add(players)
session.commit()
	
players = Players(number="92",fname="Evgeny",lname="Kuznetsov",position="F",team=16)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Brooks",lname="Laich",position="Center",team=16)
session.add(players)
session.commit()
	
players = Players(number="46",fname="Michael",lname="Latta",position="Center",team=16)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Matt",lname="Niskanen",position="Defenseman",team=16)
session.add(players)
session.commit()
	
players = Players(number="9",fname="Dmitry",lname="Orlov",position="Defenseman",team=16)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Brooks",lname="Orpik",position="Defenseman",team=16)
session.add(players)
session.commit()
	
players = Players(number="77",fname="T.J.",lname="Oshie",position="Right Wing",team=16)
session.add(players)
session.commit()
	
players = Players(number="8",fname="Alex",lname="Ovechkin",position="Left Wing",team=16)
session.add(players)
session.commit()
	
players = Players(number="35",fname="Justin",lname="Peters",position="Goaltender",team=16)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Justin",lname="Williams",position="Right Wing",team=16)
session.add(players)
session.commit()
	
players = Players(number="43",fname="Tom",lname="Wilson",position="Right Wing",team=16)
session.add(players)
session.commit()
	

#ana17
players = Players(number="31",fname="Frederik",lname="Andersen",position="Goaltender",team=17)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Kevin",lname="Bieksa",position="Defenseman",team=17)
session.add(players)
session.commit()
	
players = Players(number="7",fname="Andrew",lname="Cogliano",position="Center",team=17)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Simon",lname="Despres",position="Defenseman",team=17)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Tomas",lname="Fleischmann",position="Left Wing",team=17)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Cam",lname="Fowler",position="Defenseman",team=17)
session.add(players)
session.commit()
	
players = Players(number="43",fname="Max",lname="Friberg",position="Left Wing",team=17)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Ryan",lname="Getzlaf",position="Center",team=17)
session.add(players)
session.commit()
	
players = Players(number="36",fname="John",lname="Gibson",position="Goaltender",team=17)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Carl",lname="Hagelin",position="Left Wing",team=17)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Korbinian",lname="Holzer",position="Defenseman",team=17)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Shawn",lname="Horcoff",position="Center",team=17)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Tim",lname="Jackman",position="Right Wing",team=17)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Ryan",lname="Kesler",position="Center",team=17)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Anton",lname="Khudobin",position="Goaltender",team=17)
session.add(players)
session.commit()
	
players = Players(number="47",fname="Hampus",lname="Lindholm",position="Defenseman",team=17)
session.add(players)
session.commit()
	
players = Players(number="42",fname="Josh",lname="Manson",position="Defenseman",team=17)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Patrick",lname="Maroon",position="Left Wing",team=17)
session.add(players)
session.commit()
	
players = Players(number="75",fname="Jaycob",lname="Megna",position="Defenseman",team=17)
session.add(players)
session.commit()
	
players = Players(number="10",fname="Corey",lname="Perry",position="Right Wing",team=17)
session.add(players)
session.commit()
	
players = Players(number="67",fname="Rickard",lname="Rakell",position="Right Wing",team=17)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Mike",lname="Santorelli",position="Center",team=17)
session.add(players)
session.commit()
	
players = Players(number="46",fname="Jiri",lname="Sekac",position="Left Wing",team=17)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Jakob",lname="Silfverberg",position="Right Wing",team=17)
session.add(players)
session.commit()
	
players = Players(number="29",fname="Chris",lname="Stewart",position="Right Wing",team=17)
session.add(players)
session.commit()
	
players = Players(number="3",fname="Clayton",lname="Stoner",position="Defenseman",team=17)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Nate",lname="Thompson",position="Center",team=17)
session.add(players)
session.commit()
	
players = Players(number="45",fname="Sami",lname="Vatanen",position="Defenseman",team=17)
session.add(players)
session.commit()
	
players = Players(number="62",fname="Chris",lname="Wagner",position="Right Wing",team=17)
session.add(players)
session.commit()
	

#az18
players = Players(number="89",fname="Mikkel",lname="Boedker",position="Left Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="58",fname="Michael",lname="Bunting",position="Left Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Kyle",lname="Chipchura",position="Center",team=18)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Craig",lname="Cunningham",position="Right Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="34",fname="Klas",lname="Dahlbeck",position="Defenseman",team=18)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Shane",lname="Doan",position="Right Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Max",lname="Domi",position="Left Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="37",fname="Louis",lname="Domingue",position="Goaltender",team=18)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Steve",lname="Downie",position="Right Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="10",fname="Anthony",lname="Duclair",position="Left Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Christian",lname="Dvorak",position="Center",team=18)
session.add(players)
session.commit()
	
players = Players(number="23",fname="Oliver",lname="Ekman-Larsson",position="Defenseman",team=18)
session.add(players)
session.commit()
	
players = Players(number="45",fname="Stefan",lname="Elliott",position="Defenseman",team=18)
session.add(players)
session.commit()
	
players = Players(number="32",fname="Tyler",lname="Gaudet",position="Center",team=18)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Boyd",lname="Gordon",position="Center",team=18)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Nicklas",lname="Grossmann",position="Defenseman",team=18)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Martin",lname="Hanzal",position="Center",team=18)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Marek",lname="Langhamer",position="Goaltender",team=18)
session.add(players)
session.commit()
	
players = Players(number="38",fname="Lucas",lname="Lessio",position="Left Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="29",fname="Anders",lname="Lindback",position="Goaltender",team=18)
session.add(players)
session.commit()
	
players = Players(number="49",fname="Ryan",lname="MacInnis",position="Center",team=18)
session.add(players)
session.commit()
	
players = Players(number="48",fname="Jordan",lname="Martinook",position="Left Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="61",fname="Dysin",lname="Mayo",position="Defenseman",team=18)
session.add(players)
session.commit()
	
players = Players(number="91",fname="Dakota",lname="Mermis",position="Defenseman",team=18)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Zbynek",lname="Michalek",position="Defenseman",team=18)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Connor",lname="Murphy",position="Defenseman",team=18)
session.add(players)
session.commit()
	
players = Players(number="9",fname="Brendan",lname="Perlini",position="Left Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="43",fname="Matthias",lname="Plachta",position="Left Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Chris",lname="Pronger",position="Defenseman",team=18)
session.add(players)
session.commit()
	
players = Players(number="46",fname="Dylan",lname="Reese",position="Defenseman",team=18)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Brad",lname="Richardson",position="Right Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="8",fname="Tobias",lname="Rieder",position="Right Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="55",fname="Henrik",lname="Samuelsson",position="Right Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Philip",lname="Samuelsson",position="Defenseman",team=18)
session.add(players)
session.commit()
	
players = Players(number="28",fname="John",lname="Scott",position="Left Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="39",fname="Brendan",lname="Shinnimin",position="Center",team=18)
session.add(players)
session.commit()
	
players = Players(number="41",fname="Mike",lname="Smith",position="Goaltender",team=18)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Michael",lname="Stone",position="Defenseman",team=18)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Dylan",lname="Strome",position="Center",team=18)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Jordan",lname="Szwarz",position="Right Wing",team=18)
session.add(players)
session.commit()
	
players = Players(number="35",fname="Niklas",lname="Treutle",position="Goaltender",team=18)
session.add(players)
session.commit()
	
players = Players(number="50",fname="Antoine",lname="Vermette",position="Center",team=18)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Joe",lname="Vitale",position="Center",team=18)
session.add(players)
session.commit()
	

#Flames19
players = Players(number="51",fname="Kenny",lname="Agostino",position="Left Wing",team=19)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Mikael",lname="Backlund",position="Center",team=19)
session.add(players)
session.commit()
	
players = Players(number="93",fname="Sam",lname="Bennett",position="Center",team=19)
session.add(players)
session.commit()
	
players = Players(number="52",fname="Brandon",lname="Bollig",position="Left Wing",team=19)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Lance",lname="Bouma",position="Center",team=19)
session.add(players)
session.commit()
	
players = Players(number="7",fname="T.J.",lname="Brodie",position="Defenseman",team=19)
session.add(players)
session.commit()
	
players = Players(number="32",fname="Paul",lname="Byron",position="Center",team=19)
session.add(players)
session.commit()
	
players = Players(number="8",fname="Joe",lname="Colborne",position="Center",team=19)
session.add(players)
session.commit()
	
players = Players(number="29",fname="Deryk",lname="Engelland",position="Defenseman",team=19)
session.add(players)
session.commit()
	
players = Players(number="79",fname="Michael",lname="Ferland",position="Left Wing",team=19)
session.add(players)
session.commit()
	
players = Players(number="67",fname="Michael",lname="Frolik",position="W",team=19)
session.add(players)
session.commit()
	
players = Players(number="13",fname="Johnny",lname="Gaudreau",position="Left Wing",team=19)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Mark",lname="Giordano",position="Defenseman",team=19)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Dougie",lname="Hamilton",position="Defenseman",team=19)
session.add(players)
session.commit()
	
players = Players(number="1",fname="Jonas",lname="Hiller",position="Goaltender",team=19)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Jiri",lname="Hudler",position="Right Wing",team=19)
session.add(players)
session.commit()
	
players = Players(number="19",fname="David",lname="Jones",position="Right Wing",team=19)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Josh",lname="Jooris",position="Center",team=19)
session.add(players)
session.commit()
	
players = Players(number="23",fname="Sean",lname="Monahan",position="Center",team=19)
session.add(players)
session.commit()
	
players = Players(number="37",fname="Joni",lname="Ortio",position="Goaltender",team=19)
session.add(players)
session.commit()
	
players = Players(number="57",fname="Emile",lname="Poirier",position="Left Wing",team=19)
session.add(players)
session.commit()
	
players = Players(number="28",fname="Corey",lname="Potter",position="Defenseman",team=19)
session.add(players)
session.commit()
	
players = Players(number="31",fname="Karri",lname="Ramo",position="Goaltender",team=19)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Mason",lname="Raymond",position="Left Wing",team=19)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Kris",lname="Russell",position="Defenseman",team=19)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Drew",lname="Shore",position="Center",team=19)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Ladislav",lname="Smid",position="Defenseman",team=19)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Matt",lname="Stajan",position="Center",team=19)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Dennis",lname="Wideman",position="Defenseman",team=19)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Tyler",lname="Wotherspoon",position="Defenseman",team=19)
session.add(players)
session.commit()
	

#EDM20
players = Players(number="14",fname="Jordan",lname="Eberle",position="Right Wing",team=20)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Mark",lname="Fayne",position="Defenseman",team=20)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Andrew",lname="Ference",position="Defenseman",team=20)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Luke",lname="Gazdic",position="Left Wing",team=20)
session.add(players)
session.commit()
	
players = Players(number="62",fname="Eric",lname="Gryba",position="Defenseman",team=20)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Taylor",lname="Hall",position="Left Wing",team=20)
session.add(players)
session.commit()
	
players = Players(number="23",fname="Matt",lname="Hendricks",position="Left Wing",team=20)
session.add(players)
session.commit()
	
players = Players(number="77",fname="Oscar",lname="Klefbom",position="Defenseman",team=20)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Rob",lname="Klinkhammer",position="Left Wing",team=20)
session.add(players)
session.commit()
	
players = Players(number="28",fname="Lauri",lname="Korpikoski",position="Left Wing",team=20)
session.add(players)
session.commit()
	
players = Players(number="51",fname="Anton",lname="Lander",position="Center",team=20)
session.add(players)
session.commit()
	
players = Players(number="55",fname="Mark",lname="Letestu",position="Center",team=20)
session.add(players)
session.commit()
	
players = Players(number="97",fname="Connor",lname="McDavid",position="Center",team=20)
session.add(players)
session.commit()
	
players = Players(number="86",fname="Nikita",lname="Nikitin",position="Defenseman",team=20)
session.add(players)
session.commit()
	
players = Players(number="39",fname="Anders",lname="Nilsson",position="Goaltender",team=20)
session.add(players)
session.commit()
	
players = Players(number="93",fname="Ryan",lname="Nugent-Hopkins",position="Center",team=20)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Tyler",lname="Pitlick",position="Right Wing",team=20)
session.add(players)
session.commit()
	
players = Players(number="67",fname="Benoit",lname="Pouliot",position="Left Wing",team=20)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Teddy",lname="Purcell",position="Right Wing",team=20)
session.add(players)
session.commit()
	
players = Players(number="8",fname="Griffin",lname="Reinhart",position="Defenseman",team=20)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Justin",lname="Schultz",position="Defenseman",team=20)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Ben",lname="Scrivens",position="Goaltender",team=20)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Andrej",lname="Sekera",position="Defenseman",team=20)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Cam",lname="Talbot",position="Goaltender",team=20)
session.add(players)
session.commit()
	
players = Players(number="10",fname="Nail",lname="Yakupov",position="Right Wing",team=20)
session.add(players)
session.commit()
	

#LAK21
players = Players(number="15",fname="Andy",lname="Andreoff",position="Center/Left Wing",team=21)
session.add(players)
session.commit()
	
players = Players(number="23",fname="Dustin",lname="Brown",position="Right Wing",team=21)
session.add(players)
session.commit()
	
players = Players(number="77",fname="Jeff",lname="Carter",position="Center/Right Wing",team=21)
session.add(players)
session.commit()
	
players = Players(number="13",fname="Kyle",lname="Clifford",position="Left Wing",team=21)
session.add(players)
session.commit()
	
players = Players(number="8",fname="Drew",lname="Doughty",position="Defenseman",team=21)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Christian",lname="Ehrhoff",position="Defenseman",team=21)
session.add(players)
session.commit()
	
players = Players(number="1",fname="Jhonas",lname="Enroth",position="Goaltender",team=21)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Marian",lname="Gaborik",position="Right Wing",team=21)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Matt",lname="Greene",position="Defenseman",team=21)
session.add(players)
session.commit()
	
players = Players(number="74",fname="Dwight",lname="King",position="Left Wing",team=21)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Anze",lname="Kopitar",position="Center",team=21)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Trevor",lname="Lewis",position="Center/Right Wing",team=21)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Milan",lname="Lucic",position="Left Wing",team=21)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Alec",lname="Martinez",position="Defenseman",team=21)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Jamie",lname="McBain",position="Defenseman",team=21)
session.add(players)
session.commit()
	
players = Players(number="3",fname="Brayden",lname="McNabb",position="Defenseman",team=21)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Jake",lname="Muzzin",position="Defenseman",team=21)
session.add(players)
session.commit()
	
players = Players(number="71",fname="Jordan",lname="Nolan",position="Center/Right Wing",team=21)
session.add(players)
session.commit()
	
players = Players(number="70",fname="Tanner",lname="Pearson",position="Left Wing",team=21)
session.add(players)
session.commit()
	
players = Players(number="32",fname="Jonathan",lname="Quick",position="Goaltender",team=21)
session.add(players)
session.commit()
	
players = Players(number="37",fname="Nick",lname="Shore",position="Center",team=21)
session.add(players)
session.commit()
	
players = Players(number="73",fname="Tyler",lname="Toffoli",position="Center/Right Wing",team=21)
session.add(players)
session.commit()
	

#SJS22
players = Players(number="61",fname="Justin",lname="Braun",position="Defenseman",team=22)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Mike",lname="Brown",position="Right Wing",team=22)
session.add(players)
session.commit()
	
players = Players(number="88",fname="Brent",lname="Burns",position="Defenseman",team=22)
session.add(players)
session.commit()
	
players = Players(number="39",fname="Logan",lname="Couture",position="Center",team=22)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Brenden",lname="Dillon",position="Defenseman",team=22)
session.add(players)
session.commit()
	
players = Players(number="48",fname="Tomas",lname="Hertl",position="Center/Left Wing",team=22)
session.add(players)
session.commit()
	
players = Players(number="31",fname="Martin",lname="Jones",position="Goaltender",team=22)
session.add(players)
session.commit()
	
players = Players(number="68",fname="Melker",lname="Karlsson",position="Right Wing",team=22)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Patrick",lname="Marleau",position="Center/Left Wing",team=22)
session.add(players)
session.commit()
	
players = Players(number="7",fname="Paul",lname="Martin",position="Defenseman",team=22)
session.add(players)
session.commit()
	
players = Players(number="41",fname="Mirco",lname="Mueller",position="Defenseman",team=22)
session.add(players)
session.commit()
	
players = Players(number="83",fname="Matthew",lname="Nieto",position="Left Wing",team=22)
session.add(players)
session.commit()
	
players = Players(number="8",fname="Joe",lname="Pavelski",position="Center",team=22)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Ben",lname="Smith",position="Right Wing",team=22)
session.add(players)
session.commit()
	
players = Players(number="32",fname="Alex",lname="Stalock",position="Goaltender",team=22)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Joe",lname="Thornton",position="Center",team=22)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Marc-Edouard",lname="Vlasic",position="Defenseman",team=22)
session.add(players)
session.commit()
	
players = Players(number="42",fname="Joel",lname="Ward",position="Right Wing",team=22)
session.add(players)
session.commit()
	
players = Players(number="57",fname="Tommy",lname="Wingels",position="Center/Right Wing",team=22)
session.add(players)
session.commit()
	

#VAN23
players = Players(number="47",fname="Sven",lname="Baertschi",position="Left Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="44",fname="Matt",lname="Bartkowski",position="Defenseman",team=23)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Alexandre",lname="Burrows",position="Right Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Frank",lname="Corrado",position="Defenseman",team=23)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Adam",lname="Cracknell",position="Right Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Derek",lname="Dorsett",position="Right Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="23",fname="Alexander",lname="Edler",position="Defenseman",team=23)
session.add(players)
session.commit()
	
players = Players(number="67",fname="Alexandre",lname="Grenier",position="Right Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Dan",lname="Hamhuis",position="Defenseman",team=23)
session.add(players)
session.commit()
	
players = Players(number="36",fname="Jannik",lname="Hansen",position="Right Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Chris",lname="Higgins",position="Left Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="53",fname="Bo",lname="Horvat",position="Center",team=23)
session.add(players)
session.commit()
	
players = Players(number="46",fname="Nicklas",lname="Jensen",position="Left Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="41",fname="Ronalds",lname="Kenins",position="Left Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Jacob",lname="Markstrom",position="Goaltender",team=23)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Ryan",lname="Miller",position="Goaltender",team=23)
session.add(players)
session.commit()
	
players = Players(number="9",fname="Brandon",lname="Prust",position="Left Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Luca",lname="Sbisa",position="Defenseman",team=23)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Daniel",lname="Sedin",position="Left Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Henrik",lname="Sedin",position="Center",team=23)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Brandon",lname="Sutter",position="Center",team=23)
session.add(players)
session.commit()
	
players = Players(number="8",fname="Chris",lname="Tanev",position="Defenseman",team=23)
session.add(players)
session.commit()
	
players = Players(number="7",fname="Linden",lname="Vey",position="Right Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Radim",lname="Vrbata",position="Right Wing",team=23)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Yannick",lname="Weber",position="Defenseman",team=23)
session.add(players)
session.commit()
	

#CHI24
players = Players(number="15",fname="Artem",lname="Anisimov",position="Center",team=24)
session.add(players)
session.commit()
	
players = Players(number="39",fname="Kyle",lname="Baun",position="Right Wing",team=24)
session.add(players)
session.commit()
	
players = Players(number="29",fname="Bryan",lname="Bickell",position="Left Wing",team=24)
session.add(players)
session.commit()
	
players = Players(number="50",fname="Corey",lname="Crawford",position="Goaltender",team=24)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Trevor",lname="Daley",position="Defenseman",team=24)
session.add(players)
session.commit()
	
players = Players(number="56",fname="Marko",lname="Dano",position="Center/Right Wing",team=24)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Scott",lname="Darling",position="Goaltender",team=24)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Andrew",lname="Desjardins",position="Center",team=24)
session.add(players)
session.commit()
	
players = Players(number="28",fname="Ryan",lname="Garbutt",position="Center",team=24)
session.add(players)
session.commit()
	
players = Players(number="38",fname="Ryan",lname="Hartman",position="Right Wing",team=24)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Niklas",lname="Hjalmarsson",position="Defenseman",team=24)
session.add(players)
session.commit()
	
players = Players(number="81",fname="Marian",lname="Hossa",position="Right Wing",team=24)
session.add(players)
session.commit()
	
players = Players(number="88",fname="Patrick",lname="Kane",position="Right Wing",team=24)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Duncan",lname="Keith",position="Defenseman",team=24)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Marcus",lname="Kruger",position="Center",team=24)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Jeremy",lname="Morin",position="Left Wing",team=24)
session.add(players)
session.commit()
	
players = Players(number="72",fname="Artemi",lname="Panarin",position="F",team=24)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Ville",lname="Pokka",position="Defenseman",team=24)
session.add(players)
session.commit()
	
players = Players(number="70",fname="Dennis",lname="Rasmussen",position="Center",team=24)
session.add(players)
session.commit()
	
players = Players(number="32",fname="Michal",lname="Rozsival",position="Defenseman",team=24)
session.add(players)
session.commit()
	
players = Players(number="5",fname="David",lname="Rundblad",position="Defenseman",team=24)
session.add(players)
session.commit()
	
players = Players(number="7",fname="Brent",lname="Seabrook",position="Defenseman",team=24)
session.add(players)
session.commit()
	
players = Players(number="65",fname="Andrew",lname="Shaw",position="Center",team=24)
session.add(players)
session.commit()
	
players = Players(number="43",fname="Viktor",lname="Svedberg",position="Defenseman",team=24)
session.add(players)
session.commit()
	
players = Players(number="86",fname="Teuvo",lname="Teravainen",position="Center",team=24)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Viktor",lname="Tikhonov",position="Right Wing",team=24)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Jonathan",lname="Toews",position="Center",team=24)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Corey",lname="Tropp",position="Right Wing",team=24)
session.add(players)
session.commit()
	
players = Players(number="57",fname="Trevor",lname="van Riemsdyk",position="Defenseman",team=24)
session.add(players)
session.commit()
	

#COL25
players = Players(number="28",fname="Andrew",lname="Agozzino",position="Left Wing",team=25)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Tyson",lname="Barrie",position="Defenseman",team=25)
session.add(players)
session.commit()
	
players = Players(number="32",fname="Francois",lname="Beauchemin",position="Defenseman",team=25)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Reto",lname="Berra",position="Goaltender",team=25)
session.add(players)
session.commit()
	
players = Players(number="58",fname="Patrick",lname="Bordeleau",position="Left Wing",team=25)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Marc-Andre",lname="Cliche",position="Center",team=25)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Blake",lname="Comeau",position="Left Wing",team=25)
session.add(players)
session.commit()
	
players = Players(number="9",fname="Matt",lname="Duchene",position="Center",team=25)
session.add(players)
session.commit()
	
players = Players(number="45",fname="Dennis",lname="Everberg",position="Left Wing",team=25)
session.add(players)
session.commit()
	
players = Players(number="46",fname="Brandon",lname="Gormley",position="Defenseman",team=25)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Mikhail",lname="Grigorenko",position="Center",team=25)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Nate",lname="Guenin",position="Defenseman",team=25)
session.add(players)
session.commit()
	
players = Players(number="38",fname="Joey",lname="Hishon",position="Center",team=25)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Nick",lname="Holden",position="Defenseman",team=25)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Jarome",lname="Iginla",position="Right Wing",team=25)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Erik",lname="Johnson",position="Defenseman",team=25)
session.add(players)
session.commit()
	
players = Players(number="92",fname="Gabriel",lname="Landeskog",position="Left Wing",team=25)
session.add(players)
session.commit()
	
players = Players(number="29",fname="Nathan",lname="MacKinnon",position="Center",team=25)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Andreas",lname="Martinsen",position="Left Wing",team=25)
session.add(players)
session.commit()
	
players = Players(number="55",fname="Cody",lname="McLeod",position="Left Wing",team=25)
session.add(players)
session.commit()
	
players = Players(number="7",fname="John",lname="Mitchell",position="Center",team=25)
session.add(players)
session.commit()
	
players = Players(number="31",fname="Calvin",lname="Pickard",position="Goaltender",team=25)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Zach",lname="Redmond",position="Defenseman",team=25)
session.add(players)
session.commit()
	
players = Players(number="71",fname="Borna",lname="Rendulic",position="Right Wing",team=25)
session.add(players)
session.commit()
	
players = Players(number="37",fname="Colin",lname="Smith",position="Center",team=25)
session.add(players)
session.commit()
	
players = Players(number="34",fname="Carl",lname="Soderberg",position="Center",team=25)
session.add(players)
session.commit()
	
players = Players(number="10",fname="Ben",lname="Street",position="Center",team=25)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Brad",lname="Stuart",position="Defenseman",team=25)
session.add(players)
session.commit()
	
players = Players(number="40",fname="Alex",lname="Tanguay",position="Right Wing",team=25)
session.add(players)
session.commit()
	
players = Players(number="1",fname="Semyon",lname="Varlamov",position="Goaltender",team=25)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Jesse",lname="Winchester",position="Center",team=25)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Nikita",lname="Zadorov",position="Defenseman",team=25)
session.add(players)
session.commit()
	

#DAL26
players = Players(number="14",fname="Jamie",lname="Benn",position="Center/Left Wing",team=26)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Jordie",lname="Benn",position="Defenseman",team=26)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Jason",lname="Demers",position="Defenseman",team=26)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Cody",lname="Eakin",position="Center",team=26)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Patrick",lname="Eaves",position="Center",team=26)
session.add(players)
session.commit()
	
players = Players(number="94",fname="Radek",lname="Faksa",position="Center",team=26)
session.add(players)
session.commit()
	
players = Players(number="38",fname="Vernon",lname="Fiddler",position="Center",team=26)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Alex",lname="Goligoski",position="Defenseman",team=26)
session.add(players)
session.commit()
	
players = Players(number="83",fname="Ales",lname="Hemsky",position="Right Wing",team=26)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Jyrki",lname="Jokipakka",position="Defenseman",team=26)
session.add(players)
session.commit()
	
players = Players(number="3",fname="John",lname="Klingberg",position="Defenseman",team=26)
session.add(players)
session.commit()
	
players = Players(number="32",fname="Kari",lname="Lehtonen",position="Goaltender",team=26)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Travis",lname="Moen",position="Left Wing",team=26)
session.add(players)
session.commit()
	
players = Players(number="43",fname="Valeri",lname="Nichushkin",position="Right Wing",team=26)
session.add(players)
session.commit()
	
players = Players(number="31",fname="Antti",lname="Niemi",position="Goaltender",team=26)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Jamie",lname="Oleksiak",position="Defenseman",team=26)
session.add(players)
session.commit()
	
players = Players(number="47",fname="Johnny",lname="Oduya",position="Defenseman",team=26)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Brett",lname="Ritchie",position="Right Wing",team=26)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Antoine",lname="Roussel",position="Left Wing",team=26)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Colton",lname="Sceviour",position="Right Wing",team=26)
session.add(players)
session.commit()
	
players = Players(number="91",fname="Tyler",lname="Seguin",position="Center/Right Wing",team=26)
session.add(players)
session.commit()
	
players = Players(number="10",fname="Patrick",lname="Sharp",position="Left Wing",team=26)
session.add(players)
session.commit()
	
players = Players(number="90",fname="Jason",lname="Spezza",position="Center",team=26)
session.add(players)
session.commit()
	

#MINN27
players = Players(number="32",fname="Niklas",lname="Backstrom",position="Goaltender",team=27)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Keith",lname="Ballard",position="Defenseman",team=27)
session.add(players)
session.commit()
	
players = Players(number="23",fname="Sean",lname="Bergenheim",position="Left Wing",team=27)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Jonas",lname="Brodin",position="Defenseman",team=27)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Ryan",lname="Carter",position="Center",team=27)
session.add(players)
session.commit()
	
players = Players(number="3",fname="Charlie",lname="Coyle",position="Center",team=27)
session.add(players)
session.commit()
	
players = Players(number="40",fname="Devan",lname="Dubnyk",position="Goaltender",team=27)
session.add(players)
session.commit()
	
players = Players(number="55",fname="Matt",lname="Dumba",position="Defenseman",team=27)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Christian",lname="Folin",position="Defenseman",team=27)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Justin",lname="Fontaine",position="Right Wing",team=27)
session.add(players)
session.commit()
	
players = Players(number="64",fname="Mikael",lname="Granlund",position="Center",team=27)
session.add(players)
session.commit()
	
players = Players(number="56",fname="Erik",lname="Haula",position="Center",team=27)
session.add(players)
session.commit()
	
players = Players(number="9",fname="Mikko",lname="Koivu",position="Center",team=27)
session.add(players)
session.commit()
	
players = Players(number="35",fname="Darcy",lname="Kuemper",position="Goaltender",team=27)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Jordan",lname="Leopold",position="Defenseman",team=27)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Nino",lname="Niederreiter",position="Right Wing",team=27)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Zach",lname="Parise",position="Left Wing",team=27)
session.add(players)
session.commit()
	
players = Players(number="29",fname="Jason",lname="Pominville",position="Right Wing",team=27)
session.add(players)
session.commit()
	
players = Players(number="39",fname="Nate",lname="Prosser",position="Defenseman",team=27)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Marco",lname="Scandella",position="Defenseman",team=27)
session.add(players)
session.commit()
	
players = Players(number="10",fname="Jordan",lname="Schroeder",position="Center",team=27)
session.add(players)
session.commit()
	
players = Players(number="46",fname="Jared",lname="Spurgeon",position="Defenseman",team=27)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Ryan",lname="Suter",position="Defenseman",team=27)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Thomas",lname="Vanek",position="Left Wing",team=27)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Jason",lname="Zucker",position="Left Wing",team=27)
session.add(players)
session.commit()
	

#NSH28
players = Players(number="64",fname="Victor",lname="Bartley",position="Defenseman",team=28)
session.add(players)
session.commit()
	
players = Players(number="57",fname="Gabriel",lname="Bourque",position="Left Wing",team=28)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Mattias",lname="Ekholm",position="Defenseman",team=28)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Ryan",lname="Ellis",position="Defenseman",team=28)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Mike",lname="Fisher",position="Center",team=28)
session.add(players)
session.commit()
	
players = Players(number="9",fname="Filip",lname="Forsberg",position="Center",team=28)
session.add(players)
session.commit()
	
players = Players(number="28",fname="Paul",lname="Gaustad",position="Center",team=28)
session.add(players)
session.commit()
	
players = Players(number="11",fname="Cody",lname="Hodgson",position="Center",team=28)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Carter",lname="Hutton",position="Goaltender",team=28)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Barret",lname="Jackman",position="Defenseman",team=28)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Calle",lname="Jarnkrok",position="Center",team=28)
session.add(players)
session.commit()
	
players = Players(number="3",fname="Seth",lname="Jones",position="Defenseman",team=28)
session.add(players)
session.commit()
	
players = Players(number="59",fname="Roman",lname="Josi",position="Defenseman",team=28)
session.add(players)
session.commit()
	
players = Players(number="18",fname="James",lname="Neal",position="Left Wing",team=28)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Eric",lname="Nystrom",position="Left Wing",team=28)
session.add(players)
session.commit()
	
players = Players(number="63",fname="Mike",lname="Ribeiro",position="Center",team=28)
session.add(players)
session.commit()
	
players = Players(number="35",fname="Pekka",lname="Rinne",position="Goaltender",team=28)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Craig",lname="Smith",position="Center",team=28)
session.add(players)
session.commit()
	
players = Players(number="6",fname="Shea",lname="Weber",position="Defenseman",team=28)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Colin",lname="Wilson",position="Center",team=28)
session.add(players)
session.commit()
	

#STL29
players = Players(number="34",fname="Jake",lname="Allen",position="Goaltender",team=29)
session.add(players)
session.commit()
	
players = Players(number="42",fname="David",lname="Backes",position="Center/Right Wing",team=29)
session.add(players)
session.commit()
	
players = Players(number="21",fname="Patrik",lname="Berglund",position="Center",team=29)
session.add(players)
session.commit()
	
players = Players(number="41",fname="Robert",lname="Bortuzzo",position="Defenseman",team=29)
session.add(players)
session.commit()
	
players = Players(number="19",fname="Jay",lname="Bouwmeester",position="Defenseman",team=29)
session.add(players)
session.commit()
	
players = Players(number="28",fname="Kyle",lname="Brodziak",position="Center",team=29)
session.add(players)
session.commit()
	
players = Players(number="36",fname="Troy",lname="Brouwer",position="Right Wing",team=29)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Chris",lname="Butler",position="Defenseman",team=29)
session.add(players)
session.commit()
	
players = Players(number="1",fname="Brian",lname="Elliott",position="Goaltender",team=29)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Carl",lname="Gunnarsson",position="Defenseman",team=29)
session.add(players)
session.commit()
	
players = Players(number="23",fname="Dmitrij",lname="Jaskin",position="Right Wing",team=29)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Jori",lname="Lehtera",position="Center",team=29)
session.add(players)
session.commit()
	
players = Players(number="9",fname="Steve",lname="Ott",position="Center",team=29)
session.add(players)
session.commit()
	
players = Players(number="56",fname="Magnus",lname="Paajarvi",position="Left Wing",team=29)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Alex",lname="Pietrangelo",position="Defenseman",team=29)
session.add(players)
session.commit()
	
players = Players(number="75",fname="Ryan",lname="Reaves",position="Right Wing",team=29)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Jaden",lname="Schwartz",position="Left Wing",team=29)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Kevin",lname="Shattenkirk",position="Defenseman",team=29)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Paul",lname="Stastny",position="Center",team=29)
session.add(players)
session.commit()
	
players = Players(number="20",fname="Alexander",lname="Steen",position="Left Wing",team=29)
session.add(players)
session.commit()
	
players = Players(number="91",fname="Vladimir",lname="Tarasenko",position="Right Wing",team=29)
session.add(players)
session.commit()
	

#WPG30
players = Players(number="6",fname="Alexander",lname="Burmistrov",position="Center",team=30)
session.add(players)
session.commit()
	
players = Players(number="33",fname="Dustin",lname="Byfuglien",position="D/Right Wing",team=30)
session.add(players)
session.commit()
	
players = Players(number="7",fname="Ben",lname="Chiarot",position="Defenseman",team=30)
session.add(players)
session.commit()
	
players = Players(number="24",fname="Grant",lname="Clitsome",position="Defenseman",team=30)
session.add(players)
session.commit()
	
players = Players(number="51",fname="Andrew",lname="Copp",position="Center",team=30)
session.add(players)
session.commit()
	
players = Players(number="42",fname="Nikolaj",lname="Ehlers",position="Left Wing",team=30)
session.add(players)
session.commit()
	
players = Players(number="39",fname="Tobias",lname="Enstrom",position="Defenseman",team=30)
session.add(players)
session.commit()
	
players = Players(number="25",fname="Matt",lname="Fraser",position="Right Wing",team=30)
session.add(players)
session.commit()
	
players = Players(number="15",fname="Matt",lname="Halischuk",position="Right Wing",team=30)
session.add(players)
session.commit()
	
players = Players(number="23",fname="Jay",lname="Harrison",position="Defenseman",team=30)
session.add(players)
session.commit()
	
players = Players(number="30",fname="Connor",lname="Hellebuyck",position="Goaltender",team=30)
session.add(players)
session.commit()
	
players = Players(number="34",fname="Michael",lname="Hutchinson",position="Goaltender",team=30)
session.add(players)
session.commit()
	
players = Players(number="16",fname="Andrew",lname="Ladd",position="Left Wing",team=30)
session.add(players)
session.commit()
	
players = Players(number="18",fname="Bryan",lname="Little",position="Center",team=30)
session.add(players)
session.commit()
	
players = Players(number="17",fname="Adam",lname="Lowry",position="Center",team=30)
session.add(players)
session.commit()
	
players = Players(number="27",fname="Andrew",lname="MacWilliam",position="Defenseman",team=30)
session.add(players)
session.commit()
	
players = Players(number="57",fname="Tyler",lname="Myers",position="Defenseman",team=30)
session.add(players)
session.commit()
	
players = Players(number="2",fname="Adam",lname="Pardy",position="Defenseman",team=30)
session.add(players)
session.commit()
	
players = Players(number="31",fname="Ondrej",lname="Pavelec",position="Goaltender",team=30)
session.add(players)
session.commit()
	
players = Players(number="14",fname="Anthony",lname="Peluso",position="Right Wing",team=30)
session.add(players)
session.commit()
	
players = Players(number="85",fname="Mathieu",lname="Perreault",position="Left Wing",team=30)
session.add(players)
session.commit()
	
players = Players(number="4",fname="Paul",lname="Postma",position="Defenseman",team=30)
session.add(players)
session.commit()
	
players = Players(number="55",fname="Mark",lname="Scheifele",position="Center",team=30)
session.add(players)
session.commit()
	
players = Players(number="12",fname="Drew",lname="Stafford",position="Right Wing",team=30)
session.add(players)
session.commit()
	
players = Players(number="5",fname="Mark",lname="Stuart",position="Defenseman",team=30)
session.add(players)
session.commit()
	
players = Players(number="22",fname="Chris",lname="Thorburn",position="Right Wing",team=30)
session.add(players)
session.commit()
	
players = Players(number="8",fname="Jacob",lname="Trouba",position="Defenseman",team=30)
session.add(players)
session.commit()
	
players = Players(number="26",fname="Blake",lname="Wheeler",position="Right Wing",team=30)
session.add(players)
session.commit()
	





print "added teams and players!"
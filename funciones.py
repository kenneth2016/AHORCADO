import random

def palabras (l1):
	l1 = [
	"de",
	"la",
	"que",
	"el",
	"en",
	"pastel",
	"avion",
	"los",
	"se",
	"del",
	"las",
	"un",
	"por",
	"con",
	"no",
	"una",
	"su",
	"para",
	"es",
	"al",
	"lo",
	"como",
	"mas",
	"o",
	"pero",
	"sus",
	"le",
	"ha",
	"me",
	"si",
	"sin",
	"sobre",
	"este",
	"ya",
	"entre",
	"cuando",
	"todo",
	"esta",
	"ser",
	"son",
	"dos",
	"tambien",
	"fue",
	"habia",
	"era",
	"muy",
	"anos",
	"hasta",
	"desde",
	"esta",
	"mi",
	"porque",
	"que",
	"solo",
	"han",
	"yo",
	"hay",
	"vez",
	"puede",
	"todos",
	"asi",
	"nos",
	"ni",
	"parte",
	"tiene",
	"el",
	"uno",
	"donde",
	"bien",
	"tiempo",
	"mismo",
	"ese",
	"ahora",
	"cada",
	"e",
	"vida",
	"otro",
	"despues",
	"te",
	"otros",
	"aunque",
	"esa",
	"eso",
	"hace",
	"otra",
	"gobierno",
	"tan",
	"durante",
	"siempre",
	"dia",
	"tanto",
	"ella",
	"tres",
	"si",
	"dijo",
	"sido",
	"gran",
	"pais",
	"segun",
	"menos",
	"mundo",
	"ano",
	"antes",
	"estado",
	"contra",
	"sino",
	"forma",
	"caso",
	"nada",
	"hacer",
	"general",
	"estaba",
	"poco",
	"estos",
	"presidente",
	"mayor",
	"ante",
	"unos",
	"les",
	"algo",
	"hacia",
	"casa",
	"ellos",
	"ayer",
	"hecho",
	"primera",
	"mucho",
	"mientras",
	"ademas",
	"quien",
	"momento",
	"millones",
	"esto",
	"espana",
	"hombre",
	"estan",
	"pues",
	"hoy",
	"lugar",
	"madrid",
	"nacional",
	"trabajo",
	"otras",
	"mejor",
	"nuevo",
	"decir",
	"algunos",
	"entonces",
	"todas",
	"dias",
	"debe",
	"politica",
	"como",
	"casi",
	"toda",
	"tal",
	"luego",
	"pasado",
	"primer",
	"medio",
	"va",
	"estas",
	"sea",
	"tenia",
	"nunca",
	"poder",
	"aqui",
	"ver",
	"veces",
	"embargo",
	"partido",
	"personas",
	"grupo",
	"cuenta",
	"pueden",
	"tienen",
	"misma",
	"nueva",
	"cual",
	"fueron",
	"mujer",
	"frente",
	"jose",
	"tras",
	"cosas",
	"fin",
	"ciudad",
	"he",
	"social",
	"manera",
	"tener",
	"sistema",
	"sera",
	"historia",
	"muchos",
	"juan",
	"tipo",
	"cuatro",
	"dentro",
	"nuestro",
	"punto",
	"dice",
	"ello",
	"cualquier",
	"noche",
	"aun",
	"agua",
	"parece",
	"haber",
	"situacion",
	"fuera",
	"bajo",
	"grandes",
	"nuestra",
	"ejemplo",
	"acuerdo",
	"habian",
	"usted",
	"estados",
	"hizo",
	"nadie",
	"paises",
	"horas",
	"posible",
	"tarde",
	"ley",
	"importante",
	"guerra",
	"desarrollo",
	"proceso",
	"realidad",
	"sentido",
	"lado",
	"mi",
	"tu",
	"cambio",
	"alli",
	"mano",
	"eran",
	"estar",
	"san",
	"numero",
	"sociedad",
	"unas",
	"centro",
	"padre",
	"gente",
	"final",
	"relacion",
	"cuerpo",
	"obra",
	"incluso",
	"traves",
	"ultimo",
	"madre",
	"mis",
	"modo",
	"problemas",
	"cinco",
	"carlos",
	"hombres",
	"informacion",
	"ojos",
	"muerte",
	"nombre",
	"algunas",
	"publico",
	"mujeres",
	"siglo",
	"todavia",
	"meses",
	"manana",
	"esos",
	"nosotros",
	"hora",
	"muchas",
	"pueblo",
	"alguna",
	"dar",
	"problema",
	"don",
	"da",
	"tu",
	"derecho",
	"verdad",
	"maria",
	"unidos",
	"podria",
	"seria",
	"junto",
	"cabeza",
	"aquel",
	"luis",
	"cuanto",
	"tierra",
	"equipo",
	"segundo",
	"director",
	"dicho",
	"cierto",
	"casos",
	"manos",
	"nivel",
	"podia",
	"familia",
	"largo",
	"partir",
	"falta",
	"llegar",
	"propio",
	"ministro",
	"cosa",
	"primero",
	"seguridad",
	"hemos",
	"mal",
	"trata",
	"algun",
	"tuvo",
	"respecto",
	"semana",
	"varios",
	"real",
	"se",
	"voz",
	"paso",
	"senor",
	"mil",
	"quienes",
	"proyecto",
	"mercado",
	"mayoria",
	"luz",
	"claro",
	"iba",
	"este",
	"pesetas",
	"orden",
	"espanol",
	"buena",
	"quiere",
	"aquella",
	"programa",
	"palabras",
	"internacional",
	"van",
	"esas",
	"segunda",
	"empresa",
	"puesto",
	"ahi",
	"propia",
	"marido",
	"libro",
	"igual",
	"politico",
	"persona",
	"ultimos",
	"ellas",
	"total",
	"creo",
	"tengo",
	"dios",
	"castillo",
	"espanola",
	"condiciones",
	"mexico",
	"fuerza",
	"solo",
	"unico",
	"accion",
	"amor",
	"policia",
	"puerta",
	"pesar",
	"zona",
	"sabe",
	"calle",
	"interior",
	"tampoco",
	"musica",
	"ningun",
	"vista",
	"campo",
	"buen",
	"hubiera",
	"saber",
	"obras",
	"razon",
	"extenso",
	"ninos",
	"presencia",
	"tema",
	"dinero",
	"comision",
	"antonio",
	"servicio",
	"hijo",
	"ultima",
	"ciento",
	"estoy",
	"hablar",
	"dio",
	"minutos",
	"produccion",
	"camino",
	"seis",
	"quien",
	"fondo",
	"direccion",
	"papel",
	"demas",
	"barcelona",
	"idea",
	"especial",
	"diferentes",
	"dado",
	"base",
	"capital",
	"ambos",
	"europa",
	"libertad",
	"relaciones",
	"espacio",
	"medios",
	"ir",
	"actual",
	"poblacion",
	"empresas",
	"estudio",
	"salud",
	"servicios",
	"haya",
	"principio",
	"siendo",
	"cultura",
	"anterior",
	"alto",
	"media",
	"mediante",
	"primeros",
	"arte",
	"paz",
	"sector",
	"imagen",
	"medida",
	"deben",
	"datos",
	"consejo",
	"personal",
	"interes",
	"julio",
	"grupos",
	"miembros",
	"ninguna",
	"existe",
	"cara",
	"edad",
	"elefante",
	"movimiento",
	"visto",
	"llego",
	"puntos",
	"actividad",
	"bueno",
	"uso",
	"nino",
	"dificil",
	"joven",
	"futuro",
	"aquellos",
	"mes",
	"pronto",
	"soy",
	"hacia",
	"nuevos",
	"nuestros",
	"estaban",
	"posibilidad",
	"sigue",
	"cerca",
	"resultados",
	"educacion",
	"atencion",
	"gonzalez",
	"capacidad",
	"efecto",
	"necesario",
	"valor",
	"aire",
	"investigacion",
	"siguiente",
	"figura",
	"central",
	"comunidad",
	"necesidad",
	"serie",
	"organizacion",
	"nuevas",
	"calidad"
	]
	random.shuffle(l1)
	return l1[0]

def mezclar (l1):
	random.shuffle(l1)
	return l1[0]
 # _ _ _ _ _
 #|        |
 #|       ( ) 
 #|       _|_
 #|        |
 #|       / \
 #|


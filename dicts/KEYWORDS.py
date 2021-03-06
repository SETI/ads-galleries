########################################################################################################################
# dicts/KEYWORDS.py
#
# To use:
#   from KEYWORDS import KEYWORDS
#
# Dictionary strcuture used for scraping keywords from captions. Each dictionary value is a list of tuples
#   (regular expression, [keywords])
# where the list of keywords can contain grep string replacement patterns. If the regular expression matches any text
# found in the caption, then the keywords provided are added to the list.
#
# Keywords can have suffixes indicating the type of the keyword:
#   +t = Target
#   +T = Target Type
#   +s = System
#   +m = Mission
#   +h = Host
#   +H = Host Type
#   +i = Instrument
#   +d = Detector
#
# KEYWORDS is actually a dictionary keyed by a category. KEYWORDS['General'] is the list of keywords always searched.
# Additional keys are used if and only if the key of that dictionary is also found as a keyword. For example, if
# 'Saturn' is found among the keywords, then KEYWORDS['Saturn'] is also checked for matching text in the caption.
#
# This dictionary will need to be updated as new data sets are added to the gallery.
########################################################################################################################

KEYWORDS = {}

KEYWORDS['General'] = [

# Target categories
    ('[Aa]steroids{0,1}',                              ['Asteroid+T', 'Asteroid Belt+s']),
    ('[Cc]omets{0,1}',                                 ['Comet+T']),
    ('KBOs{0,1}',                                      ['TNO+T', 'Kuiper Belt+s']),
    ('Kuiper Belt',                                    ['TNO+T', 'Kuiper Belt+s']),
    ('(Trans-Neptunian|TNO|TNOs)',                     ['TNO+T', 'Kuiper Belt+s']),

# Target names
    ('([Ss]un)',                                       ['Sun+t+T']),
    ('(Mercury|Mercurian)',                            ['Mercury+t', 'Planet+T']),
    ('(Venus|Venusian)',                               ['Venus+t', 'Planet+T']),
    ('([Ee]arth|[Tt]errestrial)',                      ['Earth+t+s', 'Earth+s+T']),
    ('Moon(?!s)',                                      ['Moon+t', 'Satellite+T', 'Earth+s']),
    ('(Mars(?![a-z])|Martian)',                        ['Mars+t+s', 'Planet+T']),
    ('(Jupiter|[Jj]ovian)',                            ['Jupiter+t+s', 'Planet+T']),
    ('Io(?![a-z])',                                    ['Io+t', 'Jupiter+s', 'Satellite+T']),
    ('Europa',                                         ['Europa+t', 'Jupiter+s', 'Satellite+T']),
    ('Ganymede',                                       ['Ganymede+t', 'Jupiter+s', 'Satellite+T']),
    ('Callisto',                                       ['Callisto+t', 'Jupiter+s', 'Satellite+T']),
    ('Galilean',                                       ['Jupiter+t+s', 'Planet+T']),
    ('(Saturn|[Ss]aturnian|Kronian)',                  ['Saturn+t+s', 'Planet+T']),
    ('Titan(?![a-z])(?!/Cen)(?! IV)',                  ['Titan+t', 'Saturn+s', 'Satellite+T']),
    ('Enceladus',                                      ['Enceladus+t', 'Saturn+s', 'Satellite+T']),
    ('(Uranus|Uranian)',                               ['Uranus+t+s', 'Planet+T']),
    ('(Neptune|Neptunian)',                            ['Neptune+t+s', 'Planet+T']),
    ('Triton',                                         ['Triton+t', 'Neptune+s', 'Satellite+T']),
    ('(Pluto|Plutonian|Charon)',                       ['Pluto+t', 'Dwarf Planet+T']),
    ('Ceres',                                          ['1 Ceres+t', 'Asteroid+T', 'Dwarf Planet+T', 'Asteroid Belt+s']),
    ('Pallas',                                         ['2 Pallas+t', 'Asteroid+T', 'Asteroid Belt+s']),
    ('Vesta',                                          ['4 Vesta+t', 'Asteroid+T', 'Asteroid Belt+s']),
    ('Gaspra',                                         ['951 Gaspra+t', 'Asteroid+T', 'Asteroid Belt+s']),
    ('Lutetia',                                        ['21 Lutetia+t', 'Asteroid+T', 'Asteroid Belt+s']),
    ('Steins',                                         ['2867 Steins+t', 'Asteroid+T', 'Asteroid Belt+s']),
    ('Mathilde',                                       ['253 Mathilde+t', 'Asteroid+T', 'Asteroid Belt+s']),
    ('Toutatis',                                       ['4179 Toutatis+t', 'Asteroid+T', 'Asteroid Belt+s']),
    ('(MU69|Ultima(?![a-z]))',                         ['Ultima Thule+t', 'TNO+T', 'New Horizons+m', 'Kuiper Belt+s']),
    ('Haumea',                                         ['136108 Haumea+t', 'TNO+T', 'Dwarf Planet+T', 'Kuiper Belt+s']),
    ('Makemake',                                       ['136472 Makemake+t', 'TNO+T', 'Dwarf Planet+T', 'Kuiper Belt+s']),
    ('Eris',                                           ['136199 Eris+t', 'TNO+T', 'Dwarf Planet+T', 'Kuiper Belt+s']),

# Missions and Instruments
    ('[Ii]nfra(|-)red|IR',                              ['Infrared']),
    ('[Uu]ltra(|-)violet|UV|FUV',                       ['Ultraviolet']),
    ('[Rr]adio(?![a-z])',                               ['Radio']),
    ('RADAR',                                           ['RADAR+i']),
    ('(HST|Hubble.*[Tt]elescope)',                      ['Hubble Space Telescope (HST)+m+h', 'Orbiting Telescope+H']),
    ('(JWST|Webb.*[Tt]elescope)',                       ['James Webb Space Telscope (JWST)+m+h', 'Orbiting Telescope+H']),
    ('(Voyager)',                                       ['$+m', 'Flyby Spacecraft+H']),
    ('(Mariner)(?!is)',                                 ['$+m', 'Flyby Spacecraft+H']),
    ('Pioneer Venus',                                   ['Pioneer Venus+m+h', 'Venus+t+s', 'Planet+T']),
    ('(Pioneer [1-9][0-9]*)',                           ['Pioneer+m', '$+h', 'Flyby Spacecraft+H']),
    ('Probe.*Galileo',                                  ['Galileo+m', r'Galileo Probe+h', 'Jupiter+t+s', 'Probe+H']),
    ('Galileo.*Probe',                                  ['Galileo+m', r'Galileo Probe+h', 'Jupiter+t+s', 'Probe+H']),
    ('Jup.*Galileo',                                    ['Galileo+m', r'Galileo Orbiter+h', 'Jupiter+s', 'Probe+H']),
    ('Galileo.*Jup',                                    ['Galileo+m', r'Galileo Orbiter+h', 'Jupiter+s', 'Orbiter+H']),
    ('Cassini(?! [Dd]ivision)',                         ['Cassini Orbiter+h', 'Cassini-Huygens+m']),   # don't match "Cassini Division"
    ('New Horizons',                                    ['New Horizons+m+h', 'Flyby Spacecraft+H']),
    ('Juno',                                            ['Juno+m+h', 'Jupiter+s', 'Planet+T', 'Orbiter+H']),
    ('Venus.*Magellan',                                 ['Magellan+m', 'Venus+t+s', 'Planet+T', 'Orbiter+H']),
    ('Magellan.*Venus',                                 ['Magellan+m', 'Venus+t+s', 'Planet+T']),
    ('MESSENGER.',                                      ['MESSENGER+m', 'Mercury+t+s', 'Planet+T', 'Orbiter+H']),
    ('Messenger.*Mercury',                              ['MESSENGER+m', 'Mercury+t+s', 'Planet+T', 'Orbiter+H']),
    ('Mercury.*Messenger',                              ['MESSENGER+m', 'Mercury+t+s', 'Planet+T', 'Orbiter+H']),
    ('Dawn.*(Ceres|Vesta)',                             ['Dawn+m+h', 'Asteroid+T', 'Orbiter+H']),
    ('(Ceres|Vesta).*Dawn',                             ['Dawn+m+h', 'Asteroid+T', 'Orbiter+H']),
    ('(Rosetta)',                                       ['Rosetta+m+h', '67P/Churyumov-Gerasimenko+t', 'Comet+T', 'Orbiter+H']),
    ('(Philae)',                                        ['Rosetta+m', '67P/Churyumov-Gerasimenko+t', 'Comet+T', 'Philae Lander+h', 'Lander+H']),
    ('(?:Voyager|Pioneer|Mariner) (?:[1-9][0-9]*)',     ['$+h', 'Flyby Spacecraft+H']),
    ('MAVEN',                                           ['Mars Atmosphere and Volatile Evolution (MAVEN)+m+h', 'Mars+t', 'Planet+T', 'Orbiter+H']),
    ('Mars Atmosphere and Volatile Evolution',          ['Mars Atmosphere and Volatile Evolution (MAVEN)+m+h', 'Mars+t', 'Planet+T', 'Orbiter+H']),
    ('Viking',                                          ['Viking+m', 'Mars+t+s', 'Planet+T']),
    ('(Viking [12]).*[Oo]rbit',                         ['$ Orbiter+h', 'Orbiter+H']),
    ('(Viking [12]).*[Ll]ander',                        ['$ Lander+h', 'Lander+H']),
    ('(MGS|Mars Global Surveyor)',                      ['Mars Global Surveyor (MGS)+m+h', 'Mars+t+s', 'Planet+T', 'Orbiter+H']),
    ('Mars Odyssey',                                    ['2001 Mars Odyssey+m', 'Mars+t', 'Planet+T', 'Orbiter+H']),
    ('Mars Express|MEX',                                ['Mars Express+m+h', 'Mars+t', 'Planet+T']),
    ('Phoenix',                                         ['Phoenix+m', 'Phoenix Mars Lander+h', 'Mars+t', 'Planet+T', 'Lander+H']),
    ('(MOC|Mars Orbiter Camera)',                       ['Mars Orbiter Camera (MOC)+i', 'Mars Global Surveyor (MGS)+m+h', 'Mars+t+s', 'Planet+T']),
    ('(MSL|Mars [Ss]cience [Ll]aboratory)',             ['Mars Science Laboratory (MSL)+m', 'Curiosity Rover+h', 'Mars+t+s', 'Planet+T', 'Rover+H']),
    ('Curiosity.*Mars',                                 ['Mars Science Laboratory (MSL)+m', 'Curiosity Rover+h', 'Mars+t+s', 'Planet+T', 'Rover+H']),
    ('Mars .*Curiosity',                                ['Mars Science Laboratory (MSL)+m', 'Curiosity Rover+h', 'Mars+t+s', 'Planet+T', 'Rover+H']),
    ('(MRO|Mars [Rr]econnaissance [Oo]rbiter)',         ['Mars Reconnaissance Orbiter (MRO)+m+h,', 'Mars+t+s', 'Planet+T', 'Orbiter+H']),
    ('(MER|Opportunity|Spirit|Mars [Ee]xploration [Rr]over)',
                                                        ['Mars Exploration Rover (MER)+m', 'Mars+t', 'Planet+T', 'Rover+H']),
    ('MER-A',                                           ['Spirit (MER-A)+h', 'Rover+H']),
    ('MER-B',                                           ['Opportunity (MER-B)+h', 'Rover+H']),
    ('(Mars [Ee]xpress|Beagle)',                        ['Mars Express+m', 'Mars+t', 'Planet+T']),
    ('Mars [Pp]athfinder',                              ['Mars Pathfinder (MPF)+m', 'Mars+t', 'Planet+T']),
    ('Mars [Pp]athfinder.*Lander',                      ['Mars Pathfinder Lander+h', 'Lander+H']),
    ('Mars [Pp]athfinder.*Rover',                       ['Mars Pathfinder Rover+h', 'Rover+H']),
    ('Mar(s|tian).*[Rr]over',                           ['Mars+t+s', 'Planet+T', 'Rover+H']),
    ('[Rr]over.*Mar(s|tian)',                           ['Mars+t+s', 'Planet+T', 'Rover+H']),
    ('Mar(s|tian).*[Ll]ander',                          ['Mars+t+s', 'Planet+T', 'Lander+H']),
    ('[Ll]ander.*Mar(s|tian)',                          ['Mars+t+s', 'Planet+T', 'Lander+H']),
    ('(NEAR|Near Earth Asteroid Rendezvous)',           ['NEAR Shoemaker+m', '433 Eros+t', 'Asteroid+T', 'Orbiter+H']),
    (r"Chang'e",                                        ["Chang'e+m", "Moon+t", "Satellite+T", "Earth+s"]),
    ('Deep Impact',                                     ['Deep Impact+m+h', '9P/Tempel+t', 'Comet+T', 'Probe+H']),

# Other general keywords
    ('[Ww]ater',                                        ['Water']),
    ('[Mm]ethane',                                      ['Methane']),
    ('[Aa]mmonia',                                      ['Ammonia']),
    ('[Cc]rater',                                       ['Crater']),
    ('([Mm]ountains{0,1}|Mons|Montes)',                 ['Mountain']),
    ('[Dd]ust',                                         ['Dust']),
    ('[Dd]une',                                         ['Dune']),
    ('[Hh]az(y|e)',                                     ['Haze', 'Atmosphere']),
    ('[Aa]tmospher(e|es|ic)',                           ['Atmosphere']),
    ('[Pp]lume',                                        ['Plume']),
    ('[Vv]olcan(o|os|oes|ism|ic)',                      ['Volcano']),
    ('([Ss]torms{0,1}|[Rr]ed [Ss]pot|[Dd]ark [Ss]pot)', ['Storm', 'Atmosphere']),
    ('[Ss]hadow',                                       ['Shadow']),
    ('[Oo]ccultation',                                  ['Occultation']),
    ('[Ee]clipse',                                      ['Eclipse']),
    ('[Mm]agnet(ism|ic|osphere)',                       ['Magnetosphere']),
    ('[Mm]ap(?![a-z])',                                 ['Map']),
    ('[Aa]rtist',                                       ['Artwork']),
    ('[Aa]rtwork',                                      ['Artwork']),
]

# Keywords to search for if 'Mars' appears
KEYWORDS['Mars'] = [
    ('Spirit',                                          ['Spirit (MER-A)+h', 'Rover+H']),
    ('Opportunity',                                     ['Opportunity (MER-B)+h', 'Rover+H']),
    ('CRISM',                                           ['Compact Reconnaissance Imaging Spectrometer for Mars (CRISM)+i']),
    ('OMEGA',                                           ['Visible and Infrared Mineralogical Mapping Spectrometer (OMEGA)+i']),
    ('(Mars Global Surveyor|MGS).*thermal emission spectrometer',
                                                        ['Thermal Emission Spectrometer (TES)+i']),
]

# Keywords to search for if 'Jupiter' appears
KEYWORDS['Jupiter'] = [
    ('Galileo',                                         ['Galileo+m']),
    ('Jovian.{0,10} [Rr]ing',                           ['Jupiter Rings+t', 'Ring+T']),
    ('Jupiter.{0,20} [Rr]ing',                          ['Jupiter Rings+t', 'Ring+T']),
    (' [Rr]ing.{0,10}Jupiter',                          ['Jupiter Rings+t', 'Ring+T']),
    ('[Mm]ain [Rr]ings{0,1}',                           ['Main Ring+t', 'Jupiter Rings+t', 'Ring+T']),
    (' [Rr]ings{0,1} .*[Hh]alo',                        ['Halo+t', 'Jupiter Rings+t', 'Ring+T']),
    ('[Hh]alo .*[Rr]ings{0,1}',                         ['Halo+t', 'Jupiter Rings+t', 'Ring+T']),
    ('[Gg]ossamer',                                     ['Gossamer Ring+t', 'Jupiter Rings+t', 'Ring+T']),
    ('(Adrastea)',                                      ['$+t', 'Satellite+T']),
    ('(Metis)',                                         ['$+t', 'Satellite+T']),
    ('(Amalthea)',                                      ['$+t', 'Satellite+T']),
    ('(Thebe)',                                         ['$+t', 'Satellite+T']),
    ('Io(?![a-z])',                                     ['Io+t', 'Satellite+T']),
    ('(Europa)',                                        ['$+t', 'Satellite+T']),
    ('(Ganymede)',                                      ['$+t', 'Satellite+T']),
    ('(Callisto)',                                      ['$+t', 'Satellite+T']),
    ('(Themisto)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Leda)',                                          ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Himalia)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Lysithea)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Elara)',                                         ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Dia)(?![a-z])',                                  ['Dia+t', 'Satellite+T', 'Irregular+T']),
    ('(Carpo)',                                         ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Euporie)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Thelxinoe)',                                     ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Euanthe)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Helike)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Orthosie)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Iocaste)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Praxidike)',                                     ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Harpalyke)',                                     ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Mneme)',                                         ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Hermippe)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Thyone)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Ananke)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Herse)',                                         ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Aitne)',                                         ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Kale)',                                          ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Taygete)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Chaldene)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Erinome)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Aoede)',                                         ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Kallichore)',                                    ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Kalyke)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Carme)',                                         ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Callirrhoe)',                                    ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Eurydome)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Pasithee)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Kore)',                                          ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Cyllene)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Eukelade)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Pasiphae)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Hegemone)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Arche)',                                         ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Isonoe)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Sinope)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Sponde)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Autonoe)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Megaclite)',                                     ['$+t', 'Satellite+T', 'Irregular+T']),
    ('S/20[0-9][0-9] *J *[1-9][0-9]*',                  ['$+t', 'Satellite+T', 'Irregular+T']),
]

# Keywords to search for if 'Saturn' appears
KEYWORDS['Saturn'] = [
    ('(?<!Cassini-)Huygens',                            ['Huygens Probe+h', 'Cassini-Huygens+m', 'Lander+H']), # not if it says "Cassini-Huygens"
    ('(?<!imas |adus |thys |ione |Rhea |itan |rion |etus |oebe )Atlas',
                                                        ['Atlas+t', 'Satellite+T']),
    ('Saturn.{0,20} [Rr]ing',                           ['Saturn Rings+t', 'Ring+T']),
    (' [Rr]ing.{0,10}Saturn',                           ['Saturn Rings+t', 'Ring+T']),
    (' ([A-G])[- ][Rr]ing',                             ['$ Ring+t', 'Saturn Rings+t', 'Ring+T']),
    (' ([A-G])-{0,1},{0,1} and [A-G][- ][Rr]ings',      ['$ Ring+t', 'Saturn Rings+t', 'Ring+T']),
    (' [A-G]-{0,1},{0,1} and ([A-G])[- ][Rr]ings',      ['$ Ring+t', 'Saturn Rings+t', 'Ring+T']),
    (' ([A-G])-{0,1}, [A-G].{0,20} [A-G][- ][Rr]ings',  ['$ Ring+t', 'Saturn Rings+t', 'Ring+T']),
    ('Cassini [Dd]ivision',                             ['Cassini Division+t', 'Saturn Rings+t', 'Ring+T', 'Gap+T']),
    ('Encke ([Dd]ivision|[Gg]ap)',                      ['Encke Gap+t', 'Saturn Rings+t', 'Ring+T', 'Gap+T']),
    ('(Pan)(?![a-z])',                                  ['$+t', 'Satellite+T']),
    ('(Daphnis)',                                       ['$+t', 'Satellite+T']),
    ('(Prometheus)',                                    ['$+t', 'Satellite+T']),
    ('(Pandora)',                                       ['$+t', 'Satellite+T']),
    ('(Epimetheus)',                                    ['$+t', 'Satellite+T']),
    ('(Janus)',                                         ['$+t', 'Satellite+T']),
    ('(Aegaeon)',                                       ['$+t', 'Satellite+T']),
    ('(Methone)',                                       ['$+t', 'Satellite+T']),
    ('(Anthe)',                                         ['$+t', 'Satellite+T']),
    ('(Pallene)',                                       ['$+t', 'Satellite+T']),
    ('(Telesto)',                                       ['$+t', 'Satellite+T']),
    ('(Calypso)',                                       ['$+t', 'Satellite+T']),
    ('(Dione)',                                         ['$+t', 'Satellite+T']),
    ('(Helene)',                                        ['$+t', 'Satellite+T']),
    ('(Polydeuces)',                                    ['$+t', 'Satellite+T']),
    ('(Mimas)',                                         ['$+t', 'Satellite+T']),
    ('(Enceladus)',                                     ['$+t', 'Satellite+T']),
    ('(Tethys)',                                        ['$+t', 'Satellite+T']),
    ('(Dione)',                                         ['$+t', 'Satellite+T']),
    ('(Rhea)',                                          ['$+t', 'Satellite+T']),
    ('(Titan)',                                         ['$+t', 'Satellite+T']),
    ('(Hyperion)',                                      ['$+t', 'Satellite+T']),
    ('(Iapetus)',                                       ['$+t', 'Satellite+T']),
    ('(Phoebe)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Kiviuq)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Ijiraq)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Paaliaq)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Skathi)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Albiorix)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Bebhionn)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Erriapus)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Skoll)',                                         ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Siarnaq)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Tarqeq)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Greip)',                                         ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Hyrrokkin)',                                     ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Jarnsaxa)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Tarvos)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Mundilfari)',                                    ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Bergelmir)',                                     ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Narvi)',                                         ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Suttungr)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Hati)',                                          ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Farbauti)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Thrymr)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Aegir)',                                         ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Bestla)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Fenrir)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Surtur)',                                        ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Kari)',                                          ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Ymir)',                                          ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Loge)',                                          ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Fornjot)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('S/2004 *S *1',                                    ['Methone+t', 'Satellite+T']),
    ('S/2004 *S *2',                                    ['Pallene+t', 'Satellite+T']),
    ('S/2004 *S *5',                                    ['Polydeuces+t', 'Satellite+T']),
    ('S/2004 *S *([36])',                               ['F Ring+t', 'Moonlet', 'Clump']),
    ('S/2005 *S *1',                                    ['Daphnis+t', 'Satellite+T']),
    ('S/2007 *S *4',                                    ['Anthe+t', 'Satellite+T']),
    ('S/2008 *S *1',                                    ['Aegaeon+t', 'Satellite+T']),
]

# Keywords to search for if 'Uranus' appears
KEYWORDS['Uranus'] = [
    ('Uranian.{0,10} [Rr]ing',                          ['Uranus Rings+t', 'Ring+T']),
    ('Uranus.{0,20} [Rr]ing',                           ['Uranus Rings+t', 'Ring+T']),
    (' [Rr]ing.{0,10}Uranus',                           ['Uranus Rings+t', 'Ring+T']),
    (' [Zz]eta(, | | .{0,20} )[Rr]ings{0,1}',           ['Zeta Ring+t', 'Uranus Rings+t', 'Ring+T']),
    (' (6|six|Six)(, | | .{0,20} )[Rr]ings{0,1}',       ['Six Ring+t', 'Uranus Rings+t', 'Ring+T']),
    (' (5|five|Five)(, | | .{0,20} )[Rr]ings{0,1}',     ['Five Ring+t', 'Uranus Rings+t', 'Ring+T']),
    (' (4|four|Four)(, | | .{0,20} )[Rr]ings{0,1}',     ['Four Ring+t', 'Uranus Rings+t', 'Ring+T']),
    (' [Aa]lpha(, | | .{0,20} )[Rr]ings{0,1}',          ['Alpha Ring+t', 'Uranus Rings+t', 'Ring+T']),
    (' [Bb]eta(, | | .{0,20} )[Rr]ings{0,1}',           ['Beta Ring+t', 'Uranus Rings+t', 'Ring+T']),
    (' [Ee]ta(, | | .{0,20} )[Rr]ings{0,1}',            ['Eta Ring+t', 'Uranus Rings+t', 'Ring+T']),
    (' [Gg]amma(, | | .{0,20} )[Rr]ings{0,1}',          ['Gamma Ring+t', 'Uranus Rings+t', 'Ring+T']),
    (' [Dd]elta(, | | .{0,20} )[Rr]ings{0,1}',          ['Delta Ring+t', 'Uranus Rings+t', 'Ring+T']),
    (' [Ll]ambda(, | | .{0,20} )[Rr]ings{0,1}',         ['Lambda Ring+t', 'Uranus Rings+t', 'Ring+T']),
    (' [Ee]psilon(, | | .{0,20} )[Rr]ings{0,1}',        ['Epsilon Ring+t', 'Uranus Rings+t', 'Ring+T']),
    (' [Nn]u(, | | .{0,20} )[Rr]ings{0,1}',             ['Nu Ring+t', 'Uranus Rings+t', 'Ring+T']),
    (' [Mm]u(, | | .{0,20} )[Rr]ings{0,1}',             ['Mu Ring+t', 'Uranus Rings+t', 'Ring+T']),
    ('(Cordelia)',                                      ['$+t', 'Satellite+T']),
    ('(Ophelia)',                                       ['$+t', 'Satellite+T']),
    ('(Bianca)',                                        ['$+t', 'Satellite+T']),
    ('(Cressida)',                                      ['$+t', 'Satellite+T']),
    ('(Desdemona)',                                     ['$+t', 'Satellite+T']),
    ('(Juliet)',                                        ['$+t', 'Satellite+T']),
    ('(Portia)',                                        ['$+t', 'Satellite+T']),
    ('(Rosalind)',                                      ['$+t', 'Satellite+T']),
    ('(Cupid)',                                         ['$+t', 'Satellite+T']),
    ('(Belinda)',                                       ['$+t', 'Satellite+T']),
    ('(Perdita)',                                       ['$+t', 'Satellite+T']),
    ('(Puck)',                                          ['$+t', 'Satellite+T']),
    ('(Mab)',                                           ['$+t', 'Satellite+T']),
    ('(Miranda)',                                       ['$+t', 'Satellite+T']),
    ('(Ariel)',                                         ['$+t', 'Satellite+T']),
    ('(Umbriel)',                                       ['$+t', 'Satellite+T']),
    ('(Titania)',                                       ['$+t', 'Satellite+T']),
    ('(Oberon)',                                        ['$+t', 'Satellite+T']),
    ('(Francisco)',                                     ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Caliban)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Stephano)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Trinculo)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Sycorax)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Margaret)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Prospero)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Setebos)',                                       ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Ferdinand)',                                     ['$+t', 'Satellite+T', 'Irregular+T']),
]

# Keywords to search for if 'Neptune' appears
KEYWORDS['Neptune'] = [
    ('Neptun.{0,20} [Rr]ing',                           ['Neptune Rings+t', 'Ring+T']),
    (' [Rr]ing.{0,10}Neptune',                          ['Neptune Rings+t', 'Ring+T']),
    ('Adams .[Rr]ings{0,1}',                            ['Adams Ring+t', 'Neptune Rings+t', 'Ring+T']),
    ('Lassell',                                         ['Lassell Ring+t', 'Neptune Rings+t', 'Ring+T']),
    ('Le {0,1}[Vv]errier',                              ['Leverrier Ring+t', 'Neptune Rings+t', 'Ring+T']),
    ('Galle',                                           ['Galle Ring+t', 'Neptune Rings+t', 'Ring+T']),
    ('Libert[ye] .*[Aa]rcs{0,1}',                       ['Liberte+t', 'Adams Ring+t', 'Neptune Rings+t', 'Ring+T', 'Arc+T']),
    ('(Egalite|Equality) .*[Aa]rcs{0,1}',               ['Egalite+t', 'Adams Ring+t', 'Neptune Rings+t', 'Ring+T', 'Arc+T']),
    ('Fraternit[ye] .*[Aa]rcs{0,1}',                    ['Fraternite+t', 'Adams Ring+t', 'Neptune Rings+t', 'Ring+T', 'Arc+T']),
    ('Courage .*[Aa]rcs{0,1}',                          ['Courage+t', 'Adams Ring+t', 'Neptune Rings+t', 'Ring+T', 'Arc+T']),
    ('(Naiad)',                                         ['$+t', 'Satellite+T']),
    ('(Thalassa)',                                      ['$+t', 'Satellite+T']),
    ('(Despina)',                                       ['$+t', 'Satellite+T']),
    ('(Galatea)',                                       ['$+t', 'Satellite+T']),
    ('(Larissa)',                                       ['$+t', 'Satellite+T']),
    ('S/2004 *N *1',                                    ['S/2004 N 1+t', 'Satellite+T']),
    ('Proteus',                                         ['Proteus+t', 'Satellite+T']),
    ('Triton',                                          ['Triton+t', 'Satellite+T']),
    ('Nereid',                                          ['Nereid+t', 'Satellite+T', 'Irregular+T']),
    ('(Halimede)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Sao)',                                           ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Laomedeia)',                                     ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Psamathe)',                                      ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(Neso)',                                          ['$+t', 'Satellite+T', 'Irregular+T']),
    ('(|S/)1989 *N *1',                                 ['Proteus+t', 'Satellite+T']),
    ('(|S/)1989 *N *2',                                 ['Thalassa+t', 'Satellite+T']),
]

# Keywords to search for if 'Pluto' appears
KEYWORDS['Pluto'] = [
    ('(Charon)',                                        ['$+t', 'Satellite+T', 'Pluto+s']),
    ('(Styx)',                                          ['$+t', 'Satellite+T', 'Pluto+s']),
    ('(Nix)',                                           ['$+t', 'Satellite+T', 'Pluto+s']),
    ('(Kerberos)',                                      ['$+t', 'Satellite+T', 'Pluto+s']),
    ('(Hydra)',                                         ['$+t', 'Satellite+T', 'Pluto+s']),
]

# Keywords to search for if 'Comet' appears
KEYWORDS['Comet'] = [
    ('Borrelly',                                        ['19P/Borrelly+t', 'Periodic Comets+s']),
    ('Wild(?![a-z])',                                   ['81P/Wild+t', 'Periodic Comets+s']),
    ('Halley',                                          ['1P/Halley+t', 'Periodic Comets+s']),
    ('(Churyumov|Gerasimenko)',                         ['67P/Churyumov-Gerasimenko+t', 'Periodic Comets+s']),
    ('(Giacobini|Zinner)',                              ['21P/Giacobini-Zinner+t', 'Periodic Comets+s']),
    ('(Hartley)',                                       ['103P/Hartley+t', 'Periodic Comets+s']),
]

# Keywords to search for if 'Ring+T' appears
KEYWORDS['Ring'] = [
    ('[Cc]lumps{0,1}',                                  ['Clump']),
    ('[Gg]aps{0,1}',                                    ['Gap']),
    ('[Pp]ropellers{0,1}',                              ['Propeller', 'Saturn Rings+t', 'Saturn+s', 'Ring+T']),
    ('[Ww]aves{0,1}',                                   ['Wave']),
    ('[Mm]oonlets{0,1}',                                ['Moonlet']),
]

# Keywords to search for if 'HST' appears
KEYWORDS['Hubble Space Telescope (HST)'] = [
    ('(ACS|Advanced Camera for Surveys)',               ['Advanced Camera for Surveys (ACS)+i', 'Visual']),
    ('(WFPC2|Wide[- ]Field[/ ]Planetary Camera(| 2))',  ['Wide Field/Planetary Camera 2 (WFPC2)+i', 'Visual', 'Infrared']),
    ('(NICMOS)',                                        ['Near Infrared Camera and Multi-Object Spectrometer (NICMOS)+i', 'Infrared']),
    ('(WFC|Wide[- ]Field Channel)',                     ['Advanced Camera for Surveys (ACS)+i', 'Wide Field Channel (WFC)+d', 'Visual', 'Infrared']),
    ('(HRC|High[- ]Resolution Channel)',                ['Advanced Camera for Surveys (ACS)+i', 'High-Resolution Channel (HRC)+d', 'Visual', 'Infrared']),
    ('(SBC|Solar[- ]Blind Channel)',                    ['Advanced Camera for Surveys (ACS)+i', 'Solar Blind Channel (SBC)+d', 'Ultraviolet']),
    ('(WFC3|Wide Field Camera 3)',                      ['Wide Field Camera 3 (WFC3)+i']),
    ('(WFC3|Wide Field Camera 3).*(UVIS|Ultra.*|ultra.*)',
                                                        ['Ultraviolet and Visual Channel (UVIS)+d', 'Visual', 'Ultraviolet']),
    ('(UVIS|[Uu]ltra).*(WFC3|Wide Field Camera 3)',     ['Ultraviolet and Visual Channel (UVIS)+d', 'Visual', 'Ultraviolet']),
    ('(WFC3|Wide Field Camera 3).*(IR|[Ii]nfra.*)',     ['Infrared Channel (IR)+d', 'Infrared']),
    ('(IR|[Ii]nfra).*(WFC3|Wide Field Camera 3)',       ['Infrared Channel (IR)+d', 'Infrared']),
]

# Keywords to search for if 'New Horizons' appears
KEYWORDS['New Horizons'] = [
    ('LORRI',                                           ['Long Range Reconnaissance Imager (LORRI)+i', 'Visual']),
    ('Long[- ][Rr]ange.*[Ii]mager',                     ['Long Range Reconnaissance Imager (LORRI)+i', 'Visual']),
    ('MVIC',                                            ['Multispectral Visible Imaging Camera (MVIC)+i']),
    ('LEISA',                                           ['Linear Etalon Imaging Spectral Array (LEISA)+i', 'Infrared']),
    ('REX',                                             ['Radio Science Experiment (REX)+i', 'Radio']),
]

# Keywords to search for if 'Cassini' appears
KEYWORDS['Cassini-Huygens'] = [
    ('(ISS|Imaging Science Subsystem)',                 ['Imaging Science Subsystem (ISS)+i']),
    ('([Ww]ide[- ][Aa]ngle)',                           ['Imaging Science Subsystem (ISS)+i', 'Wide Angle Camera+d']),
    ('([Nn]arrow[- ][Aa]ngle)',                         ['Imaging Science Subsystem (ISS)+i', 'Narrow Angle Camera+d']),
    ('(VIMS|Visual.{1,20}[Ss]pectrometer)',             ['Visual and Infrared Mapping Spectrometer (VIMS)+i']),
    ('(UVIS|Ultra.{1,20}[Ss]pectrometer)',              ['Ultraviolet Imaging Spectrometer (UVIS)+i', 'Ultraviolet']),
    ('(CIRS|Composite.{1,20}[Ss]pectrometer)',          ['Composite Infrared Spectrometer (CIRS)+i', 'Infrared']),
    ('(RSS|Radio.{1,20}[Ss]ubsystem)',                  ['Radioscience Subsystem (RSS)+i', 'Radio']),
    ('(CDA|Dust ([Dd]etector|[Aa]nalyzer))',            ['Cosmic Dust Analzer (CDA)+i', 'Dust']),
    ('(INMS|Ion (?:|&|and) Neutral Mass Spectrometer)', ['Ion and Neutral Mass Spectrometer (INMS)+i']),
    ('(MIMI|Magnetospheric Imaging Instrument)',        ['Magnetospheric Imaging Instrument (MIMI)+i']),
]

# Keywords to search for if 'Voyager' appears
KEYWORDS['Voyager'] = [
    ('(ISS|Imaging Science Subsystem)',                 ['Imaging Science Subsystem (ISS)+i', 'Visual']),
    ('([Ww]ide[- ][Aa]ngle)',                           ['Wide Angle Camera+d', 'Imaging Science Subsystem (ISS)+i', 'Visual']),
    ('([Nn]arrow[- ][Aa]ngle)',                         ['Narrow Angle Camera+d', 'Imaging Science Subsystem (ISS)+i', 'Visual']),
    ('(PPS|[Pp]otopolarimeter)',                        ['Photopolarimeter Subsystem (PPS)+i', 'Ultraviolet']),
    ('(UVS|Ultra.{1,20}[Ss]pectrometer)',               ['Ultraviolet Spectrometer (UVS)+i', 'Ultraviolet']),
    ('(RSS|Radio.{1,20}[Ss]ubsystem)',                  ['Radioscience Subsystem (RSS)+i', 'Radio']),
]

# Keywords to search for if 'Juno' appears
KEYWORDS['Juno'] = [
    ('Juno[Cc]am',                                      ['JunoCam+i', 'Visual']),
    ('(JIRAM|Jovian .{10,30}Mapper)',                   ['Jupiter Infrared and Auroral Mapper (JIRAM)+i', 'Infrared']),
]

########################################################################################################################


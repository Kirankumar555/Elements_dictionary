''' THERMAL CONDUCTIVITY it's that dictionary'''
thermal={'Hydrogen':0.1805,'Helium':0.1513,'Lithium':85,'Beryllium':9,'Boron':27,
         'Carbon':140,'Nitrogen':0.02583,'Oxygen':0.02583,'Flurine':0.0277,
         'Neon':0.0491,'Sodium':140,'Magnesium':160,'Aluminum':235,'Silicon':150,
         'Phoshorous':0.236,'Sulfur':0.205,'Chlorine':0.0089,'Argon':0.01772,
         'Potassium':100,'Calcium':200,'Scandium':16,'Titanium':22,'Vanadium':31,
         'Chromium':94,'Manganese':7.8,'Iron':80,'Cobalt':100,'Nickel':91,'Copper':400,
         'Zinc':120,'Gallium':29,'Germanium':60,'Arsenic':50,'Selenium':0.52,
         'Bromine':0.12,'Krypton':0.00943,'Rubidium':58,'Strontium':35,'Yttrium':17,
         'Zirconium':23,'Niobium':54,'Molybdenum':139,'Technetium':51,'Ruthenium':120,
         'Rhodium':150,'Palladium':72,'Silver':430,'Cadmium':97,'Indium':82,'Tin':67,
         'Antimony':24,'Tellurium':3,'Iodine':0.449,'Xenon':0.00565,'Cesium':36,
         'Barium':18,'Lanthanum':13,'Cerium':11,'Praseodymium':13,'Neodymium':17,
         'Promethium':15,'Samarium':13,'Europium':14,'Gadolinium':11,
         'Terbium':11,'Dysporosium':11,'Holmium':16,'Erbium':15,'Thulium':17,
         'Ytterbium':39,'Lutentium':16,'Hafnium':23,'Tantalum':57,'Tungsten':170,
         'Rhenium':48,'Osmium':88,'Iridium':150,'Platinum':72,'Gold':320,'Mercury':8.3,
         'Thallium':46,'Lead':35,'Bismuth':8,'Polonium':20,'Astatine':2,
         'Radon':0.00361,'Francium':15,'Radium':19,'Actinium':12,'Thorium':54,
         'Protactinium':47,'Uranium':27,'Neptunium':6,'Plutonium':6,'Americium':10}
#above a range
def tc_above(x):
    print('in (W/m*K)')
    for element in thermal:
        if thermal[element]>x:
            print(element,thermal[element])
#below a range
def tc_below(x):
    print('in (W/m*K)')
    for element in thermal:
        if thermal[element]<x:
            print(element,thermal[element])
#between
def tc_between(x,y):
    print('in (W/m*K)')
    for element in thermal:
        if thermal[element]>x and thermal[element]<y:
            print(element,thermal[element])
#fo alist of all elements
def list_element():
    t=list()
    for element in thermal:
        t.append(element)
    print(t)
#for key values
def list_tc_value():
    print('in (W/m*K)')
    t=list()
    for element in thermal:
        t.append(thermal[element])
    print(t)
#searching
def search_tc(x):
    print('in (W/m*K)')
    for element in thermal:
        if x==element:
            print(element,thermal[element])
#exact value
def search_tc_value(x):
    print('in (W/m*K)')
    for element in thermal:
        if x==thermal[element]:
            print(element,thermal[element])
            
            
'''                   BOILING POINT                      '''

boiling={'Hydrogen':-252.87,'Helium':-268.93,
         'Litium':1342,'Berilium':2470,'Boron':4000,
         'Carbon':4027,'Nitrogen':-195.79,'Oxygen':-182.9,
         'Fluorine':-188.12,'Neon':-246.08,'Sodium':883,
         'Magnesium':1090,'Aluminium':2519,'Silicon':2900,
         'Phosphorous':280.5,'Sulphur':444.72,'Clorine':-34.04,'Argon':-185.8,
         'Potassium':759,'Calcium':1484,'Scandium':2830,
         'Titanium':3287,'Vanadium':3407,'Chromium':2671,
         'Manganese':2061,'Iron':2861,'Cobalt':2927,'Nickel':2913,
         'Copper':2927,'Zinc':907,'Gallium':2204,'Germanium':2820,
         'Arsenic':614,'Selenium':685,'Bromine':59,'Krypton':-153.22,
         'Rubidium':688,'Strontium':1382,'Yttrium':3345,'Zirconium':4409,
         'Niobium':4744,'Molybdenum':4639,'Technetium':4265,'Ruthenium':4150,
         'Rhodium':3695,'Palladium':2963,'Silver':2162,'Cadmium':767,
         'Indium':2072,'Tin':2602,'Antimony':1587,'Tellurium':988,
         'Iodine':184.3,'Xenon':-108,'Cesium':671,'Barium':1870,
         'Lanthanum':3464,'Cerium':3360,'Praseodymium':3290,'Neodymium':3100,
         'Promethium':3000,'Samarium':1803,'Europium':1527,'Gadolinium':3250,
         'Terbium':3230,'Dysporosium':2567,'Holmium':2700,'Erbium':2868,
         'Thulium':1950,'Ytterbium':1196,'Lutentium':3402,'Hafnium':4603,
         'Tantalum':5458,'Tungsten':5555,'Rhenium':5596,'Osmium':5012,
         'Iridium':4428,'Platinum':3825,'Gold':2856,'Mercury':356.73,
         'Thallium':1473,'Lead':1749,'Bismuth':1564,'Polonium':962,
         'Astatine':'not found','Radon':-61.7,'Francium':'not found',
         'Radium':1737,'Actinium':3200,'Thorium':4820,'Protactinium':4000,
         'Uranium':3927,'Neptunium':4000,'Plutonium':3230,'Americium':2011,
         'Curium':3110, 'Berkelium':'not found', 'Californium':'not found',
         'Einsteinium':'not found','Fermium':'not found','Mendelevium':'not found',
         'Nobelium':'not found','Lawrencium':'not found'}
# from Rf to Og 'not found'
def bp_above(x):
    print('in (degree celsius')
    for element in boiling:
        if boiling[element]=='not found':
            continue
        if boiling[element]>x:
            print(element,boiling[element])
#below a range
def bp_below(x):
    print('in (degree celsius)')
    for element in boiling:
        if boiling[element]=='not found':
            continue
        if boiling[element]<x:
            print(element,boiling[element])
#between
def bp_between(x,y):
    print('in (degree celsius')
    for element in boiling:
        if boiling[element]=='not found':
            continue
        if boiling[element]>x and boiling[element]<y:
            print(element,boiling[element])
#for key values
def list_bp_value():
    print('in (degree celsius')
    t=list()
    for element in boiling:
        t.append(boiling[element])
    print(t)
#searching
def search_bp(x):
    print('in (degree celsius')
    for element in boiling:
        if x==element:
            print(element,boiling[element])
#exact value
def search_bp_value(x):
    print('in (degree celsius')
    for element in boiling:
        if x==boiling[element]:
            print(element,boiling[element])



'''                              MELTING POINT                  '''

melting={'Hydrogen':-259.14,'Helium':'not found',
         'Litium':180.54,'Berilium':1287,'Boron':2075,
         'Carbon':3550,'Nitrogen':-210.1,'Oxygen':-218.3,
         'Fluorine':-219.6,'Neon':-248.59,'Sodium':97.72,
         'Magnesium':650,'Aluminium':660.32,'Silicon':1414,
         'Phosphorous':44.2,'Sulphur':115.21,'Chlorine':-101.5,'Argon':-189.3,
         'Potassium':63.38,'Calcium':842,'Scandium':1541,
         'Titanium':1668,'Vanadium':1910,'Chromium':1907,
         'Manganese':1246,'Iron':1538,'Cobalt':1495,'Nickel':1455,
         'Copper':1084.62,'Zinc':419.53,'Gallium':29.76,'Germanium':938.3,
         'Arsenic':817,'Selenium':221,'Bromine':-7.3,'Krypton':-157.36,
         'Rubidium':39.31,'Strontium':777,'Yttrium':1526,'Zirconium':1855,
         'Niobium':2477,'Molybdenum':2623,'Technetium':2157,'Ruthenium':2334,
         'Rhodium':1964,'Palladium':1554,'Silver':964.78,'Cadmium':321.07,
         'Indium':156.6,'Tin':231.93,'Antimony':630.63,'Tellurium':449.51,
         'Iodine':113.7,'Xenon':-111.8,'Cesium':28.4,'Barium':727,
         'Lanthanum':920,'Cerium':798,'Praseodymium':931,'Neodymium':1021,
         'Promethium':1100,'Samarium':1072,'Europium':822,'Gadolinium':1313,
         'Terbium':1356,'Dysporosium':1412,'Holmium':1474,'Erbium':1497,
         'Thulium':1545,'Ytterbium':819,'Lutentium':1663,'Hafnium':2233,
         'Tantalum':3017,'Tungsten':3422,'Rhenium':3186,'Osmium':3033,
         'Iridium':2466,'Platinum':1768.3,'Gold':1064,'Mercury':-38.83,
         'Thallium':304,'Lead':327.46,'Bismuth':271.3,'Polonium':254,
         'Astatine':302,'Radon':-71,'Francium':'not found',
         'Radium':700,'Actinium':1050,'Thorium':1750,'Protactinium':1572,
         'Uranium':1135,'Neptunium':644,'Plutonium':640,'Americium':1176,
         'Curium':1345, 'Berkelium':1050, 'Californium':900,
         'Einsteinium':860,'Fermium':1527,'Mendelevium':827,
         'Nobelium':827,'Lawrencium':1627
         }

def mp_above(x):
    print('in (degree celsius')
    for element in melting:
        if melting[element]=='not found':
            continue
        if melting[element]>x:
            print(element,melting[element])
#below a range
def mp_below(x):
    print('in (degree celsius)')
    for element in melting:
        if melting[element]=='not found':
            continue
        if melting[element]<x:
            print(element,melting[element])
#between
def mp_between(x,y):
    print('in (degree celsius')
    for element in melting:
        if melting[element]=='not found':
            continue
        if melting[element]>x and melting[element]<y:
            print(element,melting[element])
#for key values
def list_mp_value():
    print('in (degree celsius')
    t=list()
    for element in melting:
        t.append(melting[element])
    print(t)
#searching
def search_mp(x):
    print('in (degree celsius')
    for element in melting:
        if x==element:
            print(element,melting[element])
#exact value
def search_mp_value(x):
    print('in (degree celsius')
    for element in melting:
        if x==melting[element]:
            print(element,melting[element])



'''             ELECTRODE POTENTIAL            '''
#potential={'Hydrogen':0,'Helium':'not found',
#         'Litium':180.54,'Berilium':1287,'Boron':2075,
#         'Carbon':3550,'Nitrogen':-210.1,'Oxygen':-218.3,
#         'Fluorine':-219.6,'Neon':-248.59,'Sodium':97.72,
#         'Magnesium':650,'Aluminium':660.32,'Silicon':1414,
#         'Phosphorous':44.2,'Sulphur':115.21,'Chlorine':-101.5,'Argon':-189.3,
#         'Potassium':63.38,'Calcium':842,'Scandium':1541,
#         'Titanium':1668,'Vanadium':1910,'Chromium':1907,
#         'Manganese':1246,'Iron':1538,'Cobalt':1495,'Nickel':1455,
#         'Copper':1084.62,'Zinc':419.53,'Gallium':29.76,'Germanium':938.3,
#         'Arsenic':817,'Selenium':221,'Bromine':-7.3,'Krypton':-157.36,
#         'Rubidium':39.31,'Strontium':777,'Yttrium':1526,'Zirconium':1855,
#         'Niobium':2477,'Molybdenum':2623,'Technetium':2157,'Ruthenium':2334,
#         'Rhodium':1964,'Palladium':1554,'Silver':964.78,'Cadmium':321.07,
#         'Indium':156.6,'Tin':231.93,'Antimony':630.63,'Tellurium':449.51,
#         'Iodine':113.7,'Xenon':-111.8,'Cesium':28.4,'Barium':727,
#         'Lanthanum':920,'Cerium':798,'Praseodymium':931,'Neodymium':1021,
#         'Promethium':1100,'Samarium':1072,'Europium':822,'Gadolinium':1313,
#         'Terbium':1356,'Dysporosium':1412,'Holmium':1474,'Erbium':1497,
#         'Thulium':1545,'Ytterbium':819,'Lutentium':1663,'Hafnium':2233,
#         'Tantalum':3017,'Tungsten':3422,'Rhenium':3186,'Osmium':3033,
#         'Iridium':2466,'Platinum':1768.3,'Gold':1064,'Mercury':-38.83,
#         'Thallium':304,'Lead':327.46,'Bismuth':271.3,'Polonium':254,
#         'Astatine':302,'Radon':-71,'Francium':'not found',
#         'Radium':700,'Actinium':1050,'Thorium':1750,'Protactinium':1572,
#         'Uranium':1135,'Neptunium':644,'Plutonium':640,'Americium':1176,
#         'Curium':1345, 'Berkelium':1050, 'Californium':900,
#         'Einsteinium':860,'Fermium':1527,'Mendelevium':827,
#         'Nobelium':827,'Lawrencium':1627
        

















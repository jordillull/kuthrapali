#!/usr/bin/python3

from math import log

MALE  =False
FEMALE=True 

def calc_sex(child):
    if child == 0:
        return MALE
    elif child == 1:
        return FEMALE
    else:
        part = log(child, 2)//1
        return not calc_sex( child % (2**part)) 

def get_sex(generation, child):
    sex = calc_sex(child-1)
    if sex == MALE:
        return 'Male'
    else:
        return 'Female'

def main():
    lines = input()
    requests = []
    for i in range(int(lines)): 
        requests.append(input())

    for request in requests: 
        generation, child = map(lambda x: int(x), request.split())
        sex = get_sex(generation,child)
        print(sex)

def test():
    tests = [
    (7914,92068631258528,'Female'),
    (3789,652299663073690,'Male'),
    (2315,149152564193223,'Female'),
    (6176,980405233312659,'Female'),
    (4322,991943727483435,'Male'),
    (7117,871461111624639,'Female'),
    (2784,164030935948752,'Male'),
    (1770,254060547227449,'Male'),
    (915,855451642596375,'Male'),
    (1205,878819824707157,'Female'),
    (8489,165642806928540,'Male'),
    (1223,416833490280740,'Female'),
    (8810,867563931283286,'Female'),
    (370,877271988676961,'Male'),
    (9029,288469117158638,'Female'),
    (6742,400849636170381,'Female'),
    (7452,816087484586851,'Male'),
    (2614,618734970937676,'Male'),
    (6947,978088084920067,'Female'),
    (8327,564824549785796,'Male'),
    (6192,981610686456244,'Female'),
    (3036,202119941279496,'Female'),
    (4705,424829012571858,'Male'),
    (7414,293337066022391,'Male'),
    (6201,136979943897141,'Male'),
    (4086,767748048077148,'Female'),
    (1366,575985991841630,'Male'),
    (5845,769505421377595,'Female'),
    (1496,38592276092607,'Female'),
    (3231,450597830887350,'Male'),
    (8470,103839967962594,'Female'),
    (7118,931872699347838,'Male'),
    (9097,39898107935919,'Male'),
    (2810,540121623426897,'Female'),
    (6166,4764310174431,'Female'),
    (7772,841809420892636,'Male'),
    (2753,913686713547666,'Female'),
    (8764,619634461802358,'Male'),
    (4881,506698239313423,'Male'),
    (4263,849887308009320,'Female'),
    (253,127383851490527,'Male'),
    (1814,53902561991663,'Male'),
    (3297,503009473937936,'Male'),
    (6738,699696378058845,'Male'),
    (2398,629764260944824,'Male'),
    (8255,703254910799203,'Male'),
    (710,423879670031508,'Female'),
    (8668,586297064401943,'Female'),
    (9566,262973137626482,'Male'),
    (8395,222811096042105,'Female'),
    (8700,245972066755312,'Male'),
    (9941,261144480184234,'Female'),
    (6787,429413047708334,'Male'),
    (9732,142914791543547,'Male'),
    (1165,182372606615694,'Female'),
    (8542,642463598939147,'Male'),
    (3198,459072066590535,'Male'),
    (7257,237407739263984,'Male'),
    (6963,678943246014642,'Female'),
    (5629,544311831258478,'Male'),
    (563,889062413764912,'Female'),
    (6870,186355184855743,'Male'),
    (7719,204110817645901,'Female'),
    (5725,56641175428323,'Female'),
    (5085,117643195062648,'Female'),
    (2205,300698111526609,'Female'),
    (2571,918716644334638,'Female'),
    (4650,869938543907155,'Male'),
    (9976,712048542226771,'Female'),
    (8671,570699901279337,'Male'),
    (8106,310470850255570,'Male'),
    (9886,43011149879344,'Female'),
    (8722,580201806512219,'Male'),
    (3298,796422506198511,'Male'),
    (3349,220622902797176,'Female'),
    (1339,784325232367766,'Male'),
    (2981,906974460553218,'Female'),
    (1741,281211858792573,'Female'),
    (6403,438194712742186,'Male'),
    (490,70343956839783,'Male'),
    (3974,198673494704596,'Male'),
    (4828,27735590009994,'Male'),
    (9933,388312725913791,'Female'),
    (742,887135176875544,'Male'),
    (3281,580759083660916,'Female'),
    (6735,825281135493712,'Male'),
    (2392,715636373817873,'Male'),
    (840,263737325460931,'Male'),
    (8014,19391637643280,'Male'),
    (157,958585867091989,'Female'),
    (4900,935663733103092,'Male'),
    (5274,340423703588406,'Female'),
    (3378,990410284162647,'Female'),
    (109,364151716969916,'Male'),
    (6494,837964101245858,'Female'),
    (865,818925278831444,'Male'),
    (1824,594395500871643,'Female'),
    (2493,118387835667491,'Male'),
    (531,687286931346679,'Female'),
    (4277,180899823819973,'Female'),
    (1990,451132318019620,'Male'),
    (3169,985882797318257,'Female'),
    (6166,249818629806955,'Female'),
    (349,27039510955447,'Male'),
    (6243,783280656773837,'Male'),
    (9000,332104225519750,'Female'),
    (2890,440035476491439,'Female'),
    (2310,150148150039599,'Female'),
    (1396,154164960721200,'Female'),
    (5206,787800598291043,'Female'),
    (8122,142815254907922,'Male'),
    (9751,58816412163070,'Female'),
    (4985,639493936023201,'Female'),
    (6551,501836215375605,'Male'),
    (2864,811380568500310,'Male'),
    (4553,878920449181887,'Female'),
    (8533,317667834538077,'Male'),
    (5481,307608844611063,'Male'),
    (4424,73392813609727,'Male'),
    (772,316367500257797,'Male'),
    (9303,767403594752314,'Male'),
    (2643,459406477397955,'Female'),
    (6353,91525185642982,'Female'),
    (6403,295132211874293,'Male'),
    (3021,660191742093450,'Male'),
    (9548,426172396369013,'Male'),
    (1798,805875901942181,'Male'),
    (7665,405931134492613,'Female'),
    (8981,643907478463573,'Female'),
    (2702,772901544106233,'Female'),
    (1583,741562161599389,'Female'),
    (3065,157174478027381,'Female'),
    (3201,964759456123623,'Female'),
    (8200,408485153689328,'Female'),
    (6385,57718425390978,'Female'),
    (7641,222541577690020,'Male'),
    (3415,247795121778505,'Female'),
    (4566,729986135337661,'Male'),
    (5201,402341263885877,'Male'),
    (8075,600448502235592,'Male'),
    (5560,917068697197325,'Female'),
    (6556,65393981041661,'Female'),
    (54,635307116971571,'Female'),
    (4476,20406451278995,'Female'),
    (4072,825585419647182,'Female'),
    (9687,487196857855165,'Female'),
    (6499,10430427279306,'Female'),
    (1310,722575117237450,'Female'),
    (6530,86022461609701,'Male'),
    (7878,569497458566071,'Female'),
    (7168,769156031248265,'Female'),
    (7279,18843453417580,'Female'),
    (1319,841378444200630,'Male'),
    (2444,579338624909001,'Male'),
    (5632,745179398554027,'Female'),
    (8396,79327873524722,'Female'),
    (9601,803521694986175,'Female'),
    (4843,171573745883957,'Male'),
    (1532,613054363163391,'Female'),
    (2377,237959709508587,'Female'),
    (8575,234773523235590,'Female'),
    (5751,845697476080128,'Female'),
    (8109,623024567068520,'Male'),
    (2968,996524059196796,'Male'),
    (9929,734433386988630,'Male'),
    (2027,918607534575977,'Male'),
    (4852,134858600804132,'Female'),
    (8261,820725912397052,'Male'),
    (4951,875867632676261,'Female'),
    (5553,679659359240976,'Male'),
    (6539,999236146127204,'Male'),
    (2204,652079788100080,'Female'),
    (8857,347213462263536,'Male'),
    (6382,365579627526175,'Female'),
    (978,665407384125443,'Male'),
    (2340,199856859813910,'Female'),
    (7426,172738301636340,'Female'),
    (5263,972752743893349,'Female'),
    (2170,695475096166448,'Male'),
    (4769,383076288641891,'Female'),
    (3327,49683213809523,'Male'),
    (3899,654960149140037,'Male'),
    (7767,837870698392017,'Female'),
    (5264,700180319968916,'Female'),
    (3373,571605868334370,'Male'),
    (2266,308276377718744,'Female'),
    (5436,928822595129267,'Female'),
    (2895,475998245486576,'Male'),
    (7969,368970055771592,'Male'),
    (1327,688221038426094,'Female'),
    (135,35504908286062,'Female'),
    (7857,740571327806195,'Female'),
    (4748,835586413969891,'Male'),
    (1741,112459982912637,'Female'),
    (6703,793230799073050,'Female'),
    (1415,362648970239276,'Female'),
    (5785,807591431222850,'Female'),
    (5695,353227818963759,'Female'),
    (98,605225115550289,'Female'),
    (4400,770646286734285,'Male'),
    (1596,739461871023926,'Male'),
    (9111,982025135385552,'Female'),
    (9330,464374383015967,'Male'),
    (9139,105742810816521,'Female'),
    (7910,252027434631805,'Female'),
    (5313,713340278311862,'Male'),
    (2470,280957371695160,'Female'),
    (8523,736252689040024,'Female'),
    (8513,788818978760554,'Female'),
    (5624,631289282006348,'Female'),
    (6424,751125388317796,'Male'),
    (2269,33188978092699,'Male'),
    (9700,976501756877417,'Female'),
    (8580,463658025120490,'Female'),
    (4570,707296462454009,'Male'),
    (7460,219977549316605,'Male'),
    (7075,872594822461893,'Male'),
    (2620,935909183999626,'Male'),
    (6524,701381494804379,'Male'),
    (4704,947357722414861,'Female'),
    (2145,692762155210345,'Male'),
    (3695,353298241820742,'Female'),
    (3166,618188771078744,'Male'),
    (5884,323806807141220,'Male'),
    (4856,3985886454136,'Male'),
    (3619,61500964034357,'Female'),
    (9448,577952744963356,'Female'),
    (8648,545882699067546,'Male'),
    (1667,263448299708807,'Male'),
    (8520,790810978487166,'Female'),
    (8370,63040697608315,'Male'),
    (8861,605513445705273,'Female'),
    (695,262092350166045,'Male'),
    (3780,953751570873843,'Male'),
    (3569,976507330069103,'Male'),
    (3605,776604813967028,'Female'),
    (7004,291013602354525,'Female'),
    (8760,481808913563930,'Female'),
    (2628,358166332238478,'Male'),
    (4876,612019269689149,'Female'),
    (54,672495248964621,'Female'),
    (854,473150666606267,'Female'),
    (1736,959169813185348,'Female'),
    (7949,594910363025875,'Male'),
    (6642,760012944182113,'Female'),
    (8879,195418206315115,'Female'),
    (6399,423350598815082,'Female'),
    (4324,566741484364328,'Female'),
    (1990,381387787990356,'Female'),
    (1177,65316036448315,'Female'),
    (803,972001448944711,'Male'),
    (8533,632150372734071,'Female'),
    (7020,215003368387085,'Female'),
    (9496,631225211702130,'Female'),
    (1869,655653854778883,'Male'),
    (725,28230792494291,'Male'),
    (6177,701323428484062,'Male'),
    (4803,932042183349735,'Male'),
    (9822,629976691466519,'Female'),
    (2014,254883848430931,'Female'),
    (9467,432492412020525,'Male'),
    (8622,108946582980576,'Male'),
    (8758,416993485963182,'Female'),
    (29,206160763,'Male'),
    (6755,370654135822765,'Male'),
    (1750,859903193687506,'Female'),
    (8865,353827980064088,'Male'),
    (9917,377505060058591,'Female'),
    (7523,611705498509970,'Male'),
    (3607,535952145899247,'Female'),
    (3021,798157884185529,'Female'),
    (3851,124475119494717,'Female'),
    (274,450345096621276,'Male'),
    (2279,319148460463230,'Male'),
    (7097,729694583259816,'Male'),
    (8510,635563182603783,'Male'),
    (9761,469043138568286,'Female'),
    (6664,539608695112272,'Male'),
    (6072,224928000667822,'Male'),
    (9979,915797572114249,'Male'),
    (5390,572089030364993,'Female'),
    (9475,812024629650287,'Female'),
    (1217,344345699990754,'Male'),
    (6578,626812806282051,'Female'),
    (6544,33900479343922,'Male'),
    (3394,370187615454029,'Female'),
    (1692,644929643109417,'Male'),
    (6921,72439052067909,'Female'),
    (9980,386095067188592,'Female'),
    (7700,720539589509018,'Female'),
    (6885,86951814491471,'Male'),
    (5127,190958408922601,'Female'),
    (521,486039602733743,'Male'),
    (2260,214285145369622,'Male'),
    (9106,340793074183390,'Female'),
    (7374,815264062753501,'Male'),
    (8871,138584588760795,'Male'),
    (8826,105128306287229,'Male'),
    ] 

    for test in tests:
        sex = get_sex(test[0], test[1])
        if sex == test[2]:
            print("Ok")
        else:
            print("Fail")

if __name__ == "__main__":
    main()
   
import json
import sys 

stdoutOrigin=sys.stdout 
sys.stdout = open("data/recrusion_ex1.csv", "w")

with open('data/fbi_data.json') as f:
    data = json.load(f)
	
recursion = data['AK'] #(['dict'])['key dict']['key value']
for key,AK in recursion.items():
    print(key)
    print(AK)
    print(recursion[key])
	
recursion = data['AL'] #(['dict'])['key dict']['key value']
for key,AL in recursion.items():
    print(key)
    print(AL)
    print(recursion[key])

recursion = data['AR'] #(['dict'])['key dict']['key value']
for key,AR in recursion.items():
    print(key)
    print(AR)
    print(recursion[key])
	
recursion = data['AZ'] #(['dict'])['key dict']['key value']
for key,AZ in recursion.items():
    print(key)
    print(AZ)
    print(recursion[key])

recursion = data['CA'] #(['dict'])['key dict']['key value']
for key,CA in recursion.items():
    print(key)
    print(CA)
    print(recursion[key])
	
recursion = data['CO'] #(['dict'])['key dict']['key value']
for key,CO in recursion.items():
    print(key)
    print(CO)
    print(recursion[key])

recursion = data['CT'] #(['dict'])['key dict']['key value']
for key,CT in recursion.items():
    print(key)
    print(CT)
    print(recursion[key])
	
recursion = data['DC'] #(['diDC'])['key diDC']['key value']
for key,DC in recursion.items():
    print(key)
    print(DC)
    print(recursion[key])

recursion = data['DE'] #(['diDE'])['key diDE']['key value']
for key,DE in recursion.items():
    print(key)
    print(DE)
    print(recursion[key])
	
recursion = data['FL'] #(['diFL'])['key diFL']['key value']
for key,FL in recursion.items():
    print(key)
    print(FL)
    print(recursion[key])
	
recursion = data['GA'] #(['diGA'])['key diGA']['key value']
for key,GA in recursion.items():
    print(key)
    print(GA)
    print(recursion[key])
	
recursion = data['GM'] #(['diGM'])['key diGM']['key value']
for key,GM in recursion.items():
    print(key)
    print(GM)
    print(recursion[key])

recursion = data['HI'] #(['diHI'])['key diHI']['key value']
for key,HI in recursion.items():
    print(key)
    print(HI)
    print(recursion[key])
	
recursion = data['IA'] #(['diIA'])['key diIA']['key value']
for key,IA in recursion.items():
    print(key)
    print(IA)
    print(recursion[key])
	
recursion = data['ID'] #(['diID'])['key diID']['key value']
for key,ID in recursion.items():
    print(key)
    print(ID)
    print(recursion[key])
	
recursion = data['IL'] #(['diIL'])['key diIL']['key value']
for key,IL in recursion.items():
    print(key)
    print(IL)
    print(recursion[key])

recursion = data['IN'] #(['diIN'])['key diIN']['key value']
for key,IN in recursion.items():
    print(key)
    print(IN)
    print(recursion[key])
	
recursion = data['KS'] #(['diKS'])['key diKS']['key value']
for key,KS in recursion.items():
    print(key)
    print(KS)
    print(recursion[key])
	
recursion = data['KY'] #(['diKY'])['key diKY']['key value']
for key,KY in recursion.items():
    print(key)
    print(KY)
    print(recursion[key])
	
recursion = data['LA'] #(['diLA'])['key diLA']['key value']
for key,LA in recursion.items():
    print(key)
    print(LA)
    print(recursion[key])

recursion = data['MA'] #(['diMA'])['key diMA']['key value']
for key,MA in recursion.items():
    print(key)
    print(MA)
    print(recursion[key])
	
recursion = data['MD'] #(['diMD'])['key diMD']['key value']
for key,MD in recursion.items():
    print(key)
    print(MD)
    print(recursion[key])
	
recursion = data['ME'] #(['diME'])['key diME']['key value']
for key,ME in recursion.items():
    print(key)
    print(ME)
    print(recursion[key])
	
recursion = data['MI'] #(['diMI'])['key diMI']['key value']
for key,MI in recursion.items():
    print(key)
    print(MI)
    print(recursion[key])

recursion = data['MN'] #(['diMN'])['key diMN']['key value']
for key,MN in recursion.items():
    print(key)
    print(MN)
    print(recursion[key])
	
recursion = data['MO'] #(['diMO'])['key diMO']['key value']
for key,MO in recursion.items():
    print(key)
    print(MO)
    print(recursion[key])
	
recursion = data['MS'] #(['diMS'])['key diMS']['key value']
for key,MS in recursion.items():
    print(key)
    print(MS)
    print(recursion[key])

recursion = data['MT'] #(['diMT'])['key diMT']['key value']
for key,MT in recursion.items():
    print(key)
    print(MT)
    print(recursion[key])
	
recursion = data['NC'] #(['diNC'])['key diNC']['key value']
for key,NC in recursion.items():
    print(key)
    print(NC)
    print(recursion[key])

recursion = data['ND'] #(['diND'])['key diND']['key value']
for key,ND in recursion.items():
    print(key)
    print(ND)
    print(recursion[key])
	
recursion = data['NE'] #(['diNE'])['key diNE']['key value']
for key,NE in recursion.items():
    print(key)
    print(NE)
    print(recursion[key])

recursion = data['NH'] #(['diNH'])['key diNH']['key value']
for key,NH in recursion.items():
    print(key)
    print(NH)
    print(recursion[key])
	
recursion = data['NJ'] #(['diNJ'])['key diNJ']['key value']
for key,NJ in recursion.items():
    print(key)
    print(NJ)
    print(recursion[key])
	
recursion = data['NM'] #(['diNM'])['key diNM']['key value']
for key,NM in recursion.items():
    print(key)
    print(NM)
    print(recursion[key])
	
recursion = data['NV'] #(['diNV'])['key diNV']['key value']
for key,NV in recursion.items():
    print(key)
    print(NV)
    print(recursion[key])

recursion = data['NY'] #(['diNY'])['key diNY']['key value']
for key,NY in recursion.items():
    print(key)
    print(NY)
    print(recursion[key])
	
recursion = data['OH'] #(['diOH'])['key diOH']['key value']
for key,OH in recursion.items():
    print(key)
    print(OH)
    print(recursion[key])
	
recursion = data['OK'] #(['diOK'])['key diOK']['key value']
for key,OK in recursion.items():
    print(key)
    print(OK)
    print(recursion[key])
	
recursion = data['OR'] #(['diOR'])['key diOR']['key value']
for key,OR in recursion.items():
    print(key)
    print(OR)
    print(recursion[key])

recursion = data['PA'] #(['diPA'])['key diPA']['key value']
for key,PA in recursion.items():
    print(key)
    print(PA)
    print(recursion[key])
	
recursion = data['PR'] #(['diPR'])['key diPR']['key value']
for key,PR in recursion.items():
    print(key)
    print(PR)
    print(recursion[key])
	
recursion = data['RI'] #(['diRI'])['key diRI']['key value']
for key,RI in recursion.items():
    print(key)
    print(RI)
    print(recursion[key])
	
recursion = data['SC'] #(['diSC'])['key diSC']['key value']
for key,SC in recursion.items():
    print(key)
    print(SC)
    print(recursion[key])

recursion = data['SD'] #(['diSD'])['key diSD']['key value']
for key,SD in recursion.items():
    print(key)
    print(SD)
    print(recursion[key])

recursion = data['TN'] #(['diTX'])['key diTX']['key value']
for key,TN in recursion.items():
    print(key)
    print(TN)
    print(recursion[key])
	
recursion = data['TX'] #(['diTX'])['key diTX']['key value']
for key,TX in recursion.items():
    print(key)
    print(TX)
    print(recursion[key])
	
recursion = data['UT'] #(['diUT'])['key diUT']['key value']
for key,UT in recursion.items():
    print(key)
    print(UT)
    print(recursion[key])
	
recursion = data['VA'] #(['diVA'])['key diVA']['key value']
for key,VA in recursion.items():
    print(key)
    print(VA)
    print(recursion[key])

recursion = data['VI'] #(['diGA'])['key diGA']['key value']
for key,VI in recursion.items():
    print(key)
    print(VI)
    print(recursion[key])
	
recursion = data['VT'] #(['diVT'])['key diVT']['key value']
for key,VT in recursion.items():
    print(key)
    print(VT)
    print(recursion[key])
	
recursion = data['WA'] #(['diWA'])['key diWA']['key value']
for key,WA in recursion.items():
    print(key)
    print(WA)
    print(recursion[key])
	
recursion = data['WI'] 
for key,WI in recursion.items():
    print(key)
    print(WI)
    print(recursion[key])

recursion = data['WV'] #(['diWV'])['key diWV']['key value']
for key,WV in recursion.items():
    print(key)
    print(WV)
    print(recursion[key])

recursion = data['WY'] #(['diWY'])['key diWY']['key value']
for key,WY in recursion.items():
    print(key)
    print(WY)
    print(recursion[key])
	
sys.stdout.close()
sys.stdout=stdoutOrigin
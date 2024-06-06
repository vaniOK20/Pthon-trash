import os

e=os.path.expandvars("%appdata%")
e=e.replace('Roaming', '')+'local\\programs\\python'
if os.path.exists(e):
	sas=os.popen(f'tree /f {e}').read()
	sas2=sas[:sas.find('python.exe')]
	int_=0
	text=''
	sas3=sas2.find('ГДДД')+4
	while sas2[sas3+int_]!='і':
		text=text+sas2[sas3+int_]
		int_+=1
	os.system(f'{e}\\{text[:len(text)-1]}\\scripts\\pip.exe install pygame')
input()
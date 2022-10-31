import plotGalpropHH as gHH
import matplotlib.pyplot as plt
#Module for compressing into zip file
import zipfile as zip

antiproton=('spectra',0,-1,1,0)
proton=('spectra',0,1,1,0)
BCratio=('ratios',0,5,"-1",6,"-1")
lines=['b-','r--','g:','m-.','c-']

names=[]
names.append(['5z','60','61','62','63'])
names.append(['64','65','66','67','68'])
names.append(['69','6a','6b','6c','6d'])
names.append(['6e','6f','6g','6h','6i'])
names.append(['6j','6k','6l','6m','6n'])
names.append(['6o','6p','6q','6r','6s'])
names.append(['6t','6u','6v','6w','6x'])
names.append(['6y','6z','70','71','72'])
names.append(['73','74','75','76','77'])
names.append(['78','79','7a','7b','7c'])
names.append(['7d','7e','7f','7g','7h'])
names.append(['7i','7j','7k','7l','7m'])
names.append(['7n','7o','7p','7q','7r'])
names.append(['7s','7t','7u','7v','7w'])

for m in range(len(names)):
    msg=[]
    result=[]
    for i in range(len(names[m])):
        msg.append('')
        result.append(0)
        msg[i],result[i]=gHH.gplot('','./','54_091a00'+names[m][i]+'.gz',*antiproton)
    plt.figure('Antiproton F%s'%str(m+1))
    plt.xlabel('E (MeV)')
    plt.ylabel('E^2 dF/dE (cm^-2*s^-1*sr^-1*MeV^1)')
    zipF=zip.ZipFile('Antiproton_F%s.zip'%str(m+1),'w')
    for i in range(len(names[m])):
        file=open('AntiprotonF%s_%s.txt'%(m+1,i+1),'w')
        xi=[]
        yi=[]
        for k in range(len(result[i])/2):
            xi.append(float(result[i][k][0]))
            yi.append(pow(xi[k],2)*float(result[i][k][1]))
            file.write('%10.4f    %10.4f'%(xi[k],yi[k]))
        file.close()
        zipF.write('AntiprotonF%s_%s.txt'%(m+1,i+1))
        plt.plot(xi,yi,lines[i],label='F%d'%i)
    zipF.close()
    plt.legend(loc='lower left')
    plt.yscale('log')
    plt.xscale('log')
    plt.savefig('AntiProtonF%s.pdf'%str(m+1))
    plt.close()
    
for m in range(len(names)):
    msg=[]
    result=[]
    for i in range(len(names[m])):
        msg.append('')
        result.append(0)
        msg[i],result[i]=gHH.gplot('','./','54_091a00'+names[m][i]+'.gz',*proton)
    plt.figure('Proton F%s'%str(m+1))
    plt.xlabel('E (MeV)')
    plt.ylabel('E^2 dF/dE (cm^-2*s^-1*sr^-1*MeV^1)')
    zipF=zip.ZipFile('Proton_F%s.zip'%str(m+1),'w')
    for i in range(len(names[m])):
        file=open('ProtonF%s_%s.txt'%(m+1,i+1),'w')
        xi=[]
        yi=[]
        for k in range(len(result[i])/2):
            xi.append(float(result[i][k][0]))
            yi.append(pow(xi[k],2)*float(result[i][k][1]))
            file.write('%10.4f    %10.4f'%(xi[k],yi[k]))
        file.close()
        zipF.write('ProtonF%s_%s.txt'%(m+1,i+1))
        plt.plot(xi,yi,lines[i],label='F%d'%i)
    zipF.close()
    plt.legend(loc='lower left')
    plt.yscale('log')
    plt.xscale('log')
    plt.savefig('ProtontiF%s.pdf'%str(m+1))
    plt.close()

for m in range(len(names)):
    msg=[]
    result=[[len(names[m])]]
    for i in range(len(names[m])):
        msg.append('')
        result.append(0)
        msg[i],result[i]=gHH.gplot('','./','54_091a00'+names[m][i]+'.gz',*BCratio)
        #print(msg[i])
    plt.figure('BC ratio F%s'%str(m+1))
    plt.xlabel('E (MeV)')
    plt.ylabel('B/C')
    zipF=zip.ZipFile('BCRatio_F%s.zip'%str(m+1),'w')
    for i in range(len(names[m])):
        fileBCratio=open('BCratioF%s_%s.txt'%(m+1,i+1),'w')
        xi=[]
        yi=[]
        for k in range(len(result[i])/2):
            xi.append(float(result[i][k][0]))
            yi.append(float(result[i][k][1]))
            fileBCratio.write('%10.4f    %10.4f'%(xi[k],yi[k]))
        fileBCratio.close()
        zipF.write('BCratioF%s_%s.txt'%(m+1,i+1))
        plt.plot(xi,yi,lines[i],label='F%d'%i)
    zipF.close()
    plt.legend(loc='lower left')
    plt.yscale('log')
    plt.xscale('log')
    plt.savefig('BCratioF%s.pdf'%str(m+1))
    plt.close()
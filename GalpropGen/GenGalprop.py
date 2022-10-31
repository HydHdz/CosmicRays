#Module for compressing into zip file
import zipfile as zip

#Opening base files
namebase="GalpropGen/basefile"
basefile=['','','','','']
for i in range(1,6):
    basefile[i-1]=open(namebase+str(i),'r')
    #print basefile[i-1].read()

#This function writes the missing parts of the file    
def writedef(l,fil):
    if(l==1):
        fil.write('\nz_min                = -05.6     min z')
        fil.write('\nz_max                = +05.6     max z\n')
    elif(l==2):
        fil.write('\nISRF_factors         = 1.36,1.36,1.0     ISRF factors for IC calculation: optical, FIR, CMB')
        fil.write('\nsynchrotron          = 0     1=compute synchrotron')
        fil.write('\nnu_synch_min         = 1.0e6     min synchrotron frequency (Hz)')
        fil.write('\nnu_synch_max         = 1.0e10     max synchrotron frequency (Hz)\n')
    elif(l==3):
        fil.write('\nDM_double0           = 0.0     not used')
        fil.write('\nDM_double1           = 0.0     not used\n')
    elif(l==4):
        fil.write('\nD0_xx                = 4.85e28     diffusion coefficient at reference rigidity')
        fil.write('\nD_rigid_br           = 4.0e3     reference rigidity for diffusion coefficient, MV')
        fil.write('\nD_g_1                = 0.40     diffusion coefficient index below reference rigidity')
        fil.write('\nD_g_2                = 0.40     diffusion coefficient index above reference rigidity')
        fil.write('\ndiff_reacc           = 1     1=include diffusive reacceleration')
        fil.write('\nv_Alfven             = 24.0     Alfven speed in km s^{-1}')
        fil.write('\ndamping_p0           = 1.0e6     some rigidity, MV, (where CR density is low)')
        fil.write('\ndamping_const_G      = 0.02     a const derived from fitting B/C')
        fil.write('\ndamping_max_path_L   = 3.0e21     Lmax~1 kpc, max free path')
        fil.write('\nconvection           = 1     1=include convection')
        fil.write('\nv0_conv              = 0.0     V0 convection in km s^-1')
        fil.write('\ndvdz_conv            = 1.0     dV/dz=grad V in km s^-1 kpc^-1')
        fil.write('\nnuc_rigid_br         = 11.66e3    reference rigidity for primary nucleus injection index in MV')
        fil.write('\nnuc_g_1              = 1.88     nucleus injection index below reference rigidity')
        fil.write('\nnuc_g_2              = 2.38     nucleus injection index above reference rigidity')
        fil.write('\ninj_spectrum_type    = rigidity     rigidity||beta_rig||Etot nucleon injection spectrum tipe')
        fil.write('\nelectron_g_0         = 1.60     electron injection index below electron_rigid_br0')
        fil.write('\nelectron_rigid_br0   = 2.178e3     reference rigidity0 for electron injection index in MV')
        fil.write('\nelectron_g_1         = 2.4277     electron injection index between electron_rigid_br0 and electron_rigid_br')
        fil.write('\nelectron_rigid_br    = 2.23e6     reference rigidity for electron injection index in MV')
        fil.write('\nelectron_g_2         = 4.00     electron injection index above reference rigidity\n')

# This function writes variations of parameters
def writevar(l,fil,r,s):
    if(l==1):
        fil.write('\nz_min                = -0%3.1f     min z'%r)
        fil.write('\nz_max                = +0%3.1f     max z\n'%r)
    elif(l==2):
        fil.write('\nISRF_factors         = %4.2f,%4.2f,1.0     ISRF factors for IC calculation: optical, FIR, CMB'%(r,r))
        fil.write('\nsynchrotron          = 0     1=compute synchrotron')
        fil.write('\nnu_synch_min         = 1.0e6     min synchrotron frequency (Hz)')
        fil.write('\nnu_synch_max         = %6.1e     max synchrotron frequency (Hz)\n'%(pow(10,s)))
    elif(l==3):
        fil.write('\nDM_double0           = %4.1f     not used'%r)
        fil.write('\nDM_double1           = %4.2f     not used\n'%s)
    elif(l==4):
        fil.write('\nD0_xx                = %7.2e     diffusion coefficient at reference rigidity'%r)
        fil.write('\nD_rigid_br           = 4.0e3     reference rigidity for diffusion coefficient, MV')
        fil.write('\nD_g_1                = 0.40     diffusion coefficient index below reference rigidity')
        fil.write('\nD_g_2                = 0.40     diffusion coefficient index above reference rigidity')
        fil.write('\ndiff_reacc           = 1     1=include diffusive reacceleration')
        fil.write('\nv_Alfven             = 24.0     Alfven speed in km s^{-1}')
        fil.write('\ndamping_p0           = 1.0e6     some rigidity, MV, (where CR density is low)')
        fil.write('\ndamping_const_G      = 0.02     a const derived from fitting B/C')
        fil.write('\ndamping_max_path_L   = 3.0e21     Lmax~1 kpc, max free path')
        fil.write('\nconvection           = 1     1=include convection')
        fil.write('\nv0_conv              = 0.0     V0 convection in km s^-1')
        fil.write('\ndvdz_conv            = 1.0     dV/dz=grad V in km s^-1 kpc^-1')
        fil.write('\nnuc_rigid_br         = 11.66e3    reference rigidity for primary nucleus injection index in MV')
        fil.write('\nnuc_g_1              = 1.88     nucleus injection index below reference rigidity')
        fil.write('\nnuc_g_2              = 2.38     nucleus injection index above reference rigidity')
        fil.write('\ninj_spectrum_type    = rigidity     rigidity||beta_rig||Etot nucleon injection spectrum tipe')
        fil.write('\nelectron_g_0         = 1.60     electron injection index below electron_rigid_br0')
        fil.write('\nelectron_rigid_br0   = 2.178e3     reference rigidity0 for electron injection index in MV')
        fil.write('\nelectron_g_1         = 2.4277     electron injection index between electron_rigid_br0 and electron_rigid_br')
        fil.write('\nelectron_rigid_br    = 2.23e6     reference rigidity for electron injection index in MV')
        fil.write('\nelectron_g_2         = 4.00     electron injection index above reference rigidity\n')
    elif(l==5):
        fil.write('\nD0_xx                = 4.85e28     diffusion coefficient at reference rigidity')
        fil.write('\nD_rigid_br           = 4.0e3     reference rigidity for diffusion coefficient, MV')
        fil.write('\nD_g_1                = %4.2f     diffusion coefficient index below reference rigidity'%r)
        fil.write('\nD_g_2                = %4.2f     diffusion coefficient index above reference rigidity'%r)
        fil.write('\ndiff_reacc           = 1     1=include diffusive reacceleration')
        fil.write('\nv_Alfven             = 24.0     Alfven speed in km s^{-1}')
        fil.write('\ndamping_p0           = 1.0e6     some rigidity, MV, (where CR density is low)')
        fil.write('\ndamping_const_G      = 0.02     a const derived from fitting B/C')
        fil.write('\ndamping_max_path_L   = 3.0e21     Lmax~1 kpc, max free path')
        fil.write('\nconvection           = 1     1=include convection')
        fil.write('\nv0_conv              = 0.0     V0 convection in km s^-1')
        fil.write('\ndvdz_conv            = 1.0     dV/dz=grad V in km s^-1 kpc^-1')
        fil.write('\nnuc_rigid_br         = 11.66e3    reference rigidity for primary nucleus injection index in MV')
        fil.write('\nnuc_g_1              = 1.88     nucleus injection index below reference rigidity')
        fil.write('\nnuc_g_2              = 2.38     nucleus injection index above reference rigidity')
        fil.write('\ninj_spectrum_type    = rigidity     rigidity||beta_rig||Etot nucleon injection spectrum tipe')
        fil.write('\nelectron_g_0         = 1.60     electron injection index below electron_rigid_br0')
        fil.write('\nelectron_rigid_br0   = 2.178e3     reference rigidity0 for electron injection index in MV')
        fil.write('\nelectron_g_1         = 2.4277     electron injection index between electron_rigid_br0 and electron_rigid_br')
        fil.write('\nelectron_rigid_br    = 2.23e6     reference rigidity for electron injection index in MV')
        fil.write('\nelectron_g_2         = 4.00     electron injection index above reference rigidity\n')
    elif(l==6):
        fil.write('\nD0_xx                = 4.85e28     diffusion coefficient at reference rigidity')
        fil.write('\nD_rigid_br           = 4.0e3     reference rigidity for diffusion coefficient, MV')
        fil.write('\nD_g_1                = 0.40     diffusion coefficient index below reference rigidity')
        fil.write('\nD_g_2                = 0.40     diffusion coefficient index above reference rigidity')
        fil.write('\ndiff_reacc           = 1     1=include diffusive reacceleration')
        fil.write('\nv_Alfven             = %4.1f     Alfven speed in km s^{-1}'%r)
        fil.write('\ndamping_p0           = 1.0e6     some rigidity, MV, (where CR density is low)')
        fil.write('\ndamping_const_G      = 0.02     a const derived from fitting B/C')
        fil.write('\ndamping_max_path_L   = 3.0e21     Lmax~1 kpc, max free path')
        fil.write('\nconvection           = 1     1=include convection')
        fil.write('\nv0_conv              = 0.0     V0 convection in km s^-1')
        fil.write('\ndvdz_conv            = 1.0     dV/dz=grad V in km s^-1 kpc^-1')
        fil.write('\nnuc_rigid_br         = 11.66e3    reference rigidity for primary nucleus injection index in MV')
        fil.write('\nnuc_g_1              = 1.88     nucleus injection index below reference rigidity')
        fil.write('\nnuc_g_2              = 2.38     nucleus injection index above reference rigidity')
        fil.write('\ninj_spectrum_type    = rigidity     rigidity||beta_rig||Etot nucleon injection spectrum tipe')
        fil.write('\nelectron_g_0         = 1.60     electron injection index below electron_rigid_br0')
        fil.write('\nelectron_rigid_br0   = 2.178e3     reference rigidity0 for electron injection index in MV')
        fil.write('\nelectron_g_1         = 2.4277     electron injection index between electron_rigid_br0 and electron_rigid_br')
        fil.write('\nelectron_rigid_br    = 2.23e6     reference rigidity for electron injection index in MV')
        fil.write('\nelectron_g_2         = 4.00     electron injection index above reference rigidity\n')
    elif(l==7):
        fil.write('\nD0_xx                = 4.85e28     diffusion coefficient at reference rigidity')
        fil.write('\nD_rigid_br           = 4.0e3     reference rigidity for diffusion coefficient, MV')
        fil.write('\nD_g_1                = 0.40     diffusion coefficient index below reference rigidity')
        fil.write('\nD_g_2                = 0.40     diffusion coefficient index above reference rigidity')
        fil.write('\ndiff_reacc           = 1     1=include diffusive reacceleration')
        fil.write('\nv_Alfven             = 24.0     Alfven speed in km s^{-1}')
        fil.write('\ndamping_p0           = 1.0e6     some rigidity, MV, (where CR density is low)')
        fil.write('\ndamping_const_G      = 0.02     a const derived from fitting B/C')
        fil.write('\ndamping_max_path_L   = 3.0e21     Lmax~1 kpc, max free path')
        fil.write('\nconvection           = 1     1=include convection')
        fil.write('\nv0_conv              = 0.0     V0 convection in km s^-1')
        fil.write('\ndvdz_conv            = %3.1f     dV/dz=grad V in km s^-1 kpc^-1'%r)
        fil.write('\nnuc_rigid_br         = 11.66e3    reference rigidity for primary nucleus injection index in MV')
        fil.write('\nnuc_g_1              = 1.88     nucleus injection index below reference rigidity')
        fil.write('\nnuc_g_2              = 2.38     nucleus injection index above reference rigidity')
        fil.write('\ninj_spectrum_type    = rigidity     rigidity||beta_rig||Etot nucleon injection spectrum tipe')
        fil.write('\nelectron_g_0         = 1.60     electron injection index below electron_rigid_br0')
        fil.write('\nelectron_rigid_br0   = 2.178e3     reference rigidity0 for electron injection index in MV')
        fil.write('\nelectron_g_1         = 2.4277     electron injection index between electron_rigid_br0 and electron_rigid_br')
        fil.write('\nelectron_rigid_br    = 2.23e6     reference rigidity for electron injection index in MV')
        fil.write('\nelectron_g_2         = 4.00     electron injection index above reference rigidity\n')
    elif(l==8):
        fil.write('\nD0_xx                = 4.85e28     diffusion coefficient at reference rigidity')
        fil.write('\nD_rigid_br           = 4.0e3     reference rigidity for diffusion coefficient, MV')
        fil.write('\nD_g_1                = 0.40     diffusion coefficient index below reference rigidity')
        fil.write('\nD_g_2                = 0.40     diffusion coefficient index above reference rigidity')
        fil.write('\ndiff_reacc           = 1     1=include diffusive reacceleration')
        fil.write('\nv_Alfven             = 24.0     Alfven speed in km s^{-1}')
        fil.write('\ndamping_p0           = 1.0e6     some rigidity, MV, (where CR density is low)')
        fil.write('\ndamping_const_G      = 0.02     a const derived from fitting B/C')
        fil.write('\ndamping_max_path_L   = 3.0e21     Lmax~1 kpc, max free path')
        fil.write('\nconvection           = 1     1=include convection')
        fil.write('\nv0_conv              = 0.0     V0 convection in km s^-1')
        fil.write('\ndvdz_conv            = 1.0     dV/dz=grad V in km s^-1 kpc^-1')
        fil.write('\nnuc_rigid_br         = 11.66e3    reference rigidity for primary nucleus injection index in MV')
        fil.write('\nnuc_g_1              = %4.2f     nucleus injection index below reference rigidity'%r)
        fil.write('\nnuc_g_2              = %4.2f     nucleus injection index above reference rigidity'%s)
        fil.write('\ninj_spectrum_type    = rigidity     rigidity||beta_rig||Etot nucleon injection spectrum tipe')
        fil.write('\nelectron_g_0         = 1.60     electron injection index below electron_rigid_br0')
        fil.write('\nelectron_rigid_br0   = 2.178e3     reference rigidity0 for electron injection index in MV')
        fil.write('\nelectron_g_1         = 2.4277     electron injection index between electron_rigid_br0 and electron_rigid_br')
        fil.write('\nelectron_rigid_br    = 2.23e6     reference rigidity for electron injection index in MV')
        fil.write('\nelectron_g_2         = 4.00     electron injection index above reference rigidity\n')
    elif(l==9):
        fil.write('\nD0_xx                = 4.85e28     diffusion coefficient at reference rigidity')
        fil.write('\nD_rigid_br           = 4.0e3     reference rigidity for diffusion coefficient, MV')
        fil.write('\nD_g_1                = 0.40     diffusion coefficient index below reference rigidity')
        fil.write('\nD_g_2                = 0.40     diffusion coefficient index above reference rigidity')
        fil.write('\ndiff_reacc           = 1     1=include diffusive reacceleration')
        fil.write('\nv_Alfven             = 24.0     Alfven speed in km s^{-1}')
        fil.write('\ndamping_p0           = 1.0e6     some rigidity, MV, (where CR density is low)')
        fil.write('\ndamping_const_G      = 0.02     a const derived from fitting B/C')
        fil.write('\ndamping_max_path_L   = 3.0e21     Lmax~1 kpc, max free path')
        fil.write('\nconvection           = 1     1=include convection')
        fil.write('\nv0_conv              = 0.0     V0 convection in km s^-1')
        fil.write('\ndvdz_conv            = 1.0     dV/dz=grad V in km s^-1 kpc^-1')
        fil.write('\nnuc_rigid_br         = 11.66e3    reference rigidity for primary nucleus injection index in MV')
        fil.write('\nnuc_g_1              = 1.88     nucleus injection index below reference rigidity')
        fil.write('\nnuc_g_2              = 2.38     nucleus injection index above reference rigidity')
        fil.write('\ninj_spectrum_type    = rigidity     rigidity||beta_rig||Etot nucleon injection spectrum tipe')
        fil.write('\nelectron_g_0         = %4.2f     electron injection index below electron_rigid_br0'%r)
        fil.write('\nelectron_rigid_br0   = 2.178e3     reference rigidity0 for electron injection index in MV')
        fil.write('\nelectron_g_1         = 2.4277     electron injection index between electron_rigid_br0 and electron_rigid_br')
        fil.write('\nelectron_rigid_br    = 2.23e6     reference rigidity for electron injection index in MV')
        fil.write('\nelectron_g_2         = 4.00     electron injection index above reference rigidity\n')
    elif(l==10):
        fil.write('\nD0_xx                = 4.85e28     diffusion coefficient at reference rigidity')
        fil.write('\nD_rigid_br           = 4.0e3     reference rigidity for diffusion coefficient, MV')
        fil.write('\nD_g_1                = 0.40     diffusion coefficient index below reference rigidity')
        fil.write('\nD_g_2                = 0.40     diffusion coefficient index above reference rigidity')
        fil.write('\ndiff_reacc           = 1     1=include diffusive reacceleration')
        fil.write('\nv_Alfven             = 24.0     Alfven speed in km s^{-1}')
        fil.write('\ndamping_p0           = 1.0e6     some rigidity, MV, (where CR density is low)')
        fil.write('\ndamping_const_G      = 0.02     a const derived from fitting B/C')
        fil.write('\ndamping_max_path_L   = 3.0e21     Lmax~1 kpc, max free path')
        fil.write('\nconvection           = 1     1=include convection')
        fil.write('\nv0_conv              = 0.0     V0 convection in km s^-1')
        fil.write('\ndvdz_conv            = 1.0     dV/dz=grad V in km s^-1 kpc^-1')
        fil.write('\nnuc_rigid_br         = 11.66e3    reference rigidity for primary nucleus injection index in MV')
        fil.write('\nnuc_g_1              = 1.88     nucleus injection index below reference rigidity')
        fil.write('\nnuc_g_2              = 2.38     nucleus injection index above reference rigidity')
        fil.write('\ninj_spectrum_type    = rigidity     rigidity||beta_rig||Etot nucleon injection spectrum tipe')
        fil.write('\nelectron_g_0         = 1.60     electron injection index below electron_rigid_br0')
        fil.write('\nelectron_rigid_br0   = %7.3e     reference rigidity0 for electron injection index in MV'%r)
        fil.write('\nelectron_g_1         = 2.4277     electron injection index between electron_rigid_br0 and electron_rigid_br')
        fil.write('\nelectron_rigid_br    = 2.23e6     reference rigidity for electron injection index in MV')
        fil.write('\nelectron_g_2         = 4.00     electron injection index above reference rigidity\n')
    elif(l==11):
        fil.write('\nD0_xx                = 4.85e28     diffusion coefficient at reference rigidity')
        fil.write('\nD_rigid_br           = 4.0e3     reference rigidity for diffusion coefficient, MV')
        fil.write('\nD_g_1                = 0.40     diffusion coefficient index below reference rigidity')
        fil.write('\nD_g_2                = 0.40     diffusion coefficient index above reference rigidity')
        fil.write('\ndiff_reacc           = 1     1=include diffusive reacceleration')
        fil.write('\nv_Alfven             = 24.0     Alfven speed in km s^{-1}')
        fil.write('\ndamping_p0           = 1.0e6     some rigidity, MV, (where CR density is low)')
        fil.write('\ndamping_const_G      = 0.02     a const derived from fitting B/C')
        fil.write('\ndamping_max_path_L   = 3.0e21     Lmax~1 kpc, max free path')
        fil.write('\nconvection           = 1     1=include convection')
        fil.write('\nv0_conv              = 0.0     V0 convection in km s^-1')
        fil.write('\ndvdz_conv            = 1.0     dV/dz=grad V in km s^-1 kpc^-1')
        fil.write('\nnuc_rigid_br         = 11.66e3    reference rigidity for primary nucleus injection index in MV')
        fil.write('\nnuc_g_1              = 1.88     nucleus injection index below reference rigidity')
        fil.write('\nnuc_g_2              = 2.38     nucleus injection index above reference rigidity')
        fil.write('\ninj_spectrum_type    = rigidity     rigidity||beta_rig||Etot nucleon injection spectrum tipe')
        fil.write('\nelectron_g_0         = 1.60     electron injection index below electron_rigid_br0')
        fil.write('\nelectron_rigid_br0   = 2.178e3     reference rigidity0 for electron injection index in MV')
        fil.write('\nelectron_g_1         = %6.4f     electron injection index between electron_rigid_br0 and electron_rigid_br'%r)
        fil.write('\nelectron_rigid_br    = 2.23e6     reference rigidity for electron injection index in MV')
        fil.write('\nelectron_g_2         = 4.00     electron injection index above reference rigidity\n')
    elif(l==12):
        fil.write('\nD0_xx                = 4.85e28     diffusion coefficient at reference rigidity')
        fil.write('\nD_rigid_br           = 4.0e3     reference rigidity for diffusion coefficient, MV')
        fil.write('\nD_g_1                = 0.40     diffusion coefficient index below reference rigidity')
        fil.write('\nD_g_2                = 0.40     diffusion coefficient index above reference rigidity')
        fil.write('\ndiff_reacc           = 1     1=include diffusive reacceleration')
        fil.write('\nv_Alfven             = 24.0     Alfven speed in km s^{-1}')
        fil.write('\ndamping_p0           = 1.0e6     some rigidity, MV, (where CR density is low)')
        fil.write('\ndamping_const_G      = 0.02     a const derived from fitting B/C')
        fil.write('\ndamping_max_path_L   = 3.0e21     Lmax~1 kpc, max free path')
        fil.write('\nconvection           = 1     1=include convection')
        fil.write('\nv0_conv              = 0.0     V0 convection in km s^-1')
        fil.write('\ndvdz_conv            = 1.0     dV/dz=grad V in km s^-1 kpc^-1')
        fil.write('\nnuc_rigid_br         = 11.66e3    reference rigidity for primary nucleus injection index in MV')
        fil.write('\nnuc_g_1              = 1.88     nucleus injection index below reference rigidity')
        fil.write('\nnuc_g_2              = 2.38     nucleus injection index above reference rigidity')
        fil.write('\ninj_spectrum_type    = rigidity     rigidity||beta_rig||Etot nucleon injection spectrum tipe')
        fil.write('\nelectron_g_0         = 1.60     electron injection index below electron_rigid_br0')
        fil.write('\nelectron_rigid_br0   = 2.178e3     reference rigidity0 for electron injection index in MV')
        fil.write('\nelectron_g_1         = 2.4277     electron injection index between electron_rigid_br0 and electron_rigid_br')
        fil.write('\nelectron_rigid_br    = %6.2e     reference rigidity for electron injection index in MV'%r)
        fil.write('\nelectron_g_2         = 4.00     electron injection index above reference rigidity\n')
    elif(l==13):
        fil.write('\nD0_xx                = 4.85e28     diffusion coefficient at reference rigidity')
        fil.write('\nD_rigid_br           = 4.0e3     reference rigidity for diffusion coefficient, MV')
        fil.write('\nD_g_1                = 0.40     diffusion coefficient index below reference rigidity')
        fil.write('\nD_g_2                = 0.40     diffusion coefficient index above reference rigidity')
        fil.write('\ndiff_reacc           = 1     1=include diffusive reacceleration')
        fil.write('\nv_Alfven             = 24.0     Alfven speed in km s^{-1}')
        fil.write('\ndamping_p0           = 1.0e6     some rigidity, MV, (where CR density is low)')
        fil.write('\ndamping_const_G      = 0.02     a const derived from fitting B/C')
        fil.write('\ndamping_max_path_L   = 3.0e21     Lmax~1 kpc, max free path')
        fil.write('\nconvection           = 1     1=include convection')
        fil.write('\nv0_conv              = 0.0     V0 convection in km s^-1')
        fil.write('\ndvdz_conv            = 1.0     dV/dz=grad V in km s^-1 kpc^-1')
        fil.write('\nnuc_rigid_br         = 11.66e3    reference rigidity for primary nucleus injection index in MV')
        fil.write('\nnuc_g_1              = 1.88     nucleus injection index below reference rigidity')
        fil.write('\nnuc_g_2              = 2.38     nucleus injection index above reference rigidity')
        fil.write('\ninj_spectrum_type    = rigidity     rigidity||beta_rig||Etot nucleon injection spectrum tipe')
        fil.write('\nelectron_g_0         = 1.60     electron injection index below electron_rigid_br0')
        fil.write('\nelectron_rigid_br0   = 2.178e3     reference rigidity0 for electron injection index in MV')
        fil.write('\nelectron_g_1         = 2.4277     electron injection index between electron_rigid_br0 and electron_rigid_br')
        fil.write('\nelectron_rigid_br    = 2.23e6     reference rigidity for electron injection index in MV')
        fil.write('\nelectron_g_2         = %4.2f     electron injection index above reference rigidity\n'%r)

#Changing z_min, z_max
file1=['','','','','']
name1='galdef_54_F1'
zipF1=zip.ZipFile('galdef_54_F1.zip','w')
for i in range(1,6):
    #basefile[i-1]=open(namebase+str(i),'r')
    file1[i-1]=open(name1+"_"+str(i),'w')
    for j in range(1,6):
        file1[i-1].write(''.join(basefile[j-1]))
        if(j==1):
            x=float(3+3*float(i-1)/4)
            writevar(j,file1[i-1],x,0)
        else:
            writedef(j,file1[i-1])
        basefile[j-1].seek(0)
    file1[i-1].close()
    zipF1.write(name1+"_"+str(i))
zipF1.close()
    
#Changing ISRF factors
file2=['','','','','']
name2='galdef_54_F2'
zipF2=zip.ZipFile('galdef_54_F2.zip','w')
for i in range(1,6):
    #basefile[i-1]=open(namebase+str(i),'r')
    file2[i-1]=open(name2+"_"+str(i),'w')
    for j in range(1,6):
        file2[i-1].write(''.join(basefile[j-1]))
        if(j==2):
            x=float(1.0+0.36*float(i-1)/4)
            writevar(j,file2[i-1],x,10)
        else:
            writedef(j,file2[i-1])
        basefile[j-1].seek(0)
    file2[i-1].close()
    zipF2.write(name2+"_"+str(i))
zipF2.close()

#Changing max synchrotron freq
file3=['','','','','']
name3='galdef_54_F3'
zipF3=zip.ZipFile('galdef_54_F3.zip','w')
for i in range(1,6):
    file3[i-1]=open(name3+"_"+str(i),'w')
    for j in range(1,6):
        file3[i-1].write(''.join(basefile[j-1]))
        if(j==2):
            x=float(10+2*float(i-1)/4)
            writevar(j,file3[i-1],1.36,x)
        else:
            writedef(j,file3[i-1])
        basefile[j-1].seek(0)
    file3[i-1].close()
    zipF3.write(name3+"_"+str(i))
zipF3.close()
    

#Changing DM double parameters
file4=['','','','','']
name4='galdef_54_F4'
zipF4=zip.ZipFile('galdef_54_F4.zip','w')
for i in range(1,6):
    file4[i-1]=open(name4+"_"+str(i),'w')
    for j in range(1,6):
        file4[i-1].write(''.join(basefile[j-1]))
        if(j==3):
            x=float(20.0*float(i-1)/4)
            y=float(0.30*float(i-1)/4)
            writevar(j,file4[i-1],x,y)
        else:
            writedef(j,file4[i-1])
        basefile[j-1].seek(0)
    file4[i-1].close()
    zipF4.write(name4+"_"+str(i))
zipF4.close()
    


#Changing D0_xx
file5=['','','','','']
name5='galdef_54_F5'
zipF5=zip.ZipFile('galdef_54_F5.zip','w')
for i in range(1,6):
    file5[i-1]=open(name5+"_"+str(i),'w')
    for j in range(1,6):
        file5[i-1].write(''.join(basefile[j-1]))
        if(j==4):
            x=float((2.67+2.18*float(i-1)/4)*pow(10,28))
            writevar(j,file5[i-1],x,0)
        else:
            writedef(j,file5[i-1])
        basefile[j-1].seek(0)
    file5[i-1].close()
    zipF5.write(name5+"_"+str(i))
zipF5.close()
    

#Changing diffussion coef. D_g_1 and 2
file6=['','','','','']
name6='galdef_54_F6'
zipF6=zip.ZipFile('galdef_54_F6.zip','w')
for i in range(1,6):
    file6[i-1]=open(name6+"_"+str(i),'w')
    for j in range(1,6):
        file6[i-1].write(''.join(basefile[j-1]))
        if(j==4):
            x=float(0.4+float((i-1))*0.1/4.0)
            writevar(j+1,file6[i-1],x,0)
        else:
            writedef(j,file6[i-1])
        basefile[j-1].seek(0)
    file6[i-1].close()
    zipF6.write(name6+"_"+str(i))
zipF6.close()

#Changing Alfen velocity
file7=['','','','','']
name7='galdef_54_F7'
zipF7=zip.ZipFile('galdef_54_F7.zip','w')
for i in range(1,6):
    file7[i-1]=open(name7+"_"+str(i),'w')
    for j in range(1,6):
        file7[i-1].write(''.join(basefile[j-1]))
        if(j==4):
            x=float(22.0+float((i-1))*2.0/4.0)
            writevar(j+2,file7[i-1],x,0)
        else:
            writedef(j,file7[i-1])
        basefile[j-1].seek(0)
    file7[i-1].close()
    zipF7.write(name7+"_"+str(i))
zipF7.close()
    
    
#Changing velocity gradient
file8=['','','','','']
name8='galdef_54_F8'
zipF8=zip.ZipFile('galdef_54_F8.zip','w')
for i in range(1,6):
    file8[i-1]=open(name8+"_"+str(i),'w')
    for j in range(1,6):
        file8[i-1].write(''.join(basefile[j-1]))
        if(j==4):
            x=float(1.0+float((i-1))*8.0/4.0)
            writevar(j+3,file8[i-1],x,0)
        else:
            writedef(j,file8[i-1])
        basefile[j-1].seek(0)
    file8[i-1].close()
    zipF8.write(name8+"_"+str(i))
zipF8.close()
    
    
#Changing nucleus injection index
file9=['','','','','']
name9='galdef_54_F9'
zipF9=zip.ZipFile('galdef_54_F9.zip','w')
for i in range(1,6):
    file9[i-1]=open(name9+"_"+str(i),'w')
    for j in range(1,6):
        file9[i-1].write(''.join(basefile[j-1]))
        if(j==4):
            x=float(0.87+float((i-1))*0.01/4.0)
            y=float(2.38+float((i-1))*0.07/4.0)
            writevar(j+4,file9[i-1],x,y)
        else:
            writedef(j,file9[i-1])
        basefile[j-1].seek(0)
    file9[i-1].close()
    zipF9.write(name9+"_"+str(i))
zipF9.close()
    
#Changing electron injection index
file10=['','','','','']
name10='galdef_54_F10'
zipF10=zip.ZipFile('galdef_54_F10.zip','w')
for i in range(1,6):
    file10[i-1]=open(name10+"_"+str(i),'w')
    for j in range(1,6):
        file10[i-1].write(''.join(basefile[j-1]))
        if(j==4):
            x=float(1.60+float((i-1))*0.65/4.0)
            writevar(j+5,file10[i-1],x,0)
        else:
            writedef(j,file10[i-1])
        basefile[j-1].seek(0)
    file10[i-1].close()
    zipF10.write(name10+"_"+str(i))
zipF10.close()

#Changing electron injection index
file11=['','','','','']
name11='galdef_54_F11'
zipF11=zip.ZipFile('galdef_54_F11.zip','w')
for i in range(1,6):
    file11[i-1]=open(name11+"_"+str(i),'w')
    for j in range(1,6):
        file11[i-1].write(''.join(basefile[j-1]))
        if(j==4):
            x=float((2.178+float((i-1))*2.022/4.0)*10**3)
            writevar(j+6,file11[i-1],x,0)
        else:
            writedef(j,file11[i-1])
        basefile[j-1].seek(0)
    file11[i-1].close()
    zipF11.write(name11+"_"+str(i))
zipF11.close()

#Changing electron injection index
file12=['','','','','']
name12='galdef_54_F12'
zipF12=zip.ZipFile('galdef_54_F12.zip','w')
for i in range(1,6):
    file12[i-1]=open(name12+"_"+str(i),'w')
    for j in range(1,6):
        file12[i-1].write(''.join(basefile[j-1]))
        if(j==4):
            x=float(2.4277+float((i-1))*0.1523/4.0)
            writevar(j+7,file12[i-1],x,0)
        else:
            writedef(j,file12[i-1])
        basefile[j-1].seek(0)
    file12[i-1].close()
    zipF12.write(name12+"_"+str(i))
zipF12.close()

#Changing electron injection index
file13=['','','','','']
name13='galdef_54_F13'
zipF13=zip.ZipFile('galdef_54_F13.zip','w')
for i in range(1,6):
    file13[i-1]=open(name13+"_"+str(i),'w')
    for j in range(1,6):
        file13[i-1].write(''.join(basefile[j-1]))
        if(j==4):
            x=float((2.23+float((i-1))*0.27/4.0)*10**3)
            writevar(j+8,file13[i-1],x,0)
        else:
            writedef(j,file13[i-1])
        basefile[j-1].seek(0)
    file13[i-1].close()
    zipF13.write(name13+"_"+str(i))
zipF13.close()

#Changing electron injection index
file14=['','','','','']
name14='galdef_54_F14'
zipF14=zip.ZipFile('galdef_54_F14.zip','w')
for i in range(1,6):
    file14[i-1]=open(name14+"_"+str(i),'w')
    for j in range(1,6):
        file14[i-1].write(''.join(basefile[j-1]))
        if(j==4):
            x=float(3.7+float((i-1))*0.3/4.0)
            writevar(j+9,file14[i-1],x,0)
        else:
            writedef(j,file14[i-1])
        basefile[j-1].seek(0)
    file14[i-1].close()
    zipF14.write(name14+"_"+str(i))
zipF14.close()
    

# #Closing basefiles
for i in range(1,5):
    basefile[i-1].close()

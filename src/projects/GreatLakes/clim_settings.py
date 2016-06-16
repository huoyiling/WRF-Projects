'''
Created on Jun 4, 2016

A module that provides various project specific definitions, mainly related to experiments and plotting. 

@author:  Andre R. Erler, GPL v3
'''

# external imports
import matplotlib as mpl
# internal imports
from geodata.misc import AttrDict
from plotting import figure
from clim import plots, load_ens
from WRF_experiments import WRF_ens, WRF_exps
from projects.CESM_experiments import CESM_ens, CESM_exps


# variable collections
wetday_extensions = load_ens.wetday_extensions[:3]
variables_rc = dict(); VL = load_ens.VL
# mostly for hydrological analysis
variables_rc['temp']            = VL(vars=('T2', 'Tmax', 'Tmin'), files=('srfc','xtrm',), label='2m Temperature')
# variables_rc['temp']          = VL(vars=('T2',), files=('srfc',), label='2m Temperature')
variables_rc['precip_obs']      = VL(vars=('precip', 'solprec', 'wetfrq_010'), files=('hydro',), label='Precipitation')
variables_rc['precip_xtrm_obs'] = VL(vars=('MaxPrecip_1d', 'MaxPrecip_5d', 'wetprec_010'), files=('hydro',), label='Precipitation')
variables_rc['precip']          = VL(vars=('precip', 'preccu', 'solprec'), files=('hydro',), label='Precipitation')
variables_rc['precip_xtrm']     = VL(vars=('MaxPrecip_1d', 'MaxPrecip_5d', 'MaxPreccu_1d'), files=('hydro',), label='Precipitation')
variables_rc['precip_cesm']     = VL(vars=('MaxPrecip_1d', 'MaxPreccu_1d', ), files=('hydro',), label='Precipitation')
variables_rc['precip_alt']      = VL(vars=('MaxPrecip_1d', 'MaxPrecnc_1d', 'MaxSolprec_1d'), files=('hydro',), label='Precipitation')
variables_rc['precip_types']    = VL(vars=('precip','preccu','precnc'), files=('hydro',), label='Water Flux')
variables_rc['precip_net']      = VL(vars=('precip','solprec','p-et'), files=('hydro',), label='Water Flux')
variables_rc['flux_snow']       = VL(vars=('precip','snwmlt','solprec'), files=('hydro',), label='Water Flux')
variables_rc['flux_days']       = VL(vars=('wetfrq_010','snwmlt','p-et'), files=('hydro',), label='Water Flux')
variables_rc['wetprec']         = VL(vars=['wetprec'+ext for ext in wetday_extensions], files=('hydro',), label='Wet-day Precip.')
variables_rc['wetdays']         = VL(vars=['wetfrq'+ext for ext in wetday_extensions], files=('hydro',), label='Wet-day Ratio')
variables_rc['CWD']             = VL(vars=['CWD'+ext for ext in wetday_extensions]+['CNWD'], files=('hydro',), label='Continuous Wet-days')
variables_rc['CDD']             = VL(vars=['CDD'+ext for ext in wetday_extensions[:-1]]+['CNDD'], files=('hydro',), label='Continuous Dry-days')
variables_rc['sfcflx']          = VL(vars=('p-et','snwmlt','waterflx',), files=('hydro',), label='Surface Flux')
variables_rc['runoff']          = VL(vars=('waterflx','sfroff','runoff'), files=('lsm','hydro'), label='Runoff')
variables_rc['runoff_flux']     = VL(vars=('runoff','snwmlt','p-et'), files=('lsm','hydro'), label='Water Flux')
variables_rc['heat']            = VL(vars=('hfx','lhfx','rSM'),files=('srfc','lsm'), label='Energy Flux')
variables_rc['evap']            = VL(vars=('p-et','evap','pet',), files=('hydro',), label='Water Flux')
variables_rc['spei']            = VL(vars=('precip','evap','pet',), files=('aux','hydro',), label='Water Flux')
variables_rc['Q2']              = VL(vars=('Q2',),files=('srfc',), label='2m Humidity')
variables_rc['aSM']             = VL(vars=('aSM',),files=('lsm',), label='Soil Moisture') 
variables_rc['rSM']             = VL(vars=('rSM',),files=('lsm',), label='Relative Soil Moisture')
# N.B.: Noah-MP does not have relative soil moisture and there is not much difference anyway
# mostly for extreme value analysis
variables_rc['hydro_eva']    = VL(vars=['precip', 'p-et', 'snwmlt', 'waterflx','sfroff','runoff','aSM'],
                                  files=['hydro','lsm'], label='')
variables_rc['precip_eva']   = VL(vars=['precip', 'MaxPrecip_1h', 'MaxPrecip_6h', 'MaxPrecip_1d', 'MaxPrecip_5d',
                                        'MaxWaterflx_5d', 'wetfrq', 'CDD', 'CWD'], files=['hydro','srfc'], label='Precipitation')
variables_rc['temp_eva']     = VL(vars=['T2', 'MaxT2', 'MaxTmax', 'MinTmin', 'MaxTmax_7d', 'MinTmin_7d', 
                                        'frzfrq', 'CFD', 'CDFD', 'CNFD'], files=['srfc','xtrm'], label='Temperature')                          
variables_rc['precip_short'] = VL(vars=['MaxPreccu_1h', 'MaxPrecnc_1h', 'MaxPrecip_6h', 'MaxPreccu_6h'], 
                                  files=['xtrm','srfc'], label='MaxPrecip')
variables_rc['precip_long']  = VL(vars=['MaxPrecip_1d', 'MaxPreccu_1d', 'MaxPrecip_5d',], 
                                  files=['hydro'], label='MaxPrecip')
variables_rc['precip_CDD']   = VL(vars=['CNDD','CNWD']+[var+threshold for threshold in wetday_extensions for var in 'CDD','CWD'], 
                                  files=['hydro'], label='CDD')


# station selection criteria
constraints_rc = dict()
constraints_rc['min_len'] = 15 # for valid climatology
constraints_rc['lat'] = (45,55) 
constraints_rc['max_zerr'] = 300 # can't use this, because we are loading EC data separately from WRF
constraints_rc['prov'] = ('ON')
constraints_rc['end_after'] = 1980
                        
# dataset collections
exps_rc = dict(); EX = load_ens.EX
exps_rc['obs']     = EX(name='obs',exps=['CRU','WSC'], styles=['-','-.'], title='Observations', 
                        master='CRU', reference='CRU', target=None)
exps_rc['erai']    = EX(name='erai',exps=['erai-g','erai-t'], styles=['--','-'], title='G & T, ERA-I',
                       master='erai-g', reference=None, target=None)
# initial condition ensembles
exps_rc['g-ens']   = EX(name='g-ens',exps=['g-ens','g-ens-2050','g-ens-2100'], 
                        styles=['-','-.','--'], title='G Ensemble Average (Hist., Mid-, End-Century)',
                        master='g-ens', reference=None, target=None)
exps_rc['t-ens']   = EX(name='t-ens',exps=['t-ens','t-ens-2050','t-ens-2100'], 
                        styles=['-','-.','--'], title='G Ensemble Average (Hist., Mid-, End-Century)',
                        master='t-ens', reference=None, target=None)
# G ensemble members
exps_rc['g-Z']     = EX(name='g-Z',exps=['g-ctrl','g-ctrl-2050','g-ctrl-2100'], 
                        styles=['-','-.','--'], title='WRF-Z (Hist., Mid-, End-Century)',
                        master='g-ctrl', reference=None, target=None)
exps_rc['g-A']     = EX(name='g-A',exps=['g-ens-A','g-ens-A-2050','g-ens-A-2100'], 
                        styles=['-','-.','--'], title='WRF-A (Hist., Mid-, End-Century)',
                        master='g-ens-A', reference=None, target=None)
exps_rc['g-B']     = EX(name='g-B',exps=['g-ens-B','g-ens-B-2050','g-ens-B-2100'], 
                        styles=['-','-.','--'], title='WRF-B (Hist., Mid-, End-Century)',
                        master='g-ens-B', reference=None, target=None)
exps_rc['g-C']     = EX(name='g-C',exps=['g-ens-C','g-ens-C-2050','g-ens-C-2100'], 
                        styles=['-','-.','--'], title='WRF-C (Hist., Mid-, End-Century)',
                        master='g-ens-C', reference=None, target=None)
# sea-ice experiments
# exps_rc['seaice']  = EX(name='seaice',exps=['g-ens-2050','g-seaice-2050','g-ens-2100','g-seaice-2100'],
#                         styles=['-.','--','-','.--','.-'], title='WRF (Mid-, End-Century; Ens. Avg., Sea-ice)',
#                         master=['g-ens-2050','g-ens-2100'], reference=None, target=None)
# exps_rc['si25']    = EX(name='si25',exps=['g-ens','g-ens-2050','g-seaice-2050'], 
#                         styles=[':','--','-'], title='WRF (Hist., Mid-Century; Ens. Avg., Sea-ice)',
#                         master='g-ens-2050', reference=None, target=None)
# exps_rc['si21']    = EX(name='si21',exps=['g-ens','g-ens-2100','g-seaice-2100'], 
#                         styles=[':','--','-'], title='WRF (Hist., End-Century; Ens. Avg., Sea-ice)',
#                         master='g-ens-2100', reference=None, target=None)
# physics ensemble
exps_rc['phys']    = EX(name='phys',exps=['phys-ens','phys-ens-2050','phys-ens-2100'], 
                        styles=['-','-.','--'], title='WRF Phys. Ens. (Hist., Mid-, End-Century)',
                        master='phys-ens', reference='phys-ens', target='phys-ens')
# physics ensemble members
exps_rc['gg-ctrl'] = EX(name='gg-ctrl', exps=['Observations', 'g-ctrl','gg-ctrl', 'g-ctrl-2050','gg-ctrl-2050'],
                        styles=['-','-.','--'], master='Observations', reference='Observations', target=None, title='')  
exps_rc['m-ctrl']  = EX(name='m-ctrl',  exps=['Observations', 'm-ctrl', 'm-ctrl-2050'],   
                        styles=['-','-.','--'], master='Observations', reference='Observations', target=None, title='')
exps_rc['mm-ctrl'] = EX(name='mm-ctrl', exps=['Observations', 'mm-ctrl', 'mm-ctrl-2050'], 
                        styles=['-','-.','--'], master='Observations', reference='Observations', target=None, title='')
exps_rc['t-ctrl']  = EX(name='t-ctrl',  exps=['Observations', 't-ctrl', 't-ctrl-2050'],
                        styles=['-','-.','--'], master='Observations', reference='Observations', target=None, title='')

# set default variable atts for load functions from load_ens
def loadShapeObservations(variable_atts=None, **kwargs):
  ''' wrapper for clim.load_ens.loadShapeObservations that sets variable lists '''
  if variable_atts is None: variable_atts = variables_rc
  return load_ens.loadShapeObservations(variable_atts=variable_atts, **kwargs)
def loadShapeEnsemble(variable_atts=None, **kwargs):
  ''' wrapper for clim.load_ens.loadShapeSimulations that sets experiment and variable lists '''
  if variable_atts is None: variable_atts = variables_rc  
  return load_ens.loadShapeEnsemble(variable_atts=variable_atts, WRF_exps=WRF_exps, CESM_exps=CESM_exps, 
                                    WRF_ens=WRF_ens, CESM_ens=CESM_ens, **kwargs)
def loadStationEnsemble(variable_atts=None, **kwargs):
  ''' wrapper for clim.load_ens.loadStationEnsemble that sets experiment and variable lists '''
  if variable_atts is None: variable_atts = variables_rc  
  return load_ens.loadStationEnsemble(variable_atts=variable_atts, WRF_exps=WRF_exps, CESM_exps=CESM_exps, 
                                      WRF_ens=WRF_ens, CESM_ens=CESM_ens, **kwargs)


## plot labels
plot_labels_rc = dict()
# datasets
plot_labels_rc['Unity']           = 'Uni. Obs.'
plot_labels_rc['Observations']    = 'EC Obs.'
plot_labels_rc['EC_1935']         = 'EC (1935)'
plot_labels_rc['EC_1965']         = 'EC (1965)'
plot_labels_rc['EC_1995']         = 'EC (1995)'
plot_labels_rc['Ens']             = 'CESM'  
plot_labels_rc['Ens-2050']        = 'CESM 2050' 
plot_labels_rc['Ens-2100']        = 'CESM 2100' 
plot_labels_rc['MEns']            = 'CESM*'  
plot_labels_rc['MEns-2050']       = 'CESM* 2050' 
plot_labels_rc['MEns-2100']       = 'CESM* 2100' 
plot_labels_rc['phys-ens']        = 'Phy Ens.' 
plot_labels_rc['phys-ens-2050']   = 'Phy 2050' 
plot_labels_rc['phys-ens-2100']   = 'Phy 2100' 
plot_labels_rc['phys-ens_d01']    = 'Phy (D1)'
# plot_labels_rc['g-ens']           = 'G Ens.'  
# plot_labels_rc['g-ens-2050']      = 'G 2050' 
# plot_labels_rc['g-ens-2100']      = 'G 2100' 
plot_labels_rc['g-ens']           = 'WRF Ens.'  
plot_labels_rc['g-ens-2050']      = 'WRF 2050' 
plot_labels_rc['g-ens-2100']      = 'WRF 2100' 
plot_labels_rc['erai-g']          = 'ERA-I G'  
plot_labels_rc['t-ens']           = 'T Ens.'
plot_labels_rc['t-ens-2050']      = 'T 2050'
plot_labels_rc['t-ens-2100']      = 'T 2100'
plot_labels_rc['erai-t']          = 'ERA-I T'   
# variables
plot_labels_rc['MaxPrecip_1d']    = 'Max Precip. (1d)'
plot_labels_rc['MaxPrecip_5d']    = 'Max Precip. (5d)'
plot_labels_rc['MaxPreccu_1d']    = 'Max Conv. (1d)'
plot_labels_rc['MaxSolprec_1d']   = 'Max Snow (1d)'
plot_labels_rc['MaxWaterFlx_1d']  = 'Max Flux (1d)'
plot_labels_rc['wetfrq_010']      = 'Wet-days'
plot_labels_rc['wetprec_010']     = 'Precip. Intensity'
plot_labels_rc['T2']              = 'T (2m)'   
plot_labels_rc['precip']          = 'Precip.'  
plot_labels_rc['liqprec']         = 'Liquid' 
plot_labels_rc['solprec']         = 'Snow' 
plot_labels_rc['dryprec']         = 'dryprec' 
plot_labels_rc['preccu']          = 'Conv.'  
plot_labels_rc['precnc']          = 'NC'  
plot_labels_rc['evap']            = 'ET'    
plot_labels_rc['p-et']            = 'Net Precip.'    
plot_labels_rc['pet']             = 'PET' 
plot_labels_rc['waterflx']        = 'Water Flux'
plot_labels_rc['snwmlt']          = 'Snow Melt' 
plot_labels_rc['runoff']          = 'Total Runoff' 
plot_labels_rc['ugroff']          = 'Undergr. R\'off' 
plot_labels_rc['sfroff']          = 'Surface Runoff' 
plot_labels_rc['Tmax']            = 'T (max)'    
plot_labels_rc['Tmin']            = 'T (min)'    
plot_labels_rc['hfx']             = 'Sens. Heat'     
plot_labels_rc['lhfx']            = 'Latent Heat'    
plot_labels_rc['Q2']              = 'Q (2m)'      
plot_labels_rc['aSM']             = 'aSM'     
plot_labels_rc['rSM']             = 'Soil Moist.'       


## custom default plot styles
obs_args = AttrDict(marker='o', linestyle=' ') # 5*mpl.rcParams['lines.linewidth']
rea_args = AttrDict(marker='^', markersize=mpl.rcParams['lines.markersize'], linestyle=' ') # 'small'
# datasets (mainly obs)
dataset_plotargs_rc = dict()
dataset_plotargs_rc['Observations'] =  obs_args
dataset_plotargs_rc['WSC']          =  obs_args
dataset_plotargs_rc['Unity']        =  obs_args
dataset_plotargs_rc['CRU']          =  obs_args
dataset_plotargs_rc['GPCC']         =  obs_args
dataset_plotargs_rc['CFSR']         =  rea_args
dataset_plotargs_rc['NARR']         =  rea_args
# variable settings
variable_plotargs_rc = dict()
variable_plotargs_rc['MaxPrecip_1d']   = AttrDict(color = 'green')
variable_plotargs_rc['MaxPrecip_5d']   = AttrDict(color = 'sienna')
variable_plotargs_rc['MaxPreccu_1d']   = AttrDict(color = 'magenta')
variable_plotargs_rc['MaxPrecnc_1d']   = AttrDict(color = 'grey')
variable_plotargs_rc['MaxSolprec_1d']  = AttrDict(color = 'blue')
variable_plotargs_rc['MaxWaterFlx_1d'] = AttrDict(color = 'blue')
variable_plotargs_rc['T2']             = AttrDict(color = 'green')
variable_plotargs_rc['precip']         = AttrDict(color = 'green')
variable_plotargs_rc['liqprec']        = AttrDict(color = 'cyan')
variable_plotargs_rc['solprec']        = AttrDict(color = 'blue')
variable_plotargs_rc['dryprec']        = AttrDict(color = 'green')
variable_plotargs_rc['preccu']         = AttrDict(color = 'magenta')
variable_plotargs_rc['precnc']         = AttrDict(color = 'coral')
variable_plotargs_rc['evap']           = AttrDict(color = 'red')
variable_plotargs_rc['p-et']           = AttrDict(color = 'red')
variable_plotargs_rc['pet']            = AttrDict(color = 'purple')
variable_plotargs_rc['waterflx']       = AttrDict(color = 'dodgerblue')
variable_plotargs_rc['snwmlt']         = AttrDict(color = 'orange')
variable_plotargs_rc['runoff']         = AttrDict(color = 'purple')
variable_plotargs_rc['ugroff']         = AttrDict(color = 'coral')
variable_plotargs_rc['sfroff']         = AttrDict(color = 'green')
variable_plotargs_rc['Tmax']           = AttrDict(color = 'red')
variable_plotargs_rc['Tmin']           = AttrDict(color = 'blue')
variable_plotargs_rc['hfx']            = AttrDict(color = 'red')
variable_plotargs_rc['lhfx']           = AttrDict(color = 'purple')
variable_plotargs_rc['Q2']             = AttrDict(color = 'blue')
variable_plotargs_rc['aSM']            = AttrDict(color = 'coral')
variable_plotargs_rc['rSM']            = AttrDict(color = 'green')
variable_plotargs_rc['CNWD']           = AttrDict(color = 'green')
variable_plotargs_rc['CNDD']           = AttrDict(color = 'green')
# add wet-day threshold dependent variables    
wetday_colors = ['steelblue', 'purple', 'crimson', 'orange']   
for wdext,color in zip(load_ens.wetday_extensions,wetday_colors):
  variable_plotargs_rc['wetprec'+wdext] = AttrDict(color = color)
  variable_plotargs_rc['wetfrq' +wdext] = AttrDict(color = color)
  variable_plotargs_rc['CWD'+wdext]     = AttrDict(color = color)
  variable_plotargs_rc['CDD' +wdext]    = AttrDict(color = color)

# wrapper with custom defaults to figure creator (plotargs and label positions)
def getFigAx(subplot, dataset_plotargs=None, variable_plotargs=None, plot_labels=None, xtop=None, yright=None, **kwargs):
  if dataset_plotargs is None: dataset_plotargs = dataset_plotargs_rc 
  if variable_plotargs is None: variable_plotargs = variable_plotargs_rc
  if plot_labels is None: plot_labels = plot_labels_rc
  return figure.getFigAx(subplot, dataset_plotargs=dataset_plotargs, variable_plotargs=variable_plotargs,
                         plot_labels=plot_labels, xtop=xtop, yright=yright, **kwargs)
climFigAx = getFigAx # alias for direct project import


## climatology plot and shape annotation
# defaults
shape_defaults_rc = AttrDict(heat=(-30,130), Q2=(0,20), aSM=(0.1,0.5), temp=(245,305), wetprec=(0,25), wetfrq=(0,100))
# specific settings
shape_specifics = dict()
shape_specifics['GLB']         = AttrDict(temp=(245,300), water=(-1.,5.), precip_net=(-0.5,5.5), precip_types=(-0.5,5.5), 
                                          precip_xtrm=(-1.,29.),
                                          runoff=(-0.5,2.5), runoff_flux=(-0.5,3.5), flux=(-0.5,3.5), flux_snow=(-0.5,3.5), 
                                          spei=(-1.5,5.5), evap=(-1.5,5.5))
shape_specifics['ARB']         = AttrDict(temp=(245,300), water=(-1.5,2.5), precip=(-0.5,3.5), precip_types=(-0.5,3.5), spei=(-1.5,5.5),
                                          runoff=(-1.2,2), flux=(-1.5,3.5), flux_alt=(-0.5,3.5), evap=(-1.5,5.5))
shape_specifics['CRB']         = AttrDict(temp=(255,305), water=(-3,6), precip=(-0.5,7.))
shape_specifics['FRB']         = AttrDict(temp=(255,300), water=(-2,7.), precip=(-1,7.), precip_types=(-1,7.), runoff=(-2,7), flux_alt=(-1,7.), spei=(-1,7.))
shape_specifics['NRB']         = AttrDict(temp=(245,305), water=(-1.4,2.2), precip=(-0.4,3.4), runoff=(-2.,2.), flux=(-2,5.5))
shape_specifics['PSB']         = AttrDict(temp=(255,295), water=(-2.,16.))
shape_specifics['NorthernPSB'] = AttrDict(temp=(255,295), water=(-2.,14.), precip=(-2,14))
shape_specifics['SouthernPSB'] = AttrDict(temp=(255,295), water=(-2.,16.), precip=(-2,16))
shape_specifics['Pacific']     = AttrDict(temp=(265,300), water=(-2,10)   , precip=(0,12)    , precip_xtrm=(0,60), precip_cesm=(0,60), precip_alt=(0,40), wetprec=(0,30), wetdays=(0,80), CWD=(0,25), CDD=(0,25))
shape_specifics['Coast']       = AttrDict(temp=(265,300), water=(-4,6)    , precip=(-1,8)    , precip_xtrm=(0,40), precip_cesm=(0,40), precip_alt=(0,40), wetprec=(0,30), wetdays=(0,80), CWD=(0,20), CDD=(0,31))
shape_specifics['Plateau']     = AttrDict(temp=(255,305), water=(-2.,2.)  , precip=(-0.5,2.5), precip_xtrm=(0,20), precip_cesm=(0,20), precip_alt=(0,20), wetprec=(0,30), wetdays=(0,80), CWD=(0,15), CDD=(0,25))
shape_specifics['Prairies']    = AttrDict(temp=(250,305), water=(-1.5,1.5), precip=(-0.5,3.5), precip_xtrm=(0,30), precip_cesm=(0,30), precip_alt=(0,30), wetprec=(0,30), wetdays=(0,80), CWD=(0,15), CDD=(0,25))
# add defaults to specifics
shape_annotation_rc = dict()
for basin,specs in shape_specifics.iteritems():
  atts = shape_defaults_rc.copy()
  atts.update(specs)
  atts.update(zip([key+'_obs' for key in atts.iterkeys()],atts.itervalues())) # add obs-only versions
  shape_annotation_rc[basin] = atts
  
# wrapper with custom defaults to figure creator (plotargs and label positions)
def climPlot(shape_annotation=None, shape_defaults=None, variable_atts=None, **kwargs):
  if shape_annotation is None: shape_annotation = shape_annotation_rc 
  if shape_defaults is None: shape_defaults = shape_defaults_rc
  if variable_atts is None: variable_atts = variables_rc
  return plots.climPlot(shape_annotation=shape_annotation, shape_defaults=shape_defaults, 
                        variable_atts=variable_atts, **kwargs)


if __name__ == '__main__':
    pass
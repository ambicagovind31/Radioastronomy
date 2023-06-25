listobs(vis='sis14_twhya_calibrated_flagged.ms')

plotms(vis='sis14_twhya_calibrated_flagged.ms', xaxis='u', yaxis='v', avgchannel='10000', avgspw=False, avgtime='1e9', avgscan=False, coloraxis="field", showgui=True)

os.system('rm -rf TW_Hydrae.*')

tclean(vis='sis14_twhya_calibrated_flagged.ms',
       imagename='TW_Hydrae',
       field='5',
       spw='',
       specmode='mfs',
       deconvolver='hogbom',
       gridder='standard',
       imsize=[128,128],
       cell=['0.1arcsec'],
       weighting='briggs',
       threshold='0mJy',
       niter=5000,
       interactive=True)

imview('TW_Hydrae.psf')
imview('TW_Hydrae.image')

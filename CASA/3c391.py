listobs(vis='3c391_ctm_mosaic_spw0.ms')

plotms(vis='3c391_ctm_mosaic_spw0.ms',xaxis='uvdist',yaxis='amp',
       ydatacolumn='data', field='0',avgtime='30',correlation='RR',
       plotfile='plotms_3c391-mosaic0-uvwave.png',overwrite=True)

tclean(vis='3c391_ctm_mosaic_spw0.ms',imagename='3c391_ctm_spw0_multiscale',
      field='',spw='',
      specmode='mfs',
      niter=20000,
      gain=0.1, threshold='1.0mJy',
      gridder='mosaic',
      deconvolver='multiscale',
      scales=[0, 5, 15, 45], smallscalebias=0.9,
      interactive=True,
      imsize=[480,480], cell=['2.5arcsec','2.5arcsec'],
      stokes='I',
      weighting='briggs',robust=0.5,
      pbcor=False,
      savemodel='modelcolumn')

viewer('3c391_ctm_spw0_multiscale.image')
viewer('3c391_ctm_spw0_multiscale.psf')
viewer('3c391_ctm_spw0_multiscale.residual')

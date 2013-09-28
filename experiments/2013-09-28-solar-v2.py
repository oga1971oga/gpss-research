Experiment(description='Investigating what is happenng with solar',
           data_dir='../data/solar/',
           max_depth=20, 
           random_order=False,
           k=1,
           debug=False, 
           local_computation=False, 
           n_rand=19,
           sd=2, 
           jitter_sd=0.1,
           max_jobs=500, 
           verbose=False,
           verbose_results=True,
           make_predictions=False,
           skip_complete=True,
           results_dir='../results/2013-09-28-solar-v2/',
           iters=250,
           base_kernels='SE,Lin,Const,Fourier,Noise',
           zero_mean=True,
           random_seed=1,
           period_heuristic=5,
           subset=True,
           subset_size=250,
           full_iters=10,
           bundle_size=1,
           additive_form=True,
           model_noise=True,
           no_noise=True)
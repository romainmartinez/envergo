# 1D Statistisc

1. Flatten matrix (37x73 --> 2701) (**update values**)
2. Replace missing observations by the mean of the corresponding positions
  - X nans: Y%
3. Non-parametric one-way ANOVA repeated measure (_on positions_)
> cite Pataky parametric vs. non-parametric

  - to compute a critical threshold
  - One caveat is that this pertains only to continuum-level inference (i.e. a critical threshold)
  - alpha: 0.05
  - iterations: 10,00
  - Insert Fig. 1: ANOVA
    - only significant
    - reshaped data
    - F Statistisc (higher = more differences)

4. Posthoc: non-parametric paired t-test
  - on each combinations of positions (_6 positions: 15 combinations_)
  - alpha = 0.05
  - iterations = 10,000
  - two-tailed
  - on region of interest (significant area given by the ANOVA)
  > cite pataky ROI to increase statistical power

  - Insert Fig. 2: posthocs
    - only significant and on ROI
    - reshaped data
    - mean differences

# 0D Statistisc

1. Replace missing observations by the mean of the corresponding positions
  - 63 nans over 1470 observations: 4.3%
2. Non-parametric one-way MANOVA
  - alpha: 0.05
  - iterations: 10,000
  - As the manova reach significance, we can conduct separate Hotelling’s T$^2$ tests on each pair of groups
3. Posthoc: non-parametric paired Hotelling's T2
  - alpha: 0.05
  - iterations: 10,000
  - on each combinations of positions (_6 positions: 15 combinations_)
  - on all parameters (_7_)
  - insert Fig. 3: Hotelling
    - T statictic
  - If those tests reach significance then conduct additional post hoc t tests on each vector component, but acknowledge that this neglects vector component covariance.
4. If Hotelling reach significiance: non-parametric paired t-test
  - on each parameters
  - alpha: 0.05
  - iterations: 10,000
  - insert Fig. 4: paired t-tests

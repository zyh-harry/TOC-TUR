"""
Last Updated: 2024-03-07
Author: Idil Yaktubay (iyaktubay@iisd-ela.org)

CODE PURPOSE: Create feature tables for total dissolved solids, turbidity,
              total organic carbon, and discharge at Pinawa and Whitemouth
              AquaHive stations
"""


import pandas as pd
from feature_creation_adaptive_monitoring import calc_discharge_site_features_hrs_ago, calc_param_site_features_hrs_ago 

#=========================Load full AquaHives dataset==========================

full_dataset = pd.read_csv('aquahives_export.csv')

#==============================Turbidity Features==============================


# Whitemouth
tur_wmth_1_3_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='turbidity',
                                                        site='wmth', 
                                                        hours_ago_start=1, 
                                                        hours_ago_end=3)

tur_wmth_4_6_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='turbidity',
                                                        site='wmth', 
                                                        hours_ago_start=4, 
                                                        hours_ago_end=6)

tur_wmth_7_9_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='turbidity',
                                                        site='wmth', 
                                                        hours_ago_start=7, 
                                                        hours_ago_end=9)

tur_wmth_10_12_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='turbidity',
                                                        site='wmth', 
                                                        hours_ago_start=10, 
                                                        hours_ago_end=12)

tur_wmth_13_15_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='turbidity',
                                                        site='wmth', 
                                                        hours_ago_start=13, 
                                                        hours_ago_end=15)

# Create final turbidity concentration feature table (wmth)
tur_wmth_final_features_conc = pd.concat([tur_wmth_1_3_features[0].set_index('timestamp_ccentral'),
                                          tur_wmth_4_6_features[0].set_index('timestamp_ccentral'),
                                          tur_wmth_7_9_features[0].set_index('timestamp_ccentral'),
                                          tur_wmth_10_12_features[0].set_index('timestamp_ccentral'),
                                          tur_wmth_13_15_features[0].set_index('timestamp_ccentral')],
                                          axis=1)
# Create final turbidity load feature table (wmth)
tur_wmth_final_features_load = pd.concat([tur_wmth_1_3_features[1].set_index('timestamp_ccentral'),
                                          tur_wmth_4_6_features[1].set_index('timestamp_ccentral'),
                                          tur_wmth_7_9_features[1].set_index('timestamp_ccentral'),
                                          tur_wmth_10_12_features[1].set_index('timestamp_ccentral'),
                                          tur_wmth_13_15_features[1].set_index('timestamp_ccentral')],
                                          axis=1)

# Export datasets as csv (uncomment if need to re-export)
tur_wmth_final_features_conc.to_csv('tur_wmth_concentration_features.csv', index=True)
tur_wmth_final_features_load.to_csv('tur_wmth_load_features.csv', index=True)

# Pinawa
tur_pnwa_1_3_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='turbidity',
                                                        site='pnwa', 
                                                        hours_ago_start=1, 
                                                        hours_ago_end=3)

tur_pnwa_4_6_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='turbidity',
                                                        site='pnwa', 
                                                        hours_ago_start=4, 
                                                        hours_ago_end=6)

tur_pnwa_7_9_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='turbidity',
                                                        site='pnwa', 
                                                        hours_ago_start=7, 
                                                        hours_ago_end=9)

tur_pnwa_10_12_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='turbidity',
                                                        site='pnwa', 
                                                        hours_ago_start=10, 
                                                        hours_ago_end=12)

tur_pnwa_13_15_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='turbidity',
                                                        site='pnwa', 
                                                        hours_ago_start=13, 
                                                        hours_ago_end=15)

# Create final turbidity concentration feature table (pnwa)
tur_pnwa_final_features_conc = pd.concat([tur_pnwa_1_3_features[0].set_index('timestamp_ccentral'),
                                          tur_pnwa_4_6_features[0].set_index('timestamp_ccentral'),
                                          tur_pnwa_7_9_features[0].set_index('timestamp_ccentral'),
                                          tur_pnwa_10_12_features[0].set_index('timestamp_ccentral'),
                                          tur_pnwa_13_15_features[0].set_index('timestamp_ccentral')],
                                          axis=1)

# Create final turbidity load feature table (pnwa)
tur_pnwa_final_features_load = pd.concat([tur_pnwa_1_3_features[1].set_index('timestamp_ccentral'),
                                          tur_pnwa_4_6_features[1].set_index('timestamp_ccentral'),
                                          tur_pnwa_7_9_features[1].set_index('timestamp_ccentral'),
                                          tur_pnwa_10_12_features[1].set_index('timestamp_ccentral'),
                                          tur_pnwa_13_15_features[1].set_index('timestamp_ccentral')],
                                          axis=1)

# Export datasets as csv (uncomment if need to re-export)
tur_pnwa_final_features_conc.to_csv('tur_pnwa_concentration_features.csv', index=True)
tur_pnwa_final_features_load.to_csv('tur_pnwa_load_features.csv', index=True)


#==========================Total Organic Carbon Features=======================

# Whitemouth
toc_wmth_1_3_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='toc',
                                                        site='wmth', 
                                                        hours_ago_start=1, 
                                                        hours_ago_end=3)

toc_wmth_4_6_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='toc',
                                                        site='wmth', 
                                                        hours_ago_start=4, 
                                                        hours_ago_end=6)

toc_wmth_7_9_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='toc',
                                                        site='wmth', 
                                                        hours_ago_start=7, 
                                                        hours_ago_end=9)

toc_wmth_10_12_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='toc',
                                                        site='wmth', 
                                                        hours_ago_start=10, 
                                                        hours_ago_end=12)

toc_wmth_13_15_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='toc',
                                                        site='wmth', 
                                                        hours_ago_start=13, 
                                                        hours_ago_end=15)

# Create final total organic carbon concentration feature table (wmth)
toc_wmth_final_features_conc = pd.concat([toc_wmth_1_3_features[0].set_index('timestamp_ccentral'),
                                          toc_wmth_4_6_features[0].set_index('timestamp_ccentral'),
                                          toc_wmth_7_9_features[0].set_index('timestamp_ccentral'),
                                          toc_wmth_10_12_features[0].set_index('timestamp_ccentral'),
                                          toc_wmth_13_15_features[0].set_index('timestamp_ccentral')],
                                          axis=1)

# Create final total organic carbon load feature table (wmth)
toc_wmth_final_features_load = pd.concat([toc_wmth_1_3_features[1].set_index('timestamp_ccentral'),
                                          toc_wmth_4_6_features[1].set_index('timestamp_ccentral'),
                                          toc_wmth_7_9_features[1].set_index('timestamp_ccentral'),
                                          toc_wmth_10_12_features[1].set_index('timestamp_ccentral'),
                                          toc_wmth_13_15_features[1].set_index('timestamp_ccentral')],
                                          axis=1)

# Export datasets as csv (uncomment if need to re-export)
toc_wmth_final_features_conc.to_csv('toc_wmth_concentration_features.csv', index=True)
toc_wmth_final_features_load.to_csv('toc_wmth_load_features.csv', index=True)


# Pinawa
toc_pnwa_1_3_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='toc',
                                                        site='pnwa', 
                                                        hours_ago_start=1, 
                                                        hours_ago_end=3)

toc_pnwa_4_6_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='toc',
                                                        site='pnwa', 
                                                        hours_ago_start=4, 
                                                        hours_ago_end=6)

toc_pnwa_7_9_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='toc',
                                                        site='pnwa', 
                                                        hours_ago_start=7, 
                                                        hours_ago_end=9)

toc_pnwa_10_12_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='toc',
                                                        site='pnwa', 
                                                        hours_ago_start=10, 
                                                        hours_ago_end=12)

toc_pnwa_13_15_features = calc_param_site_features_hrs_ago(df=full_dataset, 
                                                        param='toc',
                                                        site='pnwa', 
                                                        hours_ago_start=13, 
                                                        hours_ago_end=15)

# Create final total organic carbon concentration feature table (pnwa)
toc_pnwa_final_features_conc = pd.concat([toc_pnwa_1_3_features[0].set_index('timestamp_ccentral'),
                                          toc_pnwa_4_6_features[0].set_index('timestamp_ccentral'),
                                          toc_pnwa_7_9_features[0].set_index('timestamp_ccentral'),
                                          toc_pnwa_10_12_features[0].set_index('timestamp_ccentral'),
                                          toc_pnwa_13_15_features[0].set_index('timestamp_ccentral')],
                                          axis=1)

# Create final total organic carbon load feature table (pnwa)
toc_pnwa_final_features_load = pd.concat([toc_pnwa_1_3_features[1].set_index('timestamp_ccentral'),
                                          toc_pnwa_4_6_features[1].set_index('timestamp_ccentral'),
                                          toc_pnwa_7_9_features[1].set_index('timestamp_ccentral'),
                                          toc_pnwa_10_12_features[1].set_index('timestamp_ccentral'),
                                          toc_pnwa_13_15_features[1].set_index('timestamp_ccentral')],
                                          axis=1)


# Export datasets as csv (uncomment if need to re-export)
toc_pnwa_final_features_conc.to_csv('toc_pnwa_concentration_features.csv', index=True)
toc_pnwa_final_features_load.to_csv('toc_pnwa_load_features.csv', index=True)

#===============================Discharge Features=============================

# Whitemouth
dschrg_wmth_1_3_features = calc_discharge_site_features_hrs_ago(df=full_dataset,
                                                                site='wmth',
                                                                hours_ago_start=1,
                                                                hours_ago_end=3)

dschrg_wmth_4_6_features = calc_discharge_site_features_hrs_ago(df=full_dataset,
                                                                site='wmth',
                                                                hours_ago_start=4,
                                                                hours_ago_end=6)

dschrg_wmth_7_9_features = calc_discharge_site_features_hrs_ago(df=full_dataset,
                                                                site='wmth',
                                                                hours_ago_start=7,
                                                                hours_ago_end=9)

dschrg_wmth_10_12_features = calc_discharge_site_features_hrs_ago(df=full_dataset,
                                                                site='wmth',
                                                                hours_ago_start=10,
                                                                hours_ago_end=12)

dschrg_wmth_13_15_features = calc_discharge_site_features_hrs_ago(df=full_dataset,
                                                                site='wmth',
                                                                hours_ago_start=13,
                                                                hours_ago_end=15)

# Create final discharge feature table (wmth)
dschrg_wmth_final_features = pd.concat([dschrg_wmth_1_3_features.set_index('timestamp_ccentral'),
                                        dschrg_wmth_4_6_features.set_index('timestamp_ccentral'),
                                        dschrg_wmth_7_9_features.set_index('timestamp_ccentral'),
                                        dschrg_wmth_10_12_features.set_index('timestamp_ccentral'),
                                        dschrg_wmth_13_15_features.set_index('timestamp_ccentral')],
                                          axis=1)

# Export dataset as csv (uncomment if need to re-export)
dschrg_wmth_final_features.to_csv('discharge_wmth_features.csv', index=True)


# Pinawa
dschrg_pnwa_1_3_features = calc_discharge_site_features_hrs_ago(df=full_dataset,
                                                                site='pnwa',
                                                                hours_ago_start=1,
                                                                hours_ago_end=3)

dschrg_pnwa_4_6_features = calc_discharge_site_features_hrs_ago(df=full_dataset,
                                                                site='pnwa',
                                                                hours_ago_start=4,
                                                                hours_ago_end=6)

dschrg_pnwa_7_9_features = calc_discharge_site_features_hrs_ago(df=full_dataset,
                                                                site='pnwa',
                                                                hours_ago_start=7,
                                                                hours_ago_end=9)

dschrg_pnwa_10_12_features = calc_discharge_site_features_hrs_ago(df=full_dataset,
                                                                site='pnwa',
                                                                hours_ago_start=10,
                                                                hours_ago_end=12)

dschrg_pnwa_13_15_features = calc_discharge_site_features_hrs_ago(df=full_dataset,
                                                                site='pnwa',
                                                                hours_ago_start=13,
                                                                hours_ago_end=15)

dschrg_pnwa_final_features = pd.concat([dschrg_pnwa_1_3_features.set_index('timestamp_ccentral'),
                                        dschrg_pnwa_4_6_features.set_index('timestamp_ccentral'),
                                        dschrg_pnwa_7_9_features.set_index('timestamp_ccentral'),
                                        dschrg_pnwa_10_12_features.set_index('timestamp_ccentral'),
                                        dschrg_pnwa_13_15_features.set_index('timestamp_ccentral')],
                                          axis=1)

# Export dataset as csv (uncomment if need to re-export)
dschrg_pnwa_final_features.to_csv('discharge_pnwa_features.csv', index=True)



# #=======================Total Dissolved Solids Features========================
# TOTAL DISSOLVED SOLIDS AREN'T NEEDED FOR NOW
# # Whitemouth
# tds_wmth_1_3_features = calc_param_site_features_hrs_ago(df=full_dataset, 
#                                                         param='total_dissolved_solids',
#                                                         site='wmth', 
#                                                         hours_ago_start=1, 
#                                                         hours_ago_end=3)

# tds_wmth_4_6_features = calc_param_site_features_hrs_ago(df=full_dataset, 
#                                                         param='total_dissolved_solids',
#                                                         site='wmth', 
#                                                         hours_ago_start=4, 
#                                                         hours_ago_end=6)

# tds_wmth_7_9_features = calc_param_site_features_hrs_ago(df=full_dataset, 
#                                                         param='total_dissolved_solids',
#                                                         site='wmth', 
#                                                         hours_ago_start=7, 
#                                                         hours_ago_end=9)

# tds_wmth_10_12_features = calc_param_site_features_hrs_ago(df=full_dataset, 
#                                                         param='total_dissolved_solids',
#                                                         site='wmth', 
#                                                         hours_ago_start=10, 
#                                                         hours_ago_end=12)

# tds_wmth_13_15_features = calc_param_site_features_hrs_ago(df=full_dataset, 
#                                                         param='total_dissolved_solids',
#                                                         site='wmth', 
#                                                         hours_ago_start=13, 
#                                                         hours_ago_end=15)

# # Create final total dissolved solids concentration feature table (wmth)
# tds_wmth_final_features_conc = pd.concat([tds_wmth_1_3_features[0].set_index('timestamp_ccentral'),
#                                     tds_wmth_4_6_features[0].set_index('timestamp_ccentral'),
#                                     tds_wmth_7_9_features[0].set_index('timestamp_ccentral'),
#                                     tds_wmth_10_12_features[0].set_index('timestamp_ccentral'),
#                                     tds_wmth_13_15_features[0].set_index('timestamp_ccentral')],
#                                     axis=1)
# # Create final total dissolved solids load feature table (wmth)
# tds_wmth_final_features_load = pd.concat([tds_wmth_1_3_features[1].set_index('timestamp_ccentral'),
#                                     tds_wmth_4_6_features[1].set_index('timestamp_ccentral'),
#                                     tds_wmth_7_9_features[1].set_index('timestamp_ccentral'),
#                                     tds_wmth_10_12_features[1].set_index('timestamp_ccentral'),
#                                     tds_wmth_13_15_features[1].set_index('timestamp_ccentral')],
#                                     axis=1)

# # Export datasets (uncomment if need to re-export)
# tds_wmth_final_features_conc.to_csv('tds_wmth_concentration_features.csv', index=True)
# tds_wmth_final_features_load.to_csv('tds_wmth_load_features.csv', index=True)


# # Pinawa
# tds_pnwa_1_3_features = calc_param_site_features_hrs_ago(df=full_dataset, 
#                                                         param='total_dissolved_solids',
#                                                         site='pnwa', 
#                                                         hours_ago_start=1, 
#                                                         hours_ago_end=3)

# tds_pnwa_4_6_features = calc_param_site_features_hrs_ago(df=full_dataset, 
#                                                         param='total_dissolved_solids',
#                                                         site='pnwa', 
#                                                         hours_ago_start=4, 
#                                                         hours_ago_end=6)

# tds_pnwa_7_9_features = calc_param_site_features_hrs_ago(df=full_dataset, 
#                                                         param='total_dissolved_solids',
#                                                         site='pnwa', 
#                                                         hours_ago_start=7, 
#                                                         hours_ago_end=9)

# tds_pnwa_10_12_features = calc_param_site_features_hrs_ago(df=full_dataset, 
#                                                         param='total_dissolved_solids',
#                                                         site='pnwa', 
#                                                         hours_ago_start=10, 
#                                                         hours_ago_end=12)

# tds_pnwa_13_15_features = calc_param_site_features_hrs_ago(df=full_dataset, 
#                                                         param='total_dissolved_solids',
#                                                         site='pnwa', 
#                                                         hours_ago_start=13, 
#                                                         hours_ago_end=15)

# # Create final total dissolved solids concentration feature table (pnwa)
# tds_pnwa_final_features_conc = pd.concat([tds_pnwa_1_3_features[0].set_index('timestamp_ccentral'),
#                                     tds_pnwa_4_6_features[0].set_index('timestamp_ccentral'),
#                                     tds_pnwa_7_9_features[0].set_index('timestamp_ccentral'),
#                                     tds_pnwa_10_12_features[0].set_index('timestamp_ccentral'),
#                                     tds_pnwa_13_15_features[0].set_index('timestamp_ccentral')],
#                                     axis=1)
# # Create final total dissolved solids load feature table (pnwa)
# tds_pnwa_final_features_load = pd.concat([tds_pnwa_1_3_features[1].set_index('timestamp_ccentral'),
#                                     tds_pnwa_4_6_features[1].set_index('timestamp_ccentral'),
#                                     tds_pnwa_7_9_features[1].set_index('timestamp_ccentral'),
#                                     tds_pnwa_10_12_features[1].set_index('timestamp_ccentral'),
#                                     tds_pnwa_13_15_features[1].set_index('timestamp_ccentral')],
#                                     axis=1)

# # Export datasets (uncomment if need to re-export)
# tds_pnwa_final_features_conc.to_csv('tds_pnwa_concentration_features.csv', index=True)
# tds_pnwa_final_features_load.to_csv('tds_pnwa_load_features.csv', index=True)


"""Configuration of the time in working memory study."""


# General
study_name = 'time_in_wm'
# bids_root = '/home/charb/Desktop/parietal/time_in_wm_new/'
bids_root = '/storage/store2/data/time_in_wm_new'
task = 'tiwm'
interactive = False

# subjects = ["155", "197", "215", "220"]
subjects = ["215"]
# subjects = "all"
# exclude_subjects = ["586", "812", "215", "231", "653", "972", "512"]

# 586 only 6 runs. 812: 3 runs.
# warning : subjects with 9 runs: 215, 231, 653 : one of the run was aborted.
# Warning: "972" run 7

# runs = ["01", "02", "03", "04", "05", "06", "07", "08"]
# runs = "all"
runs = ["01", "02", "03"]  # bug
runs = ["03"]  # no bug
runs = ["01", "03"]  # bug i think


find_flat_channels_meg = False
find_noisy_channels_meg = False
ch_types = ['meg']

# Max filter
use_maxwell_filter = True
mf_reference_run = '01'  # To do change it to run 4
mf_head_origin = 'auto'  # 'auto', it will be estimated from headshape points.
mf_st_duration = None  # We are interested in low frequency activity (<0.1Hz)

# Filtering and resampling
l_freq = 1.
h_freq = 150.
resample_sfreq = 500.
decim = 1  # no decimation

# Artifact correction.
spatial_filter = 'ica'
ica_max_iterations = 1500
ica_l_freq = 1.
ica_decim = 4
ica_n_components = 0.999
ica_reject_components = 'auto'
ica_reject = {'mag': 5e-11}  # traduction of reject_beforeICA
reject = {'grad': 4000e-13, 'mag': 1e-11}  # traduction of reject_afterICA
ica_ctps_ecg_threshold = 0.1  # Default value of bids-pipeline
ica_eog_threshold = 3.0

# Epochs
epochs_tmin = -4.6
epochs_tmax = 5
# trigger_time_shift = 0  # Not found in the doc and Not necessary here
baseline = (-1, 0)

# Noise estimation
process_er = True
noise_cov = 'emptyroom'


# event_id : not needed because already in events.tsv
conditions = ["1_item/short", "1_item/medium", "1_item/long",
              '3_item/short', '3_item/medium', '3_item/long']


# Decoding
decoding_metric = 'roc_auc'
decoding_n_splits = 8

# Time frequency
time_frequency_conditions = conditions

# Source space parameters
spacing = 'oct6'
mindist = 5
# loose = 0.2  # default value of mne
# depth = 0.8  # default value of mne
inverse_method = 'dSPM'
# smooth = 10  # default value of mne


# Advanced parameters
l_trans_bandwidth = 'auto'
h_trans_bandwidth = 'auto'

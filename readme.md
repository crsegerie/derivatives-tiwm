List of usefull commands:



(mne_dev) csegerie@drago4:/storage/store/work/csegerie/parietal/mne-bids-pipeline$ nice -n 5 python run.py --config=/storage/store2/data/time_in_wm_new/derivatives/mne-bids-pipeline/config.py --steps=preprocessing

Workspace saved in :
/storage/store2/data/time_in_wm_new/derivatives/mne-bids-pipeline/workspace.code-workspace

To save tmux output:
Ctrl+b + : and then type capture-pane -S -3000 + return
Ctrl+b + : and type save-buffer /storage/store2/data/time_in_wm_new/derivatives/mne-bids-pipeline/tmuxAll-preprocess-sensor.txt
Or tmux capture-pane -pS -1000000 > /storage/store2/data/time_in_wm_new/derivatives/mne-bids-pipeline/tmuxAll1itembug512_v2.txt
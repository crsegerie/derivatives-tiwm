List of usefull commands:



(mne_dev) csegerie@drago4:/storage/store/work/csegerie/parietal/mne-bids-pipeline$ nice -n 5 python run.py --config=/storage/store2/data/time_in_wm_new/derivatives/mne-bids-pipeline/config.py --steps=preprocessing

Workspace saved in :
/storage/store2/data/time_in_wm_new/derivatives/mne-bids-pipeline/workspace.code-workspace

To save tmux output:
Ctrl+b + : and then type capture-pane -S -3000 + return
Ctrl+b + : and type save-buffer /storage/store2/data/time_in_wm_new/derivatives/mne-bids-pipeline/tmux_all_subjects_first_contrasts.txt

To serve : npm i -g serve
serve /storage/store2/data/time_in_wm_new/derivatives


To explore the results:
ssh -X drago4
conda activate mne_dev
ipython --matplotlib=qt
import mne
evokeds = mne.read_evokeds("/storage/store2/data/time_in_wm_new/derivat
   ...: ives/mne-bids-pipeline/sub-155/meg/sub-155_task-tiwm_ave.fif")
evokeds[5].copy().crop(-1,1).plot()


Always up-key



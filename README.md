# enhanced_xoss_sync
Enhanced version of ekspla's [xoss_sync](https://github.com/ekspla/xoss_sync) with additional features and helper scripts for changing GPS settings and preparing display layouts.
## Features
- Command line arguments provided with ```argparse```
- Can delete FIT files on device specified in a user-provided list
- Can retrieve and send GPS settings json and to specify its filename
- Can specify workout/trace list filename (e.g., filelist.txt, workouts.json)
- Can save list of traces on device to file
- Timestamps for each notification to aid benchmarking
- User adjustable maximum transferable unit (MTU) size
## Installation
Make sure to install the Python Bluetooth library Bleak first:  

```sudo apt install python3-bleak```  
```pip install bleak```  

Then clone this GitHub repo.
## Usage
```
usage: enhanced_xoss_sync.py [-h] [--list_storage_used_only | --no-list_storage_used_only] [--delete_selected_fit_files DELETE_SELECTED_FIT_FILES] [--save_all_files | --no-save_all_files]
                             [--save_trace_filelist | --no-save_trace_filelist] [--output_trace_filelist_name OUTPUT_TRACE_FILELIST_NAME]
                             [--get_settings_from_json | --no-get_settings_from_json] [--change_settings_with_json | --no-change_settings_with_json]
                             [--settings_json_filename SETTINGS_JSON_FILENAME] [--set_mtu_size SET_MTU_SIZE] [--define_trace_list_filename DEFINE_TRACE_LIST_FILENAME]

Set parameters for XOSS bike GPS sync script (e.g., saving new files or deleting files specified in list).

options:
  -h, --help            show this help message and exit
  --list_storage_used_only, --no-list_storage_used_only
                        List GPS storage used and exit if specified (default false).
  --delete_selected_fit_files DELETE_SELECTED_FIT_FILES
                        Delete fit files from GPS in list specified by this argument. Filenames not ending with .fit or .FIT are ignored for safety (e.g., to not delete workouts.json or
                        Setting.json).
  --save_all_files, --no-save_all_files
                        Sync all files on GPS, except for those confirmed to already have been saved (default true).
  --save_trace_filelist, --no-save_trace_filelist
                        Save list of all trace files currently present on GPS (default false).
  --output_trace_filelist_name OUTPUT_TRACE_FILELIST_NAME
                        Filename for list of trace files currently present on GPS (default fit_files.txt).
  --get_settings_from_json, --no-get_settings_from_json
                        Get GPS settings by saving Settings.json JSON file to PC.
  --change_settings_with_json, --no-change_settings_with_json
                        Change GPS settings with Settings.json JSON file.
  --settings_json_filename SETTINGS_JSON_FILENAME
                        GPS settings JSON if not named Setting.json.
  --set_mtu_size SET_MTU_SIZE
                        Set maximum transferable unit (MTU) size (default 247).
  --define_trace_list_filename DEFINE_TRACE_LIST_FILENAME
                        Set name of json containing all traces/workouts (default workouts.json).
```
## Tutorial
## Adjusting Bluetooth connection parameters for optimum performance (Linux BlueZ)
In the process of testing this script on my Linux PC, I found that the XOSS BLE connection defaulted to a connection interval of 48 ms and a corresponding data transfer rate of roughly 13 kbps. I know based on ekspla's work and other Bluetooth documentation that reducing connection intervals should increase throughput. Reducing the interval to the minimum possible (7.5 ms) correspondingly increased my observed transfer rate to roughly 74 kbps. 
## Benchmarking
## Future plans
- Option to upload/download user layout files
- Helper scripts for preparing user layout and GPS settings jsons
- Options to upload/download firmware

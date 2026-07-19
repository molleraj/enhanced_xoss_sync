# enhanced_xoss_sync
Enhanced version of ekspla's [xoss_sync](https://github.com/ekspla/xoss_sync) with additional features and helper scripts for changing GPS settings and preparing display layouts. This Python script communicates with XOSS GPS cycling computer devices over Bluetooth Low Energy (BLE) to retrieve recorded traces (FIT files) without the use of the standard XOSS cloud/Android apps. I have recently also added an additional script for configuring XOSS GPS settings via command line arguments.

## Features
- Command line arguments provided with ```argparse```
- Can delete FIT files on device specified in a user-provided list
- Can retrieve and send GPS settings json and specify its filename (e.g., settings.json)
- Can specify workout/trace list filename (e.g., filelist.txt, workouts.json)
- Can save list of traces on device to file
- Can retrieve and send user layout json and specify its filename (e.g., panels.json)
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
                             [--settings_json_filename SETTINGS_JSON_FILENAME] [--get_layout_from_json | --no-get_layout_from_json]
                             [--change_layout_with_json | --no-change_layout_with_json] [--layout_json_filename LAYOUT_JSON_FILENAME] [--set_mtu_size SET_MTU_SIZE]
                             [--define_trace_list_filename DEFINE_TRACE_LIST_FILENAME]

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
                        Get GPS settings by saving Setting.json JSON file to PC.
  --change_settings_with_json, --no-change_settings_with_json
                        Change GPS settings with Setting.json JSON file.
  --settings_json_filename SETTINGS_JSON_FILENAME
                        GPS settings JSON if not named Setting.json.
  --get_layout_from_json, --no-get_layout_from_json
                        Get GPS data layout by saving Layout.json JSON file to PC.
  --change_layout_with_json, --no-change_layout_with_json
                        Change GPS data layout with Layout.json JSON file.
  --layout_json_filename LAYOUT_JSON_FILENAME
                        GPS data layout JSON if not named Layout.json.
  --set_mtu_size SET_MTU_SIZE
                        Set maximum transferable unit (MTU) size (default 247).
  --define_trace_list_filename DEFINE_TRACE_LIST_FILENAME
                        Set name of json containing all traces/workouts (default workouts.json).
```
```
usage: configure_xoss_settings.py [-h] --input_settings_json INPUT_SETTINGS_JSON --output_settings_json OUTPUT_SETTINGS_JSON
                                  [--language {en,it,ko,ja,de,es,fr,zh-cn,zh-hk,zh-tw,pt-pt,pt-br}] [--unit_type {0,1}] [--temperature_unit {0,1}]
                                  [--time_format {0,1}] [--backlight {0,1,2}] [--pause {0,1}] [--overwrite {0,1}] [--keytone {True,False}]

Configure XOSS GPS settings that are stored in settings.json file with command line parameters.

options:
  -h, --help            show this help message and exit
  --input_settings_json INPUT_SETTINGS_JSON
                        Filename for original XOSS GPS settings JSON to configure.
  --output_settings_json OUTPUT_SETTINGS_JSON
                        Filename for output edited XOSS GPS settings JSON.
  --language {en,it,ko,ja,de,es,fr,zh-cn,zh-hk,zh-tw,pt-pt,pt-br}
                        Default language for GPS based on i18n standard two-letter codes (e.g., "en" for English) documented at
                        https://www.w3.org/International/O-charset-lang.html. Available choices based on XOSS developer documentation provided.
  --unit_type {0,1}     (Distance) unit type - 0 for metric (e.g., km) or 1 for imperial (miles).
  --temperature_unit {0,1}
                        Temperature unit - 0 for Celsius or 1 for Fahrenheit.
  --time_format {0,1}   Time format - 0 for 24 hours or 1 for 12 hours.
  --backlight {0,1,2}   Backlight - 0 for auto, 1 for always on, or 2 for always off.
  --pause {0,1}         Pause GPS when not moving - 0 for auto or 1 for off.
  --overwrite {0,1}     Automatic overwrite when memory full - 0 for on or 1 for off.
  --keytone {True,False}
                        Keytone - 'true' for on or 'false' for off.
```
## Device specific notes
I have tested this script on my XOSS G Gen2 primarily, which has a workouts/traces file called ```workouts.json```, a data layout file called ``panels.json```, and a settings file called ```settings.json```. Older devices like the G Gen1 would have different respective filenames like ```filelist.txt``` and ```Setting.json```, respectively.
## Tutorial
Here is an example sync session to pull new fit files from the XOSS and save traces on the GPS to file:  
```
$ time python3 enhanced_xoss_sync.py --save_trace_filelist --output_trace_filelist_name fit_files_043026.txt
2026-04-30 03:01:37.262838 : Scanning for Bluetooth devices...
2026-04-30 03:01:37.300601 : Found device: 62-5B-78-45-64-2C - 62:5B:78:45:64:2C
2026-04-30 03:01:37.486113 : Found device: 62-5B-78-45-64-2C - 62:5B:78:45:64:2C
2026-04-30 03:01:37.677231 : Found device: 62-5B-78-45-64-2C - 62:5B:78:45:64:2C
2026-04-30 03:01:37.737387 : Found device: XOSS G-393314 - F9:62:6E:54:D2:1C
2026-04-30 03:01:37.737534 : Found target device: XOSS G-393314 - F9:62:6E:54:D2:1C
2026-04-30 03:01:39.557614 : Connected to XOSS G-393314
2026-04-30 03:01:39.563107 : Device reported MTU size 209
2026-04-30 03:01:39.563147 : User specified MTU size 247
2026-04-30 03:01:39.604649 : Notifications started
2026-04-30 03:01:39.705853 : Free Diskspace: 5072/8104kb
2026-04-30 03:01:46.350595 : Successfully wrote combined data to workouts.json
2026-04-30 03:01:46.357727 : Saving list of trace files on GPS to fit_files_043026.txt
2026-04-30 03:01:46.358150 : Skip: 20260421184624.fit
2026-04-30 03:01:46.358226 : Skip: 20260423215719.fit
2026-04-30 03:01:46.358289 : Skip: 20260410162730.fit
2026-04-30 03:01:46.358340 : Skip: 20260414144956.fit
2026-04-30 03:01:46.358389 : Skip: 20260409163301.fit
2026-04-30 03:01:46.358435 : Skip: 20260401194216.fit
2026-04-30 03:01:46.358526 : Retrieving 20260429233905.fit
2026-04-30 03:01:50.141738 : Successfully wrote combined data to 20260429233905.fit
2026-04-30 03:01:50.141865 : Skip: 20260420192410.fit
2026-04-30 03:01:50.141911 : Skip: 20260415232638.fit
2026-04-30 03:01:50.141945 : Skip: 20260421150732.fit
2026-04-30 03:01:50.141979 : Skip: 20260407185359.fit
2026-04-30 03:01:50.142051 : Skip: 20260426161943.fit
2026-04-30 03:01:50.142091 : Skip: 20260406184015.fit
2026-04-30 03:01:50.142173 : Retrieving 20260428190158.fit
2026-04-30 03:02:07.255887 : Successfully wrote combined data to 20260428190158.fit
2026-04-30 03:02:07.255927 : Skip: 20260427180112.fit
2026-04-30 03:02:07.255941 : Skip: 20260417170423.fit
2026-04-30 03:02:07.255952 : Skip: 20260404223652.fit
2026-04-30 03:02:07.255963 : Skip: 20260422193344.fit
2026-04-30 03:02:07.255974 : Skip: 20260424185105.fit
2026-04-30 03:02:07.255984 : Skip: 20260424134135.fit
2026-04-30 03:02:07.255995 : Skip: 20260413190854.fit
2026-04-30 03:02:07.256006 : Skip: 20260408190754.fit
2026-04-30 03:02:07.256039 : Skip: 20260402180218.fit
2026-04-30 03:02:07.256051 : Skip: 20260411185357.fit
2026-04-30 03:02:07.256063 : Skip: 20260417144019.fit
2026-04-30 03:02:07.256076 : Skip: 20260410141440.fit
2026-04-30 03:02:07.256090 : Skip: 20260425190516.fit
2026-04-30 03:02:07.256102 : Skip: 20260414193929.fit
2026-04-30 03:02:07.256115 : Skip: 20260410141318.fit
2026-04-30 03:02:07.256127 : Skip: 20260416191052.fit

real    0m32.947s
user    0m1.268s
sys     0m0.088s
```
Here is an example of deleting specified fit files from the XOSS:
```
$ python3 enhanced_xoss_sync.py --delete_selected_fit_files files_to_delete_050126.txt 
2026-05-01 00:15:19.778183 : Scanning for Bluetooth devices...
2026-05-01 00:15:19.903504 : Found device: XOSS G-393314 - F9:62:6E:54:D2:1C
2026-05-01 00:15:19.903606 : Found target device: XOSS G-393314 - F9:62:6E:54:D2:1C
2026-05-01 00:15:21.596059 : Connected to XOSS G-393314
2026-05-01 00:15:21.598533 : Device reported MTU size 209
2026-05-01 00:15:21.599027 : User specified MTU size 247
2026-05-01 00:15:21.631804 : Notifications started
2026-05-01 00:15:21.733499 : Free Diskspace: 4896/8104kb
2026-05-01 00:15:21.733620 : Deleting files specified in list provided as command line argument.
2026-05-01 00:15:21.734149 : Deleting  20260401194216.fit
2026-05-01 00:15:22.138212 : Successfully deleted file 20260401194216.fit.
2026-05-01 00:15:22.138302 : Deleting  20260421150732.fit
2026-05-01 00:15:22.563068 : Successfully deleted file 20260421150732.fit.
2026-05-01 00:15:22.563184 : Deleting  20260417170423.fit
2026-05-01 00:15:22.975219 : Successfully deleted file 20260417170423.fit.
2026-05-01 00:15:22.975329 : Deleting  20260417144019.fit
2026-05-01 00:15:23.397916 : Successfully deleted file 20260417144019.fit.
2026-05-01 00:15:23.398048 : Deleting  20260424134135.fit
2026-05-01 00:15:23.820013 : Successfully deleted file 20260424134135.fit.
2026-05-01 00:15:23.820127 : Deleting  20260410162730.fit
2026-05-01 00:15:24.245396 : Successfully deleted file 20260410162730.fit.
2026-05-01 00:15:24.245485 : Deleting  20260402180218.fit
2026-05-01 00:15:24.669362 : Successfully deleted file 20260402180218.fit.
2026-05-01 00:15:31.211504 : Successfully wrote combined data to workouts.json
2026-05-01 00:15:31.217477 : Skip: 20260414193929.fit
2026-05-01 00:15:31.217547 : Skip: 20260420192410.fit
2026-05-01 00:15:31.217596 : Skip: 20260409163301.fit
2026-05-01 00:15:31.217652 : Skip: 20260414144956.fit
2026-05-01 00:15:31.217702 : Skip: 20260416191052.fit
2026-05-01 00:15:31.217750 : Skip: 20260423215719.fit
2026-05-01 00:15:31.217827 : Skip: 20260429233905.fit
2026-05-01 00:15:31.217882 : Skip: 20260415232638.fit
2026-05-01 00:15:31.217928 : Skip: 20260410141318.fit
2026-05-01 00:15:31.217974 : Skip: 20260406184015.fit
2026-05-01 00:15:31.218022 : Skip: 20260410141440.fit
2026-05-01 00:15:31.218069 : Skip: 20260428190158.fit
2026-05-01 00:15:31.218115 : Skip: 20260413190854.fit
2026-05-01 00:15:31.218162 : Skip: 20260430191143.fit
2026-05-01 00:15:31.218207 : Skip: 20260407185359.fit
2026-05-01 00:15:31.218252 : Skip: 20260411185357.fit
2026-05-01 00:15:31.218297 : Skip: 20260404223652.fit
2026-05-01 00:15:31.218343 : Skip: 20260424185105.fit
2026-05-01 00:15:31.218389 : Skip: 20260408190754.fit
2026-05-01 00:15:31.218434 : Skip: 20260422193344.fit
2026-05-01 00:15:31.218480 : Skip: 20260427180112.fit
2026-05-01 00:15:31.218524 : Skip: 20260430183321.fit
2026-05-01 00:15:31.218570 : Skip: 20260421184624.fit
2026-05-01 00:15:31.218617 : Skip: 20260426161943.fit
2026-05-01 00:15:31.218662 : Skip: 20260425190516.fit
```
## Adjusting Bluetooth connection parameters for optimum performance (Linux BlueZ)
In the process of testing this script on my Linux PC, I found that the XOSS BLE connection defaulted to a connection interval of 48 ms and a corresponding data transfer rate of roughly 13 kbps. I know based on ekspla's work and other Bluetooth documentation that reducing connection intervals should increase throughput. Reducing the interval to the minimum possible (7.5 ms) correspondingly increased my observed transfer rate to roughly 74 kbps. 

I attempted to change minimum and maximum Bluetooth connection intervals globally through the following command, but I didn't see these changes reflected in the XOSS connection negotiation observed with ```btmon```.

What was successful was adding the following lines to the ```info``` file corresponding to my XOSS in ```/var/lib/bluetooth/XX:XX:XX:XX:XX:XX/YY:YY:YY:YY:YY:YY```, where XX:XX:XX:XX:XX:XX and YY:YY:YY:YY:YY:YY are the MAC addresses of my Bluetooth adapter and XOSS, respectively.

```
[ConnectionParameters]
MinInterval=6
MaxInterval=8
Latency=0
Timeout=216
```

This successfully alters connection interval parameters to a minimum of 7.5 ms (6x1.25 ms) and a maximum of 10 ms just for my XOSS and not for other Bluetooth connections.

## Benchmarking
All benchmarks were conducted with a Lenovo Thinkpad T530 (model 2392AQU) containing a Broadcom BCM20702 Bluetooth 4.0 Bluetooth interface and running Lubuntu 24.04 Noble, BlueZ 5.72, Python 3.12.3, and Bleak 0.21.1.
## Future plans
- Benchmark on multiple fit files and different computers, with at least three replicates in each case
- Helper scripts for preparing user layout and GPS settings jsons
  - User layout JSON indicates which panel contains which measurement field (e.g., average speed, maximum speed, total time, total distance, odometer)
  - GPS settings JSON includes preferences for measurement unit system (metric/imperial), language, and time zone, amongst others
- Options to upload/download user and gear profile jsons
- Helper scripts for preparing user and gear profile jsons 
- Options to upload/download firmware
- Options to get current odometer reading and reset odometer
- Helper script to automate clearing fit files from GPS storage after syncing, perhaps upon hitting a storage threshold (e.g., 2MB or less free)
## References
The product hardware documentation provided below by XOSS/imxingzhe (linked with Google Translate Chinese to English translations) has been incredibly helpful to myself and [ekspla](https://github.com/ekspla) in developing XOSS sync scripts.
1. [Smart code table file format 2.0](https://developer-imxingzhe-com.translate.goog/docs/device/devicefileformat?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_hist=true)
2. [Dabuziduo Smart Hardware Open Platform Access Guide](https://developer-imxingzhe-com.translate.goog/docs/device/getting_started/?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en)
3. [Bluetooth real-time motion data and device control communication protocol](https://developer-imxingzhe-com.translate.goog/docs/device/tracking_data_service?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_hist=true)

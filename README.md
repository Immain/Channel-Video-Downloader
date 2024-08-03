<!-- Start Generation Here -->
<p align="center">
    <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" alt="YouTube Logo" width="200" height="150"/>
</p>
<!-- End Generation Here -->

# Channel Video Downloader
Download the most recent video from a specified YouTube channel, along with its thumbnail. It automatically filters out any videos that are shorter than 60 seconds, ensuring only full-length content is saved. Both the video and thumbnail are stored in designated directories.

## Overview

### Features
- Downloads the latest video from a specified YouTube channel.
- Automatically skips videos that are shorter than 60 seconds.
- Saves both the video and its thumbnail to specified directories.
- Confirms the successful download of files.

## Getting Started

Follow these instructions to set up the project on your local machine for development and testing purposes. For deployment notes, see [deployment](#deployment).

### Prerequisites

- Python 3.7 or higher
- yt-dlp (for downloading videos and extracting metadata)
- requests (for downloading the thumbnail)

### Installation

Follow these steps to get your development environment up and running:

1. **Clone the repository**
   ```
   git clone https://github.com/yourusername/YouTube-Downloader.git
   ```

2. **Navigate to the project directory**
   ```
   cd YouTube-Downloader
   ```

3. **Install the required packages**
   ```
   pip install -r requirements.txt
   ```

4. **Run the script**
   ```
   python run.py
   ```

This will download the latest video from the specified channel and save it along with its thumbnail.


## Automation with Ansible
<!-- Start Generation Here -->
To automate the YouTube Downloader script with Ansible, you can create a playbook that sets up the environment and runs the script. Below is an example of an Ansible playbook that accomplishes this:

```yml
- hosts: localhost
  gather_facts: no
  vars:
    ansible_pyhton_interpreter: /usr/bin/python3
  tasks:
  - name: Download Latest Video
    command: python3 run.py
```

### Cronjob Schedule

To schedule the YouTube Downloader script to run automatically at specified intervals, you can set up a cron job. This cron job will execute the `run.py` script daily at 2 AM, ensuring that the latest video is downloaded automatically.

 Here’s how to do it:

1. Open the crontab configuration:
   ```
   crontab -e
   ```

2. Add the following line to schedule the script. This example runs the script every day at 2 AM:
   ```
   0 2 * * * /usr/bin/python3 /path/to/YouTube-Downloader/run.py
   ```

   Make sure to replace `/path/to/YouTube-Downloader/` with the actual path to your project directory.

3. Save and exit the crontab editor.


## Troubleshooting
- Ensure the specified paths exist and are writable.
- Verify that you have network access to download videos and thumbnails.
- Check for errors in the script output and verify that the necessary packages are installed.

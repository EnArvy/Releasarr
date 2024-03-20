# Releasarr

A simple tool to add downloads to your download client with a nice frontend. Think a stripped down version of Sonarr/Radarr, without all the automation.

Currently supports usenet with Sabnzbd and NZBHydra, and a simple login.

Contributions welcome!

## Installing

- Clone the repo
- Install dependencies using `pip install -r requirements.txt`
- Fill the environment variables in `config.py`
- Run as `gunicorn --config gunicorn_config.py releasarr:app`
- Add release terms you want to exclude to Excluded variable and terms you want to Preferred variable. `Preferred = ['hevc','h.265']`, `Excluded = ['Remux','CAM']`
- By default, releases are sort from lower to higher file size, with Preferred releases appearing at top.
## Screenshots
![Home](https://i.imgur.com/JdrexC0.png)
![Search](https://i.imgur.com/beNaPs3.png)
![Download](https://i.imgur.com/W1kWHzy.png)
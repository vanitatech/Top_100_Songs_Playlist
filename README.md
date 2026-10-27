# Top 100 Songs Playlist

A small Python script that looks up the Billboard Hot 100 chart for a selected date, then creates a private YouTube Music playlist and adds the chart songs it can find.

## How it works

1. Prompts for a date in `YYYY-MM-DD` format.
2. Fetches the chart page for that date from the App Brewery chart archive.
3. Extracts song titles from the page.
4. Searches YouTube Music for each title and adds the first matching song to a new private playlist named `<date> Billboard 100`.
5. Prints each successful addition and any songs it skips.

## Requirements

- Python 3
- A YouTube Music account
- Firefox (used to obtain the browser authentication headers)

Install the Python dependencies:

```bash
pip install requests beautifulsoup4 ytmusicapi
```

## YouTube Music authentication

The script expects a `browser.json` authentication file in the project directory. This file contains private account/session information and must not be shared or committed to version control.

1. From this project directory, run:

   ```bash
   ytmusicapi browser
   ```

2. Follow the prompts and copy the required request headers from an authenticated YouTube Music session in Firefox. The command creates `browser.json`.
3. Keep `browser.json` private. It is listed in `.gitignore` already.

Authentication instructions can change with `ytmusicapi` updates; consult its current documentation if the command or browser flow differs.

## Run

From the project directory:

```bash
python main.py
```

When prompted, enter a chart date in `YYYY-MM-DD` format, for example `2015-08-22`.

The playlist is created with **Private** visibility in the authenticated YouTube Music account. Check the titles and matches in YouTube Music afterward; searches may select a different version or fail to find a song.

## Notes

- The selected date must have a chart page available in the chart archive.
- The script does not currently validate the date or recover from network/chart-page errors.
- Each search uses the first YouTube Music song result, so matches are not guaranteed to be the exact chart recording.
- Re-running the script for the same date creates another playlist rather than updating an existing one.

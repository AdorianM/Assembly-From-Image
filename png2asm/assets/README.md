# Releasing with auto-py-to-exe

Creating a 'one-file' version of the app has a [particularity](https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/13790741#13790741). In order for pyinstaller to work, this is followed in the source code, but the release process is not as straight forward as before.

## Settings for auto-py-to-exe

- Path to file: `actual/path/to/app.py`
- Onefile: One File
- Console Window: Window Based (hide the console)
- Icon: `actual/path/to/icon.ico`
- Additional Files: `actual/path/to/icon.ico | ./assets` (actual icon path and the icon path relative to the source code)

## Equivalent command

`pyinstaller --noconfirm --onefile --windowed --icon "actual/path/to/chef.ico" --add-data "actual/path/to/chef.ico;./assets"  "actual/path/to/app.py"`

## Additional observations

Packages should be installed before trying to release (i.e. [Pillow](https://pillow.readthedocs.io/en/stable/))
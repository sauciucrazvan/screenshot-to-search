# Screenshot to Search

- Take a screenshot and automatically search it with Google Lens.

> This is just a demonstration of a concept. Built in around ~8 hours.
Written in Python with PyQt. Uses ImgBB as the image storing provider via their API.


## Installation and Usage

- Go to the [releases tab](https://github.com/sauciucrazvan/screenshot-to-search/releases/) and download the latest version.
- Press CTRL+Shift+J wherever you are to take a screenshot. The search will automatically begin.
- To exit of the screenshot state, press Escape while dragging the screenshot tool.

## Snapshot

![SS to Search](https://i.imgur.com/Tkv74JP.gif)

## Structure

The project consists of two parts: a runner (that opens the app when the hotkeys are pressed) and the app itself.

The application lays under the bin folder. Should be "compiled" with PyInstaller.

### --- Running the app locally

* Clone the repository and install all the dependencies.
* Make sure you've created the ``cred.py`` file under the application/services/ folder and filled it up with your API key.
```
def getApiKey():
    return "YOUR_API_KEY"
```

* Run the screenshot-to-search.py script to start the runner. Close it with CTRL+C when needed.

## License

Feel free to fork, edit or do whatever you want with the source-code & application.
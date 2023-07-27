# Live AI Commentary for Rat Races
A live, expressive commentary for a rat race with ChatGPT and Elevenlabs

See the Jupyer Notebook -- it contains markdown cells wth some description on how to use it.

## Setup
```
cd <YOUR_PROJECT_DIR>
git clone git@github.com:mrslacklines/ai_ratrace_live_commentator.git
cd ai_ratrace_live_commentator
python3 -m venv venv
pip install --upgrade pip
pip install -r requirements.txt
```
Put you API keys for OpenAI and Elevenlabs in the .env file. Edit `race_data.json` or use the current example data.

## Running

```
cd <PROJECT_PATH>
source venv/bin/activate
python -m jupyter notebook
```
Open the `stream_audio_commentary.ipynb` notebook and run all cells. The last cell contains a loop that will keep asking for a stage name for which to generate audio output. The available stage names are:

```
RACE_STAGES = [
    "initial",
    "prerace",
    "start",
    "midrace",
    "finish",
    "winner",
]
```

IMPORTANT: Never use the `initial` stage. This is used only for internal bot setup.
The other stages are designed to be run sequentially. The `prerace` and `midrace` stages can be run a number of times in a row. The remaining stages should be only run once. This is due to the fact that
the bot keeps the history of stages ran in a single sesh. If you run the `start` stage the bot will announce that the race has started. If you run this stage again the bot might come up with some weird output
as you will basically ask him to announce another start after the race has already started.

You might want to play around with the ChatGPT prompts to change the behavior and output of the bot but remember that these are more less fine tuned for a number of cases and adding and removing stuff
might change its behavior or even break the bot completely.

I might update the code from time to time. If you want to get the new functionality you need to `git pull origin main` in your local repository (project dir).

Have fun and do not harass any animals please. :)

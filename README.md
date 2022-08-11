## How to Build HTML

1. Update the `.rst` file in Easy-Graph Documentation - source
2. Run powershell or cmd, changing work directory to `docs_using_sphinx`
3. run `python3 -m venv .env` for the virtual environment
4. run `source .env/bin/activate` to activate
5. run `pip install -r requirements.txt` to install dependencies
6. Run ` make html`. The updated pages locate in `./_build/html`
7. Copy all the files under `./_build/html` to repository `easy-graph.github.io`
8. Push the changes to origin masters of these two repository

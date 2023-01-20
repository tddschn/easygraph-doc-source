# easygraph-doc-source

Scripts and guides for generating documentation for EasyGraph.

- [easygraph-doc-source](#easygraph-doc-source)
  - [Prerequisites](#prerequisites)
  - [Update `rst` files](#update-rst-files)
    - [Edit manually created `rst` files](#edit-manually-created-rst-files)
    - [Generate `rst` files from docstrings as references](#generate-rst-files-from-docstrings-as-references)
  - [Build HTML from `rst` files](#build-html-from-rst-files)
  - [Deploy to easy-graph.github.io](#deploy-to-easy-graphgithubio)
  - [Troubleshooting](#troubleshooting)
    - [Reference built but not correctly displayed on the website](#reference-built-but-not-correctly-displayed-on-the-website)

## Prerequisites

Clone these repositories and put them inside the same directory:

```bash
REPOS=('Easy-Graph' 'easy-graph.github.io' 'easygraph-doc-source')
for i in "${REPOS[@]}"; do
    echo "Cloning: $i"
    git clone "https://github.com/easy-graph/$i"
done
```

## Update `rst` files

### Edit manually created `rst` files

Go to `easygraph-doc-source/docs_using_sphinx`, and hand-edit / remove / add any `rst` files outside of `reference`.

### Generate `rst` files from docstrings as references


```bash
cd easygraph-doc-source/docs_using_sphinx
make gen-rst
# generated rst files in reference dir
```

## Build HTML from `rst` files

<!-- 1. Update the `.rst` file in `docs_using_sphinx`
2. Run terminal, changing work directory to `docs_using_sphinx`
3. run `python3 -m venv .env` for the virtual environment
4. run `source .env/bin/activate` to activate
5. run `pip install -r requirements.txt` to install dependencies -->
- Install dependencies in `requirements.txt`.
- Run ` make html`. The updated pages locate in `./_build/html`.

## Deploy to easy-graph.github.io

- Sync all the files under `./_build/html` to repository `easy-graph.github.io`:

```bash
cd easygraph-doc-source
make sync-to-doc-pub-repo
```

- Push the changes of these two repository to their remotes

## Troubleshooting

### Reference built but not correctly displayed on the website
- Check the `toctree` of `reference.rst`, you may need to manually update the section to reflect the built references.
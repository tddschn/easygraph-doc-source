sync-to-doc-pub-repo:
	rsync -au --delete --progress -h ./docs_using_sphinx/_build/html/ ../easy-graph.github.io/docs

.PHONY: *

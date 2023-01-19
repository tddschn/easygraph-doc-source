sync-to-doc-pub-repo:
	# rsync -au --delete --progress -h ./docs_using_sphinx/_build/html/ ../easy-graph.github.io/docs
	rsync $(if $(filter -n,$(MAKECMDGOALS)),-n,) -au --delete --progress -h ./docs_using_sphinx/_build/html/ ../easy-graph.github.io/docs

.PHONY: *


.PHONY: *

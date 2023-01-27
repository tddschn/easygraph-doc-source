.DEFAULT_GOAL := help

sync-doc-pub-repo: ## sync the docs to the easy-graph.github.io repo
	# rsync -au --delete --progress -h ./docs_using_sphinx/_build/html/ ../easy-graph.github.io/docs
	# allows the user to pass -n to the sync-to-doc-pub-repo target, which in turn passes it to the rsync command
	# https://chat.openai.com/chat/f9981feb-0732-439f-ad11-ba35634f4658
	rsync $(if $(filter -n,$(MAKECMDGOALS)),-n,) -au --delete --progress -h ./docs_using_sphinx/_build/html/ ../easy-graph.github.io/docs --exclude='**/*test*'

update-doc-pub-repo: ## update the docs to the easy-graph.github.io repo
	# rsync -au --delete --progress -h ./docs_using_sphinx/_build/html/ ../easy-graph.github.io/docs
	# allows the user to pass -n to the sync-to-doc-pub-repo target, which in turn passes it to the rsync command
	# https://chat.openai.com/chat/f9981feb-0732-439f-ad11-ba35634f4658
	rsync $(if $(filter -n,$(MAKECMDGOALS)),-n,) -au --progress -h ./docs_using_sphinx/_build/html/ ../easy-graph.github.io/docs --exclude='**/*test*'

gen-easygraph-doc-source-rst: ## generate the easygraph-doc-source.rst file
	pandoc README.md -o docs_using_sphinx/dev/easygraph-doc-source.rst


.PHONY: *

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
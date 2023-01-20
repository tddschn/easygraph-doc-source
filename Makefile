sync-to-doc-pub-repo:
	# rsync -au --delete --progress -h ./docs_using_sphinx/_build/html/ ../easy-graph.github.io/docs
	# allows the user to pass -n to the sync-to-doc-pub-repo target, which in turn passes it to the rsync command
	# https://chat.openai.com/chat/f9981feb-0732-439f-ad11-ba35634f4658
	rsync $(if $(filter -n,$(MAKECMDGOALS)),-n,) -au --delete --progress -h ./docs_using_sphinx/_build/html/ ../easy-graph.github.io/docs --exclude='**/*test*'

.PHONY: *


.PHONY: *

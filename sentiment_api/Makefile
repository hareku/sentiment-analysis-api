build-SentimentAnalysisFunction:
	cp *.py $(ARTIFACTS_DIR)
	cp -r models $(ARTIFACTS_DIR)/models
	cp requirements.txt $(ARTIFACTS_DIR)
	python -m pip install -r requirements.txt -t $(ARTIFACTS_DIR)
	rm -rf $(ARTIFACTS_DIR)/bin

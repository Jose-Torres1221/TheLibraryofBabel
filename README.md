# TheLibraryofBabel
This is a project completed for the graduate Natural Language Processing course taught at UT Austin by Professor Abhijit Mishra during the Fall 2024 semester.

# How to Run?
We have attached 5 Jupyter Notebooks, 1 Python file and 5 CSV files.

**To replicate our results in the report with fine-tuned BART model:** <br>
Following 3 notebooks are crutial to replicate our result.
  * `BART_CasaInternational.ipynb` (Notebook to fine-tune BART model)
  * `runModel_BART_CasaInternational.ipynb` (Notebook to extract summary using plain and fine-tuned BART model)
  * `evaluator_CasaInternational.ipynb` (Evaluate summary produced above using BLEU, METEOR, ROUGE and BERT scores)

Follow steps below.
  1.  Replicate 3 notebooks described above and `csvFiles` folder (includes train & test data) to the environment you want to run the model
  2.  Run 3 notebooks in the same order as described above
  3.  Inspect resulting 4 CSV files (Result for plain and fine-tuned model both for Japanese and Spanish abstracts)

**To test the pipeline with an abstract of your choice:** <br>
Use Gradio demo
  *  Run `demo_CasaInternational.ipynb`
  *  Input abstract of your choice (Japanese, Spanish or English). Note this will just return summarization, not evaluation scores.

# Detailed description of code files<br>
**Jupyter notebooks**<br>
1. BART_CasaInternational.ipynb
   *  Function: Import `facebook/bart-large-cnn` model, fine-tune using training data and return fine-tuned model
   *  Input: Train data (`csvFiles/combinedDF.csv`)
   *  Output: Fine-tuned model (`./fine_tuned_BART_summarization`)

2. runModel_BARTcasaInternational.ipynb
   *  Function: Import both plain & fine-tuned `facebook/bart-large-cnn` models. Run models and return summarized abstracts generated from test data
   *  Input:
      - Fine-tuned model: `./fine_tuned_BART_summarization`
      - test data(`csvFiles/papers_EStoEN.csv`, `csvFiles/papers_JPtoEN.csv`)
   *  Output: Summarized test data (`summarization_BART_JP.csv`,`summarization_BART_ES.csv`)

3. evaluator_CasaInternational.ipynb
   *  Function: Evaluate the quality of summarized test data using BLEU, METEOR, ROUGE, BERT score. ROUGE includes ROUGE-1,2, and L. Both ROUGE and BERT returns precision, recall, and F1 score.
   *  Input:
      - Summarized test data: `summarization_BART_JP.csv`,`summarization_BART_ES.csv`
      - Reference summary (`csvFiles/papers_EStoEN.csv`, `csvFiles/papers_JPtoEN.csv`)
   *  Output: Scores for plain and fine-tuned model (`scores_JP_BART.csv`,`scores_JP_BART_ft.csv`,`scores_ES_BART.csv`,`scores_ES_BART_ft.csv`)
  
4. demo_CasaInternational.ipynb
   *  Function: Activate Gradio demo to test the pipeline with arbitrary abstract in either Japanese, Spanish or English
   *  Input: Fine-tuned model: `./fine_tuned_BART_summarization`
   *  Output: None

5. paperTranslation_CasaInternational.ipynb
   *  Function: Clean non-English abstract & summary and translate to English using `facebook/seamless-m4t-v2-large`. Used to prepare test dataset.
   *  Input: Two Dataframes (1 Japanese and 1 Spanish) with "abstract" and "contribution" column. 
   *  Output: test data (`csvFiles/papers_EStoEN.csv`, `csvFiles/papers_JPtoEN.csv`)

**Python file**<br>
1. PreProcessesDFs_CasaInternational.py
   *  Function: Combine training data prepared by team members and preprocess the text for fine-tuning. Used to create training dataset.
   *  Input: Fragmented training data prepared by team members
   *  Output: Train data (`csvFiles/combinedDF.csv`)

----------------------------------------

Members of CasaInternational:<br>
***Ryotaro Takehara***<br>
***Jose Torres***<br>
***Naila Hajiyeva***<br>

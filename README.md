# TheLibraryofBabel
This is a project completed for the graduate Natural Language Processing course taught at UT Austin by Professor Abhijit Mishra during the Fall 2024 semester.

# How to Run?
We have attached 5 Jupyter Notebooks and 1 Python file.

To receive the same results for our best model, in this case BART, please follow these instructions:

1. Will you be using combinedDF?
  <br>a. No.
  <br>Run the Python file after ensuring that jose_English and ryotaro_English are in the same directory. This will return the combinedDF as the final saved CSV.
  <br>b. Yes.
  <br>Continue to 2.
2. Will you be using the pre-Translated papers?
  <br>a. No.
  <br> Run the paperTranslation notebook in the same directory as jose_Spanish and ryotaro_Japanese. This will return the translated papers as a CSV.
  <br>b. Yes.
  <br> Continue to 3.
3. Run the extractContributions_BART notebook
   <br>Ensure the translated papers in the same directory. This will return CSV's of the abstract, the reference summary and the computer generated summary.
   <br>Then proceed to 4.
5. Run the evaluator notebook
   <br>Ensure the summaries from the translated papers are in the same directory. This program will return the scores from the following metrics:
   <br>**BLEU**
   <br>**ROUGE**
   <br>**METEOR**
   <br>**BERTScore**
   <br> ROUGE and BERTScore will also return their precision, recall and F1 score.

<br>Following these steps will allow anyone who has downloaded our files to run this program and recreate what we did.
<br>Final report to be added when completed.
<br>Bonus: We have included the notebook for a gradio demo. Feel free to insert your own English abstracts or any abstract in the currently supported lanuages (Spanish and Japanese).

Members of CasaInternational:
<br>Ryotaro Takehara
<br>Jose Torres
<br>Naila Hajiyeva

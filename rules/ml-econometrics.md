# ML vs Econometrics Standards

Standards for distinguishing predictive ML workflows from econometric inference
workflows.

- Treat econometrics and machine learning as different workflow classes with different
  goals.
- Use econometric tools such as `statsmodels` for causal inference and hypothesis
  testing.
- Use machine-learning tools such as scikit-learn for prediction tasks.
- Never interpret machine-learning model parameters causally.
- Never skip a train/test split for prediction tasks.
- Never evaluate predictive performance on the training data alone.
- Use cross-validation for hyperparameter tuning.
- Reserve the test set for final evaluation only.

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

# Compute metrics
cm = confusion_matrix(y_true, y_pred, labels=labels)
acc = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, labels=labels, average=None)
recall = recall_score(y_true, y_pred, labels=labels, average=None)
f1 = f1_score(y_true, y_pred, labels=labels, average=None)

# Macro-averaged scores
macro_precision = precision_score(y_true, y_pred, average='macro')
macro_recall = recall_score(y_true, y_pred, average='macro')
macro_f1 = f1_score(y_true, y_pred, average='macro')

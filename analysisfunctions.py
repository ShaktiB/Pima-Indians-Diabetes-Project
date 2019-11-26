# The 'modeleval' function returns all the evaluation metrics that are being used to gage all the model's performance

from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import auc

def modeleval(yTrue, yPredict, print_metrics):
    # Area Under ROC Curve
    auc = roc_auc_score(yTrue,yPredict)

    # Confusion Matrix Evaluation 
    cm = confusion_matrix(yTrue,yPredict)

    # True negative, Flase positive, false negative, true positive
    tn, fp, fn, tp = confusion_matrix(yTrue,yPredict).ravel() 

    # True Positive Rate (Sensitivity)
    tpr = tp/(tp+fn)

    # True Negative Rate (Specificity)
    tnr = tn/(tn+fp)

    # Accuracy 
    acc = accuracy_score(yTrue,yPredict)
    
    # Model Metrics
    mm = {
        'AUC':auc,
        'Confusion Matrix':cm,
        'TN':tn,
        'FP':fp,
        'FN':fn,
        'TP':tp,
        'TPR':tpr,
        'TNR':tnr,
        'Accuracy':acc
    }
    
    if print_metrics:
        print(f"Sensitivity:{mm['TPR']}\n\n\
Specificity:{mm['TNR']}\n\n\
AUC of ROC:{mm['AUC']}\n\n\
Accuracy:{mm['Accuracy']}\n\n")
        
        x = pd.crosstab(yTrue, yPredict, rownames=['True'], colnames=['Predicted'], margins=True)
        print(f"{x}\n")
        plot_confusion_matrix(yTrue, yPredict,classes=np.array(['No Diabetes','Diabetes']),
                      title='Confusion matrix: SVM')
        plt.show()
    
    return mm       

def plotroc(yvt,yvp,modelname): # y_validation_truth & y_validation_prediction
    f, t, thresh = roc_curve(yvt, yvp)
    roc_auc = auc(f, t)
    plt.title('Receiver Operating Characteristic: ' + modelname)
    plt.plot(f, t, 'b', label = 'AUC = %0.2f' % roc_auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()
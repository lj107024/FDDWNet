from model.FDDWNet import Net

def build_model(model_name, num_classes):
    if model_name == 'FDDWNet':
        return Net(classes=num_classes)
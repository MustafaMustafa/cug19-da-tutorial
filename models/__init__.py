"""
Keras example model factory functions.
"""

def get_model(name, **model_args):
    if name == 'cnn':
        from .cnn import build_model
        return build_model(**model_args)
    if name == 'resnet18_cifar':
        from .resnet import build_resnet18_cifar
        return build_resnet18_cifar(**model_args)
    else:
        raise ValueError('Model %s unknown' % name)

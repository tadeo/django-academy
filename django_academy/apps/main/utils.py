from django.db import models

def get_model_by_name(model_name):
    """
        Returns a model class constructor from a name
        or rise an exception if the model does not exist.

        The general rule is to capitalize its argument and lookup
        a model class with that name, if not found then we check
        the model_mapping dictionary defined in this module.
    """
    try:
        model = filter(lambda m: m.__name__ == model_name, models.get_models())[0]
    except IndexError:
        raise Exception('%s doesn\'t match the name of any available model.' % model_name)

    return model


def camelcase_to_underscore(text):
    import re
    new = re.sub('(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))', '_\\1', text)
    return new.lower().strip('_')


def get_generic_object_form(model_class):
    from django.forms.models import ModelForm
    class ObjectForm(ModelForm):
        class Meta:
            model = model_class
    return ObjectForm

def get_form_by_class(model_class, suffix='Form'):
    if type(model_class) == str:
        model_class = get_model_by_name(model_class)
    model_form_class_name = model_class.__name__ + suffix
    module_path = 'apps.%s.forms' % model_class._meta.app_label
    try:
        imported_module = __import__(module_path, globals(), locals(), [model_form_class_name], -1)
        model_form = getattr(imported_module, model_form_class_name)
    except:
        model_form = get_generic_object_form(model_class)
    return model_form


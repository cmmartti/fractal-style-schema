import os
import importlib
from inspect import getmembers, isclass
from graphene import ObjectType
import logging

logger = logging.getLogger(__name__)


def schema_operations_builder(operationName, operationModule, operationBase, clsName):

    op_base_classes = build_base_classes(operationName, operationModule, operationBase, clsName)
    properties = {}
    # filter on scopes before this
    for base_class in op_base_classes:
        properties.update(base_class.__dict__['_meta'].fields)
    ALL = type(operationName, tuple(op_base_classes), properties)
    return ALL


def build_base_classes(operationName, operationModule, operationBase, clsName):
    class OperationAbstract(ObjectType):
        scopes = ['unauthorized']
        pass

    current_directory = os.path.dirname(os.path.abspath(__file__))
    current_module = current_directory.split('/')[-1]
    subdirectories = [
        x for x in os.listdir(current_directory)
            if os.path.isdir(os.path.join(current_directory, x))
               and x != '__pycache__'
               and x != 'root'
    ]
    op_base_classes = [OperationAbstract]

    for directory in subdirectories:
        # try:
            print 'graphql_api.{0}.{1}'.format(directory, operationModule)
            module = importlib.import_module(
                'graphql_api.{0}.{1}'.format(directory, operationModule)
            )
            if module:
                print 'HERE'
                classes = [x for x in getmembers(module, isclass)]
                opers = [x[1] for x in classes if clsName in x[0] and x[0] != operationBase]
                op_base_classes += opers
            else:
                print 'wat?'
                logger.info('wat?')
                logger.debug(current_directory)
        except ImportError:
            pass

    op_base_classes = op_base_classes[::-1]
    return op_base_classes

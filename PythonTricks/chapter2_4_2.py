# Underscores, Dunders & More P2

import chapter2_4_2_module

print(chapter2_4_2_module.external_func())

print(chapter2_4_2_module._internal_func())

'''
doing from chapter2_4_2_module import * does not allow
_internal_func to be defined. And so just do import
chapter2_4_2module not the wildcard import
'''
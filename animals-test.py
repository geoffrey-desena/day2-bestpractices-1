#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:24:03 2026

@author: geoffreydesena
"""

import animals

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()

# %% Part g: run ruff on the code

# Not sure what I'm supposed to do with this information

# (base) geoffreydesena@emp-51-101 day2-bestpractices-1 % ruff check animals
# animals/__init__.py:9:22: F401 `.mammals.Mammals` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
#    |
#  7 | """
#  8 |
#  9 | from .mammals import Mammals
#    |                      ^^^^^^^ F401
# 10 |
# 11 | import dangerous
#    |
#    = help: Use an explicit re-export: `Mammals as Mammals`

# animals/__init__.py:11:8: F401 `dangerous` imported but unused
#    |
#  9 | from .mammals import Mammals
# 10 |
# 11 | import dangerous
#    |        ^^^^^^^^^ F401
# 12 | import harmless
#    |
#    = help: Remove unused import: `dangerous`

# animals/__init__.py:12:8: F401 `harmless` imported but unused
#    |
# 11 | import dangerous
# 12 | import harmless
#    |        ^^^^^^^^ F401
#    |
#    = help: Remove unused import: `harmless`

# animals/dangerous/__init__.py:9:19: F401 `.fish.Fish` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
#   |
# 7 | """
# 8 |
# 9 | from .fish import Fish
#   |                   ^^^^ F401
#   |
#   = help: Use an explicit re-export: `Fish as Fish`

# animals/harmless/__init__.py:9:20: F401 `.birds.Birds` imported but unused; consider removing, adding to `__all__`, or using a redundant alias
#   |
# 7 | """
# 8 |
# 9 | from .birds import Birds
#   |                    ^^^^^ F401
#   |
#   = help: Use an explicit re-export: `Birds as Birds`


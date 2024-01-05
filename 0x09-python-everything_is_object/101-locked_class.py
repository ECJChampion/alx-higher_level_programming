#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, attr, value):
        if attr != 'first_name' and not hasattr(self, attr):
            raise AttributeError(f"Cannot create new instance attribute '{attr}'")
        else:
            object.__setattr__(self, attr, value)


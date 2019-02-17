# -*- coding: utf-8 -*-
filter_field_set = {"0", '0.00', 0, None}
preserve_field_set = []


class FilterNull:
    def __init__(self, preserve_field, filter_field):
        self.preserve_field = preserve_field
        self.filter_field = filter_field
        self.invalid_count = 0

    def filter_null(self, pass_object):
        if isinstance(pass_object, list):
            new_object = []
            if pass_object:
                for item in pass_object:
                    if isinstance(item, list):
                        new_object.append(self.filter_null(item))
                    elif isinstance(item, dict):
                        new_object.append(self.filter_null(item))
                    elif item in self.filter_field:
                        continue
                    else:
                        new_object.append(item)
                        self.invalid_count += 1
                return new_object
            else:
                return pass_object
        elif isinstance(pass_object, dict):
            new_object = dict()
            if pass_object:
                for key, value in pass_object.items():
                    if isinstance(value, list):
                        new_object[key] = self.filter_null(value)
                    elif isinstance(value, dict):
                        new_object[key] = self.filter_null(value)
                    elif value in self.filter_field:
                        if key in self.preserve_field:
                            new_object[key] = value
                        else:
                            continue
                    else:
                        new_object[key] = value
                        self.invalid_count += 1
                return new_object
            else:
                return pass_object
        else:
            self.invalid_count += 1

ins_filter = FilterNull(preserve_field_set, filter_field_set)

#if __name__ == '__main__':
#    pass_object = [0, 1, [0, 1, 1, 0], {'a': 0, "b": None, "c": 1, "d": [0, 1, 1, {}]}]
#    print(FilterNull(preserve_field_set, filter_field_set).filter_null(pass_object))

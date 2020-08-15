def rec_flattener(flat, dictionary, key=""):
    # check of each item in dict:
    for k, v in dictionary.items():
        # if items is dict :
        if isinstance(v, dict):
            # recursevly flatten this dict
            if k is not "" and key is not "":
                rec_flattener(flat, v, key + "." + str(k))
            else:
                rec_flattener(flat, v, key + str(k))
        # else: append ( "key.item")
        else:
            if k is not "" and key is not "":
                flat[key + "." + k] = v
            elif k is not "" and key is "":
                flat[k] = v
            elif k is "" and key is not "":  # k is "" and key is empty
                flat[key] = v
            else:
                flat[key] = v


def flatten_dictionary(dictionary):
    flat = {}
    rec_flattener(flat, dictionary)
    return flat


if __name__ == "__main__":
    dicti = {
        "Key1": "1",
        "Key2": {
            "a": "2",
            "b": "3",
            "c": {
                "d": "3",
                "e": {
                    "": "1"
                }
            }
        }
    }
    print(flatten_dictionary(dicti))
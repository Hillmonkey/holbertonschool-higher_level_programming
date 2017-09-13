#!/usr/bin/python3
""" 16-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
    dud_input = None
    dud_output = Rectangle.from_json_string(dud_input)

    print("[{}] {}".format(type(dud_input), dud_input))
    # print("[{}] {}".format(type(json_dud_input), json_dud_input))
    print("[{}] {}".format(type(dud_output), dud_output))

    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))

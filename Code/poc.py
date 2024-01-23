final_list = []
test_dict = {
    "Guide 1": {
        "Section 1": "Some singular paragraph",
        "Section 2": {
            "Header": "Header paragraph of heading 2",
            "Sub-section 1": "Contents of sub-section 1",
            "Sub-section 2": "Contents of sub-section 2",
            "Sub-section 3": "Contents of sub-section 3"
        }
    },
    "Guide 2": {
        "gvar": "gvar GUID string"
    },
    "Guide 3": {
        "svar": "name of svar"
    }
}

test_list = [
        "Some sort of header paragraph",
        "**subtopic**\nDetails spelled out in a paragraph of sorts",
        "**subtopic2**\nDetails spelled out in a paragraph of sorts",
        "**Subtopic3**\nDetails spelled out in a paragraph of sorts"
    ]

i = 0
for item in test_list:
    try:
        final_list[i].append(item)

    except:
        final_list.append([item])

    if len("\n\n".join(final_list[i])) > 30:
        i =+ 1

    else:
        pass

# for item in final_list:
#     print("\n\n".join(item))
#     print(len("\n\n".join(item)))

# print(final_list)


def split_string(list_of_lists: list[str], list_num: int) -> str:


    split_list = [list_of_lists.pop(0), []]

    i = 1
    for guide in list_of_lists:

        split_list[i].append(guide)
        test_string =  f'{split_list[0]}' + "\n\n".join(split_list[i])

        if len(test_string) < 300:
            pass

        else:
            i += 1
            split_list.append([])
    
    if list_num < 1:
        list_num = 1

    elif list_num > len(split_list) - 1:
        list_num = len(split_list) - 1

    else:
        pass

    if len(split_list) == 1:
        list_addon = ""

    else:
        list_addon = f"List {list_num}/{len(split_list) - 1}\n"

    return f"{list_addon}{split_list[0]}\n" + "\n\n".join(split_list[list_num])


def capitalize_name(name: str) -> str:
    """
    Capitalizes name.
    
    Args:
        name: Name to capitalize.

    Return:
        (str): Capitalized name
    """

    # For multi-word names
    name_list_temp = name.split(" ")
    name_list = []

    # Each word gets lowercased and first letter capitalized
    for temp_name in name_list_temp:
        name_list.append(temp_name.lower().capitalize())

    return " ".join(name_list)


def grab_general(general_dictionary: dict, list_num: int) -> str:
    result_list = ["## Guides"]

    for guide_key, guide_value in general_dictionary.items():
        temp_list = [f"**{capitalize_name(str(guide_key))}**"]

        for section_key in general_dictionary[guide_key].keys():
            temp_list.append(capitalize_name(str(section_key)))

        result_list.append("\n".join(temp_list))

    return split_string(result_list, list_num)


test_dict = {
    "Guide 1": {
        "skjhfajkfh jdhfjahdfjkashdfjkahjfkhakjdfhakjdfhajkdhfjklashdflkjahdfjkahsdfkjhasdfkljhadjkfhasjkfhaskjldfhkasjhfkajhdfkjashfkjahfkjahdfkjahdkfjhaskdjfhaskjfhkajsfhkjshdfkjahdfk": "Some singular paragraph",
        "Section 2": {
            "Header": "Header paragraph of heading 2",
            "Sub-section 1": "Contents of sub-section 1",
            "Sub-section 2": "Contents of sub-section 2",
            "Sub-section 3": "Contents of sub-section 3"
        }
    },
    "Guide 2": {
        "sfdgk jjiojioejwqrmiowerjc qejriqwjeriqjw eriqjewroij": "gvar GUID string"
    },
    "Guide 3": {
        "svar": "name of svar"
    },
    "Guide 4": {
        "svar": "name of svar"
    },
    "Guide 5": {
        "svar": "name of svar"
    },
    "Guide 6": {
        "svar": "name of svar"
    },
    "Guide 7": {
        "svar": "name of svar"
    }
}


print(grab_general(test_dict, -4646546))







"""10/14 Lesson on Unit Tests"""


def get_first(str_list: list[str]) -> str:
    """Return first element"""
    if len(str_list) == 0:
        return ""
    return str_list[0]


def remove_first(str_list: list[str]) -> None:
    """Remove first element"""
    str_list.pop(0)


def get_and_remove_first(str_list: list[str]) -> str:
    """Return and remove first element"""
    return str_list.pop(0)


if __name__ == "__main__":
    """Test if fns are working"""
    sent: list[str] = ["Hi", "there", "Bob"]
    print(get_first(sent))
    remove_first(sent)
    print(sent)
    print(get_and_remove_first(sent))
    print(sent)

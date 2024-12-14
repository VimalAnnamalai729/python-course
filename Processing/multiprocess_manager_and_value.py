"""
1. Sharing a List
Use multiprocessing.Manager to create a shared list.
"""

from multiprocessing import Process, Manager


def modify_list(shared_list):
    shared_list.append(100)


if __name__ == "__main__":
    with Manager() as manager:
        shared_list = manager.list([1, 2, 3])  # Shared list
        p = Process(target=modify_list, args=(shared_list,))
        p.start()
        p.join()
        print(shared_list)  # Output: [1, 2, 3, 100]

"""
2. Sharing a String
Use Manager to create a shared string or use a Value with a ctypes character array.
"""

from multiprocessing import Process, Manager


def modify_string(shared_string):
    shared_string.value = "Modified!"


if __name__ == "__main__":
    with Manager() as manager:
        shared_string = manager.Value('c', "Initial!")  # Shared string
        p = Process(target=modify_string, args=(shared_string,))
        p.start()
        p.join()
        print(shared_string.value)  # Output: Modified!

"""3. Sharing a Dictionary
Use multiprocessing.Manager to create a shared dictionary."""

from multiprocessing import Process, Manager


def modify_dict(shared_dict):
    shared_dict["key"] = "value"


if __name__ == "__main__":
    with Manager() as manager:
        shared_dict = manager.dict()  # Shared dictionary
        p = Process(target=modify_dict, args=(shared_dict,))
        p.start()
        p.join()
        print(shared_dict)  # Output: {'key': 'value'}

"""4. Sharing a Set
Use multiprocessing.Manager to create a shared set."""

from multiprocessing import Process, Manager


def modify_set(shared_set):
    shared_set.add(99)


if __name__ == "__main__":
    with Manager() as manager:
        shared_set = manager.set([1, 2, 3])  # Shared set
        p = Process(target=modify_set, args=(shared_set,))
        p.start()
        p.join()
        print(shared_set)  # Output: {1, 2, 3, 99}

"""
5. Using Value for ctypes-based Arrays and Strings
For simple use cases, you can use Value for a ctypes array to 
share a fixed-length string or array:
"""

from multiprocessing import Value, Process
import ctypes


def modify_string(shared_string):
    shared_string.value = b"Hello!"


if __name__ == "__main__":
    shared_string = Value(ctypes.c_char_p, b"Initial!")  # Shared fixed-length string
    p = Process(target=modify_string, args=(shared_string,))
    p.start()
    p.join()
    print(shared_string.value.decode())  # Output: Hello!

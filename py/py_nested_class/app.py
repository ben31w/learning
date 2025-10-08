# class MainWindow:
#     def __init__(self):
#         self.my_dict = {}
#         self.frame1 = MainWindow.Frame1()
#
#     class Frame1:
#         def __init__(self):
#             MainWindow().my_dict = {
#                 "Hello": "World"
#             }
#
#
# mw = MainWindow()
# print(mw.my_dict)


class OuterClass:
    def __init__(self):
        self.outer_variable = "I am an outer variable"

    class NestedClass:
        def nested_method(self):
            print(OuterClass().outer_variable)

    
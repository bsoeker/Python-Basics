from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class DropDownList(UIControl):
    def draw(self):
        print("DropDown!!")


class TextBox(UIControl):
    def draw(self):
        print("TextBox!")


def draw(control: UIControl) -> None:
    control.draw()


controlList: list[UIControl] = []
controlList.append(TextBox())
controlList.append(DropDownList())
controlList.append(TextBox())
controlList.append(DropDownList())


for control in controlList:
    control.draw()

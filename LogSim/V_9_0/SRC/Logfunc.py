# -*- coding: utf8 -*-
__version__ = '9.0'
__author__ = 'Ralf Adams (adams@tbs1.de)'

from abc import ABC, abstractmethod


class LogFunc(ABC):
    """
    This is the abstract base class for calculating the logical functions.
    """
    def __init__(self, nof_inputs, nof_outputs):
        isinstance(nof_inputs, int)
        isinstance(nof_outputs, int)
        if nof_inputs < 0:
            raise ValueError('nof_inputs can\'t be negative')
        if nof_outputs < 1:
            raise ValueError('nof_outputs must be at least 1.')
        self._Inputs = []
        self._Outputs = []
        self._Inputs = [False for x in range(nof_inputs)]
        self._Outputs = [False for x in range(nof_outputs)]
        self.execute()
        self.__Name = "YaGate"

    def get_input(self, index):
        """
        Returns the value of the input signal at position index.
        :param index: Position of the value. Starts with 0 and must be < nof_inputs.
        :return: value at position index
        """
        isinstance(index, int)
        if index >= self._Inputs.__len__():
            raise ValueError('index is out of range.')
        return self._Inputs[index]

    def get_output(self, index):
        """
        Returns the value of the output signal at position index.
        :param index: Position of the value. Starts with 0 and must be < nof_outputs.
        :return: value at position index
        """
        isinstance(index, int)
        if index >= self._Outputs.__len__():
            raise ValueError('index is out of range.')
        return self._Outputs[index]

    def get_name(self):
        """
        Returns the value of the name property.
        :return: Name
        """
        return self.__Name

    def set_input(self, index, value):
        """
        Sets the value of the input signal at position index
        :param index: Position of the value. Starts with 0 and must be < nof_inputs.
        :param value: new value
        :return: None
        """
        isinstance(index, int)
        isinstance(value, bool)
        if index >= self._Inputs.__len__():
            raise ValueError('index is out of range.')
        self._Inputs[index] = value

    def _set_output(self, index, value):
        """
        Sets the value of the output signal at position index
        :param index: Position of the value. Starts with 0 and must be < nof_outputs.
        :param value: new value
        :return: None
        """
        isinstance(index, int)
        isinstance(value, bool)
        if index >= self._Outputs.__len__():
            raise ValueError('index is out of range.')
        self._Outputs[index] = value

    def set_name(self, value):
        """
        Sets the value of the name property
        :param value: (string) new value
        :return: None
        """
        isinstance(value, str)
        self.__Name = value

    def __str__(self):
        """
        Converts the status of the object to a string. The function will be called
        implicitly when you try to convert the object in a string.
        :return: Printable string of the status.
        """
        status = type(self).__name__ + "." + self.get_name() + ": "
        status += str(self._Inputs) + "-> " + str(self._Outputs)
        return status

    def show(self):
        """
        Shows the value of each property of the class and the class name.
        :return: None
        """
        cwidth = 50
        first_last = ''.ljust(cwidth, '-')
        format_string = "-- {{0:10}}: {{1:{0}}} --".format(cwidth - 18)

        print(first_last)
        print(format_string.format("Name", self.get_name()))
        print(format_string.format("Type", type(self).__name__))
        for i in range(self._Inputs.__len__()):
            print(format_string.format("Input"+str(i), str(self.get_input(i))))
        for i in range(self._Outputs.__len__()):
            print(format_string.format("Output"+str(i), str(self.get_output(i))))
        print(first_last)

    @abstractmethod
    def execute(self):
        """
        Abstract method to calculate the result of the logical function.
        :return: NotImplementedError
        """
        raise NotImplementedError


class AndGate(LogFunc):
    """
    This class calculates the logical AND function.
    """
    def __init__(self, nof_inputs):
        LogFunc.__init__(self, nof_inputs, 1)
        self.__Name = "YaAndGate"

    def execute(self):
        """
        Computes the result of the logical connection of the inputs.
        :return: None
        """
        self._set_output(0, True)
        for signal in self._Inputs:
            if False == signal:
                self._set_output(0, False)
                break


class OrGate(LogFunc):
    """
    This class calculates the logical OR function.
    """
    def __init__(self, nof_inputs):
        LogFunc.__init__(self, nof_inputs, 1)
        self.__Name = "YaOrGate"

    def execute(self):
        """
        Computes the result of the logical connection of the inputs.
        :return: None
        """
        self._set_output(0, False)
        for signal in self._Inputs:
            if True == signal:
                self._set_output(0, True)
                break


class XOrGate(LogFunc):
    """
    This class calculates the logical XOR function.
    """
    def __init__(self, nof_inputs):
        LogFunc.__init__(self, nof_inputs, 1)
        self.__Name = "YaXOrGate"

    def execute(self):
        """
        Computes the result of the logical connection of the inputs.
        :return: None
        """
        self._set_output(0, self._Inputs.count(True) % 2 == 1)


class NAndGate(LogFunc):
    """
    This class calculates the logical NAnd function.
    """
    def __init__(self, nof_inputs):
        LogFunc.__init__(self, nof_inputs, 1)
        self.__Name = "YaNAndGate"

    def execute(self):
        """
        Computes the result of the logical connection of the inputs.
        :return: None
        """
        self._set_output(0, False)
        for signal in self._Inputs:
            if False == signal:
                self._set_output(0, True)
                break


class NOrGate(LogFunc):
    """
    This class calculates the logical NOr function.
    """
    def __init__(self, nof_inputs):
        LogFunc.__init__(self, nof_inputs, 1)
        self.__Name = "YaNOrGate"

    def execute(self):
        """
        Computes the result of the logical connection of the inputs.
        :return: None
        """
        self._set_output(0, True)
        for signal in self._Inputs:
            if True == signal:
                self._set_output(0, False)
                break


class NotGate(LogFunc):
    """
    This class calculates the logical Not function.
    """
    def __init__(self, nof_inputs):
        LogFunc.__init__(self, nof_inputs, nof_inputs)
        self.__Name = "YaNotGate"

    def execute(self):
        """
        Computes the result of the logical connection of the inputs.
        :return: None
        """
        for i in range(self._Inputs.__len__()):
            if True == self.get_input(i):
                self._set_output(i, False)
            else:
                self._set_output(i, True)


class HalfAdder(LogFunc):
    """
    This class calculates the logical HalfAdder function.
    """
    def __init__(self):
        self.__Sum = XOrGate(2)
        self.__Sum.set_name("sum")
        self.__Carry = AndGate(2)
        self.__Carry.set_name("carry")
        LogFunc.__init__(self, 2, 2)
        self.__Name = "YaHalfAdder"

    def execute(self):
        """
        Computes the result of the logical connection of the inputs.
        :return: None
        """
        self.__Sum.set_input(0, self.get_input(0))
        self.__Sum.set_input(1, self.get_input(1))

        self.__Carry.set_input(0, self.get_input(0))
        self.__Carry.set_input(1, self.get_input(1))

        self.__Sum.execute()
        self.__Carry.execute()


        self._set_output(0, self.__Sum.get_output(0))
        self._set_output(1, self.__Carry.get_output(0))


class FullAdder(LogFunc):
    """
    This class calculates the logical FullAdder function.
    """
    def __init__(self):
        self.__Sum = [HalfAdder(), HalfAdder()]
        self.__Carry = OrGate(2)
        self.__Carry.set_name("carry")
        LogFunc.__init__(self, 3, 2)
        self.__Name = "YaFullAdder"

    def execute(self):
        """
        Computes the result of the logical connection of the inputs.
        :return: None
        """
        self.__Sum[0].set_input(0, self.get_input(0))
        self.__Sum[0].set_input(1, self.get_input(1))
        self.__Sum[0].execute()

        self.__Sum[1].set_input(0, self.get_input(2))
        self.__Sum[1].set_input(1, self.__Sum[0].get_output(0))
        self.__Sum[1].execute()

        self.__Carry.set_input(0, self.__Sum[0].get_output(1))
        self.__Carry.set_input(1, self.__Sum[1].get_output(1))
        self.__Carry.execute()


        self._set_output(0, self.__Sum[1].get_output(0))
        self._set_output(1, self.__Carry.get_output(0))

from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):

    @abstractmethod
    def set_helm(self) -> None:
        pass

    @abstractmethod
    def set_deck(self) -> None:
        pass

    @abstractmethod
    def set_special_equipment(self) -> None:
        pass

    @abstractmethod
    def reset(self)->None:
        pass


class WarShip():
    _size_of_deck = None
    _color_of_deck = None
    _gun = None

    def __init__(self):
        self._size_of_deck = None
        self._color_of_deck = None
        self._gun = None

class RegularShip():
    _size_of_deck = None
    _color_of_deck = None
    _safe_wheel = None

    def __init__(self):
        self._size_of_deck = None
        self._color_of_deck = None
        self._safe_wheel = None

class BuilderWarShip(Builder):
    ship = WarShip()

    def set_deck(self, size_d, color_d):
        if size_d in ['mid', 'big'] and color_d in ['black', 'white']:
            self.ship._size_of_deck = size_d
            self.ship._color_of_deck = color_d
        else:
            raise Exception('unintended values')

    def set_helm(self, helm):
        if helm in ['warHelm', 'cyberHelm']:
            self.ship._helm = helm
        else:
            raise Exception('unintended values')

    def set_special_equipment(self):
        self.ship._gun='minigun'
    
    def reset(self):
        self.ship=None
    
    def get_result(self):
        if self.ship._size_of_deck is not None and self.ship._color_of_deck is not None and self.ship._gun is not None:
            tmp=self.ship
            self.reset()
            return tmp
        else:
            raise Exception('failed to get warship due to lack of parts')

        


class BuilderRegularShip(Builder):
    ship = RegularShip()


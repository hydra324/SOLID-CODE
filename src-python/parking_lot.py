from abc import ABC, abstractmethod
from time import time
from typing import List

class Slot:
    def __init__(self,slot_id:int,free:bool) -> None:
        self.slot_id = slot_id
        self.free = free

    def toggle_free(self):
        self.free = not self.free

class CompactSlot(Slot):
    def __init__(self, slot_id: int, free: bool) -> None:
        super().__init__(slot_id, free)


class LargeSlot(Slot):
    def __init__(self, slot_id: int, free: bool) -> None:
        super().__init__(slot_id, free)

class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self,duration: int) -> int:
        pass

class FlatPricingStrategy(PricingStrategy):
    def __init__(self,flat_rate) -> None:
        self.flat_rate = flat_rate

    def calculate(self, duration: int) -> int:
        return self.flat_rate


class Ticket:
    # add pricing strat
    def __init__(self,vehicle:int,start:int,slot: Slot, pricing_strategy : PricingStrategy) -> None:
        self.vehicle = vehicle
        self.start = start
        self.slot = slot
        self.pricing_strategy = pricing_strategy

class Terminal:
    def __init__(self,gate_id:int) -> None:
        self.gate_id=gate_id

class EntryTerminal(Terminal):
    def __init__(self, gate_id: int) -> None:
        super().__init__(gate_id)

    def find_and_assign_slot(self,vehicle:int,pricing_strategy:PricingStrategy):
        plot= get_plot_instance()
        slot = plot.find_slot()
        slot.toggle_free()
        current_time = time()
        return Ticket(vehicle,current_time,slot,pricing_strategy)
    
class ExitTerminal(Terminal):
    def __init__(self, gate_id: int) -> None:
        super().__init__(gate_id)
    
    def end_parking(self,ticket:Ticket) -> int:
        end_time = time()
        duration = end_time - ticket.start
        ticket.slot.toggle_free()
        return ticket.pricing_strategy.calculate(duration)

class FindingStrategy(ABC):

    @abstractmethod
    def find_slot(self,slots: List[Slot]):
        pass

class NearestSlotFindingStrategy(FindingStrategy):

    def find_slot(self, slots: List[Slot]):
        pass # returns an empty slot from the list of slots

class ParkingLot:
    _instance = None
    def __new__(cls,slots: List[Slot],terminals: List[Terminal],find_strategy: FindingStrategy) -> None:
        if cls._instance is None:
            cls._instance = super(ParkingLot,cls).__new__(cls)
        
        cls._instance.slots = slots
        cls._instance.terminals = terminals
        cls._instance.find_strategy = find_strategy
        return cls._instance

    def find_slot(cls):
        return cls._instance.find_strategy.find_slot(cls._instance.slots)


def get_plot_instance():
    return ParkingLot().get_instance()
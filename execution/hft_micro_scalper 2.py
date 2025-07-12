```python
# execution/hft_micro_scalper.py

import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

class ExecutionHandler(ABC):
    """
    Abstract class providing an interface for all subsequent 
    (inherited) execution handlers, both simulated and live.
    """
    @abstractmethod
    def execute_order(self, event):
        """
        Takes an Order event and executes it, producing 
        a Fill event that gets placed onto the Events queue.
        """
        raise NotImplementedError("Should implement execute_order()")


class MicroScalperExecutionHandler(ExecutionHandler):
    """
    Handles the execution of a portfolio of symbols using 
    the specified broker's API for creating trades.
    """
    def __init__(self, events, order_routing="Smart", currency="USD"):
        self.events = events
        self.order_routing = order_routing
        self.currency = currency

    def execute_order(self, event):
        """
        Creates the necessary InteractiveBrokers order object
        and then executes it via their API.
        """
        if event.type == 'ORDER':
            self._execute_order(event)

    def _execute_order(self, event):
        """
        Internal method that sends the order to the broker API 
        and then generates a corresponding Fill event.
        """
        # TODO: Implement broker API call here

        # For now, we'll simulate a fill event immediately after an order event
        fill_event = self._create_fill_event(event)
        self.events.put(fill_event)

    def _create_fill_event(self, event):
        """
        Handles the creation of the FillEvent that will be 
        placed onto the events queue subsequent to the OrderEvent.
        """
        timestamp = pd.Timestamp.now(tz='UTC')
        fill_event = FillEvent(timestamp, event.symbol, 'ARCA', event.quantity, event.direction, None)
        return fill_event


class FillEvent:
    """
    Encapsulates the notion of a Filled Order, as returned
    from a brokerage execution unit (be it simulated or live).
    """

    def __init__(self, timeindex, symbol, exchange, quantity, 
                 direction, fill_cost, commission=None):
        """
        Initialises the FillEvent object. Sets the symbol, exchange,
        quantity, direction, cost of fill and an optional 
        commission.
        """
        self.type = 'FILL'
        self.timeindex = timeindex
        self.symbol = symbol
        self.exchange = exchange
        self.quantity = quantity
        self.direction = direction
        self.fill_cost = fill_cost

        if commission is None:
            self.commission = self.calculate_ib_commission()
        else:
            self.commission = commission

    def calculate_ib_commission(self):
        """
        Calculates the fees of trading based on an Interactive
        Brokers fee structure for API, in USD.
        """
        full_cost = 1.3
        if self.quantity <= 500:
            full_cost = max(1.3, 0.013 * self.quantity)
        else: # Greater than 500
            full_cost = max(1.3, 0.008 * self.quantity)
        return full_cost
```
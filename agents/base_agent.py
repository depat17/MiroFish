from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """An abstract base class for intelligence agents."""

    @abstractmethod
    def act(self):
        """Implement this method to define the agent's action."""  
        pass

    @abstractmethod
    def observe(self):
        """Implement this method to define the observation process for the agent."""
        pass

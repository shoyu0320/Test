from typing import Dict, Tuple, Any


class Env:  # TODO edit docstring for Env class
    """_summary_
    """

    def __init__(self, name: str = "InitialEnv") -> None:
        """_summary_

        Args:
            name (str, optional): _description_. Defaults to "InitialEnv".
        """
        self.name: str = name
        self.episode_info: Dict[str, Any] = {}
        self.episode_done: bool = False
        self.episode_reward: float = 0.0

    def reset(self, _reset: bool = True) -> Dict[str, float]:
        """_summary_

        Args:
            _reset (bool, optional): _description_. Defaults to True.

        Returns:
            Dict[str, float]: _description_
        """
        self.episode_reward = 0.0
        self.episode_done = False
        self.episode_info = {}

        return {"obs": 0.0, "last_obs": 0.0}

    def step(
        self,
        obs: Dict[str, float] = {},
        reward: float = 0.0,
        info: Dict[str, Any] = {},
        done: bool = False,
    ) -> Tuple[Dict[str, float], float, Dict[str, Any], bool]:
        """_summary_

        Args:
            obs (Dict[str, float], optional): _description_. Defaults to {}.
            reward (float, optional): _description_. Defaults to 0.0.
            info (Dict[str, Any], optional): _description_. Defaults to {}.
            done (bool, optional): _description_. Defaults to False.

        Returns:
            Tuple[Dict[str, float], float, Dict[str, Any], bool]: _description_
        """
        return ({"obs": 0.0, "last_obs": 0.0}, 0.0, {}, False)

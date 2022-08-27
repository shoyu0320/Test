from typing import Dict, Tuple, Any


class Env:  # TODO edit docstring for Env class
    """環境の抽象クラス
    """

    def __init__(self, name: str = "InitialEnv") -> None:
        """環境を初期化するメソッド

        Args:
            name (str, optional): 環境の名前. Defaults to "InitialEnv".
        """
        self.name: str = name
        self.episode_info: Dict[str, Any] = {}
        self.episode_done: bool = False
        self.episode_reward: float = 0.0

    def reset(self, _reset: bool = True) -> Dict[str, float]:
        """環境情報のリセットをするメソッド

        Args:
            _reset (bool, optional): リセットの時に使う情報. Defaults to True.

        Returns:
            Dict[str, float]: 観測情報の初期値を返す
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
        """１ステップでの環境の変化を計算するメソッド

        Args:
            obs (Dict[str, float], optional): 観測情報の入力値. Defaults to {}.
            reward (float, optional): 報酬の入力値. Defaults to 0.0.
            info (Dict[str, Any], optional): 情報の入力値. Defaults to {}.
            done (bool, optional): エピソードの終わりを決めるブール値. Defaults to False.

        Returns:
            Tuple[Dict[str, float], float, Dict[str, Any], bool]: １ステップ後の各出力値
        """
        return ({"obs": 0.0, "last_obs": 0.0}, 0.0, {}, False)

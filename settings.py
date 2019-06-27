class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


        # 飞船的设置
        self.ship_speed_factor = 30
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 20
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 200, 200, 200
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 10
        # fleet_direction = 1 means moving to the right side
        self.fleet_direction = 1
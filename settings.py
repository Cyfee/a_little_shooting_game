# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 21:46:56 2019

@author: cyfee
"""

class Settings():
    """存储《外星人入侵》的所有设置的类"""
    
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #飞船设置
        #self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        #子弹设置
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
        
        #外星人设置
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction为1表示向右移，为-1表示向左移
        #self.fleet_direction = 1
        
        #以什么样的速度加快游戏节奏
        self.speedupp_scale = 1.1
        #外星人点数的提高速度
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """初始化随着游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        #fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1
        
        #积分
        self.alien_points = 50
        
    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedupp_scale
        self.bullet_speed_factor *= self.speedupp_scale
        self.alien_speed_factor *= self.speedupp_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
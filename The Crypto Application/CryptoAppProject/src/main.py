# -*- coding: utf-8 -*-
"""
Project Name: The Crypto App Project
Description: Custom GUI application for trading crypto on the Gemini Marketplace


Created on Tue May  9 19:16:55 2023

@author: joaquin
"""

from Code.Launch.StartUpFile import StartUp

startUp = StartUp()


def runner():
    startUp.execute_code()
    # print('is custom program?: ', startUp.custom)

if __name__ == "__main__":
    runner()


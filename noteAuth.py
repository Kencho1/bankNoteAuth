# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 23:27:08 2022

@author: Kencho
"""

from pydantic import BaseModel

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float
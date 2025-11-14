import pygame as pg
import logging
logpaths    = ['logs/info_log.txt' , 'logs/debug_log.txt' , 'logs/warning_log.txt' , 'logs/critical_log.txt' , 'logs/error_log.txt']
log_levels  = [ logging.INFO , logging.WARNING , logging.ERROR , logging.CRITICAL , logging.DEBUG ]
log_formats = ['%(asctime)s - %(levelname)s - %(message)s' , '%(levelname)s - %(asctime)s - %(message)s']
logging.basicConfig(filename = logpaths[0] , level = log_levels[0] , format = log_formats[0])    #отключить протоколирование - logging.disable()

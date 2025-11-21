
#LogsManager.py
import logging,sys
from pathlib import Path

# путь к Scripts/Python
sys.path.append(str(Path(__file__).resolve().parent))
 #отключить протоколирование - logging.disable()


logpaths    = {

"info"     : 'logs/Info/0.txt',
"debug"    : 'logs/Debug/debug/0.txt',
"warning"  : 'logs/warning/0.txt',
"critical" : 'logs/critical/0.txt',
"error"    :'logs/error/0.txt'


}




log_levels  = [ logging.INFO , logging.WARNING , logging.ERROR , logging.CRITICAL , logging.DEBUG ]

log_formats = ['%(asctime)s - %(levelname)s - %(message)s', 
               '%(levelname)s - %(asctime)s - %(message)s']

logging.basicConfig(filename = logpaths['info'], level = log_levels[0], format = log_formats[0])   


"""
твой вариант
logger = logging.getLogger("info_logger")
logger.setLevel(logging.DEBUG)  # ловим все уровни

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

"""

#мой
logger = logging.getLogger("info_logger")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')


# создаём обработчики для каждого уровня
for level_name, path in logpaths.items():
    handler = logging.FileHandler(path)
    handler.setLevel(getattr(logging, level_name.upper()))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
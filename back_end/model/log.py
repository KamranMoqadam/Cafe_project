import logging

cafe_log = logging.getLogger('cafecafe')
cafe_handler = logging.FileHandler('cafe.log')
cafe_log.setLevel(logging.INFO)
log_format = '%(asctime)s - %(levelname)s - %(message)s'
cafe_format = logging.Formatter(log_format)
cafe_handler.setFormatter(cafe_format)
cafe_log.addHandler(cafe_handler)

import logging
import os
import time

# critical>error>warning>info>debug
if __name__ == '__main__':
    logging.basicConfig(filename=os.getcwd() + '/LogFiles/testlog.log', level=logging.INFO)
    logger = logging.getLogger('__name__')
    logger.info(time.time())
    logger.debug('This is debug but wont be logged')
    logger.info('This is info')
    logger.exception('This is exception')
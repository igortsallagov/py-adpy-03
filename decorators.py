import datetime
import os


def logging(func):
    def write_logs(*args):
        date = datetime.datetime.today()
        log_string = f'{date} // {func.__name__} // {args} // {func(*args)}\n'
        with open('log.txt', 'a') as log_file:
            log_file.write(log_string)
        return func(*args)
    return write_logs


def logging_path(path):
    def logging_new(func):
        def write_logs_path(*args):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            try:
                os.mkdir(path)
                folder = path
            except FileExistsError:
                folder = path
            file_path = os.path.join(current_dir, folder, 'log_2.txt')
            date = datetime.datetime.today()
            log_string = f'{date} || {func.__name__} || {args} || {func(*args)}\n'
            with open(file_path, 'a') as log_file:
                log_file.write(log_string)
            return func(*args)
        return write_logs_path
    return logging_new

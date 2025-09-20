# Importação para logging
import logging
# Definição de classe para logging
class classe_logger:
    # Constantes para definir o nível do logging
    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL
    # Construtor da classe
    def __init__(self,
                 logger_name = 'my_logger'
                 ,logger_level = DEBUG
                 ,logger_file_name = 'logger_file_name'):
        # Atribui propriedade nome do logger
        if len(str(logger_name)) > 0:
            self.__logger_name = str(logger_name)
        else:
            self.__logger_name = 'my_logger'

        # Atribui propriedade para definir o nível do logging
        self.logger_level = logger_level
        # Atribui propriedade para definir o nome do arquivo de log
        if len(str(logger_file_name)) > 0:
            self.__logger_file_name = logger_file_name
        else:
            self.__logger_file_name = 'logger_file_name'
        # Atribui o nível do logging
        self.logger = logging.getLogger(f'{self.__logger_name}')
        # Define o nível de registro como logger_level. Isso significa que todas as mensagens com nível logger_level e acima serão registradas
        self.logger.setLevel(self.logger_level)
        # Cria manipuladores que imprimem mensagens de log no console (saída padrão) e escrevem mensagens de log em um arquivo chamado f'{__logger_name}.log'
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(f'{self.__logger_file_name}.log')
        # Define um formatador que especifica o formato das mensagens de log
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # Define o formatador para o manipulador do console e para o manipulador de arquivos
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        # Adiciona o manipulador do console ao logger. Isso significa que mensagens de log serão exibidas no console
        self.logger.addHandler(console_handler)
        # Adiciona o manipulador de arquivos ao logger. Isso significa que mensagens de log serão escritas no arquivo f'{name}.log'
        self.logger.addHandler(file_handler)
    # Logging de mensagem para debug
    def debug (self, msg):
        self.logger.debug(msg)
    # Logging de mensagem para info
    def info (self, msg):
        self.logger.info(msg)
    # Logging de mensagem para warning
    def warning (self, msg):
        self.logger.warning(msg)
    # Logging de mensagem para error
    def error (self, msg):
        self.logger.error(msg)
    # Logging de mensagem para critical
    def critical (self, msg):
        self.logger.critical(msg)     
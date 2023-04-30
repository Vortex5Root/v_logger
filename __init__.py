from Libs.Configs_API.configs import config
import json 
from colorama import init,Fore
init()

class logg(object):

    type_logg = ''

    api_config = config()

    logg_config = {
            'prefix':'',
            'success' : f"({Fore.GREEN}✓{Fore.RESET})",
            'info' : f"({Fore.LIGHTWHITE_EX}INFO{Fore.RESET})",
            'output' : f"{Fore.LIGHTCYAN_EX}",
            'pending' : f"({Fore.YELLOW}Pending{Fore.RESET})",
            'debug' : f"({Fore.CYAN}DEBUG{Fore.RESET})",
            'error' : f"({Fore.RED}ERROR{Fore.RESET})"
            }

    def __init__(self,profile_name,dirpath='loggs'):

        self.logg_config['prefix'] = profile_name

        if f"{profile_name}.json" not in [conf[1] for conf in self.api_config.configs]: #and not self.api_config.check_working_path(dirpath):
            #print('not exists')
            self.api_config.add_config(self.logg_config,profile_name,dirpath)
        else:
            #print('exists')
            self.logg_config = self.api_config.get_config(profile_name,dirpath)
            #print(self.logg_config)

    @property
    def logg(self):
        return self.type_logg

    @logg.setter
    def logg(self,type_logg):
        
        #print(self.logg_config)
        #print([_ for _ in self.logg_config]) # *
        if type_logg in [_ for _ in self.logg_config]:
            self.type_logg = type_logg
            #print(f'[Logger] type {self.type_logg.upper()} setted successfaly')
        else:
            print([_ for _ in self.logg_config]) # *
            print(f'[Logger] {self.logg_config["error"]} invalid type')
            print(f'[Logger] {self.logg_config["info"]} {[f"{_}," for _ in self.logg_config]}')
    def lprint(self,message):
        if not self.type_logg in [_ for _ in self.logg_config]:
            exit()
        print(f'{self.logg_config["prefix"]} {self.logg_config[self.type_logg]} {message}')

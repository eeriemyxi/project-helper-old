from colorama import Style, Fore
class Colors:
    def cprint(self,color, str):
        exec(f"print(Fore.{color.upper()}+'''{str}'''+Style.RESET_ALL)")
    def p_error(self,str):
        exec(f"print(Fore.RED+'''{str}'''+Style.RESET_ALL)")
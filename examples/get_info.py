from api.cline import Cline

cli = Cline(url="https://tas.blockchain-servers.world")

get_info = cli.get_info()

print(get_info)

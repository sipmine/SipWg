import os

# generate key users 
def genKey (name: str) -> None:
    os.system("wg genkey | tee /etc/wireguard/{}_privatekey | wg pubkey | tee /etc/wireguard/{}_publickey".format(name, name))


# simple generate code on config
def writeServerConfig(fileConf, key, id: int) -> None:
    fileConf.write("\n[Peer]\n")
    fileConf.write("PublicKey = {}\n".format(key))
    fileConf.write("AllowedIPs = 10.0.0.{}/32\n".format(id))


# add users on config file
def configFile(name, id: int):
    Userpublickey = open(f"/etc/wireguard/{name}_publickey", "r")
    config = open("new.conf", "w")
    writeServerConfig(config, Userpublickey, id)
    config.close()



